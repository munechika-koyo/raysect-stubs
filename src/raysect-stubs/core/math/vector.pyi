from collections.abc import Iterator

from ._vec3 import _Vec3  # pyright: ignore[reportPrivateUsage]
from .affinematrix import AffineMatrix3D

class Vector2D:
    """
    Represents a vector in 2D space.

    2D vectors are described by their (x, y) coordinates. Standard Vector2D operations are
    supported such as addition, subtraction, scaling, dot product, cross product and normalisation.

    If no initial values are passed, Vector2D defaults to a unit vector
    aligned with the x-axis: Vector2D(1.0, 0.0)

    :param float x: initial x coordinate, defaults to x = 0.0.
    :param float y: initial y coordinate, defaults to y = 0.0.

    :ivar float x: x-coordinate
    :ivar float y: y-coordinate

    .. code-block:: pycon

        >>> from raysect.core import Vector2D
        >>> a = Vector2D(1, 0)

    """

    x: float
    y: float
    def __init__(self, x: float = 1.0, y: float = 0.0) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def __repr__(self) -> str:
        """Returns a string representation of the Vector2D object."""
    def __richcmp__(self, other: Vector2D, op: int) -> bool:
        """Provides basic vector comparison operations."""
    def __getitem__(self, index: int) -> float:
        """
        Returns the vector coordinates by index ([0,1] -> [x,y]).

            >>> a = Vector2D(1, 0)
            >>> a[0]
            1
        """
    def __setitem__(self, index: int, value: float) -> None:
        """
        Sets the vector coordinates by index ([0,1] -> [x,y]).

            >>> a = Vector2D(1, 0)
            >>> a[1] = 2
            >>> a
            Vector2D(1.0, 2.0)
        """
    def __iter__(self) -> Iterator[float]:
        """
        Iterates over the vector coordinates (x, y)

            >>> a = Vector2D(1, 0)
            >>> x, y = a
            >>> x, y
            (1.0, 0.0)

        """
    def __neg__(self) -> Vector2D:
        """
        Returns a vector with the reverse orientation (negation operator).

            >>> a = Vector2D(1, 0)
            >>> -a
            Vector2D(-1.0, -0.0)

        """
    def __add__(self, other: Vector2D) -> Vector2D:
        """
        Addition operator.

            >>> Vector2D(1, 0) + Vector2D(0, 1)
            Vector2D(1.0, 1.0)
        """
    def __sub__(self, other: Vector2D) -> Vector2D:
        """
        Subtraction operator.

            >>> Vector2D(1, 0) - Vector2D(0, 1)
            Vector2D(1.0, -1.0)
        """
    def __mul__(self, other: float) -> Vector2D:
        """
        Multiplication operator.

            >>> Vector3D(1, 2) * 2
            Vector2D(2.0, 4.0)
        """
    def __rmul__(self, other: float) -> Vector2D:
        """
        Reverse multiplication operator.

            >>> 2 * Vector3D(1, 2)
            Vector2D(2.0, 4.0)
        """
    def __truediv__(self, other: float) -> Vector2D:
        """
        Division operator.

            >>> Vector2D(1, 1) / 2
            Vector2D(0.5, 0.5)
        """
    @property
    def length(self) -> float:
        """
        The vector's length.

        Raises a ZeroDivisionError if an attempt is made to change the length of
        a zero length vector. The direction of a zero length vector is
        undefined hence it can not be lengthened.

            >>> a = Vector2D(1, 1)
            >>> a.length
            1.4142135623730951

        """
    @length.setter
    def length(self, value: float) -> None: ...
    def dot(self, b: Vector2D) -> float:
        """
        Calculates the dot product between this vector and the supplied vector.

        :rtype: float

        .. code-block:: pycon

            >>> a = Vector2D(1, 1)
            >>> b = Vector2D(0, 1)
            >>> a.dot(b)
            1.0

        """
    def cross(self, b: Vector2D) -> float:
        """
        Calculates the 2D cross product analogue between this vector and the supplied vector

        C = A.cross(B) <=> C = A x B <=> det(A, B) = A.x B.y - A.y B.x

        Note that for 2D vectors, the cross product is the equivalent of the determinant of a
        2x2 matrix. The result is a scalar.

        :param Vector2D v: An input vector with which to calculate the cross product.
        :rtype: float

        .. code-block:: pycon

            >>> a = Vector2D(1, 1)
            >>> b = Vector2D(0, 1)
            >>> a.cross(b)
            >>> 1.0

        """
    def normalise(self) -> Vector2D:
        """
        Returns a normalised copy of the vector.

        The returned vector is normalised to length 1.0 - a unit vector.

        :rtype: Vector2D

        .. code-block:: pycon

            >>> a = Vector2D(1, 1)
            >>> a.normalise()
            Vector2D(0.7071067811865475, 0.7071067811865475)

        """
    def copy(self) -> Vector2D:
        """
        Returns a copy of the vector.

        :rtype: Vector2D

        .. code-block:: pycon

            >>> a = Vector2D(1, 1)
            >>> a.copy()
            Vector2D(1.0, 1.0)

        """
    def orthogonal(self) -> Vector2D:
        """
        Returns a unit vector that is guaranteed to be orthogonal to the vector.

        :rtype: vector2D

        .. code-block:: pycon

            >>> a = Vector2D(1, 1)
            >>> a.orthogonal()
            Vector2D(-0.7071067811865475, 0.7071067811865475

        """

class Vector3D(_Vec3):
    """
    Represents a vector in 3D affine space.

    Vectors are described by their (x, y, z) coordinates in the chosen coordinate system. Standard Vector3D operations are
    supported such as addition, subtraction, scaling, dot product, cross product, normalisation and coordinate
    transformations.

    If no initial values are passed, Vector3D defaults to a unit vector
    aligned with the z-axis: Vector3D(0.0, 0.0, 1.0)

    :param float x: initial x coordinate, defaults to x = 0.0.
    :param float y: initial y coordinate, defaults to y = 0.0.
    :param float z: initial z coordinate, defaults to z = 0.0.

    :ivar float x: x-coordinate
    :ivar float y: y-coordinate
    :ivar float z: z-coordinate

    .. code-block:: pycon

        >>> from raysect.core import Vector3D
        >>> a = Vector3D(1, 0, 0)
    """

    def __init__(self, x: float = 0.0, y: float = 0.0, z: float = 1.0) -> None: ...
    def __repr__(self) -> str:
        """Returns a string representation of the Vector3D object."""
    def __richcmp__(self, other: Vector3D, op: int) -> bool:
        """Provides basic vector comparison operations."""
    def __getitem__(self, index: int) -> float:
        """
        Returns the vector coordinates by index ([0,1,2] -> [x,y,z]).

            >>> a = Vector3D(1, 0, 0)
            >>> a[0]
            1
        """
    def __setitem__(self, index: int, value: float) -> None:
        """
        Sets the vector coordinates by index ([0,1,2] -> [x,y,z]).

            >>> a = Vector3D(1, 0, 0)
            >>> a[1] = 2
            >>> a
            Vector3D(1.0, 2.0, 0.0)
        """
    def __iter__(self) -> Iterator[float]:
        """
        Iterates over the vector coordinates (x, y, z)

            >>> a = Vector3D(0, 1, 2)
            >>> x, y, z = a
            >>> x, y, z
            (0.0, 1.0, 2.0)
        """
    def __neg__(self) -> Vector3D:
        """
        Returns a vector with the reverse orientation (negation operator).

            >>> a = Vector3D(1, 0, 0)
            >>> -a
            Vector3D(-1.0, -0.0, -0.0)
        """
    def __add__(self, y: _Vec3) -> Vector3D:
        """
        Addition operator.

            >>> Vector3D(1, 0, 0) + Vector3D(0, 1, 0)
            Vector3D(1.0, 1.0, 0.0)
        """
    def __radd__(self, x: _Vec3) -> Vector3D:
        """
        Reverse addition operator.

            >>> Vector3D(1, 0, 0) + Vector3D(0, 1, 0)
            Vector3D(1.0, 1.0, 0.0)
        """
    def __sub__(self, y: _Vec3) -> Vector3D:
        """
        Subtraction operator.

            >>> Vector3D(1, 0, 0) - Vector3D(0, 1, 0)
            Vector3D(1.0, -1.0, 0.0)
        """
    def __rsub__(self, x: _Vec3) -> Vector3D:
        """
        Reverse subtraction operator.

           >>> Vector3D(1, 0, 0) - Vector3D(0, 1, 0)
           Vector3D(1.0, -1.0, 0.0)
        """
    def __mul__(self, y: float) -> Vector3D:
        """
        Multiplication operator.

        3D vectors can be multiplied with both scalars and transformation matrices.

            >>> from raysect.core import Vector3D, rotate_x
            >>> Vector3D(1, 2, 3) * 2
            Vector3D(2.0, 4.0, 6.0)
        """
    def __rmul__(self, x: float) -> Vector3D:
        """
        Reverse multiplication operator.

        3D vectors can be multiplied with both scalars and transformation matrices.

            >>> from raysect.core import Vector3D, rotate_x
            >>> 2 * Vector3D(1, 2, 3)
            Vector3D(2.0, 4.0, 6.0)
            >>> rotate_x(90) * Vector3D(0, 0, 1)
            Vector3D(0.0, -1.0, 0.0)
        """
    def __truediv__(self, y: float) -> Vector3D:
        """Division operator.

        >>> Vector3D(1, 1, 1) / 2
        Vector3D(0.5, 0.5, 0.5)
        """

    def cross(self, v: _Vec3) -> Vector3D:
        """
        Calculates the cross product between this vector and the supplied vector

        C = A.cross(B) <=> :math:`\\vec{C} = \\vec{A} \\times \\vec{B}`

        :param Vector3D v: An input vector with which to calculate the cross product.
        :rtype: Vector3D

        .. code-block:: pycon

            >>> a = Vector3D(1, 0, 0)
            >>> b= Vector3D(0, 1, 0)
            >>> a.cross(b)
            Vector3D(0.0, 0.0, 1.0)
        """
    def normalise(self) -> Vector3D:
        """
        Returns a normalised copy of the vector.

        The returned vector is normalised to length 1.0 - a unit vector.

        :rtype: Vector3D

        .. code-block:: pycon

            >>> a = Vector3D(1, 1, 1)
            >>> a.normalise()
            Vector3D(0.5773502691896258, 0.5773502691896258, 0.5773502691896258)
        """
    def transform(self, m: AffineMatrix3D) -> Vector3D:
        """
        Transforms the vector with the supplied AffineMatrix3D.

        The vector is transformed by pre-multiplying the vector by the affine
        matrix.

        .. math::

            \\vec{C} = \\textbf{A} \\times \\vec{B}

        This method is substantially faster than using the multiplication
        operator of AffineMatrix3D when called from cython code.

        :param AffineMatrix3D m: The affine matrix describing the required coordinate transformation.
        :return: A new instance of this vector that has been transformed with the supplied Affine Matrix.
        :rtype: Vector3D

        .. code-block:: pycon

            >>> z = Vector3D(0, 0, 1)
            >>> y = z.transform(rotate_x(90))
            >>> y
            Vector3D(0.0, -1.0, 6.123233995736766e-17)
        """
    def copy(self) -> Vector3D:
        """
        Returns a copy of the vector.

        :rtype: Vector3D

        .. code-block:: pycon

            >>> a = Vector3D(1, 1, 1)
            >>> a.copy()
            Vector3D(1.0, 1.0, 1.0)
        """
    def orthogonal(self) -> Vector3D:
        """
        Returns a unit vector that is guaranteed to be orthogonal to the vector.

        :rtype: vector3D

        .. code-block:: pycon

            >>> a = Vector3D(1, 0, 0)
            >>> a.orthogonal()
            Vector3D(0.0, 1.0, 0.0)
        """
    def lerp(self, b: Vector3D, t: float) -> Vector3D:
        """
        Returns the linear interpolation between this vector and the supplied vector.

        .. math::

            v = t \\times \\vec{a} + (1-t) \\times \\vec{b}

        :param Vector3D b: The other vector that bounds the interpolation.
        :param double t: The parametric interpolation point t in (0, 1).

        .. code-block:: pycon

            >>> a = Vector3D(1, 0, 0)
            >>> b = Vector3D(0, 1, 0)
            >>> a.lerp(b, 0.5)
            Vector3D(0.5, 0.5, 0.0)
        """
    def slerp(self, b: Vector3D, t: float) -> Vector3D:
        """
        Performs spherical vector interpolation between two vectors.

        The difference between this function and lerp (linear interpolation) is that the
        vectors are treated as directions and their angles and magnitudes are interpolated
        separately.

        Let :math:`\\theta_0` be the angle between two arbitrary vectors :math:`\\vec{a}`
        and :math:`\\vec{b}`. :math:`\\theta_0` can be calculated through the dot product
        relationship.

        .. math::

            \\theta_0 = \\cos{^{-1}(\\vec{a} \\cdot \\vec{b})}

        The interpolated vector, :math:`\\vec{v}`, has angle :math:`\\theta` measured from
        :math:`\\vec{a}`.

        .. math::

            \\theta = t \\times \\theta_0

        Next we need to find the basis vector :math:`\\hat{e}` such that {:math:`\\hat{a}`,
        :math:`\\hat{e}`} form an orthonormal basis in the same plane as {:math:`\\vec{a}`,
        :math:`\\vec{b}`}.

        .. math::

            \\hat{e} = \\frac{\\vec{b} - \\vec{a} \\times (\\vec{a} \\cdot \\vec{b})}{|\\vec{b} - \\vec{a} \\times (\\vec{a} \\cdot \\vec{b})|}

        The resulting interpolated direction vector can now be defined as

        .. math::

            \\hat{v} = \\hat{a} \\times \\cos{\\theta} + \\hat{e} \\times \\sin{\\theta}.

        Finally, the magnitude can be interpolated separately by linearly interpolating the original
        vector magnitudes.

        .. math::

            \\vec{v} = \\hat{v} \\times (t \\times |\\vec{a}| + (1-t) \\times |\\vec{b}|)

        :param Vector3D b: The other vector that bounds the interpolation.
        :param double t: The parametric interpolation point t in (0, 1).

        .. code-block:: pycon

            >>> a = Vector3D(1, 0, 0)
            >>> b = Vector3D(0, 1.5, 0)
            >>> a.slerp(b, 0.5)
            Vector3D(0.8838834764831844, 0.8838834764831843, 0.0)
        """
