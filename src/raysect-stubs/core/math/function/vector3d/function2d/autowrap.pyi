from .base import Function2D, _VectorCallable2D

class PythonFunction2D(Function2D):
    """
    Wraps a python callable object with a Function2D object.

    This class allows a python object to interact with cython code that requires
    a Vector3DFunction2D object. The python object must implement __call__() expecting
    two arguments.

    This class is intended to be used to transparently wrap python objects that
    are passed via constructors or methods into cython optimised code. It is not
    intended that the users should need to directly interact with these wrapping
    objects. Constructors and methods expecting a Vector3DFunction2D object should be
    designed to accept a generic python object and then test that object to
    determine if it is an instance of Vector3DFunction2D. If the object is not a
    Vector3DFunction2D object it should be wrapped using this class for internal use.

    See also: autowrap_vectorfunction2d()

    :param object function: the python function to wrap, __call__() function must
    be implemented on the object.
    """

    function: _VectorCallable2D
    def __init__(self, function: _VectorCallable2D) -> None: ...
