from .affinematrix import AffineMatrix3D
from .point import Point3D
from .vector import Vector3D

def translate(x: float, y: float, z: float) -> AffineMatrix3D:
    """
    Returns an affine matrix representing a translation of the coordinate space.

    Equivalent to the transform matrix, :math:`\\mathbf{T_{AB}}`, where :math:`\\vec{t}`
    is the vector from the origin of space A to space B.

    .. math::

        \\mathbf{T_{AB}} = \\left( \\begin{array}{cccc} 1 & 0 & 0 & \\vec{t}.x \\\\
        0 & 1 & 0 & \\vec{t}.y \\\\
        0 & 0 & 1 & \\vec{t}.z \\\\
        0 & 0 & 0 & 1 \\end{array} \\right)

    :param float x: x-coordinate
    :param float y: y-coordinate
    :param float z: z-coordinate
    :rtype: AffineMatrix3D

    .. code-block:: pycon

        >>> from raysect.core import translate
        >>> translate(0, 1, 2)
        AffineMatrix3D([[1.0, 0.0, 0.0, 0.0],
                        [0.0, 1.0, 0.0, 1.0],
                        [0.0, 0.0, 1.0, 2.0],
                        [0.0, 0.0, 0.0, 1.0]])
    """

def rotate_x(angle: float) -> AffineMatrix3D:
    """
    Returns an affine matrix representing the rotation of the coordinate space
    about the X axis by the supplied angle.

    The rotation direction is clockwise when looking along the x-axis.

    .. math::

        \\mathbf{T_{AB}} = \\left( \\begin{array}{cccc} 1 & 0 & 0 & 0 \\\\
        0 & \\cos{\\theta} & -\\sin{\\theta} & 0 \\\\
        0 & \\sin{\\theta} & \\cos{\\theta} & 0 \\\\
        0 & 0 & 0 & 1 \\end{array} \\right)

    :param float angle: The angle :math:`\\theta` specified in degrees.
    :rtype: AffineMatrix3D

    .. code-block:: pycon

        >>> from raysect.core import rotate_x
        >>> rotate_x(45)
        AffineMatrix3D([[1.0, 0.0, 0.0, 0.0],
                        [0.0, 0.7071067811865476, -0.7071067811865475, 0.0],
                        [0.0, 0.7071067811865475, 0.7071067811865476, 0.0],
                        [0.0, 0.0, 0.0, 1.0]])
    """

def rotate_y(angle: float) -> AffineMatrix3D:
    """
    Returns an affine matrix representing the rotation of the coordinate space
    about the Y axis by the supplied angle.

    The rotation direction is clockwise when looking along the y-axis.

    .. math::

        \\mathbf{T_{AB}} = \\left( \\begin{array}{cccc} \\cos{\\theta} & 0 & \\sin{\\theta} & 0 \\\\
        0 & 1 & 0 & 0 \\\\
        -\\sin{\\theta} & 0 & \\cos{\\theta} & 0 \\\\
        0 & 0 & 0 & 1 \\end{array} \\right)

    :param float angle: The angle :math:`\\theta` specified in degrees.
    :rtype: AffineMatrix3D
    """

def rotate_z(angle: float) -> AffineMatrix3D:
    """
    Returns an affine matrix representing the rotation of the coordinate space
    about the Z axis by the supplied angle.

    The rotation direction is clockwise when looking along the z-axis.

    .. math::

        \\mathbf{T_{AB}} = \\left( \\begin{array}{cccc} \\cos{\\theta} & -\\sin{\\theta} & 0 & 0 \\\\
        \\sin{\\theta} & \\cos{\\theta} & 0 & 0 \\\\
        0 & 0 & 1 & 0 \\\\
        0 & 0 & 0 & 1 \\end{array} \\right)

    :param float angle: The angle :math:`\\theta` specified in degrees.
    :rtype: AffineMatrix3D
    """

def rotate_vector(angle: float, v: Vector3D) -> AffineMatrix3D:
    """
    Returns an affine matrix representing the rotation of the coordinate space
    about the supplied vector by the specified angle.

    :param float angle: The angle specified in degrees.
    :param Vector3D v: The vector about which to rotate.
    :rtype: AffineMatrix3D

    .. code-block:: pycon

        >>> from raysect.core import rotate_vector
        >>> rotate_vector(90, Vector3D(1, 0, 0))
        AffineMatrix3D([[1.0, 0.0, 0.0, 0.0],
                        [0.0, 0.0, -1.0, 0.0],
                        [0.0, 1.0, 0.0, 0.0],
                        [0.0, 0.0, 0.0, 1.0]])
    """

def rotate(yaw: float, pitch: float, roll: float) -> AffineMatrix3D:
    """
    Returns an affine transform matrix representing an intrinsic rotation with
    an axis order (-Y)(-X)'Z''.

    For an object aligned such that forward is the +ve Z-axis, left is the +ve
    X-axis and up is the +ve Y-axis then this rotation operation corresponds to
    the yaw, pitch and roll of the object.

    :param float yaw: Yaw angle in degrees.
    :param float pitch: Pitch angle in degrees.
    :param float roll: Roll angle in degrees.
    :rtype: AffineMatrix3D
    """

def rotate_basis(forward: Vector3D, up: Vector3D) -> AffineMatrix3D:
    """
    Returns a rotation matrix defined by forward and up vectors.

    The +ve Z-axis of the resulting coordinate space will be aligned with the
    forward vector. The +ve Y-axis will be aligned to lie in the plane defined
    the forward and up vectors, along the projection of the up vector that
    lies orthogonal to the forward vector. The X-axis will lie perpendicular to
    the plane.

    The forward and upwards vectors need not be orthogonal. The up vector will
    be rotated in the plane defined by the two vectors until it is orthogonal.

    :param Vector3D forward: A Vector3D object defining the forward direction.
    :param Vector3D up: A Vector3D object defining the up direction.
    :rtype: AffineMatrix3D

    .. code-block:: pycon

        >>> from raysect.core import rotate_basis, Vector3D
        >>> rotate_basis(Vector3D(1, 0, 0), Vector3D(0, 0, 1))
        AffineMatrix3D([[0.0, 0.0, 1.0, 0.0],
                        [1.0, 0.0, 0.0, 0.0],
                        [0.0, 1.0, 0.0, 0.0],
                        [0.0, 0.0, 0.0, 1.0]])
    """

def to_cylindrical(point: Point3D) -> tuple[float, float, float]:
    """
    Convert the given 3D point in cartesian space to cylindrical coordinates.

    :param Point3D point: The 3D point to be transformed into cylindrical coordinates.
    :rtype: tuple
    :return: A tuple of r, z, phi coordinates.

    .. code-block:: pycon

        >>> from raysect.core.math import to_cylindrical, Point3D

        >>> point = Point3D(1, 1, 1)
        >>> to_cylindrical(point)
        (1.4142135623730951, 1.0, 45.0)
    """

def from_cylindrical(r: float, z: float, phi: float) -> Point3D:
    """
    Convert a 3D point in cylindrical coordinates to a point in cartesian coordinates.

    :param float r: The radial coordinate.
    :param float z: The z-axis height coordinate.
    :param float phi: The azimuthal coordinate in degrees.
    :rtype: Point3D
    :return: A Point3D in cartesian space.

    .. code-block:: pycon

        >>> from raysect.core.math import from_cylindrical

        >>> from_cylindrical(1, 0, 45)
        Point3D(0.7071067811865476, 0.7071067811865475, 0.0)
    """

def extract_rotation(m: AffineMatrix3D, z_up: bool = False) -> tuple[float, float, float]:
    """
    Extracts the rotation component of the affine matrix.

    The yaw, pitch and roll can be extracted for two common coordinate
    conventions by specifying the z_axis orientation:

        forward: +ve z is forward, +ve y is up, +ve x is left
        up:      +ve z is up, +ve y is left, +ve x is forward

    The Raysect default is z axis forward. This function can be switched
    to z axis up by setting the z_up parameter to True.

    The matrix must consist of only rotation and translation operations.

    :param AffineMatrix3D m: An affine matrix.
    :param bint z_up: Is the z-axis pointed upwards (default=False).
    :return: A tuple containing (yaw, pitch, roll).
    """

def extract_translation(m: AffineMatrix3D) -> tuple[float, float, float]:
    """
    Extracts the translation component of the affine matrix.

    The matrix must consist of only rotation and translation operations.

    :param AffineMatrix3D m: An affine matrix.
    :return: tuple containing the x, y and z components of the translation.
    """
