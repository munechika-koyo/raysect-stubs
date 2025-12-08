from collections.abc import Iterator

from .affinematrix import AffineMatrix3D
from .vector import Vector3D

class Quaternion:
    x: float
    y: float
    z: float
    s: float

    def __init__(self, x: float = 0.0, y: float = 0.0, z: float = 0.0, s: float = 1.0) -> None: ...
    def __repr__(self) -> str:
        """Returns a string representation of the Quaternion object."""
    def __getitem__(self, i: int) -> float:
        """Returns the quaternion coordinates by index ([0,1,2,3] -> [x,y,z,s]).

        .. code-block:: pycon

            >>> a = Quaternion(0, 0, 0, 1)
            >>> a[3]
            1
        """
    def __setitem__(self, i: int, value: float) -> None:
        """Sets the quaternion coordinates by index ([0,1,2,3] -> [x,y,z,s]).

        .. code-block:: pycon

            >>> a = Quaternion(0, 0, 0, 1)
            >>> a[1] = 2
            >>> a
            Quaternion(0.0, 2.0, 0.0, 1.0)
        """
    def __iter__(self) -> Iterator[float]:
        """Iterates over the quaternion coordinates (x, y, z, s)

        >>> a = Quaternion(0, 1, 2, 3)
        >>> x, y, z, s = a
        >>> x, y, z, s
        (0.0, 1.0, 2.0, 3.0)
        """
    def __neg__(self) -> Quaternion:
        """
        Returns a Quaternion with the reverse orientation (negation operator).

        Note however that (s + x i + y j + z k) and (- s - x i - y j - z k)
        represent the same rotations. Even though negation generates a different
        quaternion it represents the same overall rotation.

        .. code-block:: pycon

            >>> a = Quaternion(0, 0, 0, 1)
            >>> -a
            Quaternion(-0.0, -0.0, -0.0, -1.0)
        """
    def __eq__(self, y: object) -> bool:
        """
        Equality operator.

        .. code-block:: pycon

            >>> Quaternion(0, 0, 0, 1) == Quaternion(0, 0, 0, 1)
            True
        """
    def __add__(self, y: Quaternion) -> Quaternion:
        """
        Addition operator.

        .. code-block:: pycon

            >>> Quaternion(0, 0, 0, 1) + Quaternion(0, 1, 0, 0)
            Quaternion(0.0, 1.0, 0.0, 1.0)
        """
    def __sub__(self, y: Quaternion) -> Quaternion:
        """Subtraction operator.

        .. code-block:: pycon

            >>> Quaternion(0, 0, 0, 1) - Quaternion(0, 1, 0, 0)
            Quaternion(0.0, -1.0, 0, 1.0)
        """
    def __mul__(self, y: float | Quaternion) -> Quaternion:
        """Multiplication operator.

        .. code-block:: pycon

            >>> Quaternion(0, 0, 1, 1) * 2
            Quaternion(0.0, 0.0, 2.0, 2.0)
            >>> Quaternion(0, 1, 0, 1) * Quaternion(1, 2, 3, 0)
            Quaternion(4.0, 2.0, 2.0, -2.0)
        """
    def __rmul__(self, y: float) -> Quaternion:
        """Reverse multiplication operator.

        .. code-block:: pycon

            >>> 2 * Quaternion(0, 0, 1, 1)
            Quaternion(0.0, 0.0, 2.0, 2.0)
        """
    def __truediv__(self, y: float | Quaternion) -> Quaternion:
        """Division operator.

        .. code-block:: pycon

            >>> Quaternion(0, 0, 1, 1) / 2
            Quaternion(0.0, 0.0, 0.5, 0.0.5)
            >>> Quaternion(0, 0, 1, 1) / Quaternion(1, 2, 3, 0)
            Quaternion(-0.28571, -0.14286, -0.14286, 0.14286)
        """
    @property
    def length(self) -> float:
        """
        Calculates the length (norm) of the quaternion.

        .. code-block:: pycon

            >>> Quaternion(1, 2, 3, 0).length
            3.7416573867739413
        """
    @length.setter
    def length(self, value: float) -> None: ...
    @property
    def axis(self) -> Vector3D:
        """
        The axis around which this quaternion rotates.
        """
    @property
    def angle(self) -> float:
        """
        The magnitude of rotation around this quaternion's rotation axis in degrees.
        """
    def copy(self) -> Quaternion:
        """
        Returns a copy of this quaternion.
        """
    def conjugate(self) -> Quaternion:
        """
        Complex conjugate operator.

        .. code-block:: pycon

            >>> Quaternion(1, 2, 3, 0).conjugate()
            Quaternion(-1, -2, -3, 0)
        """
    def inverse(self) -> Quaternion:
        """
        Inverse operator.

        .. code-block:: pycon

            >>> Quaternion(1, 2, 3, 0).inverse()
            Quaternion(-0.07143, -0.14286, -0.21429, 0.0)
        """
    def normalise(self) -> Quaternion:
        """
        Returns a normalised copy of the quaternion.

        The returned quaternion is normalised to have norm length 1.0 - a unit quaternion.

        .. code-block:: pycon

            >>> a = Quaternion(1, 2, 3, 0)
            >>> a.normalise()
            Quaternion(0.26726, 0.53452, 0.80178, 0.0)
        """
    def is_unit(self, tolerance: float = 1e-10) -> bool:
        """
        Returns True if this is a unit quaternion (versor) to within specified tolerance.

        :param float tolerance: The numerical tolerance by which the quaternion norm can differ by 1.0.
        """
    def transform(self, m: AffineMatrix3D) -> Quaternion:
        """
        Transforms the quaternion with the supplied AffineMatrix3D.

        :param AffineMatrix3D m: The affine matrix describing the required coordinate transformation.
        :return: A new instance of this quaternion that has been transformed with the supplied Affine Matrix.
        :rtype: Quaternion
        """
    def as_matrix(self) -> AffineMatrix3D:
        """
        Generates an AffineMatrix3D representation of this Quaternion.

        .. code-block:: pycon

           >>> from raysect.core.math import Quaternion
           >>>
           >>> q = Quaternion(0.5, 0, 0, 0.5)
           >>> q.as_matrix()
           AffineMatrix3D([[1.0, 0.0, 0.0, 0.0],
                           [0.0, 0.0, -1.0, 0.0],
                           [0.0, 1.0, 0.0, 0.0],
                           [0.0, 0.0, 0.0, 1.0]])
        """
    def quaternion_to(self, q2: Quaternion) -> Quaternion:
        """
        Calculates the quaternion between quaternions.

        This method calculates the quaternion required to map this quaternion
        onto the supplied quaternion. Both quaternions will be normalised and
        a normalised quaternion will be returned.

        .. code-block:: pycon

          >>> from raysect.core.math import Quaternion
          >>>
          >>> q1 = Quaternion.from_axis_angle(Vector3D(1,0,0), 10)
          >>> q2 = Quaternion.from_axis_angle(Vector3D(1,0,0), 25)
          >>> d = q1.quaternion_to(q2)
          >>> d
          Quaternion(0.13052619222005157, 0.0, 0.0, 0.9914448613738104)
          >>> d.angle
          15.000000000000027
          >>> d.axis
          Vector3D(1.0, 0.0, 0.0)

        :param Quaternion q: The target quaternion.
        :return: A new Quaternion object representing the specified rotation.
        """
    @classmethod
    def from_matrix(cls, matrix: AffineMatrix3D) -> Quaternion:
        """
        Extract the rotation part of an AffineMatrix3D as a Quaternion.

        Note, the translation component of this matrix will be ignored.

        :param AffineMatrix3D matrix: The AffineMatrix3D instance from which to extract the rotation component.
        :return: A quaternion representation of the rotation specified in this transform matrix.

        .. code-block:: pycon

           >>> from raysect.core.math import rotate_x, Quaternion
           >>>
           >>> Quaternion.from_matrix(rotate_x(90))
           Quaternion(0.7071067811865475, 0.0, 0.0, 0.7071067811865476)
        """
    @classmethod
    def from_axis_angle(cls, axis: Vector3D, angle: float) -> Quaternion:
        """
        Generates a new Quaternion from the axis-angle specification.

        :param Vector3D axis: The axis about which rotation will be performed.
        :param float angle: An angle in degrees specifying the magnitude of the
          rotation about the axis vector.
        :return: A new Quaternion object representing the specified rotation.

        .. code-block:: pycon

           >>> from raysect.core.math import Quaternion, Vector3D
           >>>
           >>> Quaternion.from_axis_angle(Vector3D(1, 0, 0), 45)
           Quaternion(0.3826834323650898, 0.0, 0.0, 0.9238795325112867)
        """
