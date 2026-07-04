from ....core.math import AffineMatrix3D
from ....core.scenegraph._nodebase import _NodeBase
from ....core.workflow import RenderEngine
from ... import Ray
from ..base import Observer0D, Pipeline0D

class SightLine(Observer0D):
    """
    A simple line of sight observer.

    Fires a single ray oriented along the observer's z axis in world space.

    :param float sensitivity: Optional user specified sensitivity. Defaults to sensitivity=1.0
      in which case the returned units will always be in radiance (W/m^2/str/nm)
    :param list pipelines: The list of pipelines that will process the spectrum measured
      by this line of sight (default=SpectralPipeline0D()).
    :param kwargs: **kwargs and instance properties from Observer0D and _ObserverBase

    .. code-block:: pycon

        >>> from raysect.optical import World
        >>> from raysect.optical.observer import SightLine, PowerPipeline0D
        >>>
        >>> world = World()
        >>> power = PowerPipeline0D(accumulate=False)
        >>> los = SightLine([power], min_wavelength=400, max_wavelength=720,
                            parent=world, transform=rotate(0, 0, 0)*translate(0, 0, -1))
        >>> los.observe()
    """

    def __init__(
        self,
        sensitivity: float = 1.0,
        pipelines: list[Pipeline0D] | None = None,
        parent: _NodeBase | None = None,
        transform: AffineMatrix3D | None = None,
        name: str | None = None,
        render_engine: RenderEngine | None = None,
        pixel_samples: int = 1000,
        samples_per_task: int = 250,
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
    def sensitivity(self) -> float:
        """
        User specified sensitivity (str^-1/m^-2)

        If sensitivity=1.0 the spectral units will always be in radiance (W/m^2/str/nm)

        :rtype: float
        """
    @sensitivity.setter
    def sensitivity(self, value: float) -> None: ...
    def _generate_rays(self, template: Ray, ray_count: int) -> list[tuple[Ray, float]]: ...
    def _pixel_sensitivity(self) -> float: ...
