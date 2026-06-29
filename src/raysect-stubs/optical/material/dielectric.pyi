from ...core.intersection import Intersection
from ...core.math import AffineMatrix3D, Normal3D, Point3D
from ...core.scenegraph import Primitive
from ..ray import Ray
from ..scenegraph import World
from ..spectralfunction import NumericallyIntegratedSF, SpectralFunction
from ..spectrum import Spectrum
from .material import Material

class Sellmeier(NumericallyIntegratedSF):
    """
    Material with refractive index defined by `Sellmeier equation <https://en.wikipedia.org/wiki/Sellmeier_equation>`_

    :param float b1: Sellmeier :math:`B_1` coefficient.
    :param float b2: Sellmeier :math:`B_2` coefficient.
    :param float b3: Sellmeier :math:`B_3` coefficient.
    :param float c1: Sellmeier :math:`C_1` coefficient.
    :param float c2: Sellmeier :math:`C_2` coefficient.
    :param float c3: Sellmeier :math:`C_3` coefficient.
    :param float sample_resolution: The numerical sampling resolution in nanometers.

    .. code-block:: pycon

        >>> from raysect.optical import ConstantSF
        >>> from raysect.optical.material import Dielectric, Sellmeier
        >>>
        >>> diamond_material = Dielectric(Sellmeier(0.3306, 4.3356, 0.0, 0.1750**2, 0.1060**2, 0.0),
                                          ConstantSF(1))
    """

    def __init__(
        self,
        b1: float,
        b2: float,
        b3: float,
        c1: float,
        c2: float,
        c3: float,
        sample_resolution: float = 10,
    ) -> None: ...
    def function(self, wavelength: float) -> float:
        """
        Returns a sample of the three term Sellmeier equation at the specified
        wavelength.

        :param float wavelength: Wavelength in nm.
        :return: Refractive index sample.
        :rtype: float
        """

class Dielectric(Material):
    """
    An ideal dielectric material.

    :param SpectralFunction index: Refractive index as a function of wavelength.
    :param SpectralFunction transmission: Transmission per metre as a function of wavelength.
    :param SpectralFunction external_index: Refractive index of the external material at the interface,
      defaults to a vacuum (n=1).
    :param bool transmission_only: toggles transmission only, no reflection (default=False).

    .. code-block:: pycon

        >>> from raysect.optical import ConstantSF
        >>> from raysect.optical.material import Dielectric, Sellmeier
        >>>
        >>> diamond_material = Dielectric(Sellmeier(0.3306, 4.3356, 0.0, 0.1750**2, 0.1060**2, 0.0),
                                          ConstantSF(1))
    """

    index: SpectralFunction
    external_index: SpectralFunction
    transmission: SpectralFunction
    transmission_only: bool

    def __init__(
        self,
        index: SpectralFunction,
        transmission: SpectralFunction,
        external_index: SpectralFunction | None = None,
        transmission_only: bool = False,
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
