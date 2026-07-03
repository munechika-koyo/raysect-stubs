from ....core.math import AffineMatrix3D
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
        targeted_path_prob: float = 0.9,
        pipelines: list[Pipeline0D] | None = None,
        x_width: float = 0.01,
        y_width: float = 0.01,
        pixel_samples: int = 1000,
        samples_per_task: int = 250,
        parent: _NodeBase | None = None,
        transform: AffineMatrix3D | None = None,
        name: str | None = None,
        render_engine: RenderEngine = ...,
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
    ) -> None: ...
    @property
    def x_width(self) -> float:
        """
        The rectangular collection area's width along the x-axis in local coordinates.

        :rtype: float
        """
    @x_width.setter
    def x_width(self, value: float) -> None: ...
    @property
    def y_width(self) -> float:
        """
        The rectangular collection area's width along the y-axis in local coordinates.

        :rtype: float
        """
    @y_width.setter
    def y_width(self, value: float) -> None: ...
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
    @targets.setter
    def targets(self, value: list[Primitive]) -> None: ...
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
    @targeted_path_prob.setter
    def targeted_path_prob(self, value: float) -> None: ...
    def _generate_rays(self, template: Ray, ray_count: int) -> list[tuple[Ray, float]]: ...
    def _pixel_sensitivity(self) -> float: ...
