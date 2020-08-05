class fakeattr():
    def __init__(self, run, parent):
        self._run=run
        self._parent=parent

    def __str__(self):
        return str(self._run(self._parent+';',True))

    def __get__(self):
        return self._run(self._parent+';',True)

    def __call__(self, *args, **kwargs):
        e=kwargs.setdefault('e', False)
        if len(args)==1:
            self._run(self._parent+str(args)[:-2]+');',e)
        else:
            self._run(self._parent+str(args)+';',e)
    
    def __getattr__(self,name):
        if name=='_parent':
            return self.__dict__.get(name)
        if name=='_run':
            return self.__dict__.get(name)
        return fakeattr(self._run,self._parent+'.'+name)

    def __setattr__(self,name,value):
        if name=='_parent':
            self.__dict__[name]=value
        elif name=='_run':
            self.__dict__[name]=value
        else:
            if isinstance(value,str):
                value='"'+value+'"'
            self._run(self._parent+'.'+name+'='+str(value)+';')

    def __add__(self, value):
        return self.__get__()+value
     
    def __eq__(self,value):
        return self.__get__()==value
     
    def __ge__(self, value):
        return self.__get__()>=value
        
    def __gt__(self, value):
        return self.__get__()>value
        
    def __hash__(self, value):
        return hash(self.__get__())
        
    def __le__(self, value):
        return self.__get__()<=value
        
    def __len__(self, value):
        return len(self.__get__())
        
    def __lt__(self, value):
        return self.__get__()<value
        
    def __mod__(self, value):
        return self.__get__()%value
        
    def __mul__(self, value):
        return self.__get__()*value
        
    def __ne__(self, value):
        return self.__get__()!=value
        
    def __repr__(self, value):
        return repr(self.__get__())
        
    def __rmod__(self, value):
        return value % self.__get__()
        
    def __rmul__(self, value):
        return value*self.__get__()
