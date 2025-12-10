from collections.abc import Callable

from numpy import float64
from numpy.typing import NDArray

from .base import Function1D

def sample1d(
    function: float | Function1D | Callable[[float], float],
    x_min: float,
    x_max: float,
    num_samples: int,
) -> tuple[NDArray[float64], NDArray[float64]]:
    """
    Samples Function1D over given range.

    :param function: the function to sample. a Function1D object, or a Python function
    :param x_min: minimum value for sample range
    :param x_max: maximum value for sample range
    :param x_samples: number of samples between x_min and x_max, where endpoints are included
    :return: a tuple of sampled x points and respective function samples (x, f)
    """

def sample1d_points(
    function: float | Function1D | Callable[[float], float],
    x_points: NDArray[float64],
) -> NDArray[float64]:
    """
    Samples Function1D in given x points.

    :param function: the function to sample. a Function1D object, or a Python function
    :param x_points: array containing the points at which the function is sampled.
    :return: an array containing the sampled values of the given function.
    """
