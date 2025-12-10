from collections.abc import Callable

from .base import Function1D

class PythonFunction1D(Function1D):
    """
    Wraps a python callable object with a Function1D object.

    This class allows a python object to interact with cython code that requires
    a Function1D object. The python object must implement __call__() expecting
    one argument.

    This class is intended to be used to transparently wrap python objects that
    are passed via constructors or methods into cython optimised code. It is not
    intended that the users should need to directly interact with these wrapping
    objects. Constructors and methods expecting a Function1D object should be
    designed to accept a generic python object and then test that object to
    determine if it is an instance of Function1D. If the object is not a
    Function1D object it should be wrapped using this class for internal use.

    See also: autowrap_function1d()

    :param object function: the python function to wrap, __call__() function must be
    implemented on the object.
    """

    function: Callable[[float], float]
    def __init__(self, function: Callable[[float], float]) -> None: ...

def _autowrap_function1d(obj: Function1D | float | Callable[[float], float]) -> Function1D:
    """Expose cython function for testing."""
