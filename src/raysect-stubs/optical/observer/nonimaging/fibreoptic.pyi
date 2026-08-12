from ....core.math import AffineMatrix3D
from ....core.scenegraph._nodebase import _NodeBase
from ....core.workflow import RenderEngine
from ..base import Observer0D, Pipeline0D

class FibreOptic(Observer0D):
    """
    An optical fibre observer that samples rays from an acceptance cone and circular area at the fibre tip.

    Rays are sampled over a circular area at the fibre tip and a conical solid angle
    defined by the acceptance_angle parameter.

    :param list pipelines: The list of pipelines that will process the spectrum measured
      by this optical fibre (default=SpectralPipeline0D()).
    :param float acceptance_angle: The angle in degrees between the z axis and the cone surface which defines the fibres
       solid angle sampling area.
    :param float radius: The radius of the fibre tip in metres. This radius defines a circular area at the fibre tip
       which will be sampled over.
    :param kwargs: **kwargs from Observer0D and _ObserverBase

    .. code-block:: pycon

        >>> from raysect.optical.observer import FibreOptic, RadiancePipeline0D, PowerPipeline0D
        >>>
        >>> power = PowerPipeline0D()
        >>> radiance = RadiancePipeline0D()
        >>> fibre = FibreOptic([power, radiance], acceptance_angle=10, radius=0.0005,
                                spectral_bins=500, pixel_samples=1000,
                                transform=translate(0, 0, -5), parent=world)
        >>> fibre.observe()
    """

    def __init__(
        self,
        pipelines: list[Pipeline0D] | None = None,
        acceptance_angle: float = 5.0,
        radius: float = 0.001,
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
    def acceptance_angle(self) -> float:
        """
        The angle in degrees between the z axis and the cone surface which defines the fibres
        solid angle sampling area.

        :rtype: float
        """
    @acceptance_angle.setter
    def acceptance_angle(self, value: float) -> None: ...
    @property
    def radius(self) -> float:
        """
        The radius of the fibre tip in metres. This radius defines a circular area at the fibre tip
        which will be sampled over.

        :rtype: float
        """
    @radius.setter
    def radius(self, value: float) -> None: ...
    @property
    def collection_area(self) -> float:
        """
        The fibre's collection area in m^2.

        :rtype: float
        """
    @property
    def solid_angle(self) -> float:
        """
        The fibre's solid angle in steradians str.

        :rtype: float
        """
    @property
    def sensitivity(self) -> float:
        """
        The fibre's sensitivity measured in units of per area per solid angle (m^-2 str^-1).

        :rtype: float
        """
