from collections.abc import Callable
from typing import TypeAlias

from .base import Function3D

_Function3DInput: TypeAlias = Function3D | float | Callable[[float, float, float], float]

class Exp3D(Function3D):
    """
    A Function3D class that implements the exponential of the result of a Function3D object: exp(f())

    :param Function3D function: A Function3D object.
    """

    def __init__(self, function: _Function3DInput) -> None: ...

class Sin3D(Function3D):
    """
    A Function3D class that implements the sine of the result of a Function3D object: sin(f())

    :param Function3D function: A Function3D object.
    """

    def __init__(self, function: _Function3DInput) -> None: ...

class Cos3D(Function3D):
    """
    A Function3D class that implements the cosine of the result of a Function3D object: cos(f())

    :param Function3D function: A Function3D object.
    """

    def __init__(self, function: _Function3DInput) -> None: ...

class Tan3D(Function3D):
    """
    A Function3D class that implements the tangent of the result of a Function3D object: tan(f())

    :param Function3D function: A Function3D object.
    """

    def __init__(self, function: _Function3DInput) -> None: ...

class Asin3D(Function3D):
    """
    A Function3D class that implements the arcsine of the result of a Function3D object: asin(f())

    :param Function3D function: A Function3D object.
    """

    def __init__(self, function: _Function3DInput) -> None: ...

class Acos3D(Function3D):
    """
    A Function3D class that implements the arccosine of the result of a Function3D object: acos(f())

    :param Function3D function: A Function3D object.
    """

    def __init__(self, function: _Function3DInput) -> None: ...

class Atan3D(Function3D):
    """
    A Function3D class that implements the arctangent of the result of a Function3D object: atan(f())

    :param Function3D function: A Function3D object.
    """

    def __init__(self, function: _Function3DInput) -> None: ...

class Atan4Q3D(Function3D):
    """
    A Function3D class that implements the arctangent of the result of 2 Function3D objects: atan2(f1(), f2())

    This differs from Atan3D in that it takes separate functions for the
    numerator and denominator, in order to get the quadrant correct.

    :param Function3D numerator: A Function3D object representing the numerator
    :param Function3D denominator: A Function3D object representing the denominator
    """

    def __init__(self, numerator: _Function3DInput, denominator: _Function3DInput) -> None: ...

class Sqrt3D(Function3D):
    """
    A Function3D class that implements the square root of the result of a Function3D object: sqrt(f())

    :param Function3D function: A Function3D object.
    """

    def __init__(self, function: _Function3DInput) -> None: ...

class Erf3D(Function3D):
    """
    A Function3D class that implements the error function of the result of a Function3D object: erf(f())

    :param Function3D function: A Function3D object.
    """

    def __init__(self, function: _Function3DInput) -> None: ...
