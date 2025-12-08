from abc import abstractmethod
from typing import Literal, overload

from ..vector import Vector3D

class SolidAngleSampler:
    """
    Base class for an object that generates samples over a solid angle.
    """
    @overload
    def __call__(self, samples: None = None, pdf: Literal[False] = False) -> Vector3D: ...
    @overload
    def __call__(self, samples: int, pdf: Literal[False] = False) -> list[Vector3D]: ...
    @overload
    def __call__(self, samples: None = None, pdf: Literal[True] = True) -> tuple[Vector3D, float]: ...
    @overload
    def __call__(self, samples: int, pdf: Literal[True] = True) -> list[tuple[Vector3D, float]]: ...
    def __call__(self, samples: int | None = None, pdf: bool = False) -> Vector3D | tuple[Vector3D, float] | list[Vector3D] | list[tuple[Vector3D, float]]:
        """
        If samples is not provided, returns a single Vector3D sample from
        the distribution. If samples is set to a value then a number of
        samples equal to the value specified is returned in a list.

        If pdf is set to True the Vector3D sample is returned inside a tuple
        with its associated pdf value as the second element.

        :param int samples: Number of points to generate (default=None).
        :param bool pdf: Toggle for returning associated sample pdfs (default=False).
        :return: A Vector3D, tuple or list of Vector3D objects.
        """
    @abstractmethod
    def pdf(self, sample: Vector3D) -> float:
        """
        Generates a pdf for a given sample value.

        Vectors *must* be normalised.

        :param Vector3D sample: The sample point at which to get the pdf.
        :rtype: float
        """

class SphereSampler(SolidAngleSampler):
    """
    Generates a random vector on a unit sphere.

        >>> from raysect.core.math import SphereSampler
        >>>
        >>> sphere_sampler = SphereSampler()
        >>> sphere_sampler(2)
        [Vector3D(-0.03659868898144491, 0.24230159277890417, 0.9695104301149347),
         Vector3D(-0.6983609515217772, -0.6547708308112921, -0.28907981684698814)]
    """
    def pdf(self, sample: Vector3D) -> float: ...

class HemisphereUniformSampler(SolidAngleSampler):
    """
    Generates a random vector on a unit hemisphere.

    The hemisphere is aligned along the z-axis - the plane that forms the
    hemisphere base lies in the x-y plane.

        >>> from raysect.core.math import HemisphereUniformSampler
        >>>
        >>> sampler = HemisphereUniformSampler()
        >>> sampler(2)
        [Vector3D(-0.5555921819133177, -0.41159192618517343, 0.7224329821485018),
         Vector3D(0.03447410534618117, 0.33544044138689, 0.9414304256517041)]
    """
    def pdf(self, sample: Vector3D) -> float: ...

class HemisphereCosineSampler(SolidAngleSampler):
    """
    Generates a cosine-weighted random vector on a unit hemisphere.

    The hemisphere is aligned along the z-axis - the plane that forms the
    hemisphere base lies in the x-y plane.

        >>> from raysect.core.math import HemisphereCosineSampler
        >>>
        >>> sampler = HemisphereCosineSampler()
        >>> sampler(2)
        [Vector3D(0.18950017731212562, 0.4920026797683874, 0.8497193924463526),
         Vector3D(0.21900782218503353, 0.918767789013818, 0.32848336897387853)]
    """
    def pdf(self, sample: Vector3D) -> float: ...

class ConeUniformSampler(SolidAngleSampler):
    """
    Generates a uniform weighted random vector from a cone.

    The cone is aligned along the z-axis.

    :param angle: Angle of the cone in degrees (default=45).

    .. code-block:: pycon

        >>> from raysect.core.math import ConeUniformSampler
        >>> sampler = ConeUniformSampler(5)
        >>> sampler(2)
        [Vector3D(-0.032984782761108486, 0.02339453130328099, 0.9991820154562943),
         Vector3D(0.0246657314750599, 0.08269560820438482, 0.9962695609494988)]
    """

    angle: float
    _angle_radians: float
    _angle_cosine: float
    _solid_angle: float
    _solid_angle_inv: float

    def __init__(self, angle: float = 45) -> None: ...
    def pdf(self, sample: Vector3D) -> float: ...
