from numpy import float64
from numpy.typing import NDArray

def _maximum(data: NDArray[float64]) -> float:
    """Expose cython function for testing."""

def _minimum(data: NDArray[float64]) -> float:
    """Expose cython function for testing."""

def _peak_to_peak(data: NDArray[float64]) -> float:
    """Expose cython function for testing."""

def _test_winding2d(p: NDArray[float64]) -> bool:
    """Expose cython function for testing."""

def _point_inside_polygon(vertices: NDArray[float64], ptx: float, pty: float) -> bool:
    """Expose cython function for testing."""

def _solve_cubic(a: float, b: float, c: float, d: float) -> tuple[float, float, float, float]:
    """Expose cython function for testing."""

def _solve_quartic(a: float, b: float, c: float, d: float, e: float) -> tuple[float, float, float, float, float]:
    """Expose cython function for testing."""
