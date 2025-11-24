import numpy as np
from numpy.typing import NDArray

def triangulate2d(vertices: NDArray[np.float64]) -> NDArray[np.float64]:
    """
    Triangulates a N sided simple polygon.

    An N-sided simple polygon is a closed polygon where none of the line
    segments making up the polygon intersect with each other.

    The algorithm accepts polygons with clockwise or anti-clockwise
    winding order.

    The N-sided polygon is supplied as a Nx2 array defining each vertex
    winding around the polygon. The returned array has N-2 triangles, consisting
    of 3 indices into the original vertex array for each triangle. The returned
    array will therefore have dimensions (N-2, 3).

    The final vertex is connected to the first vertex to close the polygon. The
    supplied vertex array must not include any coincident points.

    :param np.ndarray vertices: The array of Nx2 polygon vertices.
    :return: An ndarray of N-2 triangles.
    :rtype: np.ndarray
    """
