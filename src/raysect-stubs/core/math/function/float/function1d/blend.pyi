from collections.abc import Callable

from .base import Function1D

class Blend1D(Function1D):
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

    _f1: Function1D
    _f2: Function1D
    _mask: Function1D

    def __init__(
        self,
        f1: float | Function1D | Callable[[float], float],
        f2: float | Function1D | Callable[[float], float],
        mask: float | Function1D | Callable[[float], float],
    ) -> None:
        """
        :param float.Function1D f1: First scalar function.
        :param float.Function1D f2: Second scalar function.
        :param float.Function1D mask: Scalar function returning a value in the range [0, 1].
        """
