# -*- coding: utf-8 -*-

# Cloze Overlapper Add-on for Anki
#
# Copyright (C)  2016-2019 Aristotelis P. <https://glutanimate.com/>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version, with the additions
# listed at the end of the accompanied license file.
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
# terms and conditions of the GNU Affero General Public License which
# accompanied this program.
#
# If not, please request a copy through one of the means of contact
# listed here: <https://glutanimate.com/contact/>.
#
# Any modifications to this file must keep this entire header intact.

"""
Addon-wide constants
"""

from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

from ._version import __version__

__all__ = [
    "ADDON_NAME", "ADDON_ID", "ADDON_VERSION", "LINKS",
    "LICENSE", "LIBRARIES", "AUTHORS", "CONTRIBUTORS",
    "SPONSORS",
    "OLC_MODEL", "OLC_CARD", "OLC_MAX",
    "OLC_FLDS", "OLC_FLDS_IDS", "OLC_FIDS_PRIV"
]

# ADD-ON

ADDON_NAME = "Cloze Overlapper"
ADDON_ID = "969733775"
ADDON_VERSION = __version__
LINKS = {
    "help": "https://github.com/glutanimate/cloze-overlapper/wiki"
}
LICENSE = "GNU AGPLv3"
LIBRARIES = []
AUTHORS = [
    {"name": "Aristotelis P. (Glutanimate)", "years": "2016-2019",
     "contact": "https://glutanimate.com"}
]
# automatically sorted:
CONTRIBUTORS = ["zjosua"]
SPONSORS = []


# OLC

# default model
OLC_MODEL = "Cloze (overlapping)"
OLC_CARD = "cloze-ol"
OLC_MAX = 20

# default fields
OLC_FLDS = {
    'og': "Original",
    'tt': "Title",
    'rk': "Remarks",
    'sc': "Sources",
    'st': "Settings",
    'tx': "Text",
    'fl': "Full"
}
OLC_FLDS_IDS = ['og', 'tt', 'rk', 'sc', 'st', 'tx', 'fl']
OLC_FIDS_PRIV = ['og', 'st', 'tx', 'fl']  # non-user editable
