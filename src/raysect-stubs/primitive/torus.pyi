from ..core.boundingbox import BoundingBox3D
from ..core.boundingsphere import BoundingSphere3D
from ..core.intersection import Intersection
from ..core.material import Material
from ..core.math import AffineMatrix3D, Point3D
from ..core.ray import Ray
from ..core.scenegraph import Primitive
from ..core.scenegraph._nodebase import _NodeBase

class Torus(Primitive):
    """
    A torus primitive.

    The torus is defined by major and minor radius.
    The major radius is the distance from the center of the tube to the center of the torus.
    The minor radius is the radius of the tube.
    The center of the torus corresponds to the origin of the local coordinate system.
    The axis of revolution coincides with the z-axis, and The center of the torus tube lies
    on the x-y plane.

    :param float major_radius: Major radius of the torus in meters (default = 1.0).
    :param float minor_radius: Minor radius of the torus in meters (default = 0.5).
    :param Node parent: Scene-graph parent node or None (default = None).
    :param AffineMatrix3D transform: An AffineMatrix3D defining the local coordinate system relative to the scene-graph parent (default = identity matrix).
    :param Material material: A Material object defining the torus\'s material (default = None).
    :param str name: A string specifying a user-friendly name for the torus (default = "").

    :ivar float major_radius: The major radius of the torus in meters.
    :ivar float minor_radius: The minor radius of the torus in meters.

    .. code-block:: pycon

        >>> from raysect.core import translate
        >>> from raysect.primitive import Torus
        >>> from raysect.optical import World
        >>> from raysect.optical.material import UniformSurfaceEmitter
        >>> from raysect.optical.library.spectra.colours import orange
        >>>
        >>> world = World()
        >>>
        >>> torus = Torus(1.0, 0.5, parent=world, transform=translate(3, 0, 0),
                          material=UniformSurfaceEmitter(orange), name="orange torus")
    """

    def __init__(
        self,
        major_radius: float = 1.0,
        minor_radius: float = 0.5,
        parent: _NodeBase | None = None,
        transform: AffineMatrix3D | None = None,
        material: Material | None = None,
        name: str | None = None,
    ) -> None: ...
    @property
    def major_radius(self) -> float:
        """
        The major radius of this torus.

        :rtype: float
        """
    @major_radius.setter
    def major_radius(self, value: float) -> None: ...
    @property
    def minor_radius(self) -> float:
        """
        The minor radius of this torus.

        :rtype: float
        """
    @minor_radius.setter
    def minor_radius(self, value: float) -> None: ...
    def hit(self, ray: Ray) -> Intersection | None: ...
    def next_intersection(self) -> Intersection | None: ...
    def contains(self, point: Point3D) -> bool: ...  # pyrefly: ignore [bad-override-param-name]
    def bounding_box(self) -> BoundingBox3D: ...
    def bounding_sphere(self) -> BoundingSphere3D: ...
    def instance(
        self,
        parent: _NodeBase | None = None,
        transform: AffineMatrix3D | None = None,
        material: Material | None = None,
        name: str | None = None,
    ) -> Torus: ...
