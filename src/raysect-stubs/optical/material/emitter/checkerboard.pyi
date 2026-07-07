from ....core import Intersection, Primitive
from ....core.math import AffineMatrix3D, Normal3D, Point3D
from ... import Ray, Spectrum, World
from ...colour import d65_white
from ...spectralfunction import SpectralFunction
from ..material import NullVolume

class Checkerboard(NullVolume):
    """
    Isotropic checkerboard surface emitter

    Defines a plane of alternating squares of emission forming a checkerboard
    pattern. Useful in debugging and as a light source in test scenes.

    :param float width: The width of the squares in metres.
    :param SpectralFunction emission_spectrum1: Emission spectrum for square one.
    :param SpectralFunction emission_spectrum2: Emission spectrum for square two.
    :param float scale1: Intensity of square one emission.
    :param float scale2: Intensity of square two emission.

    .. code-block:: pycon

        >>> from raysect.primitive import Box
        >>> from raysect.optical import World, rotate, Point3D, d65_white
        >>> from raysect.optical.material import Checkerboard
        >>>
        >>> world = World()
        >>>
        >>> # checker board wall that acts as emitter
        >>> emitter = Box(lower=Point3D(-10, -10, 10), upper=Point3D(10, 10, 10.1), parent=world,
                          transform=rotate(45, 0, 0))
        >>> emitter.material=Checkerboard(4, d65_white, d65_white, 0.1, 2.0)
    """

    emission_spectrum1: SpectralFunction
    emission_spectrum2: SpectralFunction
    scale1: float
    scale2: float

    def __init__(
        self,
        width: float = 1.0,
        emission_spectrum1: SpectralFunction = d65_white,
        emission_spectrum2: SpectralFunction = d65_white,
        scale1: float = 0.25,
        scale2: float = 0.5,
    ) -> None: ...
    @property
    def width(self) -> float:
        """
        The width of the squares in metres.

        :rtype: float
        """
    @width.setter
    def width(self, value: float) -> None: ...
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
