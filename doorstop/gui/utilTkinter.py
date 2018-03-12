#!/usr/bin/env python

import tkinter as tk


class HyperlinkManager(object):
    def __init__(self, text) -> None:

        self.text = text

        self.text.tag_config("hyper", underline=True)

        self.text.tag_bind("hyper", "<Enter>", self._enter)
        self.text.tag_bind("hyper", "<Leave>", self._leave)
        self.text.tag_bind("hyper", "<Button-1>", self._click)

        self.reset()

    def reset(self):
        """ remove all hyperlinks"""
        self.links = {}

    def add(self, action, id, p_Tags=[]):
        """
        Add a new hyper link

        @param action: method that will be called for this hyperlink
        @param id: the arbitration id that we are associating this action.
        """
        # add an action to the manager.  returns tags to use in
        # associated text widget
        thetags = []
        uniquetag = "hyper-%d" % len(self.links)
        thetags.extend(p_Tags)
        thetags.append("hyper")
        thetags.append(uniquetag)
        self.links[uniquetag] = [action, id]
        return tuple(thetags)

    def _enter(self, event):
        self.text.config(cursor="hand2")

    def _leave(self, event):
        self.text.config(cursor="")

    def _click(self, event):
        """
        If somebody clicks on the link it will find the method to call
        """
        for tag in self.text.tag_names(tk.CURRENT):
            if tag[:6] == "hyper-":
                self.links[tag][0](self.links[tag][1])
