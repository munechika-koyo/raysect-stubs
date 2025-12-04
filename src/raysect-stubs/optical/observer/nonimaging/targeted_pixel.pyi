from ....core.math.affinematrix import AffineMatrix3D
from ....core.scenegraph._nodebase import _NodeBase
from ....core.scenegraph.primitive import Primitive
from ....core.workflow import RenderEngine
from ....optical.ray import Ray
from ..base.observer import Observer0D
from ..base.pipeline import Pipeline0D

class TargetedPixel(Observer0D):
    """
    A pixel observer that preferentially targets rays towards a given list of primitives.

    The targeted pixel takes a list of target primitives. The observer targets the
    bounding sphere that encompasses a target primitive. Therefore, for best performance,
    the target primitives should be split up such that their surfaces are closely wrapped
    by the bounding sphere.

    The sampling algorithm fires a proportion of rays at the targets, and a portion sampled
    from the full hemisphere. The proportion that is fired towards the targets is controlled
    with the targeted_path_prob attribute. By default this attribute is set to 0.9, i.e.
    90% of the rays are fired towards the targets.

    .. Warning..
       If the target probability is set to 1, rays will only be fired directly towards the
       targets. The user must ensure there are no sources of radiance outside of the
       targeted directions, otherwise they will not be sampled and the result will be biased.

    :param list targets: The list of primitives for targeted sampling.
    :param float targeted_path_prob: The probability of sampling a targeted primitive VS sampling over the whole hemisphere.
    :param list pipelines: The list of pipelines that will process the spectrum measured
      by this pixel (default=SpectralPipeline0D()).
    :param float x_width: The rectangular collection area\'s width along the
      x-axis in local coordinates (default=1cm).
    :param float y_width: The rectangular collection area\'s width along the
      y-axis in local coordinates (default=1cm).
    :param kwargs: **kwargs from Observer0D and _ObserverBase

    .. code-block:: pycon

        >>> from raysect.optical.observer import TargetedPixel, PowerPipeline0D
        >>>
        >>> # set-up scenegraph
        >>> world = World()
        >>> emitter = Sphere(radius=sphere_radius, parent=world)
        >>> emitter.material = UnityVolumeEmitter()
        >>>
        >>> # setup targeted pixel observer
        >>> targeted_pipeline = PowerPipeline0D(name="Targeted Pixel Observer")
        >>> targeted_pixel = TargetedPixel(parent=world, targets=[emitter],
        >>>                                  pixel_samples=250, pipelines=[targeted_pipeline])
        >>> targeted_pixel.observe()
    """
    def __init__(
        self,
        targets: list[Primitive],
        targeted_path_prob: float | None = None,
        pipelines: list[Pipeline0D] | None = None,
        x_width: float | None = None,
        y_width: float | None = None,
        parent: _NodeBase | None = None,
        transform: AffineMatrix3D | None = None,
        name: str | None = None,
        render_engine: RenderEngine | None = None,
        pixel_samples: int | None = None,
        samples_per_task: int | None = None,
        spectral_rays: int | None = None,
        spectral_bins: int | None = None,
        min_wavelength: float | None = None,
        max_wavelength: float | None = None,
        ray_extinction_prob: float | None = None,
        ray_extinction_min_depth: int | None = None,
        ray_max_depth: int | None = None,
        ray_importance_sampling: bool | None = None,
        ray_important_path_weight: float | None = None,
        quiet: bool = False,
    ) -> None: ...
    @property
    def x_width(self) -> float:
        """
        The rectangular collection area's width along the x-axis in local coordinates.

        :rtype: float
        """
    @property
    def y_width(self) -> float:
        """
        The rectangular collection area's width along the y-axis in local coordinates.

        :rtype: float
        """
    @property
    def collection_area(self) -> float:
        """
        The pixel's collection area in m^2.

        :rtype: float
        """
    @property
    def solid_angle(self) -> float:
        """
        The pixel's solid angle in steradians str.

        :rtype: float
        """
    @property
    def sensitivity(self) -> float:
        """
        The pixel's sensitivity measured in units of per area per solid angle (m^-2 str^-1).

        :rtype: float
        """
    @property
    def targets(self) -> list[Primitive]:
        """
        The list of primitives this pixel will target for sampling.

        :rtype: list
        """
    @property
    def targeted_path_prob(self) -> float:
        """
        The probability that an individual sample will be fired at a target instead of a sample from the whole hemisphere.

        .. Warning..
           If the target probability is set to 1, rays will only be fired directly towards the targets. The user must
           ensure there are now sources of radiance outside of the targeted directions, otherwise they will not be
           sampled and the result will be biased.

        :rtype: float
        """
    def _generate_rays(self, template: Ray, ray_count: int) -> list[tuple[Ray, float]]: ...
    def _pixel_sensitivity(self) -> float: ...
