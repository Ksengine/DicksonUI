import json
import logging
from .fakeattr import fakeattr
from .template import template
from .errors import jserrors
from .dom import document as dom
logger = logging.getLogger(__name__)
__all__ = ['window']


class _event():
    pass


class window():
    """ Window - The Browser Object Model

    There are no official standards for the Browser Object Model (BOM).

    Since modern browsers have implemented (almost) the same methods and 
    properties for JavaScript interactivity, it is often referred to, as 
    methods and properties of the BOM.

        The Window Object

    The window object is supported by all browsers. It represents the browser's window.

    All global JavaScript objects, functions, and variables automatically 
    become members of the window object.

    Global variables are properties of the window object.

    Global functions are methods of the window object.

    Even the document object (of the HTML DOM) is a property of the window 
    object:

    >>> window.document.getElementById("header");
    is the same as:

    >>> document.getElementById("header");

    eg:
    |    mywindow=window()
    |    document=mywindow.document
    |    app.add(mywindow)
    """
    document = dom()

    def __init__(self):
        self.script = ''
        self.control_counter = 0
        self.Name = None
        self.eval_id = 0
        self.eval_list = {}
        self.func_list = {}
        self.client = None
        self.clients = {}
        self.webview = None
        self.parent = None

    def initialize(self, parent):
        self.parent = parent
        self.parent.app.routes['/'+self.Name] = self.temphandler
        self.Hub = self.parent.Hub('/'+self.Name+'/Hub')
        self.Hub.Message = self.msghandler
        self.Hub.Client = self.clienthandler

    def clienthandler(self, client):
        if self.client:
            w = window()
            w.parent = self.parent
            w.Hub = self.Hub
            self.clients[client] = w
            w.clienthandler(client)
            w.onload = self.onload
        self.client = client
        if len(self.script):
            self.Hub.Send(self.script, self.client)
        self.document.initialize(self)
        self.onload(self)

    def temphandler(self, environ, start_response):
        status = '200 OK'
        response_headers = [('Content-Type', 'text/html')]
        start_response(status, response_headers)
        return[template.encode()]

    def msghandler(self, message, client):
        if client != self.client:
            self.clients[client].msghandler(message, client)
        try:
            obj = json.loads(message)
        except Exception as e:
            print(e)
            return
        if obj.get('target') != None:
            myid = int(obj['target'])
            self.eval_list[myid] = obj['data']
        else:
            myid = obj['ftarget']
            fake_target = self.document.createElement('fake')
            fake_target.id = obj['data']['target']
            fake_target.initialize(self.document)
            fake_ctarget = self.document.createElement('fake')
            fake_ctarget.id = obj['data']['currentTarget']
            fake_ctarget.initialize(self.document)
            obj['data']['target'] = fake_target
            obj['data']['currentTarget'] = fake_ctarget
            event_object = _event()
            event_object.__dict__ = obj['data']
            funcs = self.func_list[myid]
            for func in funcs:
                func(event_object)

    def format_js(self, string):
        for i, r in "\rr", "\tt", "\aa", "\ff", "\vv", "\bb", "\nn":
            string = string.replace(i, "\\"+r)
        return string

    def evaluate(self, script):
        """ evaluate javascript statements

        ** only single expression supported **

        - try to evaluate script
        - raise errors if any
        - return value
        """
        script = self.format_js(script)
        self.run('sd={};try{sd.data=' + script + 'if(sd.data===undefined){throw new '
                 + 'ReferenceError()}}catch(err){sd.data={};sd.data.error=true;'
                 + 'sd.data.name=err.name;sd.data.message=err.message;};sd.target='
                 + str(self.eval_id) + ';sock.send(JSON.stringify(JSON.decycle(sd)));')
        myid = self.eval_id
        self.eval_id += 1
        self.eval_list[myid] = ''
        while self.eval_list[myid] == '':
            pass
        else:
            rdata = self.eval_list[myid]
            del self.eval_list[myid]
            e = None
            try:
                e = rdata['error']
                name = rdata["name"]
                message = rdata["message"]
                e = jserrors.get(name)
            except:
                pass
            if e:
                raise e(message)
            return rdata

    def run(self, script, e=False):
        """ run javascript

        for e option see window.evaluate

        ** multiple statements supported **

        - try to run script
        - will not raise errors
        - return None always
        """
        script = self.format_js(script)
        if self.client:
            if e:
                return self.evaluate(script)
            else:
                self.Hub.Send(script, self.client)
        else:
            if e:
                raise Exception("Cannot evaluate before run Application.")
            else:
                self.script += script

    def __getattr__(self, name):
        d = self.__dict__.get(name, "yvci62432po947efb734b")
        if self.webview:
            d = getattr(self.webview, name, d)
        if d != "yvci62432po947efb734b":
            return d
        return fakeattr(self.run, 'window.'+name)

    def __setattr__(self, name, attr):
        if name in ['script', 'control_counter', 'Name', 'eval_id', 'eval_list', 'func_list', 'parent', 'Hub', 'client', 'clients', 'onload', 'webview']:
            self.__dict__[name] = attr
        else:
            try:
                self.run('window.'+name+'='+json.dumps(value)+';')
            except:
                raise RuntimeError("cannot set this value( %s )" % value)

    def register(self, identifier, function):
        """ register events

        identifier is a string

        function is a callable python object
        """
        if self.func_list.get(identifier):
            self.func_list[identifier].append(function)
        else:
            self.func_list[identifier] = [function]

    def onload(self, window):
        """ onload event

        Implement this to work with multiple clients .
        """
        return

    def show(self):
        """ show window

        shows window using pywebview, webruntime or webbrowser.
        """
        self.webview = self.parent.show_window(self)

    def __repr__(self):
        _repr = __name__+".window"
        if self.Name:
            _repr += "( "+self.Name+" )"
        if self.parent:
            _repr += " at "+self.parent.location+'/'+self.Name
        return _repr
