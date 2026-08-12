from ..core.boundingbox import BoundingBox3D
from ..core.boundingsphere import BoundingSphere3D
from ..core.intersection import Intersection
from ..core.material import Material
from ..core.math import AffineMatrix3D, Point3D
from ..core.ray import Ray
from ..core.scenegraph import Primitive
from ..core.scenegraph._nodebase import _NodeBase

class Sphere(Primitive):
    """
    A sphere primitive.

    The sphere is centered at the origin of the local co-ordinate system.

    :param float radius: Radius of the sphere in meters (default = 0.5).
    :param Node parent: Scene-graph parent node or None (default = None).
    :param AffineMatrix3D transform: An AffineMatrix3D defining the local co-ordinate system relative to the scene-graph parent (default = identity matrix).
    :param Material material: A Material object defining the sphere\'s material (default = None).
    :param str name: A string specifying a user-friendly name for the sphere (default = "").

    :ivar float radius: The radius of the sphere in meters.

    .. code-block:: pycon

        >>> from raysect.core import translate
        >>> from raysect.primitive import Sphere
        >>> from raysect.optical import World
        >>> from raysect.optical.material import UniformSurfaceEmitter
        >>> from raysect.optical.library.spectra.colours import orange
        >>>
        >>> world = World()
        >>>
        >>> sphere = Sphere(2.5, parent=world, transform=translate(3, 0, 0),
                            material=UniformSurfaceEmitter(orange), name="orange sphere")
    """

    def __init__(
        self,
        radius: float = 0.5,
        parent: _NodeBase | None = None,
        transform: AffineMatrix3D | None = None,
        material: Material | None = None,
        name: str | None = None,
    ) -> None: ...
    @property
    def radius(self) -> float:
        """
        The radius of this sphere.

        :rtype: float
        """
    @radius.setter
    def radius(self, value: float) -> None: ...
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
    ) -> Sphere: ...
