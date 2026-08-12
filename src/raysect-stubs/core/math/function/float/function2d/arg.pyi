from typing import Literal

from .base import Function2D

class Arg2D(Function2D):
    """
    Returns one of the arguments the function is passed, unmodified

    This is used to pass coordinates through to other functions in the
    function framework which expect a Function2D object.

    Valid options for argument are "x" and "y".

    >>> argx = Arg2D("x")
    >>> argx(2, 3)
    2.0
    >>> argy = Arg2D("y")
    >>> argy(2, 3)
    3.0
    >>> squarerx = argx**2
    >>> squarerx(2, 3)
    4.0
    >>> squarery = argy**2
    >>> squarery(2, 3)
    9.0

    :param str argument: either "x" or "y", the argument to return
    """

    def __init__(self, argument: Literal["x", "y"]) -> None: ...
