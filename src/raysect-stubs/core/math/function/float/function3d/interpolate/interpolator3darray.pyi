from typing import Literal

from numpy.typing import ArrayLike

from ..base import Function3D

class Interpolator3DArray(Function3D):
    """
    A configurable interpolator for 3D arrays.

    Coordinate array (x), array (y), array (z) and data array (f) are sorted and transformed into Numpy arrays.
    The resulting Numpy arrays are stored as read only. I.e. `writeable` flag of self.x, self.y, self.z and self.f
    is set to False. Alteration of the flag may result in unwanted behaviour.

    :param object x: 1D array-like object of real values storing the x spline knot positions.
    :param object y: 1D array-like object of real values storing the y spline knot positions.
    :param object z: 1D array-like object of real values storing the z spline knot positions.
    :param object f: 3D array-like object of real values storing the spline knot function value at x, y, z.
    :param str interpolation_type: Type of interpolation to use. Options are:
        `linear`: Interpolates the data using piecewise trilinear interpolation.
        `cubic`: Interpolates the data using piecewise tricubic interpolation.
    :param str extrapolation_type: Type of extrapolation to use. Options are:
        `none`: Attempt to access data outside of x's and y's range will yield ValueError.
        `nearest`: Extrapolation results is the nearest position x and y value in the interpolation domain.
        `linear`: Extrapolate bilinearly the interpolation function.
    :param double extrapolation_range_x:    Limits the range where extrapolation is permitted. Requesting data beyond the
        extrapolation range results in ValueError. Extrapolation range will be applied as padding symmetrically to both
        ends of the interpolation range (x).
    :param double extrapolation_range_y: Limits the range where extrapolation is permitted. Requesting data beyond the
        extrapolation range results in ValueError. Extrapolation range will be applied as padding symmetrically to both
        ends of the interpolation range (y).
    :param double extrapolation_range_z: Limits the range where extrapolation is permitted. Requesting data beyond the
        extrapolation range results in ValueError. Extrapolation range will be applied as padding symmetrically to both
        ends of the interpolation range (z).

    .. code-block:: python

        >>> from raysect.core.math.function.float.function3d.interpolate.interpolator3darray import Interpolator3DArray
        >>>
        >>> x = np.linspace(-1., 1., 20)
        >>> y = np.linspace(-1., 1., 20)
        >>> z = np.linspace(-1., 1., 20)
        >>> x_array, y_array, z_array = np.meshgrid(x, y, z, indexing='ij')
        >>> f = np.exp(-(x_array**2 + y_array**2 + z_array**2))
        >>> interpolator3D = Interpolator3DArray(x, y, z, f, 'cubic', 'nearest', 1.0, 1.0, 1.0)
        >>> # Interpolation
        >>> interpolator3D(1.0, 1.0, 0.2)
        0.1300281183136766
        >>> # Extrapolation
        >>> interpolator3D(1.0, 1.0, 1.1)
        0.0497870683678659
        >>> # Extrapolation out of bounds
        >>> interpolator3D(1.0, 1.0, 2.1)
        ValueError: The specified value (z=2.1) is outside of extrapolation range.

    :note: All input derivatives used in calculations use the previous and next indices in the spline knot arrays.
        At the edge of the spline knot arrays the index of the edge of the array is is used instead.
    :note: x, y, z arrays must be equal in shape to f in the first, second and third dimension respectively.
    :note: x, y and z must be monotonically increasing arrays.

    """

    def __init__(
        self,
        x: ArrayLike,
        y: ArrayLike,
        z: ArrayLike,
        f: ArrayLike,
        interpolation_type: Literal["linear", "cubic"],
        extrapolation_type: Literal["none", "nearest", "linear"],
        extrapolation_range_x: float,
        extrapolation_range_y: float,
        extrapolation_range_z: float,
    ) -> None: ...
    @property
    def domain(self) -> tuple[float, float, float, float, float, float]:
        """
        Returns min/max interval of 'x', 'y' and 'z' arrays.
        Order: min(x), max(x), min(y), max(y)., min(z), max(z).
        """
