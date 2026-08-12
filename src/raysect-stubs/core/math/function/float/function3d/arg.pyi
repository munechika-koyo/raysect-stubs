from typing import Literal

from .base import Function3D

class Arg3D(Function3D):
    """
    Returns one of the arguments the function is passed, unmodified

    This is used to pass coordinates through to other functions in the
    function framework which expect a Function3D object.

    Valid options for argument are "x", "y" or "z".

    >>> argx = Arg3D("x")
    >>> argx(2, 3, 5)
    2.0
    >>> argy = Arg3D("y")
    >>> argy(2, 3, 5)
    3.0
    >>> argz = Arg3D("z")
    >>> argz(2, 3, 5)
    5.0
    >>> squarerx = argx**2
    >>> squarerx(2, 3, 5)
    4.0
    >>> squarery = argy**2
    >>> squarery(2, 3, 5)
    9.0
    >>> squarerz = argz**2
    >>> squarerz(2, 3, 5)
    25.0

    :param str argument: either "x", "y" or "z", the argument to return
    """

    def __init__(self, argument: Literal["x", "y", "z"]) -> None: ...
