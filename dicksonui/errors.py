class EvalError(Exception):
    '''Creates an instance representing an error that occurs regarding the global function eval().'''


class InternalError(RuntimeError):
    '''Creates an instance representing an error that occurs when an internal error in the JavaScript engine is thrown. E.g. "too much recursion".'''


class RangeError(IndexError):
    '''Creates an instance representing an error that occurs when a numeric variable or parameter is outside of its valid range.'''


class ReferenceError(ReferenceError):
    '''Creates an instance representing an error that occurs when de-referencing an invalid reference.'''


class SyntaxError(SyntaxError):
    '''Creates an instance representing a syntax error.'''


class TypeError(TypeError):
    '''Creates an instance representing an error that occurs when a variable or parameter is not of a valid type.'''


class URIError(Exception):
    '''Creates an instance representing an error that occurs when encodeURI() or decodeURI() are passed invalid parameters.
    Constructor'''


jserrors = {
    "EvalError": EvalError,
    "InternalError": InternalError,
    "RangeError": RangeError,
    "ReferenceError": ReferenceError,
    "SyntaxError": SyntaxError,
    "TypeError": TypeError,
    "URIError": URIError,
    "Error": Exception
}
