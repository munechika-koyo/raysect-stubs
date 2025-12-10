from collections.abc import Callable
from typing import overload

from ..base import FloatFunction

class Function1D(FloatFunction):
    """
    Cython optimised class for representing an arbitrary 1D function returning a float.

    Using __call__() in cython is slow. This class provides an overloadable
    cython cdef evaluate() method which has much less overhead than a python
    function call.

    For use in cython code only, this class cannot be extended via python.

    To create a new function object, inherit this class and implement the
    evaluate() method. The new function object can then be used with any code
    that accepts a function object.
    """
    def __call__(self, x: float) -> float:
        """Evaluate the function f(x)

        :param float x: function parameter x
        :rtype: float
        """
    @overload
    def __add__(self, b: Callable[[float], float] | Function1D) -> AddFunction1D: ...
    @overload
    def __add__(self, b: float) -> AddScalar1D: ...
    @overload
    def __radd__(self, a: Callable[[float], float] | Function1D) -> AddFunction1D: ...
    @overload
    def __radd__(self, a: float) -> AddScalar1D: ...
    @overload
    def __sub__(self, b: Callable[[float], float] | Function1D) -> SubtractFunction1D: ...
    @overload
    def __sub__(self, b: float) -> SubtractScalar1D: ...
    @overload
    def __rsub__(self, a: Callable[[float], float] | Function1D) -> SubtractFunction1D: ...
    @overload
    def __rsub__(self, a: float) -> SubtractScalar1D: ...
    @overload
    def __mul__(self, b: Callable[[float], float] | Function1D) -> MultiplyFunction1D: ...
    @overload
    def __mul__(self, b: float) -> MultiplyScalar1D: ...
    @overload
    def __rmul__(self, a: Callable[[float], float] | Function1D) -> MultiplyFunction1D: ...
    @overload
    def __rmul__(self, a: float) -> MultiplyScalar1D: ...
    @overload
    def __truediv__(self, b: Callable[[float], float] | Function1D) -> DivideFunction1D: ...
    @overload
    def __truediv__(self, b: float) -> MultiplyScalar1D: ...
    @overload
    def __rtruediv__(self, a: Callable[[float], float] | Function1D) -> DivideFunction1D: ...
    @overload
    def __rtruediv__(self, a: float) -> DivideScalar1D: ...
    @overload
    def __mod__(self, b: Callable[[float], float] | Function1D) -> ModuloFunction1D: ...
    @overload
    def __mod__(self, b: float) -> ModuloFunctionScalar1D: ...
    @overload
    def __rmod__(self, a: Callable[[float], float] | Function1D) -> ModuloFunction1D: ...
    @overload
    def __rmod__(self, a: float) -> ModuloFunctionScalar1D: ...
    def __neg__(self) -> MultiplyScalar1D: ...
    @overload
    def __pow__(self, b: Callable[[float], float] | Function1D, c: Callable[[float], float] | Function1D) -> ModuloFunction1D: ...
    @overload
    def __pow__(self, b: Callable[[float], float] | Function1D, c: float) -> ModuloFunctionScalar1D: ...
    @overload
    def __pow__(self, b: Callable[[float], float] | Function1D, c: None = None) -> PowFunction1D: ...
    @overload
    def __pow__(self, b: float, c: None = None) -> PowFunctionScalar1D: ...
    def __rpow__(self, other): ...
    def __abs__(self) -> AbsFunction1D: ...
    @overload
    def __richcmp__(
        self, other: Callable[[float], float] | Function1D, op: int
    ) -> EqualsFunction1D | GreaterEqualsFunction1D | GreaterThanFunction1D | LessEqualsFunction1D | LessThanFunction1D | NotEqualsFunction1D: ...
    @overload
    def __richcmp__(self, other: float, op: int) -> EqualsScalar1D | GreaterEqualsScalar1D | GreaterThanScalar1D | LessEqualsScalar1D | LessThanScalar1D | NotEqualsScalar1D: ...

class AddFunction1D(Function1D):
    """
    A Function1D class that implements the addition of the results of two Function1D objects: f1() + f2()

    This class is not intended to be used directly, but rather returned as the result of an __add__() call on a
    Function1D object.

    :param object function1: A Function1D object or Python callable.
    :param object function2: A Function1D object or Python callable.
    """

    _function1: Function1D
    _function2: Function1D

    def __init__(self, function1: float | Callable[[float], float] | Function1D, function2: float | Callable[[float], float] | Function1D) -> None: ...

class SubtractFunction1D(Function1D):
    """
    A Function1D class that implements the subtraction of the results of two Function1D objects: f1() - f2()

    This class is not intended to be used directly, but rather returned as the result of a __sub__() call on a
    Function1D object.

    :param object function1: A Function1D object or Python callable.
    :param object function2: A Function1D object or Python callable.
    """

    _function1: Function1D
    _function2: Function1D

    def __init__(self, function1: float | Callable[[float], float] | Function1D, function2: float | Callable[[float], float] | Function1D) -> None: ...

class MultiplyFunction1D(Function1D):
    """
    A Function1D class that implements the multiplication of the results of two Function1D objects: f1() * f2()

    This class is not intended to be used directly, but rather returned as the result of a __mul__() call on a
    Function1D object.

    :param object function1: A Function1D object or Python callable.
    :param object function2: A Function1D object or Python callable.
    """

    _function1: Function1D
    _function2: Function1D

    def __init__(self, function1: float | Callable[[float], float] | Function1D, function2: float | Callable[[float], float] | Function1D) -> None: ...

class DivideFunction1D(Function1D):
    """
    A Function1D class that implements the division of the results of two Function1D objects: f1() / f2()

    This class is not intended to be used directly, but rather returned as the result of a __truediv__() call on a
    Function1D object.

    :param object function1: A Function1D object or Python callable.
    :param object function2: A Function1D object or Python callable.
    """

    _function1: Function1D
    _function2: Function1D

    def __init__(self, function1d: float | Callable[[float], float] | Function1D, function2d: float | Callable[[float], float] | Function1D) -> None: ...

class ModuloFunction1D(Function1D):
    """
    A Function1D class that implements the modulo of the results of two Function1D objects: f1() % f2()

    This class is not intended to be used directly, but rather returned as the result of a __mod__() call on a
    Function1D object.

    :param object function1: A Function1D object or Python callable.
    :param object function2: A Function1D object or Python callable.
    """

    _function1: Function1D
    _function2: Function1D

    def __init__(self, function1d: float | Callable[[float], float] | Function1D, function2d: float | Callable[[float], float] | Function1D) -> None: ...

class PowFunction1D(Function1D):
    """
    A Function1D class that implements the pow() operator on two Function1D objects.

    This class is not intended to be used directly, but rather returned as the result of a __pow__() call on a
    Function1D object.

    :param object function1: A Function1D object or Python callable.
    :param object function2: A Function1D object or Python callable.
    """

    _function1: Function1D
    _function2: Function1D

    def __init__(self, function1: float | Callable[[float], float] | Function1D, function2: float | Callable[[float], float] | Function1D) -> None: ...

class AbsFunction1D(FloatFunction):
    """
    A Function1D class that implements the absolute value of the result of a Function1D object: abs(f()).

    This class is not intended to be used directly, but rather returned as the
    result of an __abs__() call on a Function1D object.

    :param object function: A Function1D object or Python callable.
    """

    _Function: Function1D
    def __init__(self, function: Callable[[float], float] | Function1D) -> None: ...

class EqualsFunction1D(Function1D):
    """
    A Function1D class that tests the equality of the results of two Function1D objects: f1() == f2()

    This class is not intended to be used directly, but rather returned as the result of an __eq__() call on a
    Function1D object.

    :param object function1: A Function1D object or Python callable.
    :param object function2: A Function1D object or Python callable.
    """

    _function1: Function1D
    _function2: Function1D

    def __init__(self, function1: float | Callable[[float], float] | Function1D, function2: float | Callable[[float], float] | Function1D) -> None: ...

class NotEqualsFunction1D(Function1D):
    """
    A Function1D class that tests the inequality of the results of two Function1D objects: f1() != f2()

    This class is not intended to be used directly, but rather returned as the result of an __ne__() call on a
    Function1D object.

    :param object function1: A Function1D object or Python callable.
    :param object function2: A Function1D object or Python callable.
    """

    _function1: Function1D
    _function2: Function1D

    def __init__(self, function1: float | Callable[[float], float] | Function1D, function2: float | Callable[[float], float] | Function1D) -> None: ...

class LessThanFunction1D(Function1D):
    """
    A Function1D class that implements < of the results of two Function1D objects: f1() < f2()

    This class is not intended to be used directly, but rather returned as the result of an __lt__() call on a
    Function1D object.

    :param object function1: A Function1D object or Python callable.
    :param object function2: A Function1D object or Python callable.
    """

    _function1: Function1D
    _function2: Function1D

    def __init__(self, function1: float | Callable[[float], float] | Function1D, function2: float | Callable[[float], float] | Function1D) -> None: ...

class GreaterThanFunction1D(Function1D):
    """
    A Function1D class that implements > of the results of two Function1D objects: f1() > f2()

    This class is not intended to be used directly, but rather returned as the result of a __gt__() call on a
    Function1D object.

    :param object function1: A Function1D object or Python callable.
    :param object function2: A Function1D object or Python callable.
    """

    _function1: Function1D
    _function2: Function1D

    def __init__(self, function1: float | Callable[[float], float] | Function1D, function2: float | Callable[[float], float] | Function1D) -> None: ...

class LessEqualsFunction1D(Function1D):
    """
    A Function1D class that implements <= of the results of two Function1D objects: f1() <= f2()

    This class is not intended to be used directly, but rather returned as the result of an __le__() call on a
    Function1D object.

    :param object function1: A Function1D object or Python callable.
    :param object function2: A Function1D object or Python callable.
    """

    _function1: Function1D
    _function2: Function1D

    def __init__(self, function1: float | Callable[[float], float] | Function1D, function2: float | Callable[[float], float] | Function1D) -> None: ...

class GreaterEqualsFunction1D(Function1D):
    """
    A Function1D class that implements >= of the results of two Function1D objects: f1() >= f2()

    This class is not intended to be used directly, but rather returned as the result of an __ge__() call on a
    Function1D object.

    :param object function1: A Function1D object or Python callable.
    :param object function2: A Function1D object or Python callable.
    """

    _function1: Function1D
    _function2: Function1D

    def __init__(self, function1: float | Callable[[float], float] | Function1D, function2: float | Callable[[float], float] | Function1D) -> None: ...

class AddScalar1D(Function1D):
    """
    A Function1D class that implements the addition of scalar and the result of a Function1D object: K + f()

    This class is not intended to be used directly, but rather returned as the result of an __add__() call on a
    Function1D object.

    :param float value: A double value.
    :param object function: A Function1D object or Python callable.
    """

    _value: float
    _function: Function1D

    def __init__(self, value: float, function: float | Callable[[float], float] | Function1D) -> None: ...

class SubtractScalar1D(Function1D):
    """
    A Function1D class that implements the subtraction of scalar and the result of a Function1D object: K - f()

    This class is not intended to be used directly, but rather returned as the result of an __sub__() call on a
    Function1D object.

    :param double value: A double value.
    :param object function: A Function1D object or Python callable.
    """

    _value: float
    _function: Function1D

    def __init__(self, value: float, function: float | Callable[[float], float] | Function1D) -> None: ...

class MultiplyScalar1D(Function1D):
    """
    A Function1D class that implements the multiplication of scalar and the result of a Function1D object: K * f()

    This class is not intended to be used directly, but rather returned as the result of an __mul__() call on a
    Function1D object.

    :param float value: A double value.
    :param object function: A Function1D object or Python callable.
    """

    _value: float
    _function: Function1D

    def __init__(self, value: float, function: float | Callable[[float], float] | Function1D) -> None: ...

class DivideScalar1D(Function1D):
    """
    A Function1D class that implements the division of scalar and the result of a Function1D object: K / f()

    This class is not intended to be used directly, but rather returned as the result of an __div__() call on a
    Function1D object.

    :param float value: A double value.
    :param object function: A Function1D object or Python callable.
    """

    _value: float
    _function: Function1D

    def __init__(self, value: float, function: float | Callable[[float], float] | Function1D) -> None: ...

class ModuloScalarFunction1D(Function1D):
    """
    A Function1D class that implements the modulo of scalar and the result of a Function1D object: K % f()

    This class is not intended to be used directly, but rather returned as the result of a __mod__() call on a
    Function1D object.

    :param float value: A double value.
    :param object function: A Function1D object or Python callable.
    """

    _value: float
    _function: Function1D

    def __init__(self, value: float, function: float | Callable[[float], float] | Function1D) -> None: ...

class ModuloFunctionScalar1D(Function1D):
    """
    A Function1D class that implements the modulo of the result of a Function1D object and a scalar: f() % K

    This class is not intended to be used directly, but rather returned as the result of a __mod__() call on a
    Function1D object.

    :param object function: A Function1D object or Python callable.
    :param float value: A double value.
    """

    _function: Function1D
    _value: float

    def __init__(self, function: float | Callable[[float], float] | Function1D, value: float) -> None: ...

class PowScalarFunction1D(Function1D):
    """
    A Function1D class that implements the pow of scalar and the result of a Function1D object: K ** f()

    This class is not intended to be used directly, but rather returned as the result of an __pow__() call on a
    Function1D object.

    :param float value: A double value.
    :param object function: A Function1D object or Python callable.
    """

    _value: float
    _function: Function1D

    def __init__(self, value: float, function: float | Callable[[float], float] | Function1D) -> None: ...

class PowFunctionScalar1D(Function1D):
    """
    A Function1D class that implements the pow of the result of a Function1D object and a scalar: f() ** K

    This class is not intended to be used directly, but rather returned as the result of an __pow__() call on a
    Function1D object.

    :param object function: A Function1D object or Python callable.
    :param float value: A double value.
    """

    _function: Function1D
    _value: float

    def __init__(self, function: float | Callable[[float], float] | Function1D, value: float) -> None: ...

class EqualsScalar1D(Function1D):
    """
    A Function1D class that tests the equality of a scalar and the result of a Function1D object: K == f2()

    This class is not intended to be used directly, but rather returned as the result of an __eq__() call on a
    Function1D object.

    :param value: A double value.
    :param object function: A Function1D object or Python callable.
    """

    _value: float
    _function: Function1D

    def __init__(self, value: float, function: float | Callable[[float], float] | Function1D) -> None: ...

class NotEqualsScalar1D(Function1D):
    """
    A Function1D class that tests the inequality of a scalar and the result of a Function1D object: K != f2()

    This class is not intended to be used directly, but rather returned as the result of an __ne__() call on a
    Function1D object.

    :param value: A double value.
    :param object function: A Function1D object or Python callable.
    """

    _value: float
    _function: Function1D

    def __init__(self, value: float, function: float | Callable[[float], float] | Function1D) -> None: ...

class LessThanScalar1D(Function1D):
    """
    A Function1D class that implements < of a scalar and the result of a Function1D object: K < f2()

    This class is not intended to be used directly, but rather returned as the result of an __lt__() call on a
    Function1D object.

    :param value: A double value.
    :param object function: A Function1D object or Python callable.
    """

    _value: float
    _function: Function1D

    def __init__(self, value: float, function: float | Callable[[float], float] | Function1D) -> None: ...

class GreaterThanScalar1D(Function1D):
    """
    A Function1D class that implements > of a scalar and the result of a Function1D object: K > f2()

    This class is not intended to be used directly, but rather returned as the result of a __gt__() call on a
    Function1D object.

    :param value: A double value.
    :param object function: A Function1D object or Python callable.
    """

    _value: float
    _function: Function1D

    def __init__(self, value: float, function: float | Callable[[float], float] | Function1D) -> None: ...

class LessEqualsScalar1D(Function1D):
    """
    A Function1D class that implements <= of a scalar and the result of a Function1D object: K <= f2()

    This class is not intended to be used directly, but rather returned as the result of an __le__() call on a
    Function1D object.

    :param value: A double value.
    :param object function: A Function1D object or Python callable.
    """

    _value: float
    _function: Function1D

    def __init__(self, value: float, function: float | Callable[[float], float] | Function1D) -> None: ...

class GreaterEqualsScalar1D(Function1D):
    """
    A Function1D class that implements >= of a scalar and the result of a Function1D object: K >= f2()

    This class is not intended to be used directly, but rather returned as the result of an __ge__() call on a
    Function1D object.

    :param value: A double value.
    :param object function: A Function1D object or Python callable.
    """

    _value: float
    _function: Function1D

    def __init__(self, value: float, function: float | Callable[[float], float] | Function1D) -> None: ...
