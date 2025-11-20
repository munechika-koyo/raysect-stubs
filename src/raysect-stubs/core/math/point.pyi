from collections.abc import Iterator
from ._vec3 import _Vec3  # pyright: ignore[reportPrivateUsage]
from .vector import Vector2D, Vector3D
from .affinematrix import AffineMatrix3D

class Point2D:
    """
    Represents a point in 2D affine space.

    A 2D point is a location in 2D space which is defined by its x and y coordinates in a given coordinate system.
    Vector2D objects can be added/subtracted from Point2D yielding another Vector2D. You can also find the Vector2D
    and distance between two Point2Ds, and transform a Point2D from one coordinate system to another.

    If no initial values are passed, Point2D defaults to the origin: Point2D(0.0, 0.0)

    :param float x: initial x coordinate, defaults to x = 0.0.
    :param float y: initial y coordinate, defaults to y = 0.0.

    :ivar float x: x-coordinate
    :ivar float y: y-coordinate

    .. code-block:: pycon

        >>> from raysect.core import Point2D
        >>>
        >>> a = Point2D(1, 1)

    """

    x: float
    y: float
    def __init__(self, x: float = 0.0, y: float = 0.0) -> None: ...
    def __repr__(self) -> str:
        """Returns a string representation of the Point2D object."""
    def __richcmp__(self, other: Point2D, op: int) -> bool:
        """Rich comparison operator."""
    def __getitem__(self, index: int) -> float:
        """Returns the point coordinates by index ([0,1] -> [x,y]).

        >>> a = Point2D(1, 0)
        >>> a[0]
        1
        """
    def __setitem__(self, index: int, value: float) -> None:
        """Sets the point coordinates by index ([0,1] -> [x,y]).

        >>> a = Point2D(1, 0)
        >>> a[1] = 2
        >>> a
        Point2D(1.0, 2.0)
        """
    def __iter__(self) -> Iterator[float]:
        """Iterates over the coordinates (x, y)

        >>> a = Point2D(1, 1)
        >>> x, y = a
        >>> x, y
        (1.0, 1.0)

        """
    def __add__(self, y: Vector2D) -> Point2D:
        """Addition operator.

        >>> Point2D(1, 0) + Vector2D(0, 1)
        Point2D(1.0, 1.0)
        """
    def __sub__(self, y: Vector2D) -> Point2D:
        """Subtraction operator.

        >>> Point2D(1, 0) - Vector2D(0, 1)
        Point2D(1.0, -1.0)
        """
    def vector_to(self, p: Point2D) -> Vector2D:
        """
        Returns a vector from this point to the passed point.

        :param Point2D p: point to which a vector will be calculated
        :rtype: Vector2D

        .. code-block:: pycon

            >>> a = Point2D(1, 0)
            >>> b = Point2D(1, 1)
            >>> a.vector_to(b)
            Vector2D(0.0, 1.0)

        """
    def distance_to(self, p: Point2D) -> float:
        """
        Returns the distance between this point and the passed point.

        :param Point2D p: the point to which the distance will be calculated
        :rtype: float

        .. code-block:: pycon

            >>> a = Point2D(1, 0)
            >>> b = Point2D(1, 1)
            >>> a.distance_to(b)
            1.0

        """
    def copy(self) -> Point2D:
        """
        Returns a copy of the point.

        :rtype: Point2D

        .. code-block:: pycon

            >>> a = Point2D(1, 1)
            >>> a.copy()
            Point2D(1.0, 1.0)

        """

class Point3D:
    """
    Represents a point in 3D affine space.

    A point is a location in 3D space which is defined by its x, y and z coordinates in a given coordinate system.
    Vectors can be added/subtracted from Points yielding another Vector3D. You can also find the Vector3D and distance
    between two Points, and transform a Point3D from one coordinate system to another.

    If no initial values are passed, Point3D defaults to the origin:
    Point3D(0.0, 0.0, 0.0)

    :param float x: initial x coordinate, defaults to x = 0.0.
    :param float y: initial y coordinate, defaults to y = 0.0.
    :param float z: initial z coordinate, defaults to z = 0.0.

    :ivar float x: x-coordinate
    :ivar float y: y-coordinate
    :ivar float z: z-coordinate

    .. code-block:: pycon

        >>> from raysect.core import Point3D
        >>> a = Point3D(0, 1, 2)
    """

    x: float
    y: float
    z: float
    def __init__(self, x: float = 0.0, y: float = 0.0, z: float = 0.0) -> None: ...
    def __repr__(self) -> str:
        """Returns a string representation of the Point3D object."""
    def __richcmp__(self, other: Point3D, op: int) -> bool:
        """Provides basic point comparison operations."""
    def __getitem__(self, index: int) -> float:
        """Returns the point coordinates by index ([0,1,2] -> [x,y,z]).

        >>> a = Point3D(1, 0, 0)
        >>> a[0]
        1
        """
    def __setitem__(self, index: int, value: float) -> None:
        """Sets the point coordinates by index ([0,1,2] -> [x,y,z]).

        >>> a = Point3D(1, 0, 0)
        >>> a[1] = 2
        >>> a
        Point3D(1.0, 2.0, 0.0)
        """
    def __iter__(self) -> Iterator[float]:
        """Iterates over the coordinates (x, y, z)

        >>> a = Point3D(0, 1, 2)
        >>> x, y, z = a
        >>> x, y, z
        (0.0, 1.0, 2.0)
        """
    def __add__(self, y: _Vec3) -> Point3D:
        """Addition operator.

        >>> Point3D(1, 0, 0) + Vector3D(0, 1, 0)
        Point3D(1.0, 1.0, 0.0)
        """
    def __sub__(self, y: _Vec3) -> Point3D:
        """Subtraction operator.

        >>> Point3D(1, 0, 0) - Vector3D(0, 1, 0)
        Point3D(1.0, -1.0, 0.0)
        """
    def __rmul__(self, x: AffineMatrix3D) -> Point3D:
        """Multiplication operator.

        :param AffineMatrix3D x: transformation matrix x
        :return: Matrix multiplication of a 3D transformation matrix with the input point.
        :rtype: Point3D
        """
    def vector_to(self, p: Point3D) -> Vector3D:
        """
        Returns a vector from this point to the passed point.

        :param Point3D p: the point to which a vector will be calculated.
        :rtype: Vector3D

        .. code-block:: pycon

            >>> a = Point3D(0, 1, 2)
            >>> b = Point3D(1, 1, 1)
            >>> a.vector_to(b)
            Vector3D(1.0, 0.0, -1.0)

        """
    def distance_to(self, p: Point3D) -> float:
        """
        Returns the distance between this point and the passed point.

        :param Point3D p: the point to which the distance will be calculated
        :rtype: float

        .. code-block:: pycon

            >>> a = Point3D(0, 1, 2)
            >>> b = Point3D(1, 1, 1)
            >>> a.distance_to(b)
            1.4142135623730951
        """
    def transform(self, m: AffineMatrix3D) -> Point3D:
        """
        Transforms the point with the supplied Affine Matrix.

        The point is transformed by premultiplying the point by the affine
        matrix.

        For cython code this method is substantially faster than using the
        multiplication operator of the affine matrix.

        This method expects a valid affine transform. For speed reasons, minimal
        checks are performed on the matrix.

        :param AffineMatrix3D m: The affine matrix describing the required coordinate transformation.
        :return: A new instance of this point that has been transformed with the supplied Affine Matrix.
        :rtype: Point3D
        """
    def copy(self) -> Point3D:
        """
        Returns a copy of the point.

        :rtype: Point3D

        .. code-block:: pycon

            >>> a = Point3D(0, 1, 2)
            >>> a.copy()
            Point3D(0.0, 1.0, 2.0)
        """
