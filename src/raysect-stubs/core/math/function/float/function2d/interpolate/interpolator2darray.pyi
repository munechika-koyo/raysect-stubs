from typing import ClassVar, Literal

from numpy import float64
from numpy.typing import ArrayLike, NDArray

from ..base import Function2D

class Interpolator2DArray(Function2D):
    """
    A configurable interpolator for 2D arrays.

    Coordinate array (x), array (y) and data array (f) are sorted and transformed into Numpy arrays.
    The resulting Numpy arrays are stored as read only. I.e. `writeable` flag of self.x, self.y and self.f
    is set to False. Alteration of the flag may result in unwanted behaviour.

    :param object x: 1D array-like object of real values storing the x spline knot positions.
    :param object y: 1D array-like object of real values storing the y spline knot positions.
    :param object f: 2D array-like object of real values storing the spline knot function value at x, y.
    :param str interpolation_type: Type of interpolation to use. Options are:
        `linear`: Interpolates the data using piecewise bilinear interpolation.
        `cubic`: Interpolates the data using piecewise bicubic interpolation.
    :param str extrapolation_type: Type of extrapolation to use. Options are:
        `none`: Attempt to access data outside of x's and y's range will yield ValueError.
        `nearest`: Extrapolation results is the nearest position x and y value in the interpolation domain.
        `linear`: Extrapolate bilinearly the interpolation function.
    :param double extrapolation_range_x: Limits the range where extrapolation is permitted. Requesting data beyond the
        extrapolation range results in ValueError. Extrapolation range will be applied as padding symmetrically to both
        ends of the interpolation range (x).
    :param double extrapolation_range_y: Limits the range where extrapolation is permitted. Requesting data beyond the
        extrapolation range results in ValueError. Extrapolation range will be applied as padding symmetrically to both
        ends of the interpolation range (y).

    .. code-block:: python

        >>> from raysect.core.math.function.float.function2d.interpolate.interpolator2darray import Interpolator2DArray
        >>>
        >>> x = np.linspace(-1., 1., 20)
        >>> y = np.linspace(-1., 1., 20)
        >>> x_array, y_array = np.meshgrid(x, y)
        >>> f = np.exp(-(x_array**2 + y_array**2))
        >>> interpolator2D = Interpolator2DArray(x, y, f, 'cubic', 'nearest', 1.0, 1.0)
        >>> # Interpolation
        >>> interpolator2D(1.0, 0.2)
        0.35345307120078995
        >>> # Extrapolation
        >>> interpolator2D(1.0, 1.1)
        0.1353352832366128
        >>> # Extrapolation out of bounds
        >>> interpolator2D(1.0, 2.1)
        ValueError: The specified value (y=2.1) is outside of extrapolation range.

    :note: All input derivatives used in calculations use the previous and next indices in the spline knot arrays.
        At the edge of the spline knot arrays the index of the edge of the array is is used instead.
    :note: x, y arrays must be equal in shape to f in the first and second dimension respectively.
    :note: x and y must be monotonically increasing arrays.

    """

    def __init__(
        self,
        x: ArrayLike,
        y: ArrayLike,
        f: ArrayLike,
        interpolation_type: Literal["linear", "cubic"],
        extrapolation_type: Literal["none", "nearest", "linear"],
        extrapolation_range_x: float,
        extrapolation_range_y: float,
    ) -> None: ...
    @property
    def domain(self) -> tuple[float, float, float, float]:
        """
        Returns min/max interval of 'x' and 'y' arrays.
        Order: min(x), max(x), min(y), max(y).
        """

class _Interpolator2D:
    """
    Base class for 2D interpolators.

    :param x: 1D memory view of the spline point x positions.
    :param y: 1D memory view of the spline point y positions.
    :param f: 2D memory view of the function value at spline point x, y positions.
    """

    ID: ClassVar[str | None]

    def __init__(self, x: NDArray[float64], y: NDArray[float64], f: NDArray[float64]) -> None: ...

class _Interpolator2DLinear(_Interpolator2D):
    """
    Linear interpolation of 2D function.

    :param x: 1D memory view of the spline point x positions.
    :param y: 1D memory view of the spline point y positions.
    :param f: 2D memory view of the function value at spline point x, y positions.
    """

    ID: ClassVar[str | None] = "linear"

class _Interpolator2DCubic(_Interpolator2D):
    """
    Cubic interpolation of a 2D function.

    When called, stores cubic polynomial coefficients from the value of the function, df/dx, df/dy  and d2f/dxdy at the
    neighbouring spline knots using _ArrayDerivative2D object. The polynomial coefficients and gradients are calculated
    between each spline knots in a unit square.

    :param x: 1D memory view of the spline point x positions.
    :param y: 1D memory view of the spline point y positions.
    :param f: 2D memory view of the function value at spline point x, y positions.
    """

    ID: ClassVar[str | None] = "cubic"

    def __init__(self, x: NDArray[float64], y: NDArray[float64], f: NDArray[float64]) -> None: ...

class _Extrapolator2D:
    """
    Base class for Function2D extrapolators.

    :param x: 1D memory view of the spline point x positions.
    :param y: 1D memory view of the spline point y positions.
    :param f: 2D memory view of the function value at spline point x, y positions.
    :param interpolator: stored _Interpolator2D object that is being used.
    """

    ID: ClassVar[str | None]

    def __init__(
        self,
        x: NDArray[float64],
        y: NDArray[float64],
        f: NDArray[float64],
        interpolator: _Interpolator2D,
        extrapolation_range_x: float,
        extrapolation_range_y: float,
    ) -> None: ...

class _Extrapolator2DNone(_Extrapolator2D):
    """
    Extrapolator that does nothing.

    :param x: 1D memory view of the spline point x positions.
    :param y: 1D memory view of the spline point y positions.
    :param f: 2D memory view of the function value at spline point x, y positions.
    :param interpolator: stored _Interpolator2D object that is being used.
    """

    ID: ClassVar[str | None] = "none"

class _Extrapolator2DNearest(_Extrapolator2D):
    """
    Extrapolator that returns nearest input value.

    :param x: 1D memory view of the spline point x positions.
    :param y: 1D memory view of the spline point y positions.
    :param f: 2D memory view of the function value at spline point x, y positions.
    :param interpolator: stored _Interpolator2D object that is being used.
    """

    ID: ClassVar[str | None] = "nearest"

class _Extrapolator2DLinear(_Extrapolator2D):
    """
    Extrapolator that returns linearly extrapolated input value.

    :param x: 1D memory view of the spline point x positions.
    :param y: 1D memory view of the spline point y positions.
    :param f: 2D memory view of the function value at spline point x, y positions.
    :param interpolator: stored _Interpolator2D object that is being used.
    """

    ID: ClassVar[str | None] = "linear"

class _ArrayDerivative2D:
    """
    Gradient method that returns the approximate derivative of a desired order at a specified grid point.

    These methods of finding derivatives are only valid on a 2D grid of points, at the values at the points. Other
    derivative methods would be dependent on the interpolator types.

    :param x: 1D memory view of the spline point x positions.
    :param y: 1D memory view of the spline point y positions.
    :param f: 2D memory view of the function value at spline point x, y positions.
    """

    def __init__(self, x: NDArray[float64], y: NDArray[float64], f: NDArray[float64]) -> None: ...

id_to_interpolator: dict[str, type[_Interpolator2D]]
id_to_extrapolator: dict[str, type[_Extrapolator2D]]
permitted_interpolation_combinations: dict[str, list[str]]
