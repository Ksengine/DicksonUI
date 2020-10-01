#!/usr/bin/python
# -*- coding: utf-8 -*-
from signalpy import *
import signalpy.jslib
from .jslib import lib
from multiprocessing import Process
try:
    import webview
except:
    webview = False
    try:
        import webruntime
        runtime = 'browser'
        for _runtime, cls in webruntime._runtimes.items():
            try:
                if webruntime._runtimes[_runtime]()._get_exe():
                    if _runtime == 'firefox':
                        runtime = 'app'
                        break
                    elif _runtime == 'nw':
                        runtime = 'app'
                        break
                    elif _runtime == 'chrome':
                        runtime = 'chrome-app'
                        break
                    elif _runtime == 'pyqt':
                        runtime = 'pyqt-app'
                        break
                    elif _runtime == 'browser':
                        runtime = 'browser'
                        break
                    else:
                        runtime = _runtime+'-browser'
            except:
                pass
    except:
        webruntime = None
        import webbrowser

__all__ = ['Application']


class Application():
    '''
    DicksonUI Application 
    handle all windows and Extentions
    eg:
    |    app=Application()
    '''

    def __init__(self, address=('', None)):
        self._forms = []
        self.shown_forms = []
        self._counter = 0
        self.Icon = b'DicksonUI'
        self.app = app
        self.Hub = Hub
        self.server = Server(address)
        self.server.serve_forever()
        self.location = 'http://'+self.server.base_environ.get(
            'SERVER_NAME')+':'+self.server.base_environ.get('SERVER_PORT')
        app.routes['/'] = self.mainhandler
        app.routes['/favicon.ico'] = self.faviconhandler
        app.routes['/DicksonUI.js'] = self.jslibhandler

    def mainhandler(self, environ, start_response):
        fn = self._forms[0].Name
        start_response(
            '302 Object moved temporarily -- see URI list', [('Location', fn)])
        res = self.location + '/' + fn
        return res.encode()

    def faviconhandler(self, environ, start_response):
        start_response('200 OK', [])
        return[self.Icon]

    def jslibhandler(self, environ, start_response):
        start_response('200 OK', [])
        return[signalpy.jslib.data.encode()+lib.encode()]

    def add(self, bom):
        """ Add window to Application

        gives a name to window if not.
        initialize window
        """
        if bom.Name == None:
            self._counter += 1
            bom.Name = 'Window' + str(self._counter)
            self._forms.append(bom)
            bom.initialize(self)
        else:
            self._forms.append(bom)
            bom.initialize(self)

    def stop(self):
        """ stop server

        shutdowns server
        closes socket
        stop Application
        """
        self.server.shutdown()
        self.server.socket.close()
        self.server = None
        self = None

    def show_window(self, bom, **kw):
        """ show window

        shows window using pywebview, webruntime or webbrowser.
        """
        if webview:
            w = webview.create_window(bom.Name, self.location+'/'+bom.Name)
            t = Process(target=webview.start, kwargs=kw)
            t.daemon = True
            t.start()
            return w
        elif webruntime:
            return webruntime.launch(self.location+'/'+bom.Name, runtime)
        else:
            return webbrowser.open(self.location+'/'+bom.Name)

    def __repr__(self):
        _repr = __name__+".Application"
        if self.parent:
            _repr += " at "+self.location
        return _repr
