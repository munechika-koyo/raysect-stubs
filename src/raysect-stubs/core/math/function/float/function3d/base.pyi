from collections.abc import Callable
from typing import TypeAlias, overload

from ..base import FloatFunction

_Function3DCallable: TypeAlias = Callable[[float, float, float], float]

class Function3D(FloatFunction):
    """
    Cython optimised class for representing an arbitrary 3D function returning a float.

    Using __call__() in cython is slow. This class provides an overloadable
    cython cdef evaluate() method which has much less overhead than a python
    function call.

    For use in cython code only, this class cannot be extended via python.

    To create a new function object, inherit this class and implement the
    evaluate() method. The new function object can then be used with any code
    that accepts a function object.
    """

    def __call__(self, x: float, y: float, z: float) -> float:
        """Evaluate the function f(x, y, z)

        :param float x: function parameter x
        :param float y: function parameter y

        :param float z: function parameter z
        :rtype: float
        """
    @overload
    def __add__(self, other: Function3D | _Function3DCallable, /) -> AddFunction3D: ...
    @overload
    def __add__(self, other: float, /) -> AddScalar3D: ...
    @overload
    def __radd__(self, other: Function3D | _Function3DCallable, /) -> AddFunction3D: ...
    @overload
    def __radd__(self, other: float, /) -> AddScalar3D: ...
    @overload
    def __sub__(self, other: Function3D | _Function3DCallable, /) -> SubtractFunction3D: ...
    @overload
    def __sub__(self, other: float, /) -> AddScalar3D: ...
    @overload
    def __rsub__(self, other: Function3D | _Function3DCallable, /) -> SubtractFunction3D: ...
    @overload
    def __rsub__(self, other: float, /) -> SubtractScalar3D: ...
    @overload
    def __mul__(self, other: Function3D | _Function3DCallable, /) -> MultiplyFunction3D: ...
    @overload
    def __mul__(self, other: float, /) -> MultiplyScalar3D: ...
    @overload
    def __rmul__(self, other: Function3D | _Function3DCallable, /) -> MultiplyFunction3D: ...
    @overload
    def __rmul__(self, other: float, /) -> MultiplyScalar3D: ...
    @overload
    def __truediv__(self, other: Function3D | _Function3DCallable, /) -> DivideFunction3D: ...
    @overload
    def __truediv__(self, other: float, /) -> MultiplyScalar3D: ...
    @overload
    def __rtruediv__(self, other: Function3D | _Function3DCallable, /) -> DivideFunction3D: ...
    @overload
    def __rtruediv__(self, other: float, /) -> DivideScalar3D: ...
    @overload
    def __mod__(self, other: Function3D | _Function3DCallable, /) -> ModuloFunction3D: ...
    @overload
    def __mod__(self, other: float, /) -> ModuloFunctionScalar3D: ...
    @overload
    def __rmod__(self, other: Function3D | _Function3DCallable, /) -> ModuloFunction3D: ...
    @overload
    def __rmod__(self, other: float, /) -> ModuloScalarFunction3D: ...
    def __neg__(self) -> MultiplyScalar3D: ...
    @overload
    def __pow__(self, other: Function3D | _Function3DCallable, modulo: None = None, /) -> PowFunction3D: ...
    @overload
    def __pow__(self, other: float, modulo: None = None, /) -> PowFunctionScalar3D: ...
    @overload
    def __pow__(self, other: Function3D | _Function3DCallable | float, modulo: Function3D | _Function3DCallable, /) -> ModuloFunction3D: ...
    @overload
    def __pow__(self, other: Function3D | _Function3DCallable | float, modulo: float, /) -> ModuloFunctionScalar3D: ...
    @overload
    def __rpow__(self, other: Function3D | _Function3DCallable, modulo: None = None, /) -> PowFunction3D: ...
    @overload
    def __rpow__(self, other: float, modulo: None = None, /) -> PowScalarFunction3D: ...
    def __abs__(self) -> AbsFunction3D: ...
    @overload  # type: ignore[override]
    def __eq__(self, other: Function3D | _Function3DCallable, /) -> EqualsFunction3D: ...  # pyrefly: ignore [bad-override]
    @overload
    def __eq__(self, other: float, /) -> EqualsScalar3D: ...
    @overload  # type: ignore[override]
    def __ne__(self, other: Function3D | _Function3DCallable, /) -> NotEqualsFunction3D: ...  # pyrefly: ignore [bad-override]
    @overload
    def __ne__(self, other: float, /) -> NotEqualsScalar3D: ...
    @overload
    def __lt__(self, other: Function3D | _Function3DCallable, /) -> LessThanFunction3D: ...
    @overload
    def __lt__(self, other: float, /) -> GreaterThanScalar3D: ...
    @overload
    def __le__(self, other: Function3D | _Function3DCallable, /) -> LessEqualsFunction3D: ...
    @overload
    def __le__(self, other: float, /) -> GreaterEqualsScalar3D: ...
    @overload
    def __gt__(self, other: Function3D | _Function3DCallable, /) -> GreaterThanFunction3D: ...
    @overload
    def __gt__(self, other: float, /) -> LessThanScalar3D: ...
    @overload
    def __ge__(self, other: Function3D | _Function3DCallable, /) -> GreaterEqualsFunction3D: ...
    @overload
    def __ge__(self, other: float, /) -> LessEqualsScalar3D: ...

class AddFunction3D(Function3D):
    """
    A Function3D class that implements the addition of the results of two Function3D objects: f1() + f2()

    This class is not intended to be used directly, but rather returned as the result of an __add__() call on a
    Function3D object.

    :param function1: A Function3D object.
    :param function2: A Function3D object.
    """
    def __init__(self, function1: Function3D | _Function3DCallable | float, function2: Function3D | _Function3DCallable | float) -> None: ...

class SubtractFunction3D(Function3D):
    """
    A Function3D class that implements the subtraction of the results of two Function3D objects: f1() - f2()

    This class is not intended to be used directly, but rather returned as the result of a __sub__() call on a
    Function3D object.

    :param function1: A Function3D object.
    :param function2: A Function3D object.
    """
    def __init__(self, function1: Function3D | _Function3DCallable | float, function2: Function3D | _Function3DCallable | float) -> None: ...

class MultiplyFunction3D(Function3D):
    """
    A Function3D class that implements the multiplication of the results of two Function3D objects: f1() * f2()

    This class is not intended to be used directly, but rather returned as the result of a __mul__() call on a
    Function3D object.

    :param function1: A Function3D object.
    :param function2: A Function3D object.
    """
    def __init__(self, function1: Function3D | _Function3DCallable | float, function2: Function3D | _Function3DCallable | float) -> None: ...

class DivideFunction3D(Function3D):
    """
    A Function3D class that implements the division of the results of two Function3D objects: f1() / f2()

    This class is not intended to be used directly, but rather returned as the result of a __truediv__() call on a
    Function3D object.

    :param function1: A Function3D object.
    :param function2: A Function3D object.
    """
    def __init__(self, function1: Function3D | _Function3DCallable | float, function2: Function3D | _Function3DCallable | float) -> None: ...

class ModuloFunction3D(Function3D):
    """
    A Function3D class that implements the modulo of the results of two Function3D objects: f1() % f2()

    This class is not intended to be used directly, but rather returned as the result of a __mod__() call on a
    Function3D object.

    :param object function1: A Function3D object or Python callable.
    :param object function2: A Function3D object or Python callable.
    """
    def __init__(self, function1: Function3D | _Function3DCallable | float, function2: Function3D | _Function3DCallable | float) -> None: ...

class PowFunction3D(Function3D):
    """
    A Function3D class that implements the pow() operator on two Function3D objects.

    This class is not intended to be used directly, but rather returned as the result of a __pow__() call on a
    Function3D object.

    :param object function1: A Function3D object or Python callable.
    :param object function2: A Function3D object or Python callable.
    """
    def __init__(self, function1: Function3D | _Function3DCallable | float, function2: Function3D | _Function3DCallable | float) -> None: ...

class AbsFunction3D(Function3D):
    """
    A Function3D class that implements the absolute value of the result of a Function3D object: abs(f()).

    This class is not intended to be used directly, but rather returned as the
    result of an __abs__() call on a Function3D object.

    :param object function: A Function3D object or Python callable.
    """
    def __init__(self, function: Function3D | _Function3DCallable | float) -> None: ...

class EqualsFunction3D(Function3D):
    """
    A Function3D class that tests the equality of the results of two Function3D objects: f1() == f2()

    This class is not intended to be used directly, but rather returned as the result of an __eq__() call on a
    Function3D object.

    :param object function1: A Function3D object or Python callable.
    :param object function2: A Function3D object or Python callable.
    """
    def __init__(self, function1: Function3D | _Function3DCallable | float, function2: Function3D | _Function3DCallable | float) -> None: ...

class NotEqualsFunction3D(Function3D):
    """
    A Function3D class that tests the inequality of the results of two Function3D objects: f1() != f2()

    This class is not intended to be used directly, but rather returned as the result of an __ne__() call on a
    Function3D object.

    :param object function1: A Function3D object or Python callable.
    :param object function2: A Function3D object or Python callable.
    """
    def __init__(self, function1: Function3D | _Function3DCallable | float, function2: Function3D | _Function3DCallable | float) -> None: ...

class LessThanFunction3D(Function3D):
    """
    A Function3D class that implements < of the results of two Function3D objects: f1() < f2()

    This class is not intended to be used directly, but rather returned as the result of an __lt__() call on a
    Function3D object.

    :param object function1: A Function3D object or Python callable.
    :param object function2: A Function3D object or Python callable.
    """
    def __init__(self, function1: Function3D | _Function3DCallable | float, function2: Function3D | _Function3DCallable | float) -> None: ...

class GreaterThanFunction3D(Function3D):
    """
    A Function3D class that implements > of the results of two Function3D objects: f1() > f2()

    This class is not intended to be used directly, but rather returned as the result of a __gt__() call on a
    Function3D object.

    :param object function1: A Function3D object or Python callable.
    :param object function2: A Function3D object or Python callable.
    """
    def __init__(self, function1: Function3D | _Function3DCallable | float, function2: Function3D | _Function3DCallable | float) -> None: ...

class LessEqualsFunction3D(Function3D):
    """
    A Function3D class that implements <= of the results of two Function3D objects: f1() <= f2()

    This class is not intended to be used directly, but rather returned as the result of an __le__() call on a
    Function3D object.

    :param object function1: A Function3D object or Python callable.
    :param object function2: A Function3D object or Python callable.
    """
    def __init__(self, function1: Function3D | _Function3DCallable | float, function2: Function3D | _Function3DCallable | float) -> None: ...

class GreaterEqualsFunction3D(Function3D):
    """
    A Function3D class that implements >= of the results of two Function3D objects: f1() >= f2()

    This class is not intended to be used directly, but rather returned as the result of an __ge__() call on a
    Function3D object.

    :param object function1: A Function3D object or Python callable.
    :param object function2: A Function3D object or Python callable.
    """
    def __init__(self, function1: Function3D | _Function3DCallable | float, function2: Function3D | _Function3DCallable | float) -> None: ...

class AddScalar3D(Function3D):
    """
    A Function3D class that implements the addition of scalar and the result of a Function3D object: K + f()

    This class is not intended to be used directly, but rather returned as the result of an __add__() call on a
    Function3D object.

    :param value: A double value.
    :param function: A Function3D object or Python callable.
    """
    def __init__(self, value: float, function: Function3D | _Function3DCallable | float) -> None: ...

class SubtractScalar3D(Function3D):
    """
    A Function3D class that implements the subtraction of scalar and the result of a Function3D object: K - f()

    This class is not intended to be used directly, but rather returned as the result of an __sub__() call on a
    Function3D object.

    :param value: A double value.
    :param function: A Function3D object or Python callable.
    """
    def __init__(self, value: float, function: Function3D | _Function3DCallable | float) -> None: ...

class MultiplyScalar3D(Function3D):
    """
    A Function3D class that implements the multiplication of scalar and the result of a Function3D object: K * f()

    This class is not intended to be used directly, but rather returned as the result of an __mul__() call on a
    Function3D object.

    :param value: A double value.
    :param function: A Function3D object or Python callable.
    """
    def __init__(self, value: float, function: Function3D | _Function3DCallable | float) -> None: ...

class DivideScalar3D(Function3D):
    """
    A Function3D class that implements the subtraction of scalar and the result of a Function3D object: K / f()

    This class is not intended to be used directly, but rather returned as the result of an __div__() call on a
    Function3D object.

    :param value: A double value.
    :param function: A Function3D object or Python callable.
    """
    def __init__(self, value: float, function: Function3D | _Function3DCallable | float) -> None: ...

class ModuloScalarFunction3D(Function3D):
    """
    A Function3D class that implements the modulo of scalar and the result of a Function3D object: K % f()

    This class is not intended to be used directly, but rather returned as the result of a __mod__() call on a
    Function3D object.

    :param float value: A double value.
    :param object function: A Function3D object or Python callable.
    """
    def __init__(self, value: float, function: Function3D | _Function3DCallable | float) -> None: ...

class ModuloFunctionScalar3D(Function3D):
    """
    A Function3D class that implements the modulo of the result of a Function3D object and a scalar: f() % K

    This class is not intended to be used directly, but rather returned as the result of a __mod__() call on a
    Function3D object.

    :param object function: A Function3D object or Python callable.
    :param float value: A double value.
    """
    def __init__(self, function: Function3D | _Function3DCallable | float, value: float) -> None: ...

class PowScalarFunction3D(Function3D):
    """
    A Function3D class that implements the pow of scalar and the result of a Function3D object: K ** f()

    This class is not intended to be used directly, but rather returned as the result of an __pow__() call on a
    Function3D object.

    :param float value: A double value.
    :param object function: A Function3D object or Python callable.
    """
    def __init__(self, value: float, function: Function3D | _Function3DCallable | float) -> None: ...

class PowFunctionScalar3D(Function3D):
    """
    A Function3D class that implements the pow of the result of a Function3D object and a scalar: f() ** K

    This class is not intended to be used directly, but rather returned as the result of an __pow__() call on a
    Function3D object.

    :param object function: A Function3D object or Python callable.
    :param float value: A double value.
    """
    def __init__(self, function: Function3D | _Function3DCallable | float, value: float) -> None: ...

class EqualsScalar3D(Function3D):
    """
    A Function3D class that tests the equality of a scalar and the result of a Function3D object: K == f2()

    This class is not intended to be used directly, but rather returned as the result of an __eq__() call on a
    Function3D object.

    :param value: A double value.
    :param object function: A Function3D object or Python callable.
    """
    def __init__(self, value: float, function: Function3D | _Function3DCallable | float) -> None: ...

class NotEqualsScalar3D(Function3D):
    """
    A Function3D class that tests the inequality of a scalar and the result of a Function3D object: K != f2()

    This class is not intended to be used directly, but rather returned as the result of an __ne__() call on a
    Function3D object.

    :param value: A double value.
    :param object function: A Function3D object or Python callable.
    """
    def __init__(self, value: float, function: Function3D | _Function3DCallable | float) -> None: ...

class LessThanScalar3D(Function3D):
    """
    A Function3D class that implements < of a scalar and the result of a Function3D object: K < f2()

    This class is not intended to be used directly, but rather returned as the result of an __lt__() call on a
    Function3D object.

    :param value: A double value.
    :param object function: A Function3D object or Python callable.
    """
    def __init__(self, value: float, function: Function3D | _Function3DCallable | float) -> None: ...

class GreaterThanScalar3D(Function3D):
    """
    A Function3D class that implements > of a scalar and the result of a Function3D object: K > f2()

    This class is not intended to be used directly, but rather returned as the result of a __gt__() call on a
    Function3D object.

    :param value: A double value.
    :param object function: A Function3D object or Python callable.
    """
    def __init__(self, value: float, function: Function3D | _Function3DCallable | float) -> None: ...

class LessEqualsScalar3D(Function3D):
    """
    A Function3D class that implements <= of a scalar and the result of a Function3D object: K <= f2()

    This class is not intended to be used directly, but rather returned as the result of an __le__() call on a
    Function3D object.

    :param value: A double value.
    :param object function: A Function3D object or Python callable.
    """
    def __init__(self, value: float, function: Function3D | _Function3DCallable | float) -> None: ...

class GreaterEqualsScalar3D(Function3D):
    """
    A Function3D class that implements >= of a scalar and the result of a Function3D object: K >= f2()

    This class is not intended to be used directly, but rather returned as the result of an __ge__() call on a
    Function3D object.

    :param value: A double value.
    :param object function: A Function3D object or Python callable.
    """
    def __init__(self, value: float, function: Function3D | _Function3DCallable | float) -> None: ...
