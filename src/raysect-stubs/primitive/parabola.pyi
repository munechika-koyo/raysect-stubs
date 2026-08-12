from ..core.boundingbox import BoundingBox3D
from ..core.intersection import Intersection
from ..core.material import Material
from ..core.math import AffineMatrix3D, Point3D
from ..core.ray import Ray
from ..core.scenegraph import Primitive
from ..core.scenegraph._nodebase import _NodeBase

class Parabola(Primitive):
    """
    A parabola primitive.

    The parabola is defined by a radius and height. It lies along the z-axis
    and extends over the z range [0, height]. The base of the parabola is
    capped with a disk forming a closed surface. The base of the parabola lies
    on the x-y plane, the parabola vertex (tip) lies at z=height.

    :param float radius: Radius of the parabola in meters (default = 0.5).
    :param float height: Height of the parabola in meters (default = 1.0).
    :param Node parent: Scene-graph parent node or None (default = None).
    :param AffineMatrix3D transform: An AffineMatrix3D defining the local co-ordinate system relative to the scene-graph parent (default = identity matrix).
    :param Material material: A Material object defining the parabola\'s material (default = None).
    :param str name: A string specifying a user-friendly name for the parabola (default = "").

    .. code-block:: pycon

        >>> from raysect.core import translate
        >>> from raysect.primitive import Parabola
        >>> from raysect.optical import World
        >>> from raysect.optical.material import UniformSurfaceEmitter
        >>> from raysect.optical.library.spectra.colours import yellow
        >>>
        >>> world = World()
        >>>
        >>> parabola = Parabola(0.5, 2.0, parent=world, transform=translate(0, 0, 1),
                                material=UniformSurfaceEmitter(yellow), name="yellow parabola")
    """

    def __init__(
        self,
        radius: float = 0.5,
        height: float = 1.0,
        parent: _NodeBase | None = None,
        transform: AffineMatrix3D | None = None,
        material: Material | None = None,
        name: str | None = None,
    ) -> None: ...
    @property
    def radius(self) -> float:
        """
        Radius of the parabola base in x-y plane.
        """
    @radius.setter
    def radius(self, value: float) -> None: ...
    @property
    def height(self) -> float:
        """
        The parabola's extent along the z-axis [0, height].
        """
    @height.setter
    def height(self, value: float) -> None: ...
    def hit(self, ray: Ray) -> Intersection | None: ...
    def next_intersection(self) -> Intersection | None: ...
    def contains(self, point: Point3D) -> bool: ...  # pyrefly: ignore [bad-override-param-name]
    def bounding_box(self) -> BoundingBox3D: ...
    def instance(
        self,
        parent: _NodeBase | None = None,
        transform: AffineMatrix3D | None = None,
        material: Material | None = None,
        name: str | None = None,
    ) -> Parabola: ...
