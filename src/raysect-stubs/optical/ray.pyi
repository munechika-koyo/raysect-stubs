from ..core.constants import FORWARD, ORIGIN
from ..core.math import Point3D, Vector3D
from ..core.ray import Ray as CoreRay
from .scenegraph import World
from .spectrum import Spectrum

class Ray(CoreRay):
    """
    Optical Ray class for optical applications, inherits from core Ray class.

    Provides the trace(world) method.

    :param Point3D origin: Point defining ray’s origin (default=Point3D(0, 0, 0))
    :param Vector3D direction: Vector defining ray’s direction (default=Vector3D(0, 0, 1))
    :param float min_wavelength: Lower wavelength bound for observed spectrum
    :param float max_wavelength: Upper wavelength bound for observed spectrum
    :param int bins: Number of samples to use over the spectral range
    :param float max_distance: The terminating distance of the ray
    :param float extinction_prob: Probability of path extinction at every
      material surface interaction (default=0.1)
    :param int extinction_min_depth: Minimum number of paths before triggering
      extinction probability (default=3)
    :param int max_depth: Maximum number of material interactions before
      terminating ray trajectory.
    :param bool importance_sampling: Toggles use of importance sampling for
      important primitives. See help documentation on importance sampling,
      (default=True).
    :param float important_path_weight: Weight to use for important paths when
      using importance sampling.

    .. code-block:: pycon

        >>> from raysect.core import Point3D, Vector3D
        >>> from raysect.optical import World, Ray
        >>>
        >>> world = World()
        >>>
        >>> ray = Ray(origin=Point3D(0, 0, -5),
        >>>           direction=Vector3D(0, 0, 1),
        >>>           min_wavelength=375,
        >>>           max_wavelength=785,
        >>>           bins=100)
        >>>
        >>> spectrum = ray.trace(world)
        >>> spectrum
        <raysect.optical.spectrum.Spectrum at 0x7f5b08b6e048>
    """

    depth: int
    importance_sampling: bool
    ray_count: int

    def __init__(
        self,
        origin: Point3D = ORIGIN,
        direction: Vector3D = FORWARD,
        min_wavelength: float = 375,
        max_wavelength: float = 785,
        bins: int = 40,
        max_distance: float = float("inf"),
        extinction_prob: float = 0.1,
        extinction_min_depth: int = 3,
        max_depth: int = 100,
        importance_sampling: bool = True,
        important_path_weight: float = 0.25,
    ) -> None: ...
    @property
    def bins(self) -> int:
        """
        Number of spectral bins across wavelength range.

        :rtype: int
        """
    @bins.setter
    def bins(self, value: int) -> None: ...
    @property
    def min_wavelength(self) -> float:
        """
        Lower bound on wavelength range.

        :rtype: float
        """
    @min_wavelength.setter
    def min_wavelength(self, value: float) -> None: ...
    @property
    def max_wavelength(self) -> float:
        """
        Upper bound on wavelength range.

        :rtype: float
        """
    @max_wavelength.setter
    def max_wavelength(self, value: float) -> None: ...
    @property
    def wavelength_range(self) -> tuple[float, float]:
        """
        Upper and lower wavelength range.

        :rtype: tuple
        """
    @wavelength_range.setter
    def wavelength_range(self, value: tuple[float, float]) -> None: ...
    @property
    def extinction_prob(self) -> float:
        """
        Probability of path extinction at every material surface interaction.

        :rtype: float
        """
    @extinction_prob.setter
    def extinction_prob(self, value: float) -> None: ...
    @property
    def extinction_min_depth(self) -> int:
        """
        Minimum number of paths before triggering extinction probability.

        :rtype: int
        """
    @extinction_min_depth.setter
    def extinction_min_depth(self, value: int) -> None: ...
    @property
    def max_depth(self) -> int:
        """
        Maximum number of material interactions before terminating ray trajectory.

        :rtype: int
        """
    @max_depth.setter
    def max_depth(self, value: int) -> None: ...
    @property
    def important_path_weight(self) -> float:
        """
        Weight to use for important paths when using importance sampling.

        :rtype: float
        """
    @important_path_weight.setter
    def important_path_weight(self, value: float) -> None: ...
    def new_spectrum(self) -> Spectrum:
        """
        Returns a new Spectrum compatible with the ray spectral settings.

        :rtype: Spectrum

        .. code-block:: pycon

            >>> from raysect.core import Point3D, Vector3D
            >>> from raysect.optical import Ray
            >>>
            >>> ray = Ray(origin=Point3D(0, 0, -5),
            >>>           direction=Vector3D(0, 0, 1),
            >>>           min_wavelength=375,
            >>>           max_wavelength=785,
            >>>           bins=100)
            >>>
            >>> ray.new_spectrum()
            <raysect.optical.spectrum.Spectrum at 0x7f5b08b6e1b0>
        """

    def trace(self, world: World, keep_alive: bool = False) -> Spectrum:
        """
        Traces a single ray path through the world.

        :param World world: World object defining the scene.
        :param bool keep_alive: If true, disables Russian roulette termination of the ray.
        :return: The resulting Spectrum object collected by the ray.
        :rtype: Spectrum

        .. code-block:: pycon

            >>> from raysect.core import Point3D, Vector3D
            >>> from raysect.optical import World, Ray
            >>>
            >>> world = World()
            >>>
            >>> ray = Ray(origin=Point3D(0, 0, -5),
            >>>           direction=Vector3D(0, 0, 1),
            >>>           min_wavelength=375,
            >>>           max_wavelength=785,
            >>>           bins=100)
            >>>
            >>> spectrum = ray.trace(world)
            >>> spectrum
            <raysect.optical.spectrum.Spectrum at 0x7f5b08b6e048>
        """

    def sample(self, world: World, count: int) -> Spectrum:
        """
        Samples the radiance directed along the ray direction.

        This methods calls trace repeatedly to obtain a statistical sample of
        the radiance directed along the ray direction from the world. The count
        parameter specifies the number of samples to obtain. The mean spectrum
        accumulated from these samples is returned.

        :param World world: World object defining the scene.
        :param int count: Number of samples to take.
        :return: The accumulated spectrum collected by the ray.
        :rtype: Spectrum

        .. code-block:: pycon

            >>> from raysect.core import Point3D, Vector3D
            >>> from raysect.optical import World, Ray
            >>>
            >>> world = World()
            >>>
            >>> ray = Ray(origin=Point3D(0, 0, -5),
            >>>           direction=Vector3D(0, 0, 1),
            >>>           min_wavelength=375,
            >>>           max_wavelength=785,
            >>>           bins=100)
            >>>
            >>> ray.sample(world, 10)
            <raysect.optical.spectrum.Spectrum at 0x7f5b08b6e318>
        """
    def spawn_daughter(self, origin: Point3D, direction: Vector3D) -> Ray:
        """
        Spawns a new daughter of the ray.

        A daughter ray has the same spectral configuration as the source ray,
        however the ray depth is increased by 1.

        :param Point3D origin: A Point3D defining the ray origin.
        :param Vector3D direction: A vector defining the ray direction.
        :return: A daughter Ray object.
        :rtype: Ray
        """

    def copy(self, origin: Point3D | None = None, direction: Vector3D | None = None) -> Ray:
        """
        Obtain a new Ray object with the same configuration settings.

        :param Point3D origin: New Ray's origin position.
        :param Vector3D direction: New Ray's direction.
        :rtype: Ray

        .. code-block:: pycon

            >>> from raysect.core import Point3D, Vector3D
            >>> from raysect.optical import Ray
            >>>
            >>> ray = Ray(origin=Point3D(0, 0, -5),
            >>>           direction=Vector3D(0, 0, 1),
            >>>           min_wavelength=375,
            >>>           max_wavelength=785,
            >>>           bins=100)
            >>>
            >>> ray.copy()
            Ray(Point3D(0.0, 0.0, -5.0), Vector3D(0.0, 0.0, 1.0), inf)
        """
