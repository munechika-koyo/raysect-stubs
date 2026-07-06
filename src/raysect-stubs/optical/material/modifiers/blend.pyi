from ....core.intersection import Intersection
from ....core.math import AffineMatrix3D, Normal3D, Point3D
from ....core.scenegraph import Primitive
from ...ray import Ray
from ...scenegraph import World
from ...spectrum import Spectrum
from ..material import Material

class Blend(Material):
    """
    Blend combines the behaviours of two materials.

    This modifier is used to blend together the behaviours of two different
    materials. Which material handles the interaction for an incoming ray is
    determined by a random choice, weighted by the ratio argument. Low values
    of ratio bias the selection towards material 1, high values to material 2.

    It is the responsibility of the user to ensure the material combination is
    physically valid.

    By default both the volume and surface responses are blended. This may be
    configured with the surface_only and volume_only parameters. If blending
    is disabled the response from material 1 is returned.

    Blend can be used to approximate finely sputtered surfaces consisting of a
    mix of materials. For example it can be used to crudely approximate a gold
    coated glass surface:

        material = Blend(schott('N-BK7'), Gold(), 0.1, surface_only=True)

    :param m1: The first material.
    :param m2: The second material.
    :param ratio: A double value in the range (0, 1).
    :param surface_only: Only blend the surface response (default=False).
    :param volume_only: Only blend the volume response (default=False).
    """

    def __init__(
        self,
        m1: Material,
        m2: Material,
        ratio: float,
        surface_only: bool = False,
        volume_only: bool = False,
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
