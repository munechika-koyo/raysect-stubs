from .base import Function1D, _VectorCallable1D

class PythonFunction1D(Function1D):
    """
    Wraps a python callable object with a Function1D object.

    This class allows a python object to interact with cython code that requires
    a Vector3DFunction1D object. The python object must implement __call__() expecting
    two arguments.

    This class is intended to be used to transparently wrap python objects that
    are passed via constructors or methods into cython optimised code. It is not
    intended that the users should need to directly interact with these wrapping
    objects. Constructors and methods expecting a Vector3DFunction1D object should be
    designed to accept a generic python object and then test that object to
    determine if it is an instance of Vector3DFunction1D. If the object is not a
    Vector3DFunction1D object it should be wrapped using this class for internal use.

    See also: autowrap_vectorfunction1d()

    :param object function: the python function to wrap, __call__() function must
    be implemented on the object.
    """

    function: _VectorCallable1D
    def __init__(self, function: _VectorCallable1D) -> None: ...
