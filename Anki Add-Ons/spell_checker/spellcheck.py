# -*- coding: utf-8 -*-

# Spell Checker Add-on for Anki
#
# Copyright (C)  2018-2019 Aristotelis P. <https://glutanimate.com/>
# Copyright (C)  Ankitects Pty Ltd and contributors
#
# Some parts of this module were inspired by the work of the qutebrowser
# project: <https://github.com/qutebrowser/qutebrowser>
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
Spell checking dictionaries manager
"""

import os
import re
import json
import base64
from collections import OrderedDict, namedtuple
from send2trash import send2trash

from aqt.utils import showWarning
from anki.lang import _
from anki.sync import AnkiRequestsClient

from .downloader import download

# language code: verbose name
langs = {
    "af-ZA": _("Afrikaans (South Africa)"),
    "bg-BG": _("Bulgarian (Bulgaria)"),
    "ca-ES": _("Catalan (Spain)"),
    "cs-CZ": _("Czech (Czech Republic)"),
    "cy-GB": _("Welsh (United Kingdom)"),
    "da-DK": _("Danish (Denmark)"),
    "de-DE": _("German (Germany)"),
    "el-GR": _("Greek (Greece)"),
    "en-AU": _("English (Australia)"),
    "en-CA": _("English (Canada)"),
    "en-GB": _("English (United Kingdom)"),
    "en-US": _("English (United States)"),
    "es-ES": _("Spanish (Spain)"),
    "et-EE": _("Estonian (Estonia)"),
    "fa-IR": _("Farsi (Iran)"),
    "fo-FO": _("Faroese (Faroe Islands)"),
    "fr-FR": _("French (France)"),
    "he-IL": _("Hebrew (Israel)"),
    "hi-IN": _("Hindi (India)"),
    "hr-HR": _("Croatian (Croatia)"),
    "hu-HU": _("Hungarian (Hungary)"),
    "id-ID": _("Indonesian (Indonesia)"),
    "it-IT": _("Italian (Italy)"),
    "ko": _("Korean"),
    "lt-LT": _("Lithuanian (Lithuania)"),
    "lv-LV": _("Latvian (Latvia)"),
    "nb-NO": _("Norwegian (Norway)"),
    "nl-NL": _("Dutch (Netherlands)"),
    "pl-PL": _("Polish (Poland)"),
    "pt-BR": _("Portuguese (Brazil)"),
    "pt-PT": _("Portuguese (Portugal)"),
    "ro-RO": _("Romanian (Romania)"),
    "ru-RU": _("Russian (Russia)"),
    "sh": _("Serbo-Croatian"),
    "sk-SK": _("Slovak (Slovakia)"),
    "sl-SI": _("Slovenian (Slovenia)"),
    "sq": _("Albanian"),
    "sr": _("Serbian"),
    "sv-SE": _("Swedish (Sweden)"),
    "ta-IN": _("Tamil (India)"),
    "tg-TG": _("Tajik (Tajikistan)"),
    "tr-TR": _("Turkish (Turkey)"),
    "uk-UA": _("Ukrainian (Ukraine)"),
    "vi-VN": _("Vietnamese (Viet Nam)")
}


Language = namedtuple("Language", ["verbose", "code", "version", "filename"])


class SpellcheckManager:

    _api_url = ("https://chromium.googlesource.com/chromium/deps/"
                "hunspell_dictionaries.git/+/master/")
    _ext = "bdic"
    # extracts language code and version from bdic filename
    _dict_re = re.compile(
        r"(?P<filename>(?P<code>[a-z]{2}(-[A-Z]{2})?)"
        r"-(?P<version>[0-9]+-[0-9]+?))\.%s" % _ext
    )

    def __init__(self, mw):
        self.mw = mw
        os.environ["QTWEBENGINE_DICTIONARIES_PATH"] = self.dictFolder()

    # Common
    ######################################################################

    def dictFolder(self):
        pm = self.mw.pm
        return pm._ensureExists(os.path.join(pm.base, "dictionaries"))

    def _pathForLang(self, lang):
        path = os.path.join(self.dictFolder(), lang.filename + "." + self._ext)
        if not os.path.exists(path):
            return None
        return path

    def _langName(self, code):
        """Return full verbose name for specified language code"""
        return langs.get(code, code)
    
    def _versionTuple(self, vstring):
        return tuple(int(n) for n in vstring.split('-'))

    def _parseFilename(self, fullname):
        match = self._dict_re.fullmatch(fullname)
        if match is None:
            return None

        filename = match.group("filename")
        code = match.group("code")
        version = self._versionTuple(match.group("version"))

        return filename, code, version
    
    # Local
    ######################################################################

    def localLangs(self):
        """
        Return a list of all locally installed language codes
        """
        langs = []
        for full_name in os.listdir(self.dictFolder()):
            if not full_name.endswith(self._ext):
                continue
            filename = os.path.splitext(full_name)[0]
            info = self._parseFilename(full_name)
            if info is None:
                code, version = filename, None
            else:
                _, code, version = info
            verbose = self._langName(code)
            langs.append(Language(verbose, code, version, filename))

        mapped = OrderedDict((lang.code, lang) for lang in sorted(langs))

        return mapped

    def deleteLang(self, lang):
        path = self._pathForLang(lang)
        if not path:
            return
        send2trash(path)

    # Remote
    ######################################################################

    # List available languages

    def remoteLangs(self, silent=False):
        self.mw.progress.start(immediate=True)
        try:
            langs = []
            for entry in self._getRemoteDirectoryListing():
                filename = entry["name"]
                info = self._parseFilename(filename)
                if info is None:
                    continue
                filename, code, version = info
                verbose = self._langName(code)
                langs.append(Language(verbose, code, version, filename))
        except IOError as e:
            if not silent:
                showWarning((_("Please check your internet connection.") +
                            "\n\n" + str(e)), textFormat="plain")
            return
        finally:
            self.mw.progress.finish()
        
        mapped = OrderedDict((lang.code, lang) for lang in sorted(langs))

        return mapped
    
    def _getRemoteDirectoryListing(self):
        client = AnkiRequestsClient()
        resp = client.get(self._api_url + "?format=JSON")
        if resp.status_code != 200:
            raise Exception("Unexpected response code: {}".format(resp.status_code))
        # Strip 5-byte prefix that's used for XSSI prevention:
        json_content = resp.text[5:]
        entries = json.loads(json_content)["entries"]
        return entries

    # Download languages

    def downloadLangs(self, langs):
        log = []
        errs = []
        self.mw.progress.start(immediate=True)
        try:
            for lang in langs:
                full_name = lang.filename + "." + self._ext
                url = self._api_url + full_name + '?format=TEXT'

                ret = download(self.mw, url)
                if ret[0] == "error":
                    if isinstance(ret[1], int):
                        msg = _("Unexpected response code: %s" % ret[1])
                    else:
                        msg = (_("Please check your internet connection.") +
                               "\n\n" + ret[1])
                    errs.append(_("Error downloading %(lang)s: %(error)s")
                                % dict(lang=lang.verbose, error=msg))
                    continue
                
                data, f = ret
                self._install(base64.b64decode(data), full_name)
                
                log.append(_("Downloaded %(lang)s" % dict(
                    lang=lang.verbose)))
        finally:
            self.mw.progress.finish()
        
        return log, errs

    def _install(self, data, full_name):
        dest = os.path.join(self.dictFolder(), full_name)
        if os.path.exists(dest):
            send2trash(dest)
        with open(dest, "bw") as dict_file:
            dict_file.write(data)

    # Updates

    def checkForUpdates(self, silent=False):
        local_langs = self.localLangs()
        remote_langs = self.remoteLangs(silent=silent)
        if remote_langs is None or local_langs is None:
            return None, None, None
        
        updates = []
        obsolete = []
        for code, local_lang in local_langs.items():
            remote_lang = remote_langs.get(code)
            if not remote_lang:
                continue
            if remote_lang.version > local_lang.version:
                updates.append(remote_lang)
                obsolete.append(local_lang)
        
        return remote_langs, updates, obsolete

    def updateLangs(self, updates, obsolete):
        for lang in obsolete:
            self.deleteLang(lang)
        return self.downloadLangs(updates)


def initSpellcheckManager():
    from aqt import mw
    from aqt.qt import qtminor
    from anki import version
    
    try:
        vtuple = tuple(int(i) for i in version.split("."))
    except IndexError:
        vtuple = (0, 0, 0)
    
    if vtuple < (2, 1, 10) or qtminor < 10:
        mw.spellcheckManager = None
    else:
        mw.spellcheckManager = SpellcheckManager(mw)
