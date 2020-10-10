#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  __init__.py
#
from .Control import *
from .Application import Application
from .bom import window
from .dom import document
from os import environ

loglevels={
    'CRITICAL' : 50,
    'DEBUG'    : 10,
    'ERROR'    : 40,
    'FATAL'    : 50,
    'INFO'     : 20,
    'NOTSET'   : 0 ,
    'WARN'     : 30,
    'WARNING'  : 30
}

def logLevel(level=None):
    if environ.get("logLevel"):
        environ["logLevel"]="0"
    if level==None:
        return int(environ["logLevel"])
    if isinstance(level, str):
        level=int(loglevels.get(level, level))
    environ["logLevel"]=str(level)
    return level
            
