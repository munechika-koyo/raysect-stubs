from collections.abc import Callable
from typing import TypeAlias

from .base import Function2D

_Function2DInput: TypeAlias = Function2D | float | Callable[[float, float], float]

class Exp2D(Function2D):
    """
    A Function2D class that implements the exponential of the result of a Function2D object: exp(f())

    :param Function2D function: A Function2D object.
    """

    def __init__(self, function: _Function2DInput) -> None: ...

class Sin2D(Function2D):
    """
    A Function2D class that implements the sine of the result of a Function2D object: sin(f())

    :param Function2D function: A Function2D object.
    """

    def __init__(self, function: _Function2DInput) -> None: ...

class Cos2D(Function2D):
    """
    A Function2D class that implements the cosine of the result of a Function2D object: cos(f())

    :param Function2D function: A Function2D object.
    """

    def __init__(self, function: _Function2DInput) -> None: ...

class Tan2D(Function2D):
    """
    A Function2D class that implements the tangent of the result of a Function2D object: tan(f())

    :param Function2D function: A Function2D object.
    """

    def __init__(self, function: _Function2DInput) -> None: ...

class Asin2D(Function2D):
    """
    A Function2D class that implements the arcsine of the result of a Function2D object: asin(f())

    :param Function2D function: A Function2D object.
    """

    def __init__(self, function: _Function2DInput) -> None: ...

class Acos2D(Function2D):
    """
    A Function2D class that implements the arccosine of the result of a Function2D object: acos(f())

    :param Function2D function: A Function2D object.
    """

    def __init__(self, function: _Function2DInput) -> None: ...

class Atan2D(Function2D):
    """
    A Function2D class that implements the arctangent of the result of a Function2D object: atan(f())

    :param Function2D function: A Function2D object.
    """

    def __init__(self, function: _Function2DInput) -> None: ...

class Atan4Q2D(Function2D):
    """
    A Function2D class that implements the arctangent of the result of 2 Function2D objects: atan2(f1(), f2())

    This differs from Atan2D in that it takes separate functions for the
    numerator and denominator, in order to get the quadrant correct.

    :param Function2D numerator: A Function2D object representing the numerator
    :param Function2D denominator: A Function2D object representing the denominator
    """

    def __init__(self, numerator: _Function2DInput, denominator: _Function2DInput) -> None: ...

class Sqrt2D(Function2D):
    """
    A Function2D class that implements the square root of the result of a Function2D object: sqrt(f())

    :param Function2D function: A Function2D object.
    """

    def __init__(self, function: _Function2DInput) -> None: ...

class Erf2D(Function2D):
    """
    A Function2D class that implements the error function of the result of a Function2D object: erf(f())

    :param Function2D function: A Function2D object.
    """

    def __init__(self, function: _Function2DInput) -> None: ...
