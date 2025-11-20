from collections.abc import Iterator

class _Vec3:
    """3D Vector base class."""

    length: float
    x: float
    y: float
    z: float
    def __init__(self, x: float = 0.0, y: float = 0.0, z: float = 1.0) -> None:
        """
        Constructor.

        If no initial values are passed, _Vec3 defaults to a unit vector
        aligned with the z-axis: _Vec(0.0, 0.0, 1.0)
        """
    def __getitem__(self, index: int) -> float:
        """Returns the vector coordinates by index ([0,1,2] -> [x,y,z])."""
    def __setitem__(self, index: int, object: float) -> None:
        """Sets the vector coordinates by index ([0,1,2] -> [x,y,z])."""
    def __iter__(self) -> Iterator[float]:
        """Implement iter(self)."""
    def angle(self, b: _Vec3) -> float:
        """
        Calculates the angle between this vector and the supplied vector.

        Returns the angle in degrees.

            >>> a = Vector3D(1, 1, 1)
            >>> b = Vector3D(1, 0, 0)
            >>> a.angle(b)
            54.735610317245346
        """
    def dot(self, b: _Vec3) -> float:
        """
        Calculates the dot product between this vector and the supplied vector.

        :rtype: float

        .. code-block:: pycon

            >>> a = Vector3D(1, 1, 1)
            >>> b = Vector3D(1, 0, 0)
            >>> a.dot(b)
            1.0
        """
