from .fakeattr import fakeattr

def var(name, attr):
    attr._run("window.%s=%s;"%(name, attr._parent))
    return fakeattr(attr._run, "window."+name)
