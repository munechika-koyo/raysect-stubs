from collections.abc import Callable

from .base import Function2D

class Blend2D(Function2D):
    """
    Performs a linear interpolation between two scalar functions, modulated by a 3rd scalar function.

    The value of the scalar mask function is used to interpolated between the
    values returned by the two functions. Mathematically the value returned by
    this function is as follows:

    .. math::
        v = (1 - f_m(x)) f_1(x) + f_m(x) f_2(x)

    The value of the mask function is clamped to the range [0, 1] if the sampled
    value exceeds the required range.
    """

    def __init__(
        self,
        f1: Function2D | float | Callable[[float, float], float],
        f2: Function2D | float | Callable[[float, float], float],
        mask: Function2D | float | Callable[[float, float], float],
    ) -> None:
        """
        :param float.Function2D f1: First scalar function.
        :param float.Function2D f2: Second scalar function.
        :param float.Function2D mask: Scalar function returning a value in the range [0, 1].
        """
