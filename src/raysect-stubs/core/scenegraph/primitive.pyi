from abc import abstractmethod

from ..boundingbox import BoundingBox3D
from ..boundingsphere import BoundingSphere3D
from ..intersection import Intersection
from ..material import Material
from ..math import AffineMatrix3D, Point3D
from ..ray import Ray
from .node import Node

class Primitive(Node):
    """
    A scene-graph object representing a ray-intersectable surface/volume.

    A primitive class defines an open surface or closed surface (volume) that can be intersected by a ray. For example,
    this could be a geometric primitive such as a sphere, or more complicated surface such as a polyhedral mesh. The
    primitive class is the only class in the scene-graph with which a ray can interact.

    This is a base class, its functionality must be implemented fully by the deriving class.

    :param Node parent: Assigns the Node's parent to the specified scene-graph object.
    :param AffineMatrix3D transform: Sets the affine transform associated with the Node.
    :param Material material: An object representing the material properties of the primitive.
    :param str name: A string defining the node name.
    """

    def __init__(self, parent: Node | None = None, transform: AffineMatrix3D | None = None, material: Material | None = None, name: str | None = None) -> None: ...
    @property
    def material(self) -> Material:
        """
        The material assigned to this primitive.

        :rtype: Material
        """
    @material.setter
    def material(self, value: Material) -> None: ...
    @abstractmethod
    def hit(self, ray: Ray) -> Intersection:
        """
        Virtual method - to be implemented by derived classes.

        Calculates the closest intersection of the Ray with the Primitive
        surface, if such an intersection exists.

        If a hit occurs an Intersection object must be returned, otherwise None
        is returned. The intersection object holds the details of the
        intersection including the point of intersection, surface normal and
        the objects involved in the intersection.

        :param Ray ray: The ray to test for intersection.
        :return: An Intersection object or None if no intersection occurs.
        :rtype: Intersection
        """
    @abstractmethod
    def next_intersection(self) -> Intersection:
        """
        Virtual method - to be implemented by derived classes.

        Returns the next intersection of the ray with the primitive along the
        ray path.

        This method may only be called following a call to hit(). If the ray
        has further intersections with the primitive, these may be obtained by
        repeatedly calling the next_intersection() method. Each call to
        next_intersection() will return the next ray-primitive intersection
        along the ray's path. If no further intersections are found or
        intersections lie outside the ray parameters then next_intersection()
        will return None.

        If any geometric elements of the primitive, ray and/or scene-graph are
        altered between a call to hit() and calls to next_intersection() the
        data returned by next_intersection() may be invalid. Primitives may
        cache data to accelerate next_intersection() calls which will be
        invalidated by geometric alterations to the scene. If the scene is
        altered the data returned by next_intersection() is undefined.

        :rtype: Intersection
        """
    @abstractmethod
    def contains(self, point: Point3D) -> bool:
        """
        Virtual method - to be implemented by derived classes.

        Must returns True if the Point3D lies within the boundary of the surface
        defined by the Primitive. False is returned otherwise.

        :param Point3D p: The Point3D to test.
        :return: True if the Point3D is enclosed by the primitive surface, False otherwise.
        :rtype: bool
        """
    @abstractmethod
    def bounding_box(self) -> BoundingBox3D:
        """
        Virtual method - to be implemented by derived classes.

        When the primitive is connected to a scene-graph containing a World
        object at its root, this method should return a bounding box that
        fully encloses the primitive's surface (plus a small margin to
        avoid numerical accuracy problems). The bounding box must be defined in
        the world's coordinate space.

        If this method is called when the primitive is not connected to a
        scene-graph with a World object at its root, it must throw a TypeError
        exception.

        :return: A world space BoundingBox3D object.
        :rtype: BoundingBox3D
        """
    def bounding_sphere(self) -> BoundingSphere3D:
        """
        When the primitive is connected to a scene-graph containing a World
        object at its root, this method should return a bounding sphere that
        fully encloses the primitive's surface (plus a small margin to
        avoid numerical accuracy problems). The bounding sphere must be
        defined in the world's coordinate space.

        If this method is called when the primitive is not connected to a
        scene-graph with a World object at its root, it must throw a TypeError
        exception.

        The default implementation is to wrap the the primitive's bounding box
        with a sphere. If the bounding sphere can be more optimally calculated
        for the primitive, it should override this method.

        :return: A world space BoundingSphere3D object.
        :rtype: BoundingSphere3D
        """
    @abstractmethod
    def instance(self, parent: Node | None = None, transform: AffineMatrix3D | None = None, material: Material | None = None, name: str | None = None) -> Primitive:
        """
        Returns a new instance of the primitive with the same geometry.

        :param Node parent: Assigns the Node's parent to the specified scene-graph object.
        :param AffineMatrix3D transform: Sets the affine transform associated with the Node.
        :param Material material: An object representing the material properties of the primitive.
        :param str name: A string defining the node name.
        :return:
        """
    def notify_geometry_change(self) -> None:
        """
        Notifies the scene-graph root of a change to the primitive's geometry.

        This method must be called by primitives when their geometry changes.
        The notification informs the root node that any caching structures used
        to accelerate ray-tracing calculations are now potentially invalid and
        must be recalculated, taking the new geometry into account.
        """
    def notify_material_change(self) -> None:
        """
        Notifies the scene-graph root of a change to the primitive's material.

        This method must be called by primitives when their material changes.
        The notification informs the root node that any caching structures used
        to accelerate ray-tracing calculations are now potentially invalid and
        must be recalculated, taking the new material into account.
        """
