# -*- coding: utf-8 -*-

# Spell Checker Add-on for Anki
#
# Copyright (C)  2018-2019 Aristotelis P. <https://glutanimate.com/>
# Copyright (C)  2018 The Qt Company Ltd.
# Copyright (C)  Ankitects Pty Ltd and contributors
#
# Parts of this module are based on the Qt C++ spell checker example
# which is licensed under the BSD 3-Clause New License (see LICENSE_QT.txt)
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version, with the additions
# listed at the end of the license file that accompanied this program.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# NOTE: This program is subject to certain additional terms pursuant to
# Section 7 of the GNU Affero General Public License.  You should have
# received a copy of these additional terms immediately following the
# terms and conditions of the GNU Affero General Public License that
# accompanied this program.
#
# If not, please request a copy through one of the means of contact
# listed here: <https://glutanimate.com/contact/>.
#
# Any modifications to this file must keep this entire header intact.

"""
Spell-checking GUI
"""

import aqt
from aqt.qt import *
from aqt.editor import EditorWebView, Editor
from anki.hooks import runHook, addHook, remHook, wrap
from anki.lang import _

class CustomEditorWebView(EditorWebView):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.spellmgr = self.editor.mw.spellcheckManager
        self._profile = self.page().profile()
        self.setupSpellcheck()

    def setupSpellcheck(self, langs=None):
        if self.spellmgr is None:
            return None

        prefs = self.editor.mw.pm.profile
        langs = langs or self.spellmgr.localLangs()

        active_filenames = []
        for code in prefs.get('spellCheckLangs', []):
            if code not in langs:
                continue
            active_filenames.append(langs[code].filename)

        self._profile.setSpellCheckEnabled(prefs.get('spellCheck', False))
        self._profile.setSpellCheckLanguages(active_filenames)

        self._checkLangs = langs

    def toggleSpellcheck(self, checked=None):
        if checked is None:
            checked = not self.editor.mw.pm.profile.get('spellCheck')
        self._profile.setSpellCheckEnabled(checked)
        self.editor.mw.pm.profile['spellCheck'] = checked

    def _toggleLang(self, checked, lang):
        prefs = self.editor.mw.pm.profile
        active_codes = set(prefs.get('spellCheckLangs', []))
        active_filenames = set(self._profile.spellCheckLanguages())

        if checked:
            active_codes.add(lang.code)
            active_filenames.add(lang.filename)
        else:
            try:
                active_codes.remove(lang.code)
                active_filenames.remove(lang.filename)
            except KeyError:
                pass

        self._profile.setSpellCheckLanguages(list(active_filenames))
        prefs['spellCheckLangs'] = list(active_codes)

    def _openSpellCheckPrefs(self):
        prefs = aqt.dialogs.open("Preferences", self.editor.mw)
        prefs.form.tabWidget.setCurrentIndex(1)

    def _addSuggestedSpellings(self, menu, data):
        """Populate context menu with spell checker suggestions"""
        if (not self._checkLangs or not self._profile.isSpellCheckEnabled() or
                not data.misspelledWord()):
            return

        font = menu.font()
        font.setBold(True)
        suggestions = data.spellCheckerSuggestions()

        for suggested in suggestions:
            action = menu.addAction(suggested)
            action.setFont(font)
            action.triggered.connect(
                lambda _, suggested=suggested:
                    self._page.replaceMisspelledWord(suggested)
            )

        if not suggestions:
            action = menu.addAction(_("No suggestions"))
            action.setEnabled(False)

        menu.addSeparator()

    def _addSpellcheckSettings(self, menu, data):
        menu.addSeparator()

        if not self._checkLangs:
            action = menu.addAction(_("Spell checking..."))
            action.triggered.connect(self._openSpellCheckPrefs)
            return

        check_enabled = self._profile.isSpellCheckEnabled()

        action = menu.addAction(_("Check spelling\tF6"))
        action.setCheckable(True)
        action.setChecked(check_enabled)
        action.toggled.connect(self.toggleSpellcheck)

        if not check_enabled:
            return

        submenu = menu.addMenu(_("Select languages"))
        action = submenu.addAction(_("Download languages..."))
        action.triggered.connect(self._openSpellCheckPrefs)
        submenu.addSeparator()
        
        active_filenames = self._profile.spellCheckLanguages()

        for lang in self._checkLangs.values():
            action = submenu.addAction(lang.verbose)
            action.setCheckable(True)
            action.setChecked(lang.filename in active_filenames)
            action.triggered.connect(
                lambda checked, lang=lang:
                    self._toggleLang(checked, lang)
            )

    # Context menu
    ######################################################################

    def contextMenuEvent(self, evt):
        data = self._page.contextMenuData()

        # only show context menu in editable areas:
        if not data.isValid() or not data.isContentEditable():
            evt.accept()
            return

        menu = QMenu()

        # Spellcheck suggestions
        if self.spellmgr:
            self._addSuggestedSpellings(menu, data)

        # Other actions
        a = menu.addAction(_("Cut"))
        a.triggered.connect(self.onCut)
        a = menu.addAction(_("Copy"))
        a.triggered.connect(self.onCopy)
        a = menu.addAction(_("Paste"))
        a.triggered.connect(self.onPaste)

        # Spellcheck settings
        if self.spellmgr:
            self._addSpellcheckSettings(menu, data)

        runHook("EditorWebView.contextMenuEvent", self, menu)

        menu.exec_(evt.globalPos())  # popup does not seem to work


def onSetupShortcuts(cuts, self):
    cuts.append(("F6", self.web.toggleSpellcheck))

def onEditorInit(self, *args, **kwargs):
    addHook("spellLangsUpdated", self.web.setupSpellcheck)

def onEditorCleanup(self, *args, **kwargs):
    remHook("spellLangsUpdated", self.web.setupSpellcheck)

def initEditor():
    aqt.editor.EditorWebView = CustomEditorWebView
    Editor.__init__ = wrap(Editor.__init__, onEditorInit, "after")
    Editor.cleanup = wrap(Editor.cleanup, onEditorCleanup, "before")
    addHook("setupEditorShortcuts", onSetupShortcuts)
