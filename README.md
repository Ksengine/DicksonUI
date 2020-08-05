# DicksonUI - The Best GUI Library For Python

![Build Python Package](https://github.com/Ksengine/DicksonUI/workflows/Build%20Python%20Package/badge.svg)

With DicksonUI, you can make Graphical User Interfaces with python with just few lines of code. DicksonUI is super easy to use and handles everything for you. Just write your code easily
or import any HTML code.

## Overview
The DicksonUI Python GUI Library was written with lightweight use in mind. It provides the following key features
- lightweight
- few dependancies (all are designed by me)- but micro version is independant.
- Cross-Platform(Windows, Linux, Mac)
- No Runtime Installer(Runtime is Browser)
- Low Ram Usage(less on your script, all used by browser)
- full featured(Many features of html,css,js)
- only python knowladge reqired.(knowladge about web technologies is better)
- browser based(Any device has a browser installed)
- powerful(power of bootstrap/AngularJS/React Coming Soon)
- Extensible(write your own plugin and share)
- HTML support - not just web pages - with js, css or any library(eg :-bootstap).
- The most common ui widgets available
- Events - with wide range of event data(all event is handling in own thread so no errors)
- never wait - all are thraded

## Usage

In the following paragraphs, I am going to describe how you can get and use DicksonUI for your own projects.

###  Getting it
To download dicksonui, either fork this Github repo or simply use Pypi via pip.
DicksonUI is available on python 2 and 3 both. Dosen"t require Additional dependencies
```sh
$ pip install dicksonui
```
If you use easy_install,  `easy_install dicksonui`.
If you don't like package managers, just download from Github and unzip   and run
```sh
$ python setup.py install
```

## Initialize a Window
First, let's create a new Application. 

```python
from dicksonui import Application, window
mywindow=window()
document=mywindow.document
App = Application(('',1024))
App.Add(mywindow)
mywindow.show()
```

#### Run!!! 
Run your code.
For Python 3
```sh
python3 myscript.py
```
Or, For Python 2
```sh
python myscript.py
```
wait a moment...

😥😥😥 Nothing!!!but a blank window.

#### Add items to form 
Okay, now that we will learn about Controls
```Python
from dicksonui import Application, window
mywindow=window()
document=mywindow.document
App = Application(('',1024))
App.Add(mywindow)
heading=document.createElement('h1')
heading.innerHTML='Hello World!'
document.body.appendChild(heading)
mywindow.show()
```
Ru
 it.
[view docs](https://dicksonui.gitbook.io)

[report bugs](https://github.com/Ksengine/DicksonUI/issues/new)

## alternatives?

-[RemI](https://github.com/dddomodossola/remi), which has exactly the same idea (build a GUI in Python, run it in a browser). Definitely worth a look.It is little heavy and use websockets. So it cannot run on older browsers. we used both websockets and long polling
-[tkinter](https://docs.python.org/3/library/tkinter.html#module-tkinter)  (standard library)

Advantages: it's well-known. Lots of people have written tutorials and documentation for it.

Disadvantages: it feels like a wrapper around Tk, because it is. This gives good performance and detailed control, but writing it feels unintuitive (to me). it isnt based on browsers and have limited features.

-[flexx](https://github.com/flexxui/flexx) is very large and had more dependencies, it use tornado server. but we use our own library.limited features! and you can easily mix server-side and client-side

-eel is an alternative for Electron but it is based on bottle server. and it is not a pythonic way.

##Ok until next time, Bye! 
