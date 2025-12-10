from typing import ClassVar, Literal

from numpy import float64
from numpy.typing import ArrayLike, NDArray

from .base import Function1D

class Interpolator1DArray(Function1D):
    """
    A configurable interpolator for 1D arrays.

    Coordinate array (x) and data array (f) are sorted and transformed into Numpy arrays.
    The resulting Numpy arrays are stored as read only. I.e. `writeable` flag of self.x and self.f
    is set to False. Alteration of the flag may result in unwanted behaviour.

    :param object x: 1D array-like object of real values storing the x spline knot positions.
    :param object f: 1D array-like object of real values storing the spline knot function value at x.
    :param str interpolation_type: Type of interpolation to use. Options are:
        `linear`: Interpolates the data using piecewise linear interpolation.
        `cubic`: Interpolates the data using piecewise cubic interpolation.
    :param str extrapolation_type: Type of extrapolation to use. Options are:
        `none`: Attempt to access data outside of x's range will yield ValueError.
        `nearest`: Extrapolation results is the nearest position x value in the interpolation domain.
        `linear`: Extrapolate bilinearly the interpolation function.
        `quadratic`: Extrapolate quadratically the interpolation function. Constrains the function at the edge, and the
        derivative both at the edge and 1 spline knot from the edge.
    :param double extrapolation_range: Limits the range where extrapolation is permitted. Requesting data beyond the
        extrapolation range results in ValueError. Extrapolation range will be applied as padding symmetrically to both
        ends of the interpolation range (x).

    .. code-block:: python

        >>> from raysect.core.math.function.float.function1d.interpolate import Interpolator1DArray
        >>>
        >>> x = np.linspace(-1., 1., 20)
        >>> f = np.exp(-x**2)
        >>> interpolator1D = Interpolate1DArray(x, f, 'cubic', 'nearest', 1.0)
        >>> # Interpolation
        >>> interpolator1D(0.2)
        0.9607850606581484
        >>> # Extrapolation
        >>> interpolator1D(1.1)
        0.36787944117144233
        >>> # Extrapolation out of bounds
        >>> interpolator1D(2.1)
        ValueError: The specified value (x=2.1) is outside of extrapolation range.

    :note: All input derivatives used in calculations use the previous and next indices in the spline knot arrays.
        At the edge of the spline knot arrays the index of the edge of the array is is used instead.
    :note: x and f arrays must be of equal length.
    :note: x must be a monotonically increasing array.

    """

    x: NDArray[float64]
    f: NDArray[float64]
    _last_index: int
    _extrapolation_range: float
    _interpolator: _Interpolator1DLinear | _Interpolator1DCubic
    _extrapolator: _Extrapolator1DLinear | _Extrapolator1DNearest | _Extrapolator1DNone | _Extrapolator1DQuadratic

    def __init__(
        self,
        x: ArrayLike,
        f: ArrayLike,
        interpolation_type: Literal["linear", "cubic"],
        extrapolation_type: Literal["none", "nearest", "linear", "quadratic"],
        extrapolation_range: float,
    ) -> None: ...
    @property
    def domain(self) -> tuple[float, float]:
        """
        Returns min/max interval of 'x' array.
        Order: min(x), max(x).
        """

class _Interpolator1D:
    """
    Base class for 1D interpolators.

    :param x: 1D memory view of the spline point x positions.
    :param f: 1D memory view of the function value at spline point x positions.
    """

    _x: NDArray[float64]
    _f: NDArray[float64]
    _last_index: int
    def __init__(self, x: NDArray[float64], f: NDArray[float64]) -> None: ...

class _Interpolator1DLinear(_Interpolator1D):
    """
    Linear interpolation of 1D function.

    :param x: 1D memory view of the spline point x positions.
    :param f: 1D memory view of the function value at spline point x positions.
    """

    ID: ClassVar[str] = "linear"
    def __init__(self, x: NDArray[float64], f: NDArray[float64]) -> None: ...

class _Interpolator1DCubic(_Interpolator1D):
    """
    Cubic interpolation of 1D function

    When called, stores cubic polynomial coefficients from the value of the function at the neighboring spline points
    and the gradient at the neighbouring spline points based on central difference gradients. The polynomial
    coefficients and gradients are calculated between each spline knots normalised to between 0 and 1.

    :param x: 1D memory view of the spline point x positions.
    :param f: 1D memory view of the function value at spline point x positions.
    """

    ID: ClassVar[str] = "cubic"
    def __init__(self, x: NDArray[float64], f: NDArray[float64]) -> None: ...

class _Extrapolator1D:
    """
    Base class for Function1D extrapolators.

    :param object x: 1D array-like object of real values.
    :param object f: 1D array-like object of real values.
    """

    _x: NDArray[float64]
    _f: NDArray[float64]
    _last_index: int
    def __init__(self, x: NDArray[float64], f: NDArray[float64]) -> None: ...

class _Extrapolator1DNone(_Extrapolator1D):
    """
    Extrapolator that does nothing.
    """

    ID: ClassVar[str] = "none"
    def __init__(self, x: NDArray[float64], f: NDArray[float64]) -> None: ...

class _Extrapolator1DNearest(_Extrapolator1D):
    """
    Extrapolator that returns nearest input value.

    :param object x: 1D array-like object of real values.
    :param object f: 1D array-like object of real values.
    """

    ID: ClassVar[str] = "nearest"

class _Extrapolator1DLinear(_Extrapolator1D):
    """
    Extrapolator that extrapolates linearly.

    :param object x: 1D array-like object of real values.
    :param object f: 1D array-like object of real values.
    """

    ID: ClassVar[str] = "linear"

class _Extrapolator1DQuadratic(_Extrapolator1D):
    """
    Extrapolator that extrapolates quadratically.

    :param object x: 1D array-like object of real values.
    :param object f: 1D array-like object of real values.
    """

    ID: ClassVar[str] = "quadratic"
    def __init__(self, x: NDArray[float64], f: NDArray[float64]) -> None: ...

class _ArrayDerivative1D:
    """
    Gradient method that returns the approximate derivative of a desired order at a specified grid point.

    These methods of finding derivatives are only valid on a 1D grid of points, at the values at the points. Other
    derivative method would be dependent on the interpolator types.

    :param x: 1D memory view of the spline point x positions.
    :param f: 1D memory view of the function value at spline point x positions.
    """

    _x: NDArray[float64]
    _f: NDArray[float64]
    _last_index: int
    def __init__(self, x: NDArray[float64], f: NDArray[float64]) -> None: ...

id_to_interpolator: dict[str, type[_Interpolator1D]]
id_to_extrapolator: dict[str, type[_Extrapolator1D]]
permitted_interpolation_combinations: dict[str, list[str]]
