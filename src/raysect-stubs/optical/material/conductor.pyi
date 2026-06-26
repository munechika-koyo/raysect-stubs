from ...core.intersection import Intersection
from ...core.math import AffineMatrix3D, Normal3D, Point3D, Vector3D
from ...core.scenegraph import Primitive
from ..ray import Ray
from ..scenegraph import World
from ..spectralfunction import SpectralFunction
from ..spectrum import Spectrum
from .material import ContinuousBSDF, Material

class Conductor(Material):
    """
    Conductor material.

    The conductor material simulates the interaction of light with a
    homogeneous conducting material, such as, gold, silver or aluminium.

    This material implements the Fresnel equations for a conducting surface. To
    use the material, the complex refractive index of the conductor must be
    supplied.

    :param SpectralFunction index: Real component of the refractive
      index - :math:`n(\\lambda)`.
    :param SpectralFunction extinction: Imaginary component of the
      refractive index (extinction) - :math:`k(\\lambda)`.

    .. code-block:: pycon

        >>> import numpy as np
        >>> from raysect.optical import InterpolatedSF
        >>> from raysect.optical.material import Conductor
        >>>
        >>> wavelength = np.array(...)
        >>> index = InterpolatedSF(wavelength, np.array(...))
        >>> extinction = InterpolatedSF(wavelength, np.array(...))
        >>>
        >>> metal = Conductor(index, extinction)
    """

    index: SpectralFunction
    extinction: SpectralFunction

    def __init__(self, index: SpectralFunction, extinction: SpectralFunction) -> None: ...
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

class RoughConductor(ContinuousBSDF):
    """
    This is implementing Cook-Torrence with conducting fresnel microfacets.

    Smith shadowing and GGX facet distribution used to model roughness.

    :param SpectralFunction index: Real component of the refractive
      index - :math:`n(\\lambda)`.
    :param SpectralFunction extinction: Imaginary component of the
      refractive index (extinction) - :math:`k(\\lambda)`.
    :param float roughness: The roughness parameter in range (0, 1]. 0 is
      perfectly specular, 1 is perfectly rough.

    .. code-block:: pycon

        >>> import numpy as np
        >>> from raysect.optical import InterpolatedSF
        >>> from raysect.optical.material import RoughConductor
        >>>
        >>> wavelength = np.array(...)
        >>> index = InterpolatedSF(wavelength, np.array(...))
        >>> extinction = InterpolatedSF(wavelength, np.array(...))
        >>>
        >>> rough_metal = RoughConductor(index, extinction, 0.25)
    """

    index: SpectralFunction
    extinction: SpectralFunction

    def __init__(self, index: SpectralFunction, extinction: SpectralFunction, roughness: float) -> None: ...
    @property
    def roughness(self) -> float: ...
    @roughness.setter
    def roughness(self, value: float) -> None: ...
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
