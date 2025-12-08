from ..core import BoundingBox3D, ChangeSignal, Intersection, Material, Primitive, Ray
from ..core.math import AffineMatrix3D, Point3D
from ..core.scenegraph import Node
from ..core.scenegraph._nodebase import _NodeBase

class CSGPrimitive(Primitive):
    """
    Constructive Solid Geometry (CSG) Primitive base class.

    This is an abstract base class and can not be used directly.

    CSG is a modeling technique that uses Boolean operations like union
    and intersection to combine 3D solids. For example, the volumes of a
    sphere and box could be unified with the 'union' operation to create a
    primitive with the combined volume of the underlying primitives.

    :param Primitive primitive_a: Component primitive A of the compound primitive.
    :param Primitive primitive_b: Component primitive B of the compound primitive.
    :param Node parent: Scene-graph parent node or None (default = None).
    :param AffineMatrix3D transform: An AffineMatrix3D defining the local co-ordinate
      system relative to the scene-graph parent (default = identity matrix).
    :param Material material: A Material object defining the CSG primitive's
      material (default = None).
    """
    def __init__(
        self,
        primitive_a: Primitive | None = None,
        primitive_b: Primitive | None = None,
        parent: _NodeBase | None = None,
        transform: AffineMatrix3D | None = None,
        material: Material | None = None,
        name: str | None = None,
    ) -> None: ...
    @property
    def primitive_a(self) -> Primitive:
        """
        Component primitive A of the compound CSG primitive.

        :rtype: Primitive
        """
    @primitive_a.setter
    def primitive_a(self, value: Primitive) -> None: ...
    @property
    def primitive_b(self) -> Primitive:
        """
        Component primitive B of the compound CSG primitive.

        :rtype: Primitive
        """
    @primitive_b.setter
    def primitive_b(self, value: Primitive) -> None: ...
    def hit(self, ray: Ray) -> Intersection: ...
    def next_intersection(self) -> Intersection: ...

class NullPrimitive(Primitive):
    """
    Dummy primitive class.

    The _CSGPrimitive base class requires a primitive that returns a valid bounding box.
    This class overrides the bounding_box method to return an empty bounding box.
    This class is intended to act as a place holder until a user sets a valid primitive.
    """
    def bounding_box(self) -> BoundingBox3D: ...

class CSGRoot(Node):
    """
    Specialised scenegraph root node for CSG primitives.

    The root node responds to geometry change notifications and propagates them
    to the CSG primitive and its enclosing scenegraph.
    """
    def __init__(self, csg_primitive: CSGPrimitive) -> None: ...
    def _change(self, node: _NodeBase, signal: ChangeSignal) -> None:
        """
        Handles a scenegraph node change handler.

        Propagates geometry change notifications to the enclosing CSG primitive and its
        scenegraph.
        """

class Union(CSGPrimitive):
    """
    CSGPrimitive that is the volumetric union of primitives A and B.

    All of the original volume from A and B will be in the new primitive.

    :param Primitive primitive_a: Component primitive A of the union operation.
    :param Primitive primitive_b: Component primitive B of the union operation.
    :param Node parent: Scene-graph parent node or None (default = None).
    :param AffineMatrix3D transform: An AffineMatrix3D defining the local co-ordinate
      system relative to the scene-graph parent (default = identity matrix).
    :param Material material: A Material object defining the new CSG primitive's
      material (default = None).

    Some example code for creating the union between two cylinders.

    .. code-block:: python

        from raysect.core import rotate, translate
        from raysect.primitive import Cylinder, Union
        from raysect.optical import World
        from raysect.optical.material import AbsorbingSurface

        world = World()

        cyl_x = Cylinder(1, 4.2, transform=rotate(90, 0, 0)*translate(0, 0, -2.1))
        cyl_y = Cylinder(1, 4.2, transform=rotate(0, 90, 0)*translate(0, 0, -2.1))

        csg_union = Union(cyl_x, cyl_y, world, material=AbsorbingSurface(),
                          transform=translate(-2.1, 2.1, 2.5)*rotate(30, -20, 0))

    """

    def contains(self, point: Point3D) -> bool: ...
    def bounding_box(self) -> BoundingBox3D: ...
    def instance(
        self,
        parent: _NodeBase | None = None,
        transform: AffineMatrix3D | None = None,
        material: Material | None = None,
        name: str | None = None,
    ) -> Union: ...

class Intersect(CSGPrimitive):
    """
    CSGPrimitive that is the volumetric intersection of primitives A and B.

    Only volumes that are present in both primitives will be present in the new
    CSG primitive.

    :param Primitive primitive_a: Component primitive A of the intersection operation.
    :param Primitive primitive_b: Component primitive B of the intersection operation.
    :param Node parent: Scene-graph parent node or None (default = None).
    :param AffineMatrix3D transform: An AffineMatrix3D defining the local co-ordinate
      system relative to the scene-graph parent (default = identity matrix).
    :param Material material: A Material object defining the new CSG primitive's
      material (default = None).

    Some example code for creating the intersection between two cylinders.

    .. code-block:: python

        from raysect.core import rotate, translate
        from raysect.primitive import Cylinder, Sphere, Intersect
        from raysect.optical import World
        from raysect.optical.material import AbsorbingSurface

        world = World()

        cyl_x = Cylinder(1, 4.2, transform=rotate(90, 0, 0)*translate(0, 0, -2.1))
        sphere = Sphere(1.5)

        csg_intersection = Intersect(cyl_x, sphere, world, material=AbsorbingSurface(),
                                     transform=translate(-2.1, 2.1, 2.5)*rotate(30, -20, 0))

    """

    def contains(self, point: Point3D) -> bool: ...
    def bounding_box(self) -> BoundingBox3D: ...
    def instance(
        self,
        parent: _NodeBase | None = None,
        transform: AffineMatrix3D | None = None,
        material: Material | None = None,
        name: str | None = None,
    ) -> Intersect: ...

class Subtract(CSGPrimitive):
    """
    CSGPrimitive that is the remaining volume of primitive A minus volume B.

    Only volumes that are unique to primitive A and don't overlap with primitive
    B will be in the new CSG primitive.

    :param Primitive primitive_a: Component primitive A of the subtract operation.
    :param Primitive primitive_b: Component primitive B of the subtract operation.
    :param Node parent: Scene-graph parent node or None (default = None).
    :param AffineMatrix3D transform: An AffineMatrix3D defining the local co-ordinate
      system relative to the scene-graph parent (default = identity matrix).
    :param Material material: A Material object defining the new CSG primitive's
      material (default = None).

    .. code-block:: python

        from raysect.core import rotate, translate, Point3D
        from raysect.primitive import Box, Sphere, Subtract
        from raysect.optical import World
        from raysect.optical.material import AbsorbingSurface

        world = World()

        cube = Box(Point3D(-1.5, -1.5, -1.5), Point3D(1.5, 1.5, 1.5))
        sphere = Sphere(1.75)

        csg_subtraction = Subtract(cube, sphere, world, material=AbsorbingSurface(),
                                   transform=translate(-2.1, 2.1, 2.5)*rotate(30, -20, 0))

    """

    def contains(self, point: Point3D) -> bool: ...
    def bounding_box(self) -> BoundingBox3D: ...
    def instance(
        self,
        parent: _NodeBase | None = None,
        transform: AffineMatrix3D | None = None,
        material: Material | None = None,
        name: str | None = None,
    ) -> Subtract: ...
