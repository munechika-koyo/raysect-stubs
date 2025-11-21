from .math import AffineMatrix3D, Normal3D, Point3D
from .ray import Ray
from .scenegraph.primitive import Primitive

class Intersection:
    """
    Describes the result of a ray-primitive intersection.

    Users are unlikely to instance this class themselves, in most cases they will
    need to inspect this object as the result of a Ray-Primitive intersection
    encountered in the world.hit() method
    (:meth:`raysect.core.scenegraph.world.World.hit <raysect.core.scenegraph.world.World.hit>`).

    The inside and outside points are launch points for rays emitted from the hit point on the surface. Rays cannot be
    launched from the hit point directly as they risk re-intersecting the same surface due to numerical accuracy. The
    inside and outside points are slightly displaced from the primitive surface at a sufficient distance to prevent
    re-intersection due to numerical accuracy issues. The inside_point is shifted backwards into the surface relative to
    the surface normal. The outside_point is equivalently shifted away from the surface in the direction of the surface
    normal.

    :param Ray ray: The incident ray object (world space).
    :param double ray_distance: The distance of the intersection along the ray path.
    :param Primitive primitive: The intersected primitive object.
    :param Point3D hit_point: The point of intersection between the ray and the primitive (primitive local space).
    :param Point3D inside_point: The interior ray launch point (primitive local space).
    :param Point3D outside_point: The exterior ray launch point (primitive local space).
    :param Normal3D normal: The surface normal (primitive local space)
    :param bool exiting: True if the ray is exiting the surface, False otherwise.
    :param AffineMatrix3D world_to_primitive: A world to primitive local transform matrix.
    :param AffineMatrix3D primitive_to_world: A primitive local to world transform matrix.

    :ivar bool exiting: True if the ray is exiting the surface, False otherwise.
    :ivar Point3D hit_point: The point of intersection between the ray and the primitive
      (primitive local space).
    :ivar Point3D inside_point: The interior ray launch point (primitive local space).
    :ivar Normal3D normal: The surface normal (primitive local space).
    :ivar Point3D outside_point: The exterior ray launch point (primitive local space).
    :ivar Primitive primitive: The primitive object that was intersected by the Ray.
    :ivar AffineMatrix3D primitive_to_world: The primitive's local to world transform matrix.
    :ivar Ray ray: The incident ray object (world space).
    :ivar double ray_distance: The distance of the intersection along the ray path.
    :ivar AffineMatrix3D world_to_primitive: A world to primitive local transform matrix.

    .. code-block:: pycon

        >>> from raysect.core import Point3D, Vector3D
        >>> from raysect.core.ray import Ray as CoreRay
        >>>
        >>> intersection = world.hit(CoreRay(Point3D(0, 0, 0,), Vector3D(1, 0, 0)))
        >>> if intersection is not None:
        >>>     hit_point = intersection.hit_point.transform(intersection.primitive_to_world)
        >>>     # do something with the hit point...
    """

    ray: Ray
    ray_distance: float
    exiting: bool
    hit_point: Point3D
    inside_point: Point3D
    normal: Normal3D
    outside_point: Point3D
    primitive: Primitive
    primitive_to_world: AffineMatrix3D
    world_to_primitive: AffineMatrix3D
    def __init__(
        self,
        ray: Ray,
        ray_distance: float,
        primitive: Primitive,
        hit_point: Point3D,
        inside_point: Point3D,
        outside_point: Point3D,
        normal: Normal3D,
        exiting: bool,
        world_to_primitive: AffineMatrix3D,
        primitive_to_world: AffineMatrix3D,
    ) -> None: ...
