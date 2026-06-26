from ....core import Intersection, Primitive
from ....core.math import AffineMatrix3D, Normal3D, Point3D, Vector3D
from ... import Ray, Spectrum, World
from ..material import NullVolume
from .homogeneous import HomogeneousVolumeEmitter

class UnitySurfaceEmitter(NullVolume):
    """
    Uniform and isotropic surface emitter with emission 1W/str/m^2/ x nm,
    where x is the spectrum's wavelength interval.

    This material is useful for general purpose debugging and testing energy
    conservation.

        >>> from raysect.primitive import Sphere
        >>> from raysect.optical import World
        >>> from raysect.optical.material import UnitySurfaceEmitter
        >>>
        >>> # set-up scenegraph
        >>> world = World()
        >>> emitter = Sphere(radius=0.01, parent=world, material=UnitySurfaceEmitter())
    """

    def __init__(self) -> None: ...
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

class UnityVolumeEmitter(HomogeneousVolumeEmitter):
    """
    Uniform, isotropic volume emitter with emission 1W/str/m^3/ x nm,
    where x is the spectrum's wavelength interval.

    This material is useful for general purpose debugging and evaluating the coupling
    coefficients between cameras and emitting volumes.

        >>> from raysect.primitive import Sphere
        >>> from raysect.optical import World
        >>> from raysect.optical.material import UnityVolumeEmitter
        >>>
        >>> # set-up scenegraph
        >>> world = World()
        >>> emitter = Sphere(radius=0.01, parent=world, material=UnityVolumeEmitter())
    """

    def __init__(self) -> None: ...
    def emission_function(
        self,
        direction: Vector3D,
        spectrum: Spectrum,
        world: World,
        ray: Ray,
        primitive: Primitive,
        world_to_primitive: AffineMatrix3D,
        primitive_to_world: AffineMatrix3D,
    ) -> Spectrum: ...
