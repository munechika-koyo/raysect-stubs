from ..core.boundingbox import BoundingBox3D
from ..core.intersection import Intersection
from ..core.material import Material
from ..core.math import AffineMatrix3D, Point3D
from ..core.ray import Ray
from ..core.scenegraph import Primitive
from ..core.scenegraph._nodebase import _NodeBase

class Cylinder(Primitive):
    """
    A cylinder primitive.

    The cylinder is defined by a radius and height. It lies along the z-axis
    and extends over the z range [0, height]. The ends of the cylinder are
    capped with disks forming a closed surface.

    :param float radius: Radius of the cylinder in meters (default = 0.5).
    :param float height: Height of the cylinder in meters (default = 1.0).
    :param Node parent: Scene-graph parent node or None (default = None).
    :param AffineMatrix3D transform: An AffineMatrix3D defining the local co-ordinate
      system relative to the scene-graph parent (default = identity matrix).
    :param Material material: A Material object defining the cylinder\'s material (default = None).
    :param str name: A string specifying a user-friendly name for the cylinder (default = "").

    .. code-block:: pycon

        >>> from raysect.core import translate
        >>> from raysect.primitive import Cylinder
        >>> from raysect.optical import World
        >>> from raysect.optical.material import UniformSurfaceEmitter
        >>> from raysect.optical.library.spectra.colours import blue
        >>>
        >>> world = World()
        >>>
        >>> cylinder = Cylinder(0.5, 2.0, parent=world, transform=translate(0, 0, 1),
                                material=UniformSurfaceEmitter(blue), name="blue cylinder")
    """

    height: float
    radius: float
    def __init__(
        self,
        radius: float = 0.5,
        height: float = 1.0,
        parent: _NodeBase | None = None,
        transform: AffineMatrix3D | None = None,
        material: Material | None = None,
        name: str | None = None,
        **kwargs,
    ) -> None: ...
    @property
    def radius(self) -> float:
        """
        Radius of the cylinder in x-y plane.
        """
    @radius.setter
    def radius(self, value: float) -> None: ...
    @property
    def height(self) -> float:
        """
        Extent of the cylinder along the z-axis.
        """
    @height.setter
    def height(self, value: float) -> None: ...
    def hit(self, ray: Ray) -> Intersection | None: ...
    def next_intersection(self) -> Intersection | None: ...
    def contains(self, point: Point3D) -> bool: ...
    def bounding_box(self) -> BoundingBox3D: ...
    def instance(
        self,
        parent: _NodeBase | None = None,
        transform: AffineMatrix3D | None = None,
        material: Material | None = None,
        name: str | None = None,
    ) -> Cylinder: ...
