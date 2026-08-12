from collections.abc import Callable, Iterable
from typing import TypeAlias

from ....vector import Vector3D
from ...float.function1d.base import Function1D as FloatFunction1D
from ..base import Vector3DFunction

_VectorCallable1D: TypeAlias = Callable[[float], Vector3D]
_ScalarCallable1D: TypeAlias = Callable[[float], float]
_VectorOperand1D: TypeAlias = Function1D | _VectorCallable1D | Vector3D | Iterable[float]
_ScalarOperand1D: TypeAlias = FloatFunction1D | _ScalarCallable1D | float

class Function1D(Vector3DFunction):
    """
    Cython optimised class for representing an arbitrary 1D vector function.

    Using __call__() in cython is slow. This class provides an overloadable
    cython cdef evaluate() method which has much less overhead than a python
    function call.

    For use in cython code only, this class cannot be extended via python.

    To create a new function object, inherit this class and implement the
    evaluate() method. The new function object can then be used with any code
    that accepts a function object returning a Vector3D.
    """

    def __call__(self, x: float) -> Vector3D:
        """Evaluate the function f(x)

        :param float x: function parameter x
        :rtype: float
        """
    def __add__(self, other: _VectorOperand1D, /) -> AddFunction1D: ...
    def __radd__(self, other: _VectorOperand1D, /) -> AddFunction1D: ...
    def __sub__(self, other: _VectorOperand1D, /) -> SubtractFunction1D: ...
    def __rsub__(self, other: _VectorOperand1D, /) -> SubtractFunction1D: ...
    def __mul__(self, other: _ScalarOperand1D, /) -> MultiplyFunction1D: ...
    def __rmul__(self, other: _ScalarOperand1D, /) -> MultiplyFunction1D: ...
    def __truediv__(self, other: _ScalarOperand1D, /) -> DivideFunction1D: ...
    def __neg__(self) -> NegFunction1D: ...
    def __eq__(self, other: _VectorOperand1D, /) -> EqualsFunction1D: ...  # type: ignore[override]
    def __ne__(self, other: _VectorOperand1D, /) -> NotEqualsFunction1D: ...  # type: ignore[override]

class AddFunction1D(Function1D):
    """
    A vector3d.Function1D class that implements the addition of the results of two vector3d.Function1D objects: f1() + f2()

    This class is not intended to be used directly, but rather returned as the result of an __add__() call on a
    Function1D object.

    :param object function1: A vector3d.Function1D object or Python callable.
    :param object function2: A vector3d.Function1D object or Python callable.
    """

    def __init__(self, function1: _VectorOperand1D, function2: _VectorOperand1D) -> None: ...

class SubtractFunction1D(Function1D):
    """
    A vector3d.Function1D class that implements the subtraction of the results of two vector3d.Function1D objects: f1() - f2()

    This class is not intended to be used directly, but rather returned as the result of a __sub__() call on a
    Function1D object.

    :param object function1: A vector3d.Function1D object or Python callable.
    :param object function2: A vector3d.Function1D object or Python callable.
    """

    def __init__(self, function1: _VectorOperand1D, function2: _VectorOperand1D) -> None: ...

class MultiplyFunction1D(Function1D):
    """
    A vector3d.Function1D class that implements the multiplication of the result of a vector3d.Function1D object with the result of a float.Function1D object scalar: f1() * f2().

    This class is not intended to be used directly, but rather returned as the result of a __sub__() call on a
    vector3d.Function1D object.

    :param object function1: A vector3d.Function1D object or Python callable returning a Vector3D.
    :param object function2: A float.Function1D object or Python callable returning a double.
    """

    def __init__(self, function1: _VectorOperand1D, function2: _ScalarOperand1D) -> None: ...

class DivideFunction1D(Function1D):
    """
    A vector3d.Function1D class that implements the division of the results of a vector3d.Function1D object and a float.Function1D object: f1() / f2()

    This class is not intended to be used directly, but rather returned as the result of a __truediv__() call on a
    vector3d.Function1D object.

    :param object function1: A vector3d.Function1D object or Python callable returning a Vector3D.
    :param object function2: A float.Function1D object or Python callable returning a double.
    """

    def __init__(self, function1: _VectorOperand1D, function2: _ScalarOperand1D) -> None: ...

class NegFunction1D(Function1D):
    """
    A vector3d.Function1D class that implements the negation of the result of a vector3d.Function1D: -f().

    This class is not intended to be used directly, but rather returned as the result of a __neg__() call on a
    vector3d.Function1D object.

    :param object function: A vector3d.Function1D object or Python callable.
    """

    def __init__(self, function: _VectorOperand1D) -> None: ...

class EqualsFunction1D(FloatFunction1D):
    """
    A float.Function1D class that tests the equality of the results of two vector3d.Function1D objects: f1() == f2()

    This class is not intended to be used directly, but rather returned as the result of an __eq__() call on a
    vector3d.Function1D object.

    N.B. This is a float.Function1D class, so returns a double rather than a Vector3D.

    :param object function1: A vector3d.Function1D object or Python callable.
    :param object function2: A vector3d.Function1D object or Python callable.
    """

    def __init__(self, function1: _VectorOperand1D, function2: _VectorOperand1D) -> None: ...

class NotEqualsFunction1D(FloatFunction1D):
    """
    A float.Function1D class that tests the inequality of the results of two vector3d.Function1D objects: f1() != f2()

    This class is not intended to be used directly, but rather returned as the result of an __neq__() call on a
    vector3d.Function1D object.

    N.B. This is a float.Function1D class, so returns a double rather than a Vector3D.

    :param object function1: A vector3d.Function1D object or Python callable.
    :param object function2: A vector3d.Function1D object or Python callable.
    """

    def __init__(self, function1: _VectorOperand1D, function2: _VectorOperand1D) -> None: ...
