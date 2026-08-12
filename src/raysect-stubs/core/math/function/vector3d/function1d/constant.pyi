from collections.abc import Iterable

from ....vector import Vector3D
from .base import Function1D

class Constant1D(Function1D):
    """
    Wraps a Vector3D object with a Function1D object.

    This class allows a constant vector object to interact with cython code that
    requires a vector3d.Function1D object. The object must be convertible to a
    Vector3D. The value of the Vector3D constant will be returned independent of
    the arguments the function is called with.

    This class is intended to be used to transparently wrap python objects that
    are passed via constructors or methods into cython optimised code. It is not
    intended that the users should need to directly interact with these wrapping
    objects. Constructors and methods expecting a vector3d.function1D object should be
    designed to accept a generic python object and then test that object to
    determine if it is an instance of vector3d.Function1D. If the object is not a
    vector3d.Function1D object it should be wrapped using this class for internal use.

    See also: float3d.autowrap_function1d()

    :param object value: the constant value, convertible to Vector3D, to return when called.
    """

    def __init__(self, value: Vector3D | Iterable[float]) -> None: ...
