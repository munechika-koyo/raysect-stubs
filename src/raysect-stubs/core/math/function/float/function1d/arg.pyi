from .base import Function1D

class Arg1D(Function1D):
    """
    Returns the argument the function is passed, unmodified

    This is used to pass coordinates through to other functions in the
    function framework which expect a Function1D object.

    >>> arg = Arg1D()
    >>> arg(2)
    2.0
    >>> arg(-3.14)
    -3.14
    >>> squarer = Arg1D()**2
    >>> squarer(2)
    4.0
    >>> squarer(-3.14)
    9.8596
    """
