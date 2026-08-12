from collections.abc import Callable, Iterable
from typing import TypeAlias

from ....vector import Vector3D
from ...float.function2d.base import Function2D as FloatFunction2D
from ..base import Vector3DFunction

_VectorCallable2D: TypeAlias = Callable[[float, float], Vector3D]
_ScalarCallable2D: TypeAlias = Callable[[float, float], float]
_VectorOperand2D: TypeAlias = Function2D | _VectorCallable2D | Vector3D | Iterable[float]
_ScalarOperand2D: TypeAlias = FloatFunction2D | _ScalarCallable2D | float

class Function2D(Vector3DFunction):
    """
    Cython optimised class for representing an arbitrary 2D vector function.

    Using __call__() in cython is slow. This class provides an overloadable
    cython cdef evaluate() method which has much less overhead than a python
    function call.

    For use in cython code only, this class cannot be extended via python.

    To create a new function object, inherit this class and implement the
    evaluate() method. The new function object can then be used with any code
    that accepts a function object returning a Vector3D.
    """

    def __call__(self, x: float, y: float) -> Vector3D:
        """Evaluate the function f(x, y)

        :param float x: function parameter x
        :param float y: function parameter y
        :rtype: float
        """
    def __add__(self, other: _VectorOperand2D, /) -> AddFunction2D: ...
    def __radd__(self, other: _VectorOperand2D, /) -> AddFunction2D: ...
    def __sub__(self, other: _VectorOperand2D, /) -> SubtractFunction2D: ...
    def __rsub__(self, other: _VectorOperand2D, /) -> SubtractFunction2D: ...
    def __mul__(self, other: _ScalarOperand2D, /) -> MultiplyFunction2D: ...
    def __rmul__(self, other: _ScalarOperand2D, /) -> MultiplyFunction2D: ...
    def __truediv__(self, other: _ScalarOperand2D, /) -> DivideFunction2D: ...
    def __neg__(self) -> NegFunction2D: ...
    def __eq__(self, other: _VectorOperand2D, /) -> EqualsFunction2D: ...  # type: ignore[override]
    def __ne__(self, other: _VectorOperand2D, /) -> NotEqualsFunction2D: ...  # type: ignore[override]

class AddFunction2D(Function2D):
    """
    A vector3d.Function2D class that implements the addition of the results of two vector3d.Function2D objects: f1() + f2()

    This class is not intended to be used directly, but rather returned as the result of an __add__() call on a
    Function2D object.

    :param object function1: A vector3d.Function2D object or Python callable.
    :param object function2: A vector3d.Function2D object or Python callable.
    """

    def __init__(self, function1: _VectorOperand2D, function2: _VectorOperand2D) -> None: ...

class SubtractFunction2D(Function2D):
    """
    A vector3d.Function2D class that implements the subtraction of the results of two vector3d.Function2D objects: f1() - f2()

    This class is not intended to be used directly, but rather returned as the result of a __sub__() call on a
    Function2D object.

    :param object function1: A vector3d.Function2D object or Python callable.
    :param object function2: A vector3d.Function2D object or Python callable.
    """

    def __init__(self, function1: _VectorOperand2D, function2: _VectorOperand2D) -> None: ...

class MultiplyFunction2D(Function2D):
    """
    A vector3d.Function2D class that implements the multiplication of the result of a vector3d.Function2D object with the result of a float.Function2D object scalar: f1() * f2().

    This class is not intended to be used directly, but rather returned as the result of a __sub__() call on a
    vector3d.Function2D object.

    :param object function1: A vector3d.Function2D object or Python callable returning a Vector3D.
    :param object function2: A float.Function2D object or Python callable returning a double.
    """

    def __init__(self, function1: _VectorOperand2D, function2: _ScalarOperand2D) -> None: ...

class DivideFunction2D(Function2D):
    """
    A vector3d.Function2D class that implements the division of the results of a vector3d.Function2D object and a float.Function2D object: f1() / f2()

    This class is not intended to be used directly, but rather returned as the result of a __truediv__() call on a
    vector3d.Function2D object.

    :param object function1: A vector3d.Function2D object or Python callable returning a Vector3D.
    :param object function2: A float.Function2D object or Python callable returning a double.
    """

    def __init__(self, function1: _VectorOperand2D, function2: _ScalarOperand2D) -> None: ...

class NegFunction2D(Function2D):
    """
    A vector3d.Function2D class that implements the negation of the result of a vector3d.Function2D: -f().

    This class is not intended to be used directly, but rather returned as the result of a __neg__() call on a
    vector3d.Function2D object.

    :param object function: A vector3d.Function2D object or Python callable.
    """

    def __init__(self, function: _VectorOperand2D) -> None: ...

class EqualsFunction2D(FloatFunction2D):
    """
    A float.Function2D class that tests the equality of the results of two vector3d.Function2D objects: f1() == f2()

    This class is not intended to be used directly, but rather returned as the result of an __eq__() call on a
    vector3d.Function2D object.

    N.B. This is a float.Function2D class, so returns a double rather than a Vector3D.

    :param object function1: A vector3d.Function2D object or Python callable.
    :param object function2: A vector3d.Function2D object or Python callable.
    """

    def __init__(self, function1: _VectorOperand2D, function2: _VectorOperand2D) -> None: ...

class NotEqualsFunction2D(FloatFunction2D):
    """
    A float.Function2D class that tests the inequality of the results of two vector3d.Function2D objects: f1() != f2()

    This class is not intended to be used directly, but rather returned as the result of an __neq__() call on a
    vector3d.Function2D object.

    N.B. This is a float.Function2D class, so returns a double rather than a Vector3D.

    :param object function1: A vector3d.Function2D object or Python callable.
    :param object function2: A vector3d.Function2D object or Python callable.
    """

    def __init__(self, function1: _VectorOperand2D, function2: _VectorOperand2D) -> None: ...
