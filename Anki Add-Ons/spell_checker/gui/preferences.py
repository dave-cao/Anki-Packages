# -*- coding: utf-8 -*-

# Spell Checker Add-on for Anki
#
# Copyright (C)  2018-2019 Aristotelis P. <https://glutanimate.com/>
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
Custom preferences pane
"""

import aqt
from aqt.qt import *
from aqt.utils import askUser, tooltip, showWarning
from aqt.preferences import Preferences
from aqt.forms.preferences import Ui_Preferences

from .contrib import invokeContributionsDialog

from anki.hooks import runHook
from anki.utils import isMac
from anki.lang import _


class CustomPreferences(Preferences):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupSpellcheck()
        self.setupContrib()
    
    def setupContrib(self):
        self.form.spellContrib.clicked.connect(
            lambda: invokeContributionsDialog(self))

    def setupSpellcheck(self):
        self.spellmgr = self.mw.spellcheckManager
        # Adjust UI for alternate builds:
        if self.spellmgr is None:
            self.form.spellWidget.hide()
            return
        else:
            self.form.spellNotSupported.hide()

        self.localSpellLangs = None
        self.remoteSpellLangs = self.remoteSpellLangsAll = None
        self.redrawLocalSpellLangs()

        f = self.form
        f.spellRefresh.clicked.connect(self.onRefreshSpellLangs)
        f.spellDownload.clicked.connect(self.onDownloadSpellLangs)
        f.spellRemove.clicked.connect(self.onRemoveSpellLangs)
        f.tabWidget.currentChanged.connect(self.onTabChanged)
    
    def onTabChanged(self, idx):
        if idx != 1 or self.remoteSpellLangs is not None:
            return
        self.onRefreshSpellLangs(silent=True)

    def onRefreshSpellLangs(self, silent=False):
        remote, updates, obsolete = self.spellmgr.checkForUpdates(
            silent=silent)
        if remote is None:
            return
        remote = list(remote.values())
        self.redrawRemoteSpellLangs(langs=remote)
        if not updates:
            return

        msg = _("""\
Updates are available for the following downloaded languages:\n
%(langs)s\n\nWould you like to \
update them now?""") % dict(langs="\n".join(
                            lang.verbose for lang in updates))
        if not askUser(msg, parent=self):
            return

        log, errs = self.spellmgr.updateLangs(updates, obsolete)

        if log:
            tooltip("<br>".join(log))
        if errs:
            showWarning("\n\n".join(errs), textFormat="plain", parent=self)

        self.redrawLocalSpellLangs(signal=True)

    def onDownloadSpellLangs(self):
        selected = self.getSelectedSpellLangs(self.form.spellRemote,
                                              self.remoteSpellLangs)
        if not selected:
            tooltip(_("Please select a language first."))
            return

        log, errs = self.spellmgr.downloadLangs(selected)

        if log:
            tooltip("<br>".join(log), parent=self)
        if errs:
            showWarning("\n\n".join(errs), textFormat="plain", parent=self)

        self.redrawLocalSpellLangs(signal=True)
        self.redrawRemoteSpellLangs()
        self.selectSpellLangs(self.form.spellLocal, self.localSpellLangs,
                              selected)

    def onRemoveSpellLangs(self):
        selected = self.getSelectedSpellLangs(self.form.spellLocal,
                                              self.localSpellLangs)
        if not selected:
            tooltip(_("Please select a language first."))
            return

        for lang in selected:
            self.spellmgr.deleteLang(lang)
            try:
                self.prof.get("spellCheckLangs", []).remove(lang.code)
            except ValueError:
                pass

        self.form.spellLocal.clearSelection()
        self.redrawLocalSpellLangs(signal=True)
        self.redrawRemoteSpellLangs()
        self.selectSpellLangs(self.form.spellRemote, self.remoteSpellLangs,
                              selected)

        tooltip("<br>".join(_("Deleted %(lang)s" % dict(lang=lang.verbose)
                              for lang in selected)))

    def redrawLocalSpellLangs(self, signal=False):
        langs = self.spellmgr.localLangs()
        if langs is None:
            return
        self.localSpellLangs = list(langs.values())
        self.redrawSpellLangs(self.form.spellLocal, self.localSpellLangs)
        if signal:
            runHook("spellLangsUpdated", langs)

    def redrawRemoteSpellLangs(self, langs=None):
        if langs is None:
            langs = self.remoteSpellLangsAll
        else:
            self.remoteSpellLangsAll = langs
        if langs is None:
            return
        self.remoteSpellLangs = [i for i in langs
                                 if i not in self.localSpellLangs]
        self.redrawSpellLangs(self.form.spellRemote, self.remoteSpellLangs)

    def redrawSpellLangs(self, langList, model):
        selected = set(self.getSelectedSpellLangs(langList, model))
        langList.clear()
        for lang in model:
            item = QListWidgetItem(lang.verbose, langList)
            if lang in selected:
                item.setSelected(True)
        langList.clearSelection()
        langList.repaint()

    def getSelectedSpellLangs(self, langList, model):
        idxs = [x.row() for x in langList.selectedIndexes()]
        langs = []
        for idx in idxs:
            try:
                langs.append(model[idx])
            except IndexError:
                continue
        return langs

    def selectSpellLangs(self, langList, model, langs):
        for lang in langs:
            try:
                idx = model.index(lang)
                item = langList.item(idx)
            except (ValueError, AttributeError):
                continue
            item.setSelected(True)


class CustomPreferencesForm(Ui_Preferences):
    def setupUi(self, Preferences):
        super().setupUi(Preferences)
        self.spellTab = QWidget()
        self.spellTab.setObjectName("spellTab")
        self.spellTabLayout = QVBoxLayout(self.spellTab)
        self.spellTabLayout.setObjectName("spellTabLayout")
        self.spellWidget = QWidget(self.spellTab)
        self.spellWidget.setObjectName("spellWidget")
        self.spellGridLayout = QGridLayout(self.spellWidget)
        self.spellGridLayout.setObjectName("spellGridLayout")
        spacerItem1 = QSpacerItem(
            20, 10, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.spellGridLayout.addItem(spacerItem1, 1, 0, 1, 3)
        self.spellRemote = QListWidget(self.spellWidget)
        self.spellRemote.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.spellRemote.setObjectName("spellRemote")
        self.spellGridLayout.addWidget(self.spellRemote, 3, 0, 1, 1)
        self.spellLabel1 = QLabel(self.spellWidget)
        self.spellLabel1.setAlignment(Qt.AlignCenter)
        self.spellLabel1.setObjectName("spellLabel1")
        self.spellGridLayout.addWidget(self.spellLabel1, 2, 0, 1, 1)
        self.spellLabel2 = QLabel(self.spellWidget)
        self.spellLabel2.setAlignment(Qt.AlignCenter)
        self.spellLabel2.setObjectName("spellLabel2")
        self.spellGridLayout.addWidget(self.spellLabel2, 2, 2, 1, 1)
        self.spellLocal = QListWidget(self.spellWidget)
        self.spellLocal.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.spellLocal.setObjectName("spellLocal")
        self.spellGridLayout.addWidget(self.spellLocal, 3, 2, 1, 1)
        self.spellButtonLayout = QVBoxLayout()
        self.spellButtonLayout.setObjectName("spellButtonLayout")
        self.spellDownload = QToolButton(self.spellWidget)
        self.spellDownload.setObjectName("spellDownload")
        self.spellButtonLayout.addWidget(self.spellDownload)
        self.spellRemove = QToolButton(self.spellWidget)
        self.spellRemove.setObjectName("spellRemove")
        self.spellButtonLayout.addWidget(self.spellRemove)
        spacerItem2 = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.spellContrib = QToolButton(self.spellWidget)
        self.spellContrib.setObjectName("spellContrib")
        self.spellContrib.setIcon(QIcon(":/spell_checker/icons/heart.svg"))
        self.spellButtonLayout.addWidget(self.spellContrib)
        self.spellButtonLayout.addItem(spacerItem2)
        self.spellGridLayout.addLayout(self.spellButtonLayout, 3, 1, 1, 1)
        self.spellLabel0 = QLabel(self.spellWidget)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.spellLabel0.sizePolicy().hasHeightForWidth())
        self.spellLabel0.setSizePolicy(sizePolicy)
        self.spellLabel0.setObjectName("spellLabel0")
        self.spellGridLayout.addWidget(self.spellLabel0, 0, 0, 1, 3)
        # self.pushButton = QPushButton(self.spellWidget)
        # self.pushButton.setObjectName("pushButton")
        # self.spellGridLayout.addWidget(self.pushButton, 4, 2, 1, 1)
        self.spellRefresh = QPushButton(self.spellWidget)
        self.spellRefresh.setObjectName("spellRefresh")
        self.spellGridLayout.addWidget(self.spellRefresh, 4, 0, 1, 1)
        self.spellTabLayout.addWidget(self.spellWidget)
        self.spellNotSupported = QLabel(self.spellTab)
        self.spellNotSupported.setWordWrap(True)
        self.spellNotSupported.setObjectName("spellNotSupported")
        self.spellTabLayout.addWidget(self.spellNotSupported)
        spacerItem3 = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.spellTabLayout.addItem(spacerItem3)
        self.tabWidget.insertTab(1, self.spellTab, "")

        self.spellLabel1.setText(_("Available"))
        self.spellLabel2.setText(_("Downloaded"))
        self.spellDownload.setText(_("→"))
        self.spellRemove.setText(_("←"))
        self.spellContrib.setToolTip(_("Support my work"))
        self.spellLabel0.setText(_("Spell checking dictionaries:"))
        # self.pushButton.setText(_("Install from File..."))
        self.spellRefresh.setText(_("Refresh List"))
        self.spellNotSupported.setText(
            _("It appears like you are using an older version of Anki or an alternate app build. "
              "The Spell Checker add-on only works on standard builds of Anki 2.1.10 and up.")
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.spellTab), _("Spelling"))

        if isMac:
            self.spellGridLayout.setContentsMargins(3, 3, 3, 3)
            self.spellTabLayout.setContentsMargins(3, 3, 3, 3)

def initPreferences():
    aqt.forms.preferences.Ui_Preferences = CustomPreferencesForm
    aqt.dialogs._dialogs["Preferences"] = [CustomPreferences, None]
