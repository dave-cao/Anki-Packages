# -*- coding: utf-8 -*-

# Spell Checker Add-on for Anki
#
# Copyright (C) 2018-2019  Aristotelis P. <https://glutanimate.com/>
# Copyright (C) Ankitects Pty Ltd and contributors
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

import time, re
from aqt.qt import *
from anki.sync import AnkiRequestsClient
from anki.hooks import addHook, remHook


def download(mw, url):
    "Download remote data (e.g. add-on). Caller must start & stop progress diag."
    # create downloading thread
    thread = Downloader(url)
    done = False
    def onRecv():
        if done:
            return
        mw.progress.update(label="%dKB downloaded" % (thread.recvTotal/1024))
    thread.recv.connect(onRecv)
    thread.start()
    while not thread.isFinished():
        mw.app.processEvents()
        thread.wait(100)

    # make sure any posted events don't fire after we return
    done = True

    if not thread.error:
        # success
        return thread.data, thread.fname
    else:
        return "error", thread.error

class Downloader(QThread):

    recv = pyqtSignal()

    def __init__(self, url):
        QThread.__init__(self)
        self.url = url
        self.error = None

    def run(self):
        # setup progress handler
        self.byteUpdate = time.time()
        self.recvTotal = 0
        def recvEvent(bytes):
            self.recvTotal += bytes
            self.recv.emit()
        addHook("httpRecv", recvEvent)
        client = AnkiRequestsClient()
        try:
            resp = client.get(self.url)
            if resp.status_code == 200:
                data = client.streamContent(resp)
            else:
                self.error = resp.status_code
                return
        except Exception as e:
            self.error = str(e)
            return
        finally:
            remHook("httpRecv", recvEvent)
        
        content_disp = resp.headers.get('content-disposition')
        if content_disp:
            m = re.match("attachment; filename=(.+)", content_disp)
            self.fname = m.group(1) if m else None

        self.data = data
