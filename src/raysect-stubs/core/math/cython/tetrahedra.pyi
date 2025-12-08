from numpy.typing import ArrayLike

def _test_inside_tetrahedra(
    v1x: float,
    v1y: float,
    v1z: float,
    v2x: float,
    v2y: float,
    v2z: float,
    v3x: float,
    v3y: float,
    v3z: float,
    v4x: float,
    v4y: float,
    v4z: float,
    px: float,
    py: float,
    pz: float,
) -> bool:
    """Expose cython function for testing."""

def _test_barycentric_tetrahedra(vertices: ArrayLike, point: ArrayLike) -> tuple[float, float, float, float]:
    """Expose cython function for testing.
    Obtain the barycentric coords.

    :param array-like (4, 3)
    :param vector-like (1, 2)
    :rtype: tuple: (alpha, beta, gamma, delta)
    """

def _test_barycentric_inside_tetrahedra(
    v1x: float,
    v1y: float,
    v1z: float,
    v2x: float,
    v2y: float,
    v2z: float,
    v3x: float,
    v3y: float,
    v3z: float,
    v4x: float,
    v4y: float,
    v4z: float,
    px: float,
    py: float,
    pz: float,
) -> bool:
    """Expose cython function for testing."""
