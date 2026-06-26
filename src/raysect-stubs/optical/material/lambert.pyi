from ...core.intersection import Intersection
from ...core.math import AffineMatrix3D, Point3D, Vector3D
from ...core.scenegraph import Primitive
from ..ray import Ray
from ..scenegraph import World
from ..spectralfunction import SpectralFunction
from ..spectrum import Spectrum
from .material import ContinuousBSDF

class Lambert(ContinuousBSDF):
    """
    An ideal Lambertian surface material.

    A Lambertian is a perfectly diffuse surface that scatters light equally in
    all directions. It is a good approximation to many real world surfaces.

    :param SpectralFunction reflectivity: Reflectance function which defines the
      fraction of light scattered at each wavelength.

    .. code-block:: pycon

        >>> from raysect.primitive import Sphere
        >>> from raysect.optical import World, ConstantSF
        >>> from raysect.optical.material import Lambert
        >>>
        >>> # set-up scenegraph
        >>> world = World()
        >>> sphere = Sphere(radius=0.01, parent=world)
        >>> sphere.material=Lambert(0.25)  # 25% diffuse reflectivity
    """

    def __init__(self, reflectivity: SpectralFunction | None = None) -> None: ...
    def pdf(self, s_incoming: Vector3D, s_outgoing: Vector3D, back_face: bool) -> float: ...
    def sample(self, s_incoming: Vector3D, back_face: bool) -> Vector3D: ...
    def evaluate_shading(
        self,
        world: World,
        ray: Ray,
        s_incoming: Vector3D,
        s_outgoing: Vector3D,
        w_reflection_origin: Point3D,
        w_transmission_origin: Point3D,
        back_face: bool,
        world_to_surface: AffineMatrix3D,
        surface_to_world: AffineMatrix3D,
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
