from collections.abc import Callable

from .base import Function3D

class PythonFunction3D(Function3D):
    """
    Wraps a python callable object with a Function3D object.

    This class allows a python object to interact with cython code that requires
    a Function3D object. The python object must implement __call__() expecting
    three arguments.

    This class is intended to be used to transparently wrap python objects that
    are passed via constructors or methods into cython optimised code. It is not
    intended that the users should need to directly interact with these wrapping
    objects. Constructors and methods expecting a Function3D object should be
    designed to accept a generic python object and then test that object to
    determine if it is an instance of Function3D. If the object is not a
    Function3D object it should be wrapped using this class for internal use.

    See also: autowrap_function3d()
    """

    function: Callable[[float, float, float], float]

    def __init__(self, function: Callable[[float, float, float], float]) -> None: ...
