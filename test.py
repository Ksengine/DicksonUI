#!/usr/bin/python
# -*- coding: utf-8 -*-
from dicksonui import Application, window
def accepted(event):
    print(document.getElementById('lcd').value)
mywindow=window()
document=mywindow.document
App = Application(('',1024))
App.add(mywindow)
document.body.innerHTML='''
<input id="lcd" type="text"/>
<button id="accept" onclick="dicksonui_event_handler(event)">send</button>
'''
mywindow.register('accept.click',accepted)
print("Navigate To - "+App.location)
mywindow.show()
