from ....core.intersection import Intersection
from ....core.math import AffineMatrix3D, Normal3D, Point3D
from ....core.scenegraph import Primitive
from ...ray import Ray
from ...scenegraph import World
from ...spectrum import Spectrum
from ..material import Material

class VolumeTransform(Material):
    """
    Translate/rotate the volume material relative to the primitive.

    Applies an affine transform to the start and end points of the volume
    response calculation. This modifier is intended for use with volume
    texture materials, allowing them to be translated/rotated.

    As a modifier material, it takes another material (the base material) as an
    argument. Using a supplied an affine transform, this material will modify
    the start and end coordinate of the volume integration.

    :param material: The base material.
    :param transform: An affine transform.
    """

    def __init__(self, material: Material, transform: AffineMatrix3D) -> None: ...
    @property
    def material(self) -> Material: ...
    @material.setter
    def material(self, value: Material) -> None: ...
    @property
    def transform(self) -> AffineMatrix3D: ...
    @transform.setter
    def transform(self, value: AffineMatrix3D) -> None: ...
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
