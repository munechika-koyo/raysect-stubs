from collections.abc import Callable
from typing import TypeAlias, overload

from ..base import FloatFunction

_Function2DCallable: TypeAlias = Callable[[float, float], float]

class Function2D(FloatFunction):
    """
    Cython optimised class for representing an arbitrary 2D function returning a float.

    Using __call__() in cython is slow. This class provides an overloadable
    cython cdef evaluate() method which has much less overhead than a python
    function call.

    For use in cython code only, this class cannot be extended via python.

    To create a new function object, inherit this class and implement the
    evaluate() method. The new function object can then be used with any code
    that accepts a function object.
    """

    def __call__(self, x: float, y: float) -> float:
        """Evaluate the function f(x, y)

        :param float x: function parameter x
        :param float y: function parameter y
        :rtype: float
        """
    @overload
    def __add__(self, other: Function2D | _Function2DCallable, /) -> AddFunction2D: ...
    @overload
    def __add__(self, other: float, /) -> AddScalar2D: ...
    @overload
    def __radd__(self, other: Function2D | _Function2DCallable, /) -> AddFunction2D: ...
    @overload
    def __radd__(self, other: float, /) -> AddScalar2D: ...
    @overload
    def __sub__(self, other: Function2D | _Function2DCallable, /) -> SubtractFunction2D: ...
    @overload
    def __sub__(self, other: float, /) -> AddScalar2D: ...
    @overload
    def __rsub__(self, other: Function2D | _Function2DCallable, /) -> SubtractFunction2D: ...
    @overload
    def __rsub__(self, other: float, /) -> SubtractScalar2D: ...
    @overload
    def __mul__(self, other: Function2D | _Function2DCallable, /) -> MultiplyFunction2D: ...
    @overload
    def __mul__(self, other: float, /) -> MultiplyScalar2D: ...
    @overload
    def __rmul__(self, other: Function2D | _Function2DCallable, /) -> MultiplyFunction2D: ...
    @overload
    def __rmul__(self, other: float, /) -> MultiplyScalar2D: ...
    @overload
    def __truediv__(self, other: Function2D | _Function2DCallable, /) -> DivideFunction2D: ...
    @overload
    def __truediv__(self, other: float, /) -> MultiplyScalar2D: ...
    @overload
    def __rtruediv__(self, other: Function2D | _Function2DCallable, /) -> DivideFunction2D: ...
    @overload
    def __rtruediv__(self, other: float, /) -> DivideScalar2D: ...
    @overload
    def __mod__(self, other: Function2D | _Function2DCallable, /) -> ModuloFunction2D: ...
    @overload
    def __mod__(self, other: float, /) -> ModuloFunctionScalar2D: ...
    @overload
    def __rmod__(self, other: Function2D | _Function2DCallable, /) -> ModuloFunction2D: ...
    @overload
    def __rmod__(self, other: float, /) -> ModuloScalarFunction2D: ...
    def __neg__(self) -> MultiplyScalar2D: ...
    @overload
    def __pow__(self, other: Function2D | _Function2DCallable, modulo: None = None, /) -> PowFunction2D: ...
    @overload
    def __pow__(self, other: float, modulo: None = None, /) -> PowFunctionScalar2D: ...
    @overload
    def __pow__(self, other: Function2D | _Function2DCallable | float, modulo: Function2D | _Function2DCallable, /) -> ModuloFunction2D: ...
    @overload
    def __pow__(self, other: Function2D | _Function2DCallable | float, modulo: float, /) -> ModuloFunctionScalar2D: ...
    @overload
    def __rpow__(self, other: Function2D | _Function2DCallable, modulo: None = None, /) -> PowFunction2D: ...
    @overload
    def __rpow__(self, other: float, modulo: None = None, /) -> PowScalarFunction2D: ...
    def __abs__(self) -> AbsFunction2D: ...
    @overload  # type: ignore[override]
    def __eq__(self, other: Function2D | _Function2DCallable, /) -> EqualsFunction2D: ...  # pyrefly: ignore [bad-override]
    @overload
    def __eq__(self, other: float, /) -> EqualsScalar2D: ...
    @overload  # type: ignore[override]
    def __ne__(self, other: Function2D | _Function2DCallable, /) -> NotEqualsFunction2D: ...  # pyrefly: ignore [bad-override]
    @overload
    def __ne__(self, other: float, /) -> NotEqualsScalar2D: ...
    @overload
    def __lt__(self, other: Function2D | _Function2DCallable, /) -> LessThanFunction2D: ...
    @overload
    def __lt__(self, other: float, /) -> GreaterThanScalar2D: ...
    @overload
    def __le__(self, other: Function2D | _Function2DCallable, /) -> LessEqualsFunction2D: ...
    @overload
    def __le__(self, other: float, /) -> GreaterEqualsScalar2D: ...
    @overload
    def __gt__(self, other: Function2D | _Function2DCallable, /) -> GreaterThanFunction2D: ...
    @overload
    def __gt__(self, other: float, /) -> LessThanScalar2D: ...
    @overload
    def __ge__(self, other: Function2D | _Function2DCallable, /) -> GreaterEqualsFunction2D: ...
    @overload
    def __ge__(self, other: float, /) -> LessEqualsScalar2D: ...

class AddFunction2D(Function2D):
    """
    A Function2D class that implements the addition of the results of two Function2D objects: f1() + f2()

    This class is not intended to be used directly, but rather returned as the result of an __add__() call on a
    Function2D object.

    :param object function1: A Function2D object or Python callable.
    :param object function2: A Function2D object or Python callable.
    """
    def __init__(self, function1: Function2D | _Function2DCallable | float, function2: Function2D | _Function2DCallable | float) -> None: ...

class SubtractFunction2D(Function2D):
    """
    A Function2D class that implements the subtraction of the results of two Function2D objects: f1() - f2()

    This class is not intended to be used directly, but rather returned as the result of a __sub__() call on a
    Function2D object.

    :param object function1: A Function2D object or Python callable.
    :param object function2: A Function2D object or Python callable.
    """
    def __init__(self, function1: Function2D | _Function2DCallable | float, function2: Function2D | _Function2DCallable | float) -> None: ...

class MultiplyFunction2D(Function2D):
    """
    A Function2D class that implements the multiplication of the results of two Function2D objects: f1() * f2()

    This class is not intended to be used directly, but rather returned as the result of a __mul__() call on a
    Function2D object.

    :param object function1: A Function2D object or Python callable.
    :param object function2: A Function2D object or Python callable.
    """
    def __init__(self, function1: Function2D | _Function2DCallable | float, function2: Function2D | _Function2DCallable | float) -> None: ...

class DivideFunction2D(Function2D):
    """
    A Function2D class that implements the division of the results of two Function2D objects: f1() / f2()

    This class is not intended to be used directly, but rather returned as the result of a __truediv__() call on a
    Function2D object.

    :param object function1: A Function2D object or Python callable.
    :param object function2: A Function2D object or Python callable.
    """
    def __init__(self, function1: Function2D | _Function2DCallable | float, function2: Function2D | _Function2DCallable | float) -> None: ...

class ModuloFunction2D(Function2D):
    """
    A Function2D class that implements the modulo of the results of two Function2D objects: f1() % f2()

    This class is not intended to be used directly, but rather returned as the result of a __mod__() call on a
    Function2D object.

    :param object function1: A Function2D object or Python callable.
    :param object function2: A Function2D object or Python callable.
    """
    def __init__(self, function1: Function2D | _Function2DCallable | float, function2: Function2D | _Function2DCallable | float) -> None: ...

class PowFunction2D(Function2D):
    """
    A Function2D class that implements the pow() operator on two Function2D objects.

    This class is not intended to be used directly, but rather returned as the result of a __pow__() call on a
    Function2D object.

    :param object function1: A Function2D object or Python callable.
    :param object function2: A Function2D object or Python callable.
    """
    def __init__(self, function1: Function2D | _Function2DCallable | float, function2: Function2D | _Function2DCallable | float) -> None: ...

class AbsFunction2D(Function2D):
    """
    A Function2D class that implements the absolute value of the result of a Function2D object: abs(f()).

    This class is not intended to be used directly, but rather returned as the
    result of an __abs__() call on a Function2D object.

    :param object function: A Function2D object or Python callable.
    """
    def __init__(self, function: Function2D | _Function2DCallable | float) -> None: ...

class EqualsFunction2D(Function2D):
    """
    A Function2D class that tests the equality of the results of two Function2D objects: f1() == f2()

    This class is not intended to be used directly, but rather returned as the result of an __eq__() call on a
    Function2D object.

    :param object function1: A Function2D object or Python callable.
    :param object function2: A Function2D object or Python callable.
    """
    def __init__(self, function1: Function2D | _Function2DCallable | float, function2: Function2D | _Function2DCallable | float) -> None: ...

class NotEqualsFunction2D(Function2D):
    """
    A Function2D class that tests the inequality of the results of two Function2D objects: f1() != f2()

    This class is not intended to be used directly, but rather returned as the result of an __ne__() call on a
    Function2D object.

    :param object function1: A Function2D object or Python callable.
    :param object function2: A Function2D object or Python callable.
    """
    def __init__(self, function1: Function2D | _Function2DCallable | float, function2: Function2D | _Function2DCallable | float) -> None: ...

class LessThanFunction2D(Function2D):
    """
    A Function2D class that implements < of the results of two Function2D objects: f1() < f2()

    This class is not intended to be used directly, but rather returned as the result of an __lt__() call on a
    Function2D object.

    :param object function1: A Function2D object or Python callable.
    :param object function2: A Function2D object or Python callable.
    """
    def __init__(self, function1: Function2D | _Function2DCallable | float, function2: Function2D | _Function2DCallable | float) -> None: ...

class GreaterThanFunction2D(Function2D):
    """
    A Function2D class that implements > of the results of two Function2D objects: f1() > f2()

    This class is not intended to be used directly, but rather returned as the result of a __gt__() call on a
    Function2D object.

    :param object function1: A Function2D object or Python callable.
    :param object function2: A Function2D object or Python callable.
    """
    def __init__(self, function1: Function2D | _Function2DCallable | float, function2: Function2D | _Function2DCallable | float) -> None: ...

class LessEqualsFunction2D(Function2D):
    """
    A Function2D class that implements <= of the results of two Function2D objects: f1() <= f2()

    This class is not intended to be used directly, but rather returned as the result of an __le__() call on a
    Function2D object.

    :param object function1: A Function2D object or Python callable.
    :param object function2: A Function2D object or Python callable.
    """
    def __init__(self, function1: Function2D | _Function2DCallable | float, function2: Function2D | _Function2DCallable | float) -> None: ...

class GreaterEqualsFunction2D(Function2D):
    """
    A Function2D class that implements >= of the results of two Function2D objects: f1() >= f2()

    This class is not intended to be used directly, but rather returned as the result of an __ge__() call on a
    Function2D object.

    :param object function1: A Function2D object or Python callable.
    :param object function2: A Function2D object or Python callable.
    """
    def __init__(self, function1: Function2D | _Function2DCallable | float, function2: Function2D | _Function2DCallable | float) -> None: ...

class AddScalar2D(Function2D):
    """
    A Function2D class that implements the addition of scalar and the result of a Function2D object: K + f()

    This class is not intended to be used directly, but rather returned as the result of an __add__() call on a
    Function2D object.

    :param float value: A double value.
    :param object function: A Function2D object or Python callable.
    """
    def __init__(self, value: float, function: Function2D | _Function2DCallable | float) -> None: ...

class SubtractScalar2D(Function2D):
    """
    A Function2D class that implements the subtraction of scalar and the result of a Function2D object: K - f()

    This class is not intended to be used directly, but rather returned as the result of an __sub__() call on a
    Function2D object.

    :param value: A double value.
    :param function: A Function2D object or Python callable.
    """
    def __init__(self, value: float, function: Function2D | _Function2DCallable | float) -> None: ...

class MultiplyScalar2D(Function2D):
    """
    A Function2D class that implements the multiplication of scalar and the result of a Function2D object: K * f()

    This class is not intended to be used directly, but rather returned as the result of an __mul__() call on a
    Function2D object.

    :param value: A double value.
    :param function: A Function2D object or Python callable.
    """
    def __init__(self, value: float, function: Function2D | _Function2DCallable | float) -> None: ...

class DivideScalar2D(Function2D):
    """
    A Function2D class that implements the subtraction of scalar and the result of a Function2D object: K / f()

    This class is not intended to be used directly, but rather returned as the result of an __div__() call on a
    Function2D object.

    :param value: A double value.
    :param function: A Function2D object or Python callable.
    """
    def __init__(self, value: float, function: Function2D | _Function2DCallable | float) -> None: ...

class ModuloScalarFunction2D(Function2D):
    """
    A Function2D class that implements the modulo of scalar and the result of a Function2D object: K % f()

    This class is not intended to be used directly, but rather returned as the result of a __mod__() call on a
    Function2D object.

    :param float value: A double value.
    :param object function: A Function2D object or Python callable.
    """
    def __init__(self, value: float, function: Function2D | _Function2DCallable | float) -> None: ...

class ModuloFunctionScalar2D(Function2D):
    """
    A Function2D class that implements the modulo of the result of a Function2D object and a scalar: f() % K

    This class is not intended to be used directly, but rather returned as the result of a __mod__() call on a
    Function2D object.

    :param object function: A Function2D object or Python callable.
    :param float value: A double value.
    """
    def __init__(self, function: Function2D | _Function2DCallable | float, value: float) -> None: ...

class PowScalarFunction2D(Function2D):
    """
    A Function2D class that implements the pow of scalar and the result of a Function2D object: K ** f()

    This class is not intended to be used directly, but rather returned as the result of an __pow__() call on a
    Function2D object.

    :param float value: A double value.
    :param object function: A Function2D object or Python callable.
    """
    def __init__(self, value: float, function: Function2D | _Function2DCallable | float) -> None: ...

class PowFunctionScalar2D(Function2D):
    """
    A Function2D class that implements the pow of the result of a Function2D object and a scalar: f() ** K

    This class is not intended to be used directly, but rather returned as the result of an __pow__() call on a
    Function2D object.

    :param object function: A Function2D object or Python callable.
    :param float value: A double value.
    """
    def __init__(self, function: Function2D | _Function2DCallable | float, value: float) -> None: ...

class EqualsScalar2D(Function2D):
    """
    A Function2D class that tests the equality of a scalar and the result of a Function2D object: K == f2()

    This class is not intended to be used directly, but rather returned as the result of an __eq__() call on a
    Function2D object.

    :param value: A double value.
    :param object function: A Function2D object or Python callable.
    """
    def __init__(self, value: float, function: Function2D | _Function2DCallable | float) -> None: ...

class NotEqualsScalar2D(Function2D):
    """
    A Function2D class that tests the inequality of a scalar and the result of a Function2D object: K != f2()

    This class is not intended to be used directly, but rather returned as the result of an __ne__() call on a
    Function2D object.

    :param value: A double value.
    :param object function: A Function2D object or Python callable.
    """
    def __init__(self, value: float, function: Function2D | _Function2DCallable | float) -> None: ...

class LessThanScalar2D(Function2D):
    """
    A Function2D class that implements < of a scalar and the result of a Function2D object: K < f2()

    This class is not intended to be used directly, but rather returned as the result of an __lt__() call on a
    Function2D object.

    :param value: A double value.
    :param object function: A Function2D object or Python callable.
    """
    def __init__(self, value: float, function: Function2D | _Function2DCallable | float) -> None: ...

class GreaterThanScalar2D(Function2D):
    """
    A Function2D class that implements > of a scalar and the result of a Function2D object: K > f2()

    This class is not intended to be used directly, but rather returned as the result of a __gt__() call on a
    Function2D object.

    :param value: A double value.
    :param object function: A Function2D object or Python callable.
    """
    def __init__(self, value: float, function: Function2D | _Function2DCallable | float) -> None: ...

class LessEqualsScalar2D(Function2D):
    """
    A Function2D class that implements <= of a scalar and the result of a Function2D object: K <= f2()

    This class is not intended to be used directly, but rather returned as the result of an __le__() call on a
    Function2D object.

    :param value: A double value.
    :param object function: A Function2D object or Python callable.
    """
    def __init__(self, value: float, function: Function2D | _Function2DCallable | float) -> None: ...

class GreaterEqualsScalar2D(Function2D):
    """
    A Function2D class that implements >= of a scalar and the result of a Function2D object: K >= f2()

    This class is not intended to be used directly, but rather returned as the result of an __ge__() call on a
    Function2D object.

    :param value: A double value.
    :param object function: A Function2D object or Python callable.
    """
    def __init__(self, value: float, function: Function2D | _Function2DCallable | float) -> None: ...
