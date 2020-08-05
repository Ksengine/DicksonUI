import json
import os
from .fakeattr import fakeattr
from .dom import document as dom
package_dir = os.path.dirname(__file__)

__all__=['window']

class _event():pass

class window():
    '''
    window class
    all window object methods and properties included.
    eg:
    |    mywindow=window()
    |    app.add(mywindow)
    '''
    document=dom()
    def __init__(self):
        self.script = ''
        self.control_counter = 0
        self.Name = None
        self.eval_id = 0
        self.eval_list = {}
        self.func_list = {}
        self.client=None
        self.webview=None

    def initialize(self, parent):
        self.parent=parent
        self.parent.app.routes['/'+self.Name]=self.temphandler
        self.Hub=self.parent.Hub('/'+self.Name+'/Hub')
        self.Hub.Message=self.msghandler
        self.Hub.Client=self.clienthandler

    def clienthandler(self, client):
        self.client=client
        self.Hub.Send(self.script,self.client)
        self.document.initialize(self)
        self.onload()

    def on_shown(self):
        self.webview.evaluate_js(self.script)
        print(self.script)
        self.document.initialize(self)
        self.onload()

    def temphandler(self, environ, start_response):
        path=os.path.join(package_dir,'index.html')
        status = '200 OK'
        response_headers = [('Content-Type', 'text/html')]
        start_response(status, response_headers)
        return[open(path).read().encode()]
            
    def msghandler(self, message, client):
        try:
            obj=json.loads(message)
        except Exception as e:
            print(e)
            return
        if obj.get('target') != None:
            myid = int(obj['target'])
            self.eval_list[myid] = obj['data']
        else:
            myid = obj['ftarget']
            fake_target=self.document.createElement('fake')
            fake_target.id=obj['data']['target']
            fake_target.initialize(self.document)
            fake_ctarget=self.document.createElement('fake')
            fake_ctarget.id=obj['data']['currentTarget']
            fake_ctarget.initialize(self.document)
            obj['data']['target']=fake_target
            obj['data']['currentTarget']=fake_ctarget
            event_object=_event()
            event_object.__dict__=obj['data']
            funcs=self.func_list[myid]
            for func in funcs:
                func(event_object)

    def evaluate(self, script):
        '''evaluate javascript statements'''
        self.run('sd={};sd.data=' + script + 'sd.target='
                 + str(self.eval_id) + ';sock.send(JSON.stringify(JSON.decycle(sd)));')
        myid = self.eval_id
        self.eval_id += 1
        self.eval_list[myid] = ''
        while self.eval_list[myid] == '':
            pass
        else:
            rdata = self.eval_list[myid]
            del self.eval_list[myid]
            return rdata

    def run(self, script,e=False):
        '''run javascript'''
        if self.client:
            if e:
                return self.evaluate(script)
            else:
                self.Hub.Send(script,self.client)
        else:
            if e:
                raise Exception("Cannot evaluate before run Application.")
            else:
                self.script+=script

    def __getattr__(self, name):
        d=self.__dict__.get(name)
        if self.webview:
            d=getattr(self.webview, name)
        if d:
            return d
        return fakeattr(self.run,'window.'+name)

    def __setattr__(self, name, attr):
        if name in ['script','control_counter','Name','eval_id','eval_list','func_list','parent','Hub','client','onload','webview']:
            self.__dict__[name]=attr
        else:
            if isinstance(attr,str):
                attr='"'+attr.replace('"','\\'+'"').replace('\'','\\'+'\'').replace('\n','\\'+'n')+'"'
            self.run(self._parent+'.'+name+'='+str(attr)+';')
    
    def register(self,identifier, function):
        '''register events'''
        if self.func_list.get(identifier):
            self.func_list[identifier].append(function)
        else:
            self.func_list[identifier]=[function]

    def onload(self):
        return

    def show(self):
        self.webview = self.parent.show_window(self)
