from collections.abc import Callable

from .base import Function2D

class PythonFunction2D(Function2D):
    """
    Wraps a python callable object with a Function2D object.

    This class allows a python object to interact with cython code that requires
    a Function2D object. The python object must implement __call__() expecting
    two arguments.

    This class is intended to be used to transparently wrap python objects that
    are passed via constructors or methods into cython optimised code. It is not
    intended that the users should need to directly interact with these wrapping
    objects. Constructors and methods expecting a Function2D object should be
    designed to accept a generic python object and then test that object to
    determine if it is an instance of Function2D. If the object is not a
    Function2D object it should be wrapped using this class for internal use.

    See also: autowrap_function2d()

    :param object function: the python function to wrap, __call__() function must
    be implemented on the object.
    """

    function: Callable[[float, float], float]

    def __init__(self, function: Callable[[float, float], float]) -> None: ...

def _autowrap_function2d(obj: Function2D | float | Callable[[float, float], float]) -> Function2D:
    """Expose cython function for testing."""
