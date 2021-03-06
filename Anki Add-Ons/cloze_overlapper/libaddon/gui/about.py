# -*- coding: utf-8 -*-

# Libaddon for Anki
#
# Copyright (C) 2018  Aristotelis P. <https//glutanimate.com/>
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
Generate 'about' info, including credits, copyright, etc.
"""

from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

from ..consts import (ADDON_NAME, LICENSE, LIBRARIES,
                      AUTHORS, CONTRIBUTORS, MEMBERS_CREDITED, MEMBERS_TOP,
                      QRC_PREFIX)

from ..platform import ANKI20

if not ANKI20:
    string = str
else:
    import string

libs_header = (
    "<p>{} ships with the following open-source libraries:</p>".format(ADDON_NAME))

html_template = """\
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">
<html>
<head>
    <style type="text/css">
        ul {{
            margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;
        }}
        li {{
            margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;
        }}
        body {{
            margin-left: 10px; margin-right: 10px;
        }}
    </style>
</head>
<body>
    {title}
    <p><span style="font-weight:600;">Credits</span></p>
    {authors_string}
    <p>With patches from: <i>{contributors_string}</i></p>
    {libs_string}
    
    <p><img src="qrc:/{qrc_prefix}/icons/heart_small.svg"/><span style=" font-weight:600;"> Thank you!</span></p>
    <p>My heartfelt thanks go out to everyone who has <b>supported</b> this add-on through their tips,
        contributions, or any other means. You guys rock!</p>
    <p>In particular I would like to thank all of the awesome people who support me
        on <b><a href="https://www.patreon.com/glutanimate">Patreon</a></b>, including:</p>
    <p><i><span style="color:#aa2a4c;">{members_string}</span></i></p>
    <p><i>Want to be listed here?
        <b><a href="https://www.patreon.com/bePatron?u=7522179">Pledge your support on Patreon now</a></b>
        to receive all kinds of exclusive goodies!
    </i></p>
    
    <p><span style="font-weight:600;">License</span></p>
    <p><i>{display_name}</i> is <b>free and open-source</b> software. The add-on code that runs within
        Anki is released under the {license} license, extended by a number of additional terms.
        For more information please see the accompanied license file.</p>
    <p>This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY.
        Please see the license file for more details.</p>
</body>
</html>\
"""

authors_template = """\
<p>?? {years} <a href="{contact}">{name}</a></p>\
"""

libs_item_template = """\
<li><a href="{url}">{name}</a> ({version}), ?? {author}, {license}</li>\
"""

title_template = """\
<h3>About {display_name}</h3>\
"""

def get_about_string(title=False):
    authors_string = "\n".join(authors_template.format(**dct)
                               for dct in AUTHORS)
    libs_entries = "\n".join(libs_item_template.format(**dct)
                             for dct in LIBRARIES)
    if libs_entries:
        libs_string = "\n".join((libs_header, "<ul>", libs_entries, "</ul>"))
    else:
        libs_string = ""
    contributors_string = ", ".join(sorted(CONTRIBUTORS, key=string.lower))

    members_top_string = "<b>{}</b>".format(", ".join(MEMBERS_TOP))
    members_credited_string = ", ".join(MEMBERS_CREDITED)
    members_string = ", ".join((members_top_string, members_credited_string))

    if title:
        title_string = title_template.format(display_name=ADDON_NAME)
    else:
        title_string = ""

    return html_template.format(display_name=ADDON_NAME,
                                license=LICENSE,
                                title=title_string,
                                authors_string=authors_string,
                                libs_string=libs_string,
                                contributors_string=contributors_string,
                                members_string=members_string,
                                qrc_prefix=QRC_PREFIX)
