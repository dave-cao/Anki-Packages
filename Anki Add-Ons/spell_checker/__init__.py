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
Initializes add-on components.
"""

from ._version import __version__  # noqa: F401

from aqt.utils import showWarning
from anki.hooks import addHook

from .editor import initEditor
from .gui.preferences import initPreferences
from .gui import initializeQtResources
from .spellcheck import initSpellcheckManager

def init():
    try:
        from aqt import spellcheck  # noqa: F401
        showWarning("Spell checking is now natively integrated in Anki.<br>"
                    "Please uninstall the Spell Checker add-on.")
    except ImportError:
        initSpellcheckManager()
        initializeQtResources()
        initPreferences()
        initEditor()

addHook("profileLoaded", init)
