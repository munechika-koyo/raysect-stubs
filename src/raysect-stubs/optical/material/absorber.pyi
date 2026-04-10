from ...core.intersection import Intersection
from ...core.math import AffineMatrix3D, Normal3D, Point3D
from ...core.scenegraph import Primitive
from ..ray import Ray
from ..scenegraph import World
from ..spectrum import Spectrum
from .material import NullVolume

class AbsorbingSurface(NullVolume):
    """
    A perfectly absorbing surface material.

        >>> from raysect.primitive import Sphere
        >>> from raysect.optical import World
        >>> from raysect.optical.material import AbsorbingSurface
        >>>
        >>> # set-up scenegraph
        >>> world = World()
        >>> absorber = Sphere(radius=0.01, parent=world, material=AbsorbingSurface())
    """

    def evaluate_surface(
        self,
        world: World,
        ray: Ray,
        primitive: Primitive,
        hit_point: Point3D,
        exiting: bool,
        inside_point: Point3D,
        outside_point: Point3D,
        normal: Normal3D,
        world_to_primitive: AffineMatrix3D,
        primitive_to_world: AffineMatrix3D,
        intersection: Intersection,
    ) -> Spectrum: ...
