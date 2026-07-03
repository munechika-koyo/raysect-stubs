from ....core.math import AffineMatrix3D
from ....core.scenegraph._nodebase import _NodeBase
from ....core.workflow import RenderEngine
from ... import Ray
from ..base import Observer0D, Pipeline0D

class Pixel(Observer0D):
    """
    A pixel observer that samples rays from a hemisphere and rectangular area.

    :param list pipelines: The list of pipelines that will process the spectrum measured
      by this pixel (default=SpectralPipeline0D()).
    :param float x_width: The rectangular collection area's width along the
      x-axis in local coordinates (default=1cm).
    :param float y_width: The rectangular collection area's width along the
      y-axis in local coordinates (default=1cm).
    :param kwargs: **kwargs from Observer0D and _ObserverBase

    .. code-block:: pycon

        >>> from raysect.optical import World
        >>> from raysect.optical.observer import Pixel, PowerPipeline0D
        >>>
        >>> world = World()
        >>> power = PowerPipeline0D(accumulate=False)
        >>> observing_plane = Pixel([power], x_width=2.0, y_width=2.0,
                                    min_wavelength=400, max_wavelength=720,
                                    spectral_bins=1, pixel_samples=250,
                                    parent=world, transform=rotate(0, 0, 0)*translate(0, 0, -1))
        >>> observing_plane.observe()
    """

    def __init__(
        self,
        pipelines: list[Pipeline0D] = ...,
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

    def _generate_rays(self, template: Ray, ray_count: int) -> list[tuple[Ray, float]]: ...
    def _pixel_sensitivity(self) -> float: ...
