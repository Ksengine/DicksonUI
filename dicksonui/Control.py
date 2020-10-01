#!/usr/bin/python
# -*- coding: utf-8 -*-

#
#  Control.py
#
from .fakeattr import fakeattr
import json
__all__ = ['Control']


class Control:
    def __init__(self, TagName):
        self._hosted = False  # Is added to Form
        self.script = ''  # Javascript code (Used before added to Form)
        self.id = None
        self.script += 'var Control = document.createElement("' \
            + TagName + '");'
        self.Controls = []
        self.handlers = {}

    def initialize(self, parent):
        self.parent = parent
        if not self.id:
            parent.controls_id_index += 1
            self.id = str(parent.controls_id_index)
        self._run = parent._run
        self.register = parent.register
        self._hosted = True
        for handler in self.handlers:
            for function in self.handlers[handler]:
                self.register(self.id+'.'+handler, function)
        return self.script + 'Control.id = "' + self.id + '";'

    def child_handler(self):
        for Control in self.Controls:
            self.appendChild(Control)

    def run(self, message, evaluate=False):
        """This will change script(Javascript) """
        if self._hosted:  # check if control is added to Form
            if evaluate:
                return self._run('document.getElementById("'
                                 + self.id + '").' + message, True)
            else:
                self._run('document.getElementById("' + self.id
                          + '").' + message)
        else:
            if evaluate:
                raise Exception("Cannot evaluate before run Application.")
            self.script += 'Control.'
            self.script += message

    def appendChild(self, child):
        if self._hosted:
            self._run(child.initialize(self.parent)+'document.getElementById("'
                      + self.id + '").appendChild(Control);')
            child.child_handler()
        else:
            self.Controls.append(child)

    def __getattr__(self, name):
        d = self.__dict__.get(name)
        if d:
            return d
        return fakeattr(self.run, name)

    def __setattr__(self, name, attr):
        if name in ['script', '_hosted', 'id', 'Controls', 'parent', '_run', 'handlers', 'register']:
            self.__dict__[name] = attr
        else:
            try:
                self.run(name+'='+json.dumps(attr)+';')
            except:
                raise RuntimeError("cannot set this value( %s )" % attr)

    def addEventListener(self, _type, listner):
        if not self._hosted:
            if self.handlers.get(_type):
                self.handlers[_type].append(listner)
            else:
                self.handlers[_type] = [listner]
        else:
            self.register(self.id+'.'+_type, listner)
        self.run('addEventListener("'+_type+'",dicksonui_event_handler);')
