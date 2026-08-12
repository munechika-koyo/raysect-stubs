from collections.abc import Callable, Iterable
from typing import TypeAlias

from ....vector import Vector3D
from ...float.function3d.base import Function3D as FloatFunction3D
from ..base import Vector3DFunction

_VectorCallable3D: TypeAlias = Callable[[float, float, float], Vector3D]
_ScalarCallable3D: TypeAlias = Callable[[float, float, float], float]
_VectorOperand3D: TypeAlias = Function3D | _VectorCallable3D | Vector3D | Iterable[float]
_ScalarOperand3D: TypeAlias = FloatFunction3D | _ScalarCallable3D | float

class Function3D(Vector3DFunction):
    """
    Cython optimised class for representing an arbitrary 3D vector function.

    Using __call__() in cython is slow. This class provides an overloadable
    cython cdef evaluate() method which has much less overhead than a python
    function call.

    For use in cython code only, this class cannot be extended via python.

    To create a new function object, inherit this class and implement the
    evaluate() method. The new function object can then be used with any code
    that accepts a function object returning a Vector3D.
    """

    def __call__(self, x: float, y: float, z: float) -> Vector3D:
        """Evaluate the function f(x, y, z)

        :param float x: function parameter x
        :param float y: function parameter y
        :param float z: function parameter z

        :rtype: Vector3D
        """
    def __add__(self, other: _VectorOperand3D, /) -> AddFunction3D: ...
    def __radd__(self, other: _VectorOperand3D, /) -> AddFunction3D: ...
    def __sub__(self, other: _VectorOperand3D, /) -> SubtractFunction3D: ...
    def __rsub__(self, other: _VectorOperand3D, /) -> SubtractFunction3D: ...
    def __mul__(self, other: _ScalarOperand3D, /) -> MultiplyFunction3D: ...
    def __rmul__(self, other: _ScalarOperand3D, /) -> MultiplyFunction3D: ...
    def __truediv__(self, other: _ScalarOperand3D, /) -> DivideFunction3D: ...
    def __neg__(self) -> NegFunction3D: ...
    def __eq__(self, other: _VectorOperand3D, /) -> EqualsFunction3D: ...  # type: ignore[override]
    def __ne__(self, other: _VectorOperand3D, /) -> NotEqualsFunction3D: ...  # type: ignore[override]

class AddFunction3D(Function3D):
    """
    A vector3d.Function3D class that implements the addition of the results of two vector3d.Function3D objects: f1() + f2()

    This class is not intended to be used directly, but rather returned as the result of an __add__() call on a
    Function3D object.

    :param object function1: A vector3d.Function3D object or Python callable.
    :param object function2: A vector3d.Function3D object or Python callable.
    """

    def __init__(self, function1: _VectorOperand3D, function2: _VectorOperand3D) -> None: ...

class SubtractFunction3D(Function3D):
    """
    A vector3d.Function3D class that implements the subtraction of the results of two vector3d.Function3D objects: f1() - f2()

    This class is not intended to be used directly, but rather returned as the result of a __sub__() call on a
    Function3D object.

    :param object function1: A vector3d.Function3D object or Python callable.
    :param object function2: A vector3d.Function3D object or Python callable.
    """

    def __init__(self, function1: _VectorOperand3D, function2: _VectorOperand3D) -> None: ...

class MultiplyFunction3D(Function3D):
    """
    A vector3d.Function3D class that implements the multiplication of the result of a vector3d.Function3D object with the result of a float.Function3D object scalar: f1() * f2().

    This class is not intended to be used directly, but rather returned as the result of a __sub__() call on a
    vector3d.Function3D object.

    :param object function1: A vector3d.Function3D object or Python callable returning a Vector3D.
    :param object function2: A float.Function3D object or Python callable returning a double.
    """

    def __init__(self, function1: _VectorOperand3D, function2: _ScalarOperand3D) -> None: ...

class DivideFunction3D(Function3D):
    """
    A vector3d.Function3D class that implements the division of the results of a vector3d.Function3D object and a float.Function3D object: f1() / f2()

    This class is not intended to be used directly, but rather returned as the result of a __truediv__() call on a
    vector3d.Function3D object.

    :param object function1: A vector3d.Function3D object or Python callable returning a Vector3D.
    :param object function2: A float.Function3D object or Python callable returning a double.
    """

    def __init__(self, function1: _VectorOperand3D, function2: _ScalarOperand3D) -> None: ...

class NegFunction3D(Function3D):
    """
    A vector3d.Function3D class that implements the negation of the result of a vector3d.Function3D: -f().

    This class is not intended to be used directly, but rather returned as the result of a __neg__() call on a
    vector3d.Function3D object.

    :param object function: A vector3d.Function3D object or Python callable.
    """

    def __init__(self, function: _VectorOperand3D) -> None: ...

class EqualsFunction3D(FloatFunction3D):
    """
    A float.Function3D class that tests the equality of the results of two vector3d.Function3D objects: f1() == f2()

    This class is not intended to be used directly, but rather returned as the result of an __eq__() call on a
    vector3d.Function3D object.

    N.B. This is a float.Function3D class, so returns a double rather than a Vector3D.

    :param object function1: A vector3d.Function3D object or Python callable.
    :param object function2: A vector3d.Function3D object or Python callable.
    """

    def __init__(self, function1: _VectorOperand3D, function2: _VectorOperand3D) -> None: ...

class NotEqualsFunction3D(FloatFunction3D):
    """
    A float.Function3D class that tests the inequality of the results of two vector3d.Function3D objects: f1() != f2()

    This class is not intended to be used directly, but rather returned as the result of an __neq__() call on a
    vector3d.Function3D object.

    N.B. This is a float.Function3D class, so returns a double rather than a Vector3D.

    :param object function1: A vector3d.Function3D object or Python callable.
    :param object function2: A vector3d.Function3D object or Python callable.
    """

    def __init__(self, function1: _VectorOperand3D, function2: _VectorOperand3D) -> None: ...
