from collections.abc import Sequence
from typing import Protocol, TypeAlias

from typing_extensions import Buffer

class _SupportsTupleIndexing(Protocol):
    """Protocol for objects that support tuple indexing like arr[i, j]."""
    def __getitem__(self, key: tuple[int, int]) -> float: ...

class _SupportsNestedIndexing(Protocol):
    """Protocol for objects that support nested indexing like arr[i][j]."""
    def __getitem__(self, key: int) -> Sequence[float]: ...

# Type alias for _Mat4 constructor 'v' parameter
Mat4InitValue: TypeAlias = (
    # Another _Mat4 instance
    "_Mat4"
    |
    # 4x4 nested sequences (list of lists, tuple of tuples, etc.)
    Sequence[Sequence[float]]
    |
    # Objects supporting tuple indexing like numpy arrays
    _SupportsTupleIndexing
    |
    # Objects supporting nested indexing
    _SupportsNestedIndexing
    |
    # 16-element sequence (row-major order)
    Sequence[float]
    |
    # Buffer protocol objects (numpy arrays, etc.)
    Buffer
)

class _Mat4:
    """4x4 matrix base class."""

    def __init__(self, v: Mat4InitValue = ((1.0, 0.0, 0.0, 0.0), (0.0, 1.0, 0.0, 0.0), (0.0, 0.0, 1.0, 0.0), (0.0, 0.0, 0.0, 1.0))) -> None:
        """
        4x4 Matrix constructor.

        If no initial values are passed, _Mat4 defaults to an identity matrix.

        Any 4 x 4 indexable or 16 element object can be used to initialise the
        matrix. 16 element objects must be specified in row-major format.
        """
    def __getitem__(self, index: tuple[int, int]) -> float:
        """
        Indexing get operator.

        Expects a tuple (row, column) as the index.

        e.g. v = matrix[1, 2]
        """
    def __setitem__(self, index: tuple[int, int], value: float) -> None:
        """
        Indexing set operator.

        Expects a tuple (row, column) as the index.

        e.g. matrix[1, 2] = 7.0
        """
    def is_identity(self, tolerance: float = 1e-8) -> bool:
        """
        Identifies if the matrix is an identity matrix.

        Returns True if the matrix is an identify matrix, False otherwise.

        The method has a default tolerance of 1e-8 to account for errors due to
        numerical accuracy limits. The tolerance may be altered by setting the
        tolerance argument.

        :param tolerance: Numerical tolerance (default: 1e-8)
        :return: True/False
        """
    def is_close(self, other: _Mat4, tolerance: float = 1e-8) -> bool:
        """
        Is this matrix equal to another matrix within a numerical tolerance.

        The method has a default tolerance of 1e-8 to account for errors that
        may have accumulated due to numerical accuracy limits. The tolerance
        may be altered by setting the tolerance argument.

        :param other: The other matrix.
        :param tolerance: Numerical tolerance (default: 1e-8)
        :return: True/False
        """
