from ....core import Intersection, Primitive
from ....core.math import AffineMatrix3D, Normal3D, Point3D
from ... import Ray, Spectrum, World
from ..material import NullVolume

class AnisotropicSurfaceEmitter(NullVolume):
    """
    Base class for anisotropic surface emitters.

    Simplifies the development of anisotropic light sources. The emitter
    spectrum can be varied based on the angle between the normal and
    incident observation direction, and the side of the surface.
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
    def emission_function(self, spectrum: Spectrum, cosine: float, back_face: bool) -> Spectrum:
        """
        Returns the emission along the observation direction.

        This is a virtual method and must be implemented by sub-classing. The emission is modulated
        by the angle between the observation direction and the surface normal. To this end, the
        cosine of the angle between the normal and observation directions is supplied. This value
        is always in the range [0, 1], no matter which side the ray intersects.

        If the emission must vary according to the side of the surface the ray intersects, this may
        be determined by inspecting the back_face argument. This will be True if the inside (or back)
        surface is struck by the ray, otherwise it is False.

        :param Spectrum spectrum: The Spectrum object in which to place the observed emission.
        :param float cosine: The cosine of the angle between the normal and the observation
        direction.
        :param bool back_face: True if the back face of the surface (inside), False otherwise.
        :return: The spectrum object.
        """
