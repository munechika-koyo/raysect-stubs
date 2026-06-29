from ...core.intersection import Intersection
from ...core.math import AffineMatrix3D, Normal3D, Point3D, Vector3D
from ...core.scenegraph import Primitive
from ..ray import Ray
from ..scenegraph import World
from ..spectralfunction import SpectralFunction
from ..spectrum import Spectrum
from .material import Material, NullVolume

class Light(NullVolume):
    """
    A Lambertian surface material illuminated by a distant light source.

    This debug material lights the primitive from the world direction specified
    by a vector passed to the light_direction parameter. An optional intensity
    and emission spectrum may be supplied. By default the light spectrum is the
    D65 white point spectrum.

    :param Vector3D light_direction: A world space Vector3D defining the light direction.
    :param float intensity: The light intensity in units of radiance (default is 1.0).
    :param SpectralFunction spectrum: A SpectralFunction defining the light's
      emission spectrum (default is D65 white).
    """

    def __init__(
        self,
        light_direction: Vector3D,
        intensity: float = 1.0,
        spectrum: SpectralFunction | None = None,
    ) -> None: ...
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

class PerfectReflectingSurface(Material):
    """
    A material that is perfectly reflecting.
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
