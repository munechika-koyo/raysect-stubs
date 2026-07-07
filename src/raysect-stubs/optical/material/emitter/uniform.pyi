from ....core import Intersection, Primitive
from ....core.math import AffineMatrix3D, Normal3D, Point3D, Vector3D
from ... import Ray, Spectrum, World
from ...spectrum import SpectralFunction
from ..material import NullVolume
from .homogeneous import HomogeneousVolumeEmitter

class UniformSurfaceEmitter(NullVolume):
    """
    Uniform and isotropic surface emitter.

    Uniform emission will be given by the emission_spectrum multiplied by the
    emission scale.

    :param SpectralFunction emission_spectrum: The surface's emission function.
    :param float scale: Scale of the emission function (default = 1 W/m^2/str/nm).

    .. code-block:: pycon

        >>> from raysect.primitive import Sphere
        >>> from raysect.optical import World, ConstantSF
        >>> from raysect.optical.material import UniformSurfaceEmitter
        >>>
        >>> # set-up scenegraph
        >>> world = World()
        >>> emitter = Sphere(radius=0.01, parent=world)
        >>> emitter.material=UniformSurfaceEmitter(ConstantSF(1.0))
    """

    emission_spectrum: SpectralFunction
    scale: float

    def __init__(self, emission_spectrum: SpectralFunction, scale: float = 1.0) -> None: ...
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
    def evaluate_volume(
        self,
        spectrum: Spectrum,
        world: World,
        ray: Ray,
        primitive: Primitive,
        start_point: Point3D,
        end_point: Point3D,
        world_to_primitive: AffineMatrix3D,
        primitive_to_world: AffineMatrix3D,
    ) -> Spectrum: ...

class UniformVolumeEmitter(HomogeneousVolumeEmitter):
    """
    Uniform, homogeneous and isotropic volume emitter.

    Uniform emission will be given by the emission_spectrum multiplied by the
    emission scale in radiance.

    :param SpectralFunction emission_spectrum: The volume's emission function.
    :param float scale: Scale of the emission function (default = 1 W/m^3/str/nm).

    .. code-block:: pycon

        >>> from raysect.primitive import Sphere
        >>> from raysect.optical import World, ConstantSF
        >>> from raysect.optical.material import UniformVolumeEmitter
        >>>
        >>> # set-up scenegraph
        >>> world = World()
        >>> emitter = Sphere(radius=0.01, parent=world)
        >>> emitter.material=UniformVolumeEmitter(ConstantSF(1.0))
    """

    emission_spectrum: SpectralFunction
    scale: float

    def __init__(self, emission_spectrum: SpectralFunction, scale: float = 1.0) -> None: ...
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
