from ....core.math import AffineMatrix3D
from ....core.scenegraph._nodebase import _NodeBase
from ....core.workflow import RenderEngine
from ....primitive.mesh import Mesh
from ..base import Observer0D, Pipeline0D

class MeshPixel(Observer0D):
    """
    Uses a supplied mesh surface as a pixel.

    .. Warning::
       Users must be careful when using this camera to not double count radiance. For example,
       if you have a concave mesh its possible for two surfaces to see the same emission. In cases
       like this, the mesh should have an absorbing surface to prevent double counting.

    This observer samples over the surface defined by a triangular mesh. At each point on the surface
    the incoming radiance over a hemisphere is sampled.

    A mesh surface offset can be set to ensure sample don\'t collide with a coincident primitive. When set,
    the surface offset specifies the distance along the surface normal that the ray launch origin is shifted.

    :param Mesh mesh: The mesh instance to use for observations.
    :param float surface_offset: The offset from the mesh surface (default=0).
    :param list pipelines: The list of pipelines that will process the spectrum measured
      by this pixel (default=SpectralPowerPipeline0D()).
    :param kwargs: **kwargs from Observer0D and _ObserverBase

    .. code-block:: pycon

        >>> from raysect.primitive import Mesh
        >>> from raysect.optical import World
        >>> from raysect.optical.material import AbsorbingSurface
        >>> from raysect.optical.observer import MeshPixel, PowerPipeline0D
        >>>
        >>> world = World()
        >>>
        >>> mesh = Mesh.from_file("my_mesh.rsm", material=AbsorbingSurface(), parent=world)
        >>>
        >>> power = PowerPipeline0D(accumulate=False)
        >>> observer = MeshPixel(mesh, pipelines=[power], parent=world,
        >>>                      min_wavelength=400, max_wavelength=750,
        >>>                      spectral_bins=1, pixel_samples=10000, surface_offset=1E-6)
        >>> observer.observe()
    """

    mesh: Mesh

    def __init__(
        self,
        mesh: Mesh,
        surface_offset: float = 0.0,
        pipelines: list[Pipeline0D] | None = ...,
        parent: _NodeBase | None = None,
        transform: AffineMatrix3D | None = None,
        name: str | None = None,
        render_engine: RenderEngine | None = ...,
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
