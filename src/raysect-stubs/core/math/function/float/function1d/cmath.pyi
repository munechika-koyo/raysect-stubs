from collections.abc import Callable

from .base import Function1D

class Exp1D(Function1D):
    """
    A Function1D class that implements the exponential of the result of a Function1D object: exp(f())

    :param Function1D function: A Function1D object.
    """

    _function: Function1D
    def __init__(self, function: float | Function1D | Callable[[float], float]) -> None: ...

class Sin1D(Function1D):
    """
    A Function1D class that implements the sine of the result of a Function1D object: sin(f())

    :param Function1D function: A Function1D object.
    """

    _function: Function1D
    def __init__(self, function: float | Function1D | Callable[[float], float]) -> None: ...

class Cos1D(Function1D):
    """
    A Function1D class that implements the cosine of the result of a Function1D object: cos(f())

    :param Function1D function: A Function1D object.
    """

    _function: Function1D
    def __init__(self, function: float | Function1D | Callable[[float], float]) -> None: ...

class Tan1D(Function1D):
    """
    A Function1D class that implements the tangent of the result of a Function1D object: tan(f())

    :param Function1D function: A Function1D object.
    """

    _function: Function1D
    def __init__(self, function: float | Function1D | Callable[[float], float]) -> None: ...

class Asin1D(Function1D):
    """
    A Function1D class that implements the arcsine of the result of a Function1D object: asin(f())

    :param Function1D function: A Function1D object.
    """

    _function: Function1D

    def __init__(self, function: float | Function1D | Callable[[float], float]) -> None: ...

class Acos1D(Function1D):
    """
    A Function1D class that implements the arccosine of the result of a Function1D object: acos(f())

    :param Function1D function: A Function1D object.
    """

    _function: Function1D

    def __init__(self, function: float | Function1D | Callable[[float], float]) -> None: ...

class Atan1D(Function1D):
    """
    A Function1D class that implements the arctangent of the result of a Function1D object: atan(f())

    :param Function1D function: A Function1D object.
    """

    _function: Function1D

    def __init__(self, function: float | Function1D | Callable[[float], float]) -> None: ...

class Atan4Q1D(Function1D):
    """
    A Function1D class that implements the arctangent of the result of 2 Function1D objects: atan2(f1(), f2())

    This differs from Atan1D in that it takes separate functions for the
    numerator and denominator, in order to get the quadrant correct.

    :param Function1D numerator: A Function1D object representing the numerator
    :param Function1D denominator: A Function1D object representing the denominator
    """

    _numerator: Function1D
    _denominator: Function1D
    def __init__(
        self,
        numerator: float | Function1D | Callable[[float], float],
        denominator: float | Function1D | Callable[[float], float],
    ) -> None: ...

class Sqrt1D(Function1D):
    """
    A Function1D class that implements the square root of the result of a Function1D object: sqrt(f())

    :param Function1D function: A Function1D object.
    """

    _function: Function1D
    def __init__(self, function: float | Function1D | Callable[[float], float]) -> None: ...

class Erf1D(Function1D):
    """
    A Function1D class that implements the error function of the result of a Function1D object: erf(f())

    :param Function1D function: A Function1D object.
    """

    _function: Function1D
    def __init__(self, function: float | Function1D | Callable[[float], float]) -> None: ...
