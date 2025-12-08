from .boundingsphere import BoundingSphere3D
from .math import Point2D, Point3D
from .ray import Ray

class BoundingBox2D:
    """
    Axis-aligned 2D bounding box.

    :param Point2D lower: (optional) starting point for lower box corner
    :param Point2D upper: (optional) starting point for upper box corner
    """

    def __init__(self, lower: Point2D | None = None, upper: Point2D | None = None) -> None: ...
    def __repr__(self) -> str: ...
    @property
    def lower(self) -> Point2D:
        """
        The point defining the lower corner of the bounding box.

        :rtype: Point2D
        """
    @lower.setter
    def lower(self, value: Point2D) -> None: ...
    @property
    def upper(self) -> Point2D:
        """
        The point defining the upper corner of the bounding box.

        :rtype: Point2D
        """
    @upper.setter
    def upper(self, value: Point2D) -> None: ...
    def contains(self, point: Point2D) -> bool:
        """
        Returns true if the given 2D point lies inside the bounding box.

        :param Point2D point: A given test point.
        :rtype: boolean
        """
    def union(self, box: BoundingBox2D) -> None:
        """
        Union this bounding box instance with the input bounding box.

        The resulting bounding box will be larger so as to just enclose both bounding boxes. This class instance
        will be edited in place to have the new bounding box dimensions.

        :param BoundingBox2D box: A bounding box instance to union with this bounding box instance.
        """
    def extend(self, point: Point2D, padding: float = 0.0) -> None:
        """
        Enlarge this bounding box to enclose the given point.

        The resulting bounding box will be larger so as to just enclose the existing bounding box and the new point.
        This class instance will be edited in place to have the new bounding box dimensions.

        :param Point2D point: the point to use for extending the bounding box.
        :param float padding: optional padding parameter, gives extra margin around the new point.
        """
    def surface_area(self) -> float:
        """
        Returns the surface area of the bounding box.

        :rtype: float
        """
    def vertices(self) -> list[Point2D]:
        """
        Get the list of vertices for this bounding box.

        :return: A list of Point2D's representing the corners of the bounding box.
        :rtype: list
        """
    def extent(self, axis: int) -> float:
        """
        Returns the spatial extend of this bounding box along the given dimension.

        :param int axis: specifies the axis to return, {0: X axis, 1: Y axis}.
        :rtype: float
        """
    def largest_axis(self) -> int:
        """
        Find the largest axis of this bounding box.

        :return: an int specifying the longest axis, {0: X axis, 1: Y axis}.
        :rtype: int
        """
    def largest_extent(self) -> float:
        """
        Find the largest spatial extent across all axes.

        :return: distance along the largest bounding box axis.
        :rtype: float
        """
    def pad(self, padding: float) -> None:
        """
        Makes the bounding box larger by the specified amount of padding.

        Every bounding box axis will end up larger by a factor of 2 x padding.

        :param float padding: distance to use as padding margin
        """
    def pad_axis(self, axis: int, padding: float) -> None:
        """
        Makes the bounding box larger along the specified axis by amount of padding.

        The specified bounding box axis will end up larger by a factor of 2 x padding.

        :param int axis: The axis to apply padding to {0: X axis, 1: Y axis}.
        :param float padding: Distance to use as padding margin.
        """

class BoundingBox3D:
    """
    Axis-aligned bounding box.

    Represents a bounding box around a primitive's surface. The points defining
    the lower and upper corners of the box must be specified in world space.

    Axis aligned bounding box ray intersections are extremely fast to evaluate
    compared to intersections with more general geometry. Prior to testing a
    primitives hit() method the hit() method of the bounding box is called. If
    the bounding box is not hit, then the expensive primitive hit() method is
    avoided.

    Combined with a spatial subdivision acceleration structure, the cost of ray-
    primitive evaluations can be heavily reduced (O(n) -> O(log n)).

    For optimal speed the bounding box is aligned with the world space axes. As
    rays are propagated in world space, co-ordinate transforms can be avoided.

    :param Point3D lower: (optional) starting point for lower box corner
    :param Point3D upper: (optional) starting point for upper box corner
    """

    def __init__(self, lower: Point3D | None = None, upper: Point3D | None = None) -> None: ...
    def __repr__(self) -> str: ...
    @property
    def lower(self) -> Point3D:
        """
        The point defining the lower corner of the bounding box.

        :rtype: Point3D
        """
    @lower.setter
    def lower(self, value: Point3D) -> None: ...
    @property
    def upper(self) -> Point3D:
        """
        The point defining the upper corner of the bounding box.

        :rtype: Point3D
        """
    @upper.setter
    def upper(self, value: Point3D) -> None: ...
    @property
    def centre(self) -> Point3D:
        """
        The point defining the geometric centre of the bounding box.

        :rtype: Point3D
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
        Returns true if the given 3D point lies inside the bounding box.

        :param Point3D point: A given test point.
        :rtype: boolean
        """
    def union(self, box: BoundingBox3D) -> None:
        """
        Union this bounding box instance with the input bounding box.

        The resulting bounding box will be larger so as to just enclose both bounding boxes. This class instance
        will be edited in place to have the new bounding box dimensions.

        :param BoundingBox3D box: A bounding box instance to union with this bounding box instance.
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
        Returns the surface area of the bounding box.

        :rtype: float
        """
    def volume(self) -> float:
        """
        Returns the volume of the bounding box.

        :rtype: float
        """
    def vertices(self) -> list[Point3D]:
        """
        Get the list of vertices for this bounding box.

        :return: A list of Point3D's representing the corners of the bounding box.
        :rtype: list
        """
    def extent(self, axis: int) -> float:
        """
        Returns the spatial extend of this bounding box along the given dimension.

        :param int axis: specifies the axis to return, {0: X axis, 1: Y axis, 2: Z axis}.
        :rtype: float
        """
    def largest_axis(self) -> int:
        """
        Find the largest axis of this bounding box.

        :return: an int specifying the longest axis, {0: X axis, 1: Y axis, 2: Z axis}.
        :rtype: int
        """
    def largest_extent(self) -> float:
        """
        Find the largest spatial extent across all axes.

        :return: distance along the largest bounding box axis.
        :rtype: float
        """
    def pad(self, padding: float) -> None:
        """
        Makes the bounding box larger by the specified amount of padding.

        Every bounding box axis will end up larger by a factor of 2 x padding.

        :param float padding: distance to use as padding margin
        """
    def pad_axis(self, axis: int, padding: float) -> None:
        """
        Makes the bounding box larger along the specified axis by amount of padding.

        The specified bounding box axis will end up larger by a factor of 2 x padding.

        :param int axis: The axis to apply padding to {0: X axis, 1: Y axis, 2: Z axis}.
        :param float padding: Distance to use as padding margin.
        """
    def enclosing_sphere(self) -> BoundingSphere3D:
        """
        Returns a BoundingSphere3D guaranteed to enclose the bounding box.

        The sphere is centred at the box centre. A small degree of padding is
        added to avoid numerical accuracy issues.

        :return: A BoundingSphere3D object.
        :rtype: BoundingSphere3D
        """
