from ..core import AffineMatrix3D, BoundingBox3D, Intersection, Material, Point3D, Primitive, Ray

class Box(Primitive):
    """
    A box primitive.

    The box is defined by lower and upper points in the local co-ordinate
    system.

    :param Point3D lower: Lower point of the box (default = Point3D(-0.5, -0.5, -0.5)).
    :param Point3D upper: Upper point of the box (default = Point3D(0.5, 0.5, 0.5)).
    :param Node parent: Scene-graph parent node or None (default = None).
    :param AffineMatrix3D transform: An AffineMatrix3D defining the local co-ordinate system relative to the scene-graph parent (default = identity matrix).
    :param Material material: A Material object defining the box\'s material (default = None).
    :param str name: A string specifying a user-friendly name for the box (default = "").

    .. code-block:: pycon

        >>> from raysect.core import Point3D, translate
        >>> from raysect.primitive import Box
        >>> from raysect.optical import World
        >>> from raysect.optical.material import UniformSurfaceEmitter
        >>> from raysect.optical.library.spectra.colours import red
        >>>
        >>> world = World()
        >>>
        >>> cube = Box(Point3D(0,0,0), Point3D(1,1,1), parent=world, transform=translate(0, 1, 0),
                       material=UniformSurfaceEmitter(red), name="red cube")
    """
    def __init__(
        self,
        lower: Point3D | None = None,
        upper: Point3D | None = None,
        parent: object | None = None,
        transform: AffineMatrix3D | None = None,
        material: Material | None = None,
        name: str | None = None,
    ) -> None: ...
    @property
    def lower(self) -> Point3D:
        """
        Lower 3D coordinate of the box in primitive's local coordinates.

        :rtype: Point3D
        """
    @property
    def upper(self) -> Point3D:
        """
        Upper 3D coordinate of the box in primitive's local coordinates.

        :rtype: Point3D
        """
    def hit(self, ray: Ray) -> Intersection: ...
    def next_intersection(self) -> Intersection: ...
    def contains(self, point: Point3D) -> bool: ...
    def bounding_box(self) -> BoundingBox3D: ...
    def instance(self, parent: object | None = None, transform: AffineMatrix3D | None = None, material: Material | None = None, name: str | None = None) -> Box: ...
