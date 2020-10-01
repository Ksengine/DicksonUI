import json


class fakeattr():
    def __init__(self, run, parent):
        self._run = run
        self._parent = parent

    def __get__(self):
        return self._run(self._parent+';', True)

    def __getattr__(self, name):
        attr = self.__dict__.get(name)
        if attr:
            return attr
        return fakeattr(self._run, self._parent+'.'+name)

    def __setattr__(self, name, value):
        if name == '_parent':
            self.__dict__[name] = value
        elif name == '_run':
            self.__dict__[name] = value
        else:
            try:
                self._run(self._parent+'.'+name+'='+json.dumps(value)+';')
            except:
                raise RuntimeError("cannot set this value( %s )" % value)

    def __repr__(self):
        try:
            return self.__str__()
        except:
            return "<object %s>" % self._parent

    def __str__(self):
        return self._run(self._parent+'.toString();', True)

    def __call__(self, *args, **kwargs):
        e = kwargs.setdefault('e', True)
        e = kwargs.pop('e')
        nargs = []
        for arg in args:
            if isinstance(arg, object):
                nargs.append(arg._parent)
            else:
                nargs.append(arg)
        try:
            self._run(self._parent+"("+json.dumps(list(nargs))[1:-1]+');', e)
        except Exception as e:
            raise e

    def __setitem__(self, key, value):
        try:
            if isinstance(key, int):
                self._run(self._parent +
                          json.dumps([key])+"="+json.dumps(value)+';')
            else:
                self.__setattr__(key, value)
        except Exception as e:
            raise e

    def __and__(self, value):
        return self.__get__() & value

    def __rand__(self, value):
        return value & self.__get__()

    def __xor__(self, value):
        return self.__get__() ^ value

    def __rxor__(self, value):
        return value ^ self.__get__()

    def __or__(self, value):
        return self.__get__() | value

    def __ror__(self, value):
        return value | self.__get__()

    def __hash__(self):
        return hash(self.__get__())

    def __getitem__(self, key):
        try:
            return self[key]
        except:
            try:
                return getattr(self.__get__(), key)
            except:
                return self[key]

    def __lt__(self, value):
        return self.__get__() < value

    def __le__(self, value):
        return self.__get__() <= value

    def __eq__(self, value):
        return self.__get__() == value

    def __ne__(self, value):
        return self.__get__() != value

    def __gt__(self, value):
        return self.__get__() > value

    def __ge__(self, value):
        return self.__get__() >= value

    def __add__(self, value):
        return self.__get__() + value

    def __radd__(self, value):
        return value + self.__get__()

    def __sub__(self, value):
        return self.__get__() - value

    def __rsub__(self, value):
        return value - self.__get__()

    def __mul__(self, value):
        return self.__get__() * value

    def __rmul__(self, value):
        return value * self.__get__()

    def __mod__(self, value):
        return self.__get__() % value

    def __rmod__(self, value):
        return value % self.__get__()

    def __divmod__(self, value):
        return divmod(self.__get__(), value)

    def __rdivmod__(self, value):
        return divmod(value, self.__get__())

    def __pow__(self, value, mod=None):
        return pow(self.__get__(), value, mod)

    def __rpow__(self, value, mod=None):
        return pow(value, self.__get__(), mod)

    def __neg__(self):
        return - self.__get__()

    def __pos__(self):
        return +self.__get__()

    def __abs__(self):
        return abs(self.__get__())

    def __bool__(self):
        return self._run(self._parent+'.valueOf() == 0 ? false : true;', True)

    def __invert__(self):
        return self._run('~'+self._parent+';', True)

    def __lshift__(self, value):
        return self.__get__() << value

    def __rlshift__(self, value):
        return value << self.__get__()

    def __rshift__(self, value):
        return self.__get__() >> value

    def __rrshift__(self, value):
        return value >> self.__get__()

    def __int__(self):
        return self._run(self._parent+'.parseInt();', True)

    def __float__(self):
        return self._run(self._parent+'.parseFloat();', True)

    def __floordiv__(self, value):
        return self.__get__() // value

    def __rfloordiv__(self, value):
        return value // self.__get__()

    def __truediv__(self, value):
        return self.__get__() / value

    def __rtruediv__(self, value):
        return value / self.__get__()

    def __index__(self):
        return self.__get__().__index__()

    def conjugate(self, *a, **kw):
        return self.__get__().conjugate(*a, **kw)

    def bit_length(self):
        return self.__get__().bit_length()

    def to_bytes(self, *a, **kw):
        return self.__get__().to_bytes(*a, **kw)

    @classmethod
    def from_bytes(self, *a, **kw):
        return self.__get__().from_bytes(*a, **kw)

    def __trunc__(self):
        return self.__get__().__trunc__()

    def __floor__(self, *a, **kw):
        return self.__get__().__floor__()

    def __ceil__(self, *a, **kw):
        return self._run('Math.ceil('+self._parent+');', True)

    def __round__(self, ndigits=None):
        return round(self.__get__(), ndigits)

    def __getnewargs__(self):
        return self.__get__().__getnewargs__()

    def __format__(self, format_spec=''):
        return format(self.__get__(), format_spec)

    def __sizeof__(self):
        return self.__get__().__sizeof__()

    @property
    def real(self):
        return self.__get__().real

    @property
    def imag(self):
        return self.__get__().imag

    @property
    def numerator(self):
        return self.__get__().numerator

    @property
    def denominator(self):
        return self.__get__().denominator

    def as_integer_ratio(self):
        return self.__get__().as_integer_ratio()

    @classmethod
    def fromhex(self, string):
        return self.__get__().fromhex(string)

    def hex(self):
        return hex(self.__get__())

    def is_integer(self):
        return self.__get__().is_integer()

    @classmethod
    def __getformat__(self, typestr):
        return self.__get__().__getformat__(typestr)

    @classmethod
    def __set_format__(self, typestr, fmt):
        return self.__get__().__set_format__(typestr, fmt)

    def __iter__(self):
        return iter(self.__get__())

    def __len__(self):
        return self._run(self._parent+'.length;', True)

    def __contains__(self, key):
        return key in self.__get__()

    def encode(self, encoding='utf-8', errors='strict'):
        return self.__get__().encode(encoding, errors)

    def replace(self, old, new, count=-1):
        if count == -1:
            return self._run(self._parent+'.replace(/%s/g,"%s");' % (old, new), True)

    def split(self, sep=None, maxsplit=-1):
        r = self._run(self._parent+'.split("%s");%', True)
        if maxsplit > -1:
            return r[:maxsplit]
        return r

    def rsplit(self, sep=None, maxsplit=-1):
        return self.__get__().rsplit(sep, maxsplit)

    def join(self, iterable):
        return self.__get__().join(iterable)

    def capitalize(self):
        return self.__get__().capitalize(*a, **kw)

    def casefold(self, *a, **kw):
        return self.__get__().casefold(*a, **kw)

    def title(self):
        return self.__get__().title()

    def center(self, width, fillchar=' '):
        return self.__get__().center(width, fillchar)

    def count(self, *a, **kw):
        return self.__get__().count(*a, **kw)

    def expandtabs(self, tabsize=8):
        return self.__get__().expandtabs(tabsize)

    def find(self, sub, start=0, end=2147483647):
        if stop == 2147483647:
            r = self._run(self._parent+'.indexOf("%s",%i);' %
                          (value, start), True)
        else:
            r = self._run(self._parent+'.slice(%i,%i).indexOf("%s");' %
                          (start, end, value), True)
        return r

    def partition(self, *a, **kw):
        return self.__get__().partition(*a, **kw)

    def ljust(self, width, fillchar=' '):
        return self.__get__().ljust(width, fillchar)

    def lower(self):
        return self._run(self._parent+'.toLowerCase();', True)

    def lstrip(self, chars=None):
        return self.__get__().lstrip(chars)

    def rfind(self, sub, start=0, end=2147483647):
        if stop == 2147483647:
            r = self._run(self._parent+'.LastIndexOf("%s",%i);' %
                          (value, start), True)
        else:
            r = self._run(self._parent+'.slice(%i,%i).LastindexOf("%s");' %
                          (start, end, value), True)
        return r

    def rindex(self, value, start=0, stop=2147483647):
        if stop == 2147483647:
            r = self._run(self._parent+'.lastIndexOf("%s",%i);' %
                          (value, start), True)
        else:
            r = self._run(self._parent+'.slice(%i,%i).LastindexOf("%s");' %
                          (start, stop, value), True)
        if r == -1:
            raise ValueError("substring not found")
        return r

    def rjust(self, width, fillchar=' '):
        return self.__get__().rjust(width, fillchar)

    def rstrip(self, chars=None):
        return self.__get__().rstrip(chars)

    def rpartition(self, sep):
        return self.__get__().rpartition(sep)

    def splitlines(self, keepends=False):
        return self.__get__().splitlines(keepends)

    def strip(self, chars=None):
        ie8code = '''if (!String.prototype.trim) {
  String.prototype.trim = function () {
    return this.replace(/^[\\s\\uFEFF\\xA0]+|[\\s\\uFEFF\\xA0]+$/g, '');
  };
};'''  # for IE 8
        if not chars:
            try:
                return self._run(self._parent+'.trim();', True)
            except:
                return self._run(ie8code+self._parent+'.trim();', True)
        return self.__get__().strip(chars)

    def swapcase(self):
        return self.__get__().swapcase()

    def translate(self, table):
        return self.__get__().translate(table)

    def upper(self):
        c

    def startswith(self, *a, **kw):
        return self.__get__().rindex(*a, **kw)

    def endswith(self, *a, **kw):
        return self.__get__().endswith(*a, **kw)

    def isascii(self):
        return self.__get__().isascii()

    def islower(self):
        return self.__get__().islower()

    def isupper(self):
        return self.__get__().isupper()

    def istitle(self):
        return self.__get__().istitle()

    def isspace(self):
        return self.__get__().isspace()

    def isdecimal(self):
        return self.__get__().isdecimal()

    def isdigit(self):
        return self.__get__().isdigit()

    def isnumeric(self):
        return self.__get__().isnumeric()

    def isalpha(self):
        return self.__get__().isalpha()

    def isalnum(self):
        return self.__get__().isalnum()

    def isidentifier(self):
        return self.__get__().isidentifier()

    def isprintable(self):
        return self.__get__().isprintable()

    def zfill(self, width):
        return self.__get__().zfill(width)

    def format(self, *a, **kw):
        return self.__get__().format(*a, **kw)

    def format_map(self, *a, **kw):
        return self.__get__().format_map(*a, **kw)

    @staticmethod
    def maketrans(x, y=None, z=None):
        return self.__get__().maketrans(x, y, z)

    def __delitem__(self, key):
        self._run(self._parent+".pop("+str(int(key))+");", False)

    def __iadd__(self, value):
        try:
            self._run(self._parent+"+="+json.dumps(value)+';', False)
        except Exception as e:
            raise e

    def __imul__(self, value):
        try:
            self._run(self._parent+"*="+json.dumps(value)+';', False)
        except Exception as e:
            raise e

    def __iter__(self):
        return iter(self.__get__())

    def __reversed__(self):
        return reversed(self.__get__())

    def append(self, object):
        try:
            self._run(self._parent+".concat("+json.dumps(object)+');', False)
        except Exception as e:
            raise e

    def clear(self):
        try:
            self._run(self._parent+"=[];", False)
        except Exception as e:
            raise e

    def copy(self):
        return self.__get__()

    def count(self, value):
        return self.__get__().count()

    def extend(self, iterable):
        try:
            self._run(self._parent +
                      ".push("+json.dumps(list(iterable))[1:-1]+');', False)
        except Exception as e:
            raise e

    def index(self, value, start=0, stop=2147483647):
        if stop == 2147483647:
            r = self._run(self._parent+'.indexOf(%s,%i);' %
                          (json.dumps(value), start), True)
        else:
            r = self._run(self._parent+'.slice(%i,%i).LastindexOf("%s");' %
                          (start, stop, json.dumps(value)), True)
        if r == -1:
            raise ValueError("substring not found")
        return r
        return self.__get__().index(value, start, stop)

    def insert(self, index, object):
        self._run(self._parent+".splice(%i,0,%s);" %
                  (index, json.dumps(object)))

    def pop(self, index=-1):  # TODO: working with dicts
        try:
            if index > -1:
                self._run(self._parent+".pop("+str(index)+");")
            else:
                self._run(self._parent+".pop();")
        except Exception as e:
            raise e

    def remove(self, value):
        self._run("if(! %s in %s){throw Error('list.remove(x): x not in list')};%s.splice(%s.indexOf(%s),1);" % (
            json.dumps(value), self._parent, self._parent, self._parent, json.dumps(value)))

    def reverse(self):
        self._run(self._parent+".reverse();")

    def sort(self, key=None, reverse=False):
        code = "%s.sort(function(a, b){if(a<b){return -1};if(a>b){return 1};return 0});"
        if key:
            arr = self.__get__()
            arr.sort(key=key, reverse=reverse)
            self._run(self._parent+"=%s;" % json.dumps(arr))
            return
        if reverse:
            self._run(code % self._parent+self.parent+'.reverse();')
        else:
            self._run(code % self._parent)

    def items(self):
        return self.__get__().items()

    def keys(self):
        return self.__get__().items()

    def values(self):
        return self.__get__().values()

    def popitem(self):
        return self.__get__().popitem()

    def setdefault(self, key, default=None):
        return self.__get__().setdefault(self, key, default)

    def update(self, *a, **kw):
        new = {}
        new.update(*a, **kw)
        src = ""
        for i in new:
            src += self._parent+"."+i+"="+json.dumps(new[i])+";"
        self._run(src, False)

    @classmethod
    def fromkeys(self, iterable, value=None):
        return self.__get__().fromkeys(iterable, value)
