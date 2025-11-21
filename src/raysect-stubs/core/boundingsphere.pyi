from .math import Point3D
from .ray import Ray

class BoundingSphere3D:
    """
    A bounding sphere.

    Represents a bounding sphere around a primitive's surface. The sphere's
    centre point and radius must be specified in world space.

    :param Point3D centre: the centre point of the bounding sphere.
    :param float radius: the radius of the sphere that bounds the primitive.
    """

    def __init__(self, centre: Point3D, radius: float) -> None: ...
    def __repr__(self) -> str: ...
    @property
    def centre(self) -> Point3D:
        """
        The point defining the centre of the bounding sphere.

        :rtype: Point3D
        """
    @property
    def radius(self) -> float:
        """
        The radius of the bounding sphere.

        :rtype: float
        """
    def hit(self, ray: Ray) -> bool:
        """
        Returns true if the ray hits the bounding box.

        :param Ray ray: The ray to test for intersection.
        :rtype: boolean
        """
    def full_intersection(self, ray: Ray) -> tuple[bool, float, float]:
        """
        Returns full intersection information for an intersection between a ray and a bounding box.

        The first value is a boolean which is true if an intersection has occurred, false otherwise. Each intersection
        with a bounding box will produce two intersections, one on the front and back of the box. The remaining two
        tuple parameters are floats representing the distance along the ray path to the respective intersections.

        :param ray: The ray to test for intersection
        :return: A tuple of intersection parameters, (hit, front_intersection, back_intersection).
        :rtype: tuple
        """
    def contains(self, point: Point3D) -> bool:
        """
        Returns true if the given 3D point lies inside the bounding sphere.

        :param Point3D point: A given test point.
        :rtype: boolean
        """
    def union(self, sphere: BoundingSphere3D) -> None:
        """
        Union this bounding sphere instance with the input bounding sphere.

        The resulting bounding sphere will be larger so as to just enclose both bounding spheres.
        This class instance will be edited in place to have the new bounding sphere dimensions.

        :param BoundingSphere3D sphere: A bounding sphere instance to union with this bounding sphere instance.
        """
    def extend(self, point: Point3D, padding: float = 0.0) -> None:
        """
        Enlarge this bounding box to enclose the given point.

        The resulting bounding box will be larger so as to just enclose the existing bounding box and the new point.
        This class instance will be edited in place to have the new bounding box dimensions.

        :param Point3D point: the point to use for extending the bounding box.
        :param float padding: optional padding parameter, gives extra margin around the new point.
        """
    def surface_area(self) -> float:
        """
        Returns the surface area of the bounding sphere.

        :rtype: float
        """
    def volume(self) -> float:
        """
        Returns the volume of the bounding sphere.

        :rtype: float
        """
    def pad(self, padding: float) -> None:
        """
        Makes the bounding sphere larger by the specified amount of padding.

        :param float padding: Distance to use as padding margin.
        """
