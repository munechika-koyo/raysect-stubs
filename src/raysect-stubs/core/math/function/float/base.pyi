from ..base import Function

class FloatFunction(Function):
    """
    The base class of all functions that return a float.

    All functions that return a float or double derive from this class.
    """
    def __repr__(self) -> str: ...
