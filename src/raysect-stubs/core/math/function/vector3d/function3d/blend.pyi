from .base import Function3D, _ScalarOperand3D, _VectorOperand3D

class Blend3D(Function3D):
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

    def __init__(self, f1: _VectorOperand3D, f2: _VectorOperand3D, mask: _ScalarOperand3D) -> None: ...
