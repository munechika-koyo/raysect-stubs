from ....core.intersection import Intersection
from ....core.math import AffineMatrix3D, Normal3D, Point3D
from ....core.scenegraph import Primitive
from ...ray import Ray
from ...scenegraph import World
from ...spectrum import Spectrum
from ..material import Material

class Add(Material):
    """
    Adds the response of two materials.

    This modifier is used to sum together the behaviours of two different
    materials. The surface response is the simple sum of the two surface
    material responses. The volume response is more nuanced. The volume method
    of material 1 is applied first, followed by the volume method of material
    2. Depending on the choice of volume material, this may result in a simple
    summation or a more complex interaction.

    The Add modifier should be used with caution, it is possible to produce
    unphysical material combinations that violate energy conservation. It is
    the responsibility of the user to ensure the material combination is
    physically valid.

    By default both the volume and surface responses are combined. This may be
    configured with the surface_only and volume_only parameters. If summation
    is disabled the response from material 1 is returned.

    Add can be used to introduce a surface emission component to a non-emitting
    surface. For example, A hot metal surface can be approximated by adding a
    black body emitter to a metal material:

        material = Add(
            Iron(),
            UniformSurfaceEmitter(BlackBody(800)),
            surface_only=True
        )

    Combining volumes is more complex and must only be used with materials that
    are mathematically commutative, for example two volume emitters or two
    absorbing volumes.

    :param m1: The first material.
    :param m2: The second material.
    :param surface_only: Only blend the surface response (default=False).
    :param volume_only: Only blend the volume response (default=False).
    """

    def __init__(
        self,
        m1: Material,
        m2: Material,
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
