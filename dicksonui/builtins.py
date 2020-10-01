from .fakeattr import fakeattr


class undefined():
    def __init__(self, window):
        self.run = window.run
        self.name = 'undefined'

    def __getattr__(self, name):
        d = self.__dict__.get(name, "yvci62432po947efb734b")
        if d != "yvci62432po947efb734b":
            return d
        return fakeattr(self.run, self.name+'.'+name)

    def __setattr__(self, name, attr):
        if name in ['run', 'name']:
            self.__dict__[name] = attr
        else:
            try:
                self.run(self.name+'.'+name+'='+json.dumps(value)+';')
            except:
                raise RuntimeError("cannot set this value( %s )" % value)


class Number(undefined):
    def __init__(self, window):
        self.run = window.run
        self.name = 'Number'


class Boolean(undefined):
    def __init__(self, window):
        self.run = window.run
        self.name = 'Boolean'


class String(undefined):
    def __init__(self, window):
        self.run = window.run
        self.name = 'String'


class Array(undefined):
    def __init__(self, window):
        self.run = window.run
        self.name = 'Array'


class Math(undefined):
    def __init__(self, window):
        self.run = window.run
        self.name = 'Math'
