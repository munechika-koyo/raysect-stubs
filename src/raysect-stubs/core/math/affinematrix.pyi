from ._mat4 import _Mat4  # pyright: ignore[reportPrivateUsage]

class AffineMatrix3D(_Mat4):
    """A 4x4 affine matrix.

    These matrices are used for transforming between coordinate systems. Every
    primitive in Raysect works in its own local coordinate system, so it is common
    to need to transform 3D points from local to world spave and vice versa. Even
    though the vectors themselves are 3D, a 4x4 matrix is needed to completely
    specify a transformation from one 3D space to another.

    The coordinate transformation is applied by multiplying the column vector for
    the desired Point3D/Vector3D against the transformation matrix. For example,
    if the original vector :math:`\\vec{V_a}` is in space A and the transformation matrix
    :math:`\\mathbf{T_{AB}}` describes the position and orientation of Space A relative
    to Space B, then the multiplication

    .. math::

        \\vec{V_{b}} = \\mathbf{T_{AB}} \\times \\vec{V_a}

    yields the same vector transformed into coordinate Space B, :math:`\\vec{V_b}`.

    The individual terms of the transformation matrix can be visualised in terms of
    the way they change the underlying basis vectors.

    .. math::

        \\mathbf{T_{AB}} = \\left( \\begin{array}{cccc} \\vec{x_b}.x & \\vec{y_b}.x & \\vec{z_b}.x & \\vec{t}.x \\\\
        \\vec{x_b}.y & \\vec{y_b}.y & \\vec{z_b}.y & \\vec{t}.y \\\\
        \\vec{x_b}.z & \\vec{y_b}.z & \\vec{z_b}.z & \\vec{t}.z \\\\
        0 & 0 & 0 & 1 \\end{array} \\right)

    Here the unit x-axis vector in space A, :math:`\\vec{x}_a = (1, 0, 0)`, has been transformed
    into space B, :math:`\\vec{x_b}`. The same applies to :math:`\\vec{y_b}` and :math:`\\vec{z_b}` for
    the  :math:`\\vec{y}_a` and :math:`\\vec{z}_a` unit vectors respectively. Together the new basis
    vectors describe a rotation of the original coordinate system.

    The vector :math:`\\vec{t}` in the last column corresponds to a translation vector between the
    origin's of space A and space B.

    Strictly speaking, the new rotation vectors don't have to be normalised which
    corresponds to a scaling in addition to the rotation. For example, a scaling matrix
    would look like the following.

    .. math::

        \\mathbf{T_{scale}} = \\left( \\begin{array}{cccc} \\vec{s}.x & 0 & 0 & 0 \\\\
        0 & \\vec{s}.y & & 0 \\\\
        0 & 0 & \\vec{s}.z & 0 \\\\
        0 & 0 & 0 & 1 \\end{array} \\right)

    Multiple transformations can be chained together by multiplying the
    matrices together, the resulting matrix will encode the full transformation.
    The order in which transformations are applied is very important. The operation
    :math:`\\mathbf{M_{translate}} \\times \\mathbf{M_{rotate}}` is different to
    :math:`\\mathbf{M_{rotate}} \\times \\mathbf{M_{translate}}` because matrices don't
    commute, and physically these are different operations.

    .. warning::
        Because we are using column vectors, transformations should be
        applied **right to left**.

    An an example operation, let us consider the case of moving and rotating a camera in
    our scene. Suppose we want to rotate our camera at an angle of :math:`\\theta_x=45`
    around the x-axis and translate the camera to position :math:`p=(0, 0, 3.5)`. This set
    of operations would be equivalent to:

    .. math::

        \\mathbf{T} = \\mathbf{T_{translate}} \\times \\mathbf{T_{rotate}}

    In code this would be equivalent to: ::

        >>> transform = translate(0, 0, -3.5) * rotate_x(45)

    If no initial values are passed to the matrix, it defaults to an identity matrix.

    :param object m: Any 4 x 4 indexable or 16 element object can be used to
      initialise the matrix. 16 element objects must be specified in
      row-major format.

    """
    def __repr__(self) -> str:
        """String representation."""
    def __mul__(self, y: AffineMatrix3D) -> AffineMatrix3D:
        """Multiplication operator.

        >>> from raysect.core import translate, rotate_x
        >>> translate(0, 0, -3.5) * rotate_x(45)
        AffineMatrix3D([[1.0, 0.0, 0.0, 0.0],
                        [0.0, 0.7071067811865476, -0.7071067811865475, 0.0],
                        [0.0, 0.7071067811865475, 0.7071067811865476, -3.5],
                        [0.0, 0.0, 0.0, 1.0]])
        """
    def inverse(self) -> AffineMatrix3D:
        """
        Calculates the inverse of the affine matrix.

        Returns an AffineMatrix3D containing the inverse.

        Raises a ValueError if the matrix is singular and the inverse can not be
        calculated. All valid affine transforms should be invertable.

            >>> from raysect.core import AffineMatrix3D
            >>> m = AffineMatrix3D([[0.0, 0.0, 1.0, 0.0],
                                    [1.0, 0.0, 0.0, 0.0],
                                    [0.0, 1.0, 0.0, 0.0],
                                    [0.0, 0.0, 0.0, 1.0]])
            >>> m.inverse()
            AffineMatrix3D([[0.0, 1.0, 0.0, -0.0],
                            [0.0, 0.0, 1.0, 0.0],
                            [1.0, 0.0, 0.0, -0.0],
                            [0.0, 0.0, -0.0, 1.0]])
        """
