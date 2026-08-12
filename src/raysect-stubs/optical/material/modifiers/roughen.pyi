from ....core.intersection import Intersection
from ....core.math import AffineMatrix3D, Normal3D, Point3D
from ....core.scenegraph import Primitive
from ...ray import Ray
from ...scenegraph import World
from ...spectrum import Spectrum
from ..material import Material

class Roughen(Material):
    """
    Modifies the surface normal to approximate a rough surface.

    This is a modifier material, it takes another material (the base material)
    as an argument.

    The roughen modifier works by randomly deflecting the surface normal about
    its true position before passing the intersection parameters on to the base
    material.

    The deflection is calculated by interpolating between the existing normal
    and a vector sampled from a cosine weighted hemisphere. The strength of the
    interpolation, and hence the roughness of the surface, is controlled by the
    roughness argument. The roughness argument takes a value in the range
    [0, 1] where 1 is a fully rough, lambert-like surface and 0 is a smooth,
    untainted surface.

    :param material: The base material.
    :param roughness: A double value in the range [0, 1].
    """

    def __init__(self, material: Material, roughness: float) -> None: ...
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
    def evaluate_volume(  # pyrefly: ignore [bad-override-param-name]
        self,
        spectrum: Spectrum,
        world: World,
        ray: Ray,
        primitive: Primitive,
        start_point: Point3D,
        end_point: Point3D,
        to_local: AffineMatrix3D,
        to_world: AffineMatrix3D,
    ) -> Spectrum: ...
