from numpy import uint64

from ....core.math import AffineMatrix3D
from ....core.scenegraph import Observer
from ....core.scenegraph._nodebase import _NodeBase
from ....core.workflow import MulticoreEngine, RenderEngine
from ... import Ray
from .pipeline import Pipeline0D, Pipeline1D, Pipeline2D
from .processor import PixelProcessor
from .sampler import FrameSampler1D, FrameSampler2D
from .slice import SpectralSlice

DEFAULT_ENGINE = MulticoreEngine()

class _ObserverBase(Observer):
    """
    Observer base class.

    This is an abstract class and cannot be used for observing.

    :param Node parent: The parent node in the scenegraph. Observers will only observe items
      in the same scenegraph as them.
    :param AffineMatrix3D transform: Affine matrix describing the location and orientation of
      this observer in the world.
    :param str name: User friendly name for this observer.
    :param object render_engine: A workflow manager for controlling whether tasks will be
      executed in serial, parallel or on a cluster (default=MulticoreEngine()).
    :param int spectral_rays: The number of smaller sub-spectrum rays the full spectrum will
      be divided into (default=1).
    :param int spectral_bins: The number of spectral samples over the wavelength range (default=15).
    :param float min_wavelength: Lower wavelength bound for sampled spectral range (default=375nm).
    :param float max_wavelength: Upper wavelength bound for sampled spectral range (default=740nm).
    :param float ray_extinction_prob: Probability of ray extinction after every material
      intersection (default=0.01).
    :param int ray_extinction_min_depth: Minimum number of paths before russian roulette style
      ray extinction (default=3).
    :param int ray_max_depth: Maximum number of Ray paths before terminating Ray (default=500).
    :param bool ray_importance_sampling: Toggle importance sampling behaviour (default=True).
    :param float ray_important_path_weight: Relative weight of important path sampling
      (default=0.2).
    :param bool quiet: When True, suppresses the printing of observer performance statistics and completion
      (default=False).
    """

    render_engine: RenderEngine
    ray_importance_sampling: bool
    render_complete: bool
    quiet: bool

    def __init__(
        self,
        parent: _NodeBase | None = None,
        transform: AffineMatrix3D | None = None,
        name: str | None = None,
        render_engine: RenderEngine = DEFAULT_ENGINE,
        spectral_rays: int = 1,
        spectral_bins: int = 15,
        min_wavelength: float = 375.0,
        max_wavelength: float = 740.0,
        ray_extinction_prob: float = 0.01,
        ray_extinction_min_depth: int = 3,
        ray_max_depth: int = 500,
        ray_importance_sampling: bool = True,
        ray_important_path_weight: float = 0.2,
        quiet: bool = False,
    ): ...
    @property
    def spectral_bins(self) -> int:
        """
        The number of spectral samples over the wavelength range.

        :rtype: int
        """
    @spectral_bins.setter
    def spectral_bins(self, value: int) -> None: ...
    @property
    def spectral_rays(self) -> int:
        """
        The number of smaller sub-spectrum rays the full spectrum will be divided into.

        This setting is important for scenes with dispersive elements such as glass prisms. This
        setting allows the parent spectrum to be divided into N smaller sub-regions that will be
        individually sampled. This allows rays with different active wavelength ranges to take
        different paths when passing through materials wit different refractive indexes.

        Note that the number of spectral rays cannot be greater than the number of spectral
        bins.

        :rtype: int
        """
    @spectral_rays.setter
    def spectral_rays(self, value: int) -> None: ...
    @property
    def min_wavelength(self) -> float:
        """
        Lower wavelength bound for sampled spectral range.

        :rtype: float
        """
    @min_wavelength.setter
    def min_wavelength(self, value: float) -> None: ...
    @property
    def max_wavelength(self) -> float:
        """
        Upper wavelength bound for sampled spectral range.

        :rtype: float
        """
    @max_wavelength.setter
    def max_wavelength(self, value: float) -> None: ...
    @property
    def ray_extinction_prob(self) -> float:
        """
        Probability of ray extinction after every material intersection.

        :rtype: float
        """
    @ray_extinction_prob.setter
    def ray_extinction_prob(self, value: float) -> None: ...
    @property
    def ray_extinction_min_depth(self) -> int:
        """
        Minimum number of paths before russian roulette style ray extinction.

        :rtype: int
        """
    @ray_extinction_min_depth.setter
    def ray_extinction_min_depth(self, value: int) -> None: ...
    @property
    def ray_max_depth(self) -> int:
        """
        Maximum number of Ray paths before terminating Ray.

        :rtype: int
        """
    @ray_max_depth.setter
    def ray_max_depth(self, value: int) -> None: ...
    @property
    def ray_important_path_weight(self) -> float:
        """
        Relative weight of important path sampling.

        :rtype: float
        """
    @ray_important_path_weight.setter
    def ray_important_path_weight(self, value: float) -> None: ...
    def observe(self) -> None:
        """Ask this Camera to Observe its world."""

    def _slice_spectrum(self) -> list[SpectralSlice]:
        """
        Sub-divides the spectral range into smaller wavelength slices.

        In dispersive rendering, where multiple rays are launched across the full spectral range, each ray samples a small
        portion of the spectrum. A slice defines a sub region of the spectral range that is sampled
        by launching a ray.

        :return: A list of SpectralSlice objects.
        """
    def _generate_templates(self, slices: list[SpectralSlice]) -> list[Ray]: ...
    def _render_pixel(self, task: tuple, slice_id: int, template: Ray) -> tuple[tuple, list[tuple], int]:
        """
        - passed in are ray_template and pipeline object references
        - unpack task ID (pixel id)
        - launch the rays and sample pixel using pixel_sampler() and ray_template,
        returns a frame 1D object representing a spectrum with variance and sample count
        for each bin.
        - passes frame 1D to each pipeline object for pixel processing. Each of those
        returns a custom tuple of data tied to details of that pipeline.
        - All results packaged together with pixel ID and returned to consumer.
        :return:
        """
    def _update_state(self, packed_result: tuple[tuple, list[tuple], int], slice_id: int) -> None:
        """
        - unpack task configuration and pipeline result tuples.
        - pass results to each pipeline to update pipelines internal state
        - print workflow statistics and any statistics for each pipeline.
        - display visual imagery for each pipeline as required
        - save state for each pipeline as required.

        :return:
        """
    def _generate_tasks(self) -> list[tuple]: ...
    def _obtain_pixel_processors(self, task: tuple, slice_id: int) -> list: ...
    def _initialise_pipelines(self, min_wavelength: float, max_wavelength: float, spectral_bins: int, slices: list[SpectralSlice], quiet: bool) -> None: ...
    def _update_pipelines(self, task: tuple, results: list, slice_id: int) -> None: ...
    def _finalise_pipelines(self) -> None: ...
    def _initialise_statistics(self, tasks: list[tuple]) -> None:
        """
        Initialise statistics.
        """
    def _update_statistics(self, sample_ray_count: uint64) -> None:
        """
        Display progress statistics.
        """

    def _finalise_statistics(self) -> None:
        """
        Final statistics output.
        """
    def _obtain_rays(self, task: tuple, template: Ray) -> list[tuple[Ray, float]]:
        """
        Returns a list of Rays that sample over the sensitivity of the pixel.

        This is a virtual method to be implemented by derived classes.

        Runs during the observe() loop to generate the rays. Allows observers
        to customise how they launch rays.

        This method must return a list of tuples, with each tuple containing
        a Ray object and a corresponding weighting, typically the projected
        area/direction cosine.

        If the projected area weight is not required (due to the ray sampling
        algorithm taking the weighting into account in the distribution e.g.
        cosine weighted) then the weight should be set to 1.0.

        :param tuple task: The render task configuration.
        :param Ray template: The template ray from which all rays should be generated.
        :return list: A list of tuples of (ray, weight)
        """
    def _obtain_sensitivity(self, task: tuple) -> float:
        """

        :param pixel_id:
        :return:
        """

class Observer0D(_ObserverBase):
    """
    0D observer base class.

    This is an abstract class and cannot be used for observing.

    :param list pipelines: A list of pipelines that will process the resulting spectra
      from this observer.
    :param int pixel_samples: Number of samples to generate per pixel with one call to
      observe() (default=1000).
    :param int samples_per_task: Minimum number of samples to request per task (default=250).
    :param kwargs: **kwargs from _ObserverBase.

    .. automethod:: raysect.optical.observer.base.observer.Observer0D._generate_rays
    """

    def __init__(
        self,
        pipelines: list[Pipeline0D],
        pixel_samples: int = 1000,
        samples_per_task: int = 250,
        **kwargs,
    ) -> None: ...
    @property
    def pixel_samples(self) -> int:
        """
        The number of samples to take per pixel.

        :rtype: int
        """
    @pixel_samples.setter
    def pixel_samples(self, value: int) -> None: ...
    @property
    def samples_per_task(self) -> int:
        """
        Minimum number of samples to request per task.

        For efficiency reasons this should not be set below 100 samples.

        :rtype: int
        """
    @samples_per_task.setter
    def samples_per_task(self, value: int) -> None: ...
    @property
    def pipelines(self) -> list[Pipeline0D]:
        """
        A list of pipelines to process the output spectra of these observations.

        :rtype: list
        """
    @pipelines.setter
    def pipelines(self, value: list[Pipeline0D]) -> None: ...
    def _generate_tasks(self) -> list[tuple[int, None]]: ...
    def _obtain_pixel_processors(self, task: tuple[int, None], slice_id: int) -> list[PixelProcessor]: ...
    def _initialise_pipelines(self, min_wavelength: float, max_wavelength: float, spectral_bins: int, slices: list[SpectralSlice], quiet: bool) -> None: ...
    def _update_pipelines(self, task: tuple[int, None], results: list, slice_id: int) -> None: ...
    def _finalise_pipelines(self) -> None: ...
    def _obtain_rays(self, task: tuple[int, None], template: Ray) -> list[tuple[Ray, float]]: ...
    def _obtain_sensitivity(self, task: tuple[int, None]) -> float: ...
    def _generate_rays(self, template: Ray, ray_count: int) -> list[tuple[Ray, float]]:
        """
        Generate a list of Rays that sample over the sensitivity of the pixel.

        This is a virtual method to be implemented by derived classes.

        Runs during the observe() loop to generate the rays. Allows observers
        to customise how they launch rays.

        This method must return a list of tuples, with each tuple containing
        a Ray object and a corresponding weighting, typically the projected
        area/direction cosine. In general the weight will be:

        .. math::
           W = \\frac{1}{2\\pi} * \\frac{1}{A} * \\frac{1}{pdf_A} * \\frac{1}{pdf_\\Omega} * cos(\\theta)

        If the projected area weight is not required (due to the ray sampling
        algorithm taking the weighting into account in the distribution e.g.
        cosine weighted) then the weight should be set to 1.0.

        The number of rays returned must be equal to
        ray_count otherwise pipeline statistics will be incorrectly calculated.

        :param Ray template: The template ray from which all rays should be generated.
        :param int ray_count: The number of rays to be generated.
        :return list: A list of tuples of (ray, weight)
        """
    def _pixel_sensitivity(self) -> float:
        """

        :return:
        """

class Observer1D(_ObserverBase):
    """
    1D observer base class.

    This is an abstract class and cannot be used for observing.

    :param int pixels: The number of pixels for this observer, i.e. 512.
    :param FrameSampler1D frame_sampler: A frame sampler class.
    :param list pipelines: A list of pipelines that will process the resulting spectra
      from this observer.
    :param int pixel_samples: Number of samples to generate per pixel with one call to
      observe() (default=1000).
    :param kwargs: **kwargs from _ObserverBase.
    """

    def __init__(
        self,
        pixels: int,
        frame_sampler: FrameSampler1D,
        pipelines: list[Pipeline1D],
        pixel_samples: int = 1000,
        **kwargs,
    ) -> None: ...
    @property
    def pixel_samples(self) -> int:
        """
        The number of samples to take per pixel.

        :rtype: int
        """
    @pixel_samples.setter
    def pixel_samples(self, value: int) -> None: ...
    @property
    def pixels(self) -> int:
        """
        The number of pixels for this observer, i.e. 512.

        :rtype: int
        """
    @pixels.setter
    def pixels(self, value: int) -> None: ...
    @property
    def frame_sampler(self) -> FrameSampler1D:
        """
        The FrameSampler1D class for this observer.

        :rtype: FrameSampler1D
        """
    @frame_sampler.setter
    def frame_sampler(self, value: FrameSampler1D) -> None: ...
    @property
    def pipelines(self) -> list[Pipeline1D]:
        """
        A list of pipelines to process the output spectra of these observations.

        :rtype: list
        """
    @pipelines.setter
    def pipelines(self, value: list[Pipeline1D]) -> None: ...
    def _generate_tasks(self) -> list[tuple[int]]: ...
    def _obtain_pixel_processors(self, task: tuple[int], slice_id: int) -> list[PixelProcessor]: ...
    def _initialise_pipelines(self, min_wavelength: float, max_wavelength: float, spectral_bins: int, slices: list[SpectralSlice], quiet: bool) -> None: ...
    def _update_pipelines(self, task: tuple[int], results: list, slice_id: int) -> None: ...
    def _finalise_pipelines(self) -> None: ...
    def _obtain_rays(self, task: tuple[int], template: Ray) -> list[tuple[Ray, float]]: ...
    def _obtain_sensitivity(self, task: tuple[int]) -> float: ...
    def _generate_rays(self, pixel: int, template: Ray, ray_count: int) -> list[tuple[Ray, float]]:
        """
        Generate a list of Rays that sample over the sensitivity of the pixel.

        This is a virtual method to be implemented by derived classes.

        Runs during the observe() loop to generate the rays. Allows observers
        to customise how they launch rays.

        This method must return a list of tuples, with each tuple containing
        a Ray object and a corresponding weighting, typically the projected
        area/direction cosine. In general the weight will be:

        .. math::
           W = \\frac{1}{2\\pi} * \\frac{1}{A} * \\frac{1}{pdf_A} * \\frac{1}{pdf_\\Omega} * cos(\\theta)

        If the projected area weight is not required (due to the ray sampling
        algorithm taking the weighting into account in the distribution e.g.
        cosine weighted) then the weight should be set to 1.0.

        The number of rays returned must be equal to ray_count otherwise pipeline
        statistics will be incorrectly calculated.

        :param int pixel: Pixel index.
        :param Ray template: The template ray from which all rays should be generated.
        :param int ray_count: The number of rays to be generated.
        :return list: A list of tuples of (ray, weight)
        """
    def _pixel_sensitivity(self, pixel: int) -> float:
        """

        :param int pixel: Pixel index.
        :return:
        """

class Observer2D(_ObserverBase):
    """
    2D observer base class.

    This is an abstract class and cannot be used for observing.

    :param tuple pixels: A tuple of pixel dimensions for this observer, i.e. (512, 512).
    :param FrameSampler2D frame_sampler: A frame sampler class.
    :param list pipelines: A list of pipelines that will process the resulting spectra
      from this observer.
    :param int pixel_samples: Number of samples to generate per pixel with one call to
      observe() (default=100).
    :param kwargs: **kwargs from _ObserverBase.
    """

    def __init__(
        self,
        pixels: tuple[int, int],
        frame_sampler: FrameSampler2D,
        pipelines: list[Pipeline2D],
        pixel_samples: int = 100,
        **kwargs,
    ) -> None: ...
    @property
    def pixel_samples(self) -> int:
        """
        The number of samples to take per pixel.

        :rtype: int
        """
    @pixel_samples.setter
    def pixel_samples(self, value: int) -> None: ...
    @property
    def pixels(self) -> tuple[int, int]:
        """
        Tuple describing the pixel dimensions for this observer (nx, ny), i.e. (512, 512).

        :rtype: tuple
        """
    @pixels.setter
    def pixels(self, value: tuple[int, int]) -> None: ...
    @property
    def frame_sampler(self) -> FrameSampler2D:
        """
        The FrameSampler2D class for this observer.

        :rtype: FrameSampler2D
        """
    @frame_sampler.setter
    def frame_sampler(self, value: FrameSampler2D) -> None: ...
    @property
    def pipelines(self) -> list[Pipeline2D]:
        """
        A list of pipelines to process the output spectra of these observations.

        :rtype: list
        """
    @pipelines.setter
    def pipelines(self, value: list[Pipeline2D]) -> None: ...
    def _generate_tasks(self) -> list[tuple[int, int]]: ...
    def _obtain_pixel_processors(self, task: tuple[int, int], slice_id: int) -> list[PixelProcessor]: ...
    def _initialise_pipelines(self, min_wavelength: float, max_wavelength: float, spectral_bins: int, slices: list[SpectralSlice], quiet: bool) -> None: ...
    def _update_pipelines(self, task: tuple[int, int], results: list, slice_id: int) -> None: ...
    def _finalise_pipelines(self) -> None: ...
    def _obtain_rays(self, task: tuple[int, int], template: Ray) -> list[tuple[Ray, float]]: ...
    def _obtain_sensitivity(self, task: tuple[int, int]) -> float: ...
    def _generate_rays(self, x: int, y: int, template: Ray, ray_count: int) -> list[tuple[Ray, float]]:
        """
        Generate a list of Rays that sample over the sensitivity of the pixel.

        This is a virtual method to be implemented by derived classes.

        Runs during the observe() loop to generate the rays. Allows observers
        to customise how they launch rays.

        This method must return a list of tuples, with each tuple containing
        a Ray object and a corresponding weighting, typically the projected
        area/direction cosine. In general the weight will be:

        .. math::
           W = \\frac{1}{2\\pi} * \\frac{1}{A} * \\frac{1}{pdf_A} * \\frac{1}{pdf_\\Omega} * cos(\\theta)

        If the projected area weight is not required (due to the ray sampling
        algorithm taking the weighting into account in the distribution e.g.
        cosine weighted) then the weight should be set to 1.0.

        The number of rays returned must be equal to ray_count otherwise pipeline
        statistics will be incorrectly calculated.

        :param int x: Pixel x index.
        :param int y: Pixel y index.
        :param Ray template: The template ray from which all rays should be generated.
        :param int ray_count: The number of rays to be generated.
        :return list: A list of tuples of (ray, weight)
        """
    def _pixel_sensitivity(self, x: int, y: int) -> float:
        """

        :param int x: Pixel x index.
        :param int y: Pixel y index.
        :return:
        """
