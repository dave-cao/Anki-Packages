# -*- mode: python ; coding: utf-8 -*-
# © 2012–2018 Roland Sieker <ospalh@gmail.com>
# https://github.com/ospalh/anki-addons/tree/develop/deck_name_in_title
# License: GNU AGPL, version 3 or later; http://www.gnu.org/licenses/agpl.html

"""
Anki 2.1 add-on to show the deck name in the window title.
"""

import functools
import sys
import os
import types
from anki.hooks import wrap, addHook
from aqt import mw

config = mw.addonManager.getConfig(__name__)

## Put these into the config file
## Several separators between the current ‘activity’ (file, directory,
## web page) and the program name seem common. Pick one to taste:
title_separator = ' – '
# title_separator = ' : '
# title_separator = ' - '

# How to separate the clicked-on deck from the subdeck.
subdeck_format = '{parent}:–:{child} ({homeDeck})'
# subdeck_format = '{parent}(::{child})'  # Old style

## Use either "Anki" or the program file name.
use_argv_0 = False
# use_argv_0 = True

__version__ = '1.4.0'


def wrapmethod(orig, wrapper, pos="after"):
    """Like anki.hooks.wrap, but for bound methods.
    Caveat: does not preserve function signatures."""

    wrapped = None
    if pos == "after":
        def wrapped(self, *args, **kwargs):
            orig(*args, **kwargs)
            return wrapper(*args, **kwargs)
    elif pos == "before":
        def wrapped(self, *args, **kwargs):
            wrapper(*args, **kwargs)
            return orig(*args, **kwargs)
    else:
        def wrapped(self, *args, **kwargs):
            return wrapper(_old=orig, *args, **kwargs)
    if not isinstance(wrapper, types.MethodType) or wrapper.__self__ is None:
        # wrapper is not a bound method, need to pass self
        wrapper = functools.partial(wrapper, orig.__self__)

    # Copy over attributes such as __name__ or __annotations__
    wrapped = functools.update_wrapper(wrapped, orig.__func__)
    # Convert wrapped function to bound method
    wrapped = wrapped.__get__(orig.__self__, orig.__class__)
    return wrapped


def get_prog_name():
    """Return either "Anki" org argv[0]"""
    if use_argv_0 and sys.argv[0]:
        return os.path.basename(sys.argv[0])
    return 'Anki'


class DeckNamer(object):
    """Functions to set the title to the deck name in Anki2 """

    def __init__(self):
        self.prog_name = get_prog_name()
        self.profile_string = ''
        self.deck_name = ''
        self.subdeck_name = ''
        self.homeDeck_name = ''
        
    def get_deck_name(self):
        """Return the deck name"""
        try:
            self.deck_name = mw.col.decks.current()['name']
        except AttributeError:
            self.deck_name = ''
        return self.deck_name

    def get_profile_string(self):
        """
        Return the profile name.

        When there is more than one profile, return that name,
        together with the title separator.
        """
        if len(mw.pm.profiles()) > 1 and mw.pm.name:
            self.profile_string = mw.pm.name + title_separator
        else:
            self.profile_string = ''
        return self.profile_string

    def deck_browser_title(self):
        """Set the window title when we are in the deck browser."""
        mw.setWindowTitle(self.get_profile_string() + self.prog_name)

    def overview_title(self):
        """Set the window title when we are at the overview."""
        mw.setWindowTitle(self.get_deck_name() + title_separator +
                          self.profile_string + self.prog_name)

    def card_title(self):
        """Set the window title when we are reviewing."""
        self.subdeck_name = mw.col.decks.get(mw.reviewer.card.did)['name']
        self.homeDeck_name = mw.col.decks.get(mw.reviewer.card.odid)['name']
        if self.homeDeck_name == 'Default':
            self.homeDeck_name = ''
        if self.subdeck_name == self.deck_name and self.homeDeck_name == '':
            self.overview_title()
            return
        mw.setWindowTitle(
            subdeck_format.format(
                parent=self.deck_name,
                child=self.subdeck_name[(len(self.deck_name) + 2):],
                homeDeck=self.homeDeck_name)
            + title_separator + self.profile_string + self.prog_name)


deck_namer = DeckNamer()
mw.deckBrowser.show = wrapmethod(mw.deckBrowser.show, deck_namer.deck_browser_title)
mw.overview.show = wrapmethod(mw.overview.show, deck_namer.overview_title)
addHook('showQuestion', deck_namer.card_title)
    

