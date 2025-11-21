from .math import Point3D, Vector3D

class Ray:
    """
    Describes a line in space with an origin and direction.

    Note that the core Ray class only implements the geometry calculations needed for
    intersections and is not capable of any optical simulations. For that you would
    need the derived optical Ray class (:meth:`raysect.optical.ray.Ray <raysect.optical.ray.Ray>`).

    :param Point3D origin: Point defining ray's origin (default is Point3D(0, 0, 0)).
    :param Vector3D direction: Vector defining ray's direction (default is Vector3D(0, 0, 1)).
    :param double max_distance: The terminating distance of the ray.

    :ivar Point3D origin: The Ray's origin point.
    :ivar Vector3D direction: The Ray's direction.
    :ivar float max_distance: The terminating distance of the ray.

    .. code-block:: pycon

        >>> from raysect.core import Point3D, Vector3D
        >>> from raysect.core.ray import Ray as CoreRay
        >>>
        >>> intersection = world.hit(CoreRay(Point3D(0, 0, 0,), Vector3D(1, 0, 0)))
        >>> if intersection is not None:
        >>>     # do something with the intersection results
    """

    origin: Point3D
    direction: Vector3D
    max_distance: float
    def __init__(self, origin: Point3D | None = None, direction: Vector3D | None = None, max_distance: float = float("inf")) -> None: ...
    def point_on(self, t: float) -> Point3D:
        """
        Returns the point on the ray at the specified parametric distance from the ray origin.

        Positive values correspond to points forward of the ray origin, along the ray direction.

        :param double t: The distance along the ray.
        :return: A point at distance t along the ray direction measured from its origin.
        :rtype: Point3D

        .. code-block:: pycon

            >>> from raysect.core import Point3D, Vector3D
            >>> from raysect.core.ray import Ray as CoreRay
            >>>
            >>> a = CoreRay(Point3D(0, 0, 0,), Vector3D(1, 0, 0))
            >>> a.point_on(2)
            Point3D(2.0, 0.0, 0.0)
        """
    def copy(self, origin: Point3D | None = None, direction: Vector3D | None = None) -> Ray:
        """
        Copy this ray to a new Ray instance.

        :param Point3D origin: Point defining origin (default is Point3D(0, 0, 0)).
        :param Vector3D direction: Vector defining direction (default is Vector3D(0, 0, 1)).
        :return: A new Ray instance.
        :rtype: Ray

        .. code-block:: pycon

            >>> from raysect.core import Point3D, Vector3D
            >>> from raysect.core.ray import Ray as CoreRay
            >>>
            >>> a = CoreRay(Point3D(0, 0, 0,), Vector3D(1, 0, 0))
            >>> a.copy()
            Ray(Point3D(0.0, 0.0, 0.0), Vector3D(1.0, 0.0, 0.0), inf)
        """
