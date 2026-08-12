from .base import Function1D, _ScalarOperand1D, _VectorOperand1D

class Blend1D(Function1D):
    """
    Performs a spherical linear interpolation between two vector functions, modulated by a 3rd scalar function.

    The value of the scalar mask function is used to spherically interpolated
    between the vectors returned by the two functions. Mathematically the value
    returned by this function is as follows:

    .. math::
        v = (1 - f_m(x)) f_1(x) + f_m(x) f_2(x)

    The value of the mask function is clamped to the range [0, 1] if the
    sampled value exceeds the required range.
    """

    def __init__(self, f1: _VectorOperand1D, f2: _VectorOperand1D, mask: _ScalarOperand1D) -> None: ...
