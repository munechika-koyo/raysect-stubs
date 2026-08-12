import numpy as np
from numpy.typing import NDArray

from ....core.math import AffineMatrix3D
from ....core.scenegraph._nodebase import _NodeBase
from ....core.workflow import RenderEngine
from ....primitive.mesh import Mesh
from ..base.observer import Observer1D
from ..base.pipeline import Pipeline1D
from ..base.sampler import FrameSampler1D

class MeshCamera(Observer1D):
    """
    Uses a supplied mesh surface as a linear camera.

    .. Warning::
       Users must be careful when using this camera to not double count radiance. For example,
       if you have a concave mesh its possible for two surfaces to see the same emission. In cases
       like this, the mesh should have an absorbing surface to prevent double counting.

    This observer samples over each triangle or a triangular mesh. At each point on the surface
    the incoming radiance over a hemisphere is sampled. The pixel id corresponds to the triangle
    id in the mesh.

    A mesh surface offset can be set to ensure samples don\'t collide with a coincident primitive.
    When set, the surface offset specifies the distance along the surface normal that the ray
    launch origin is shifted.

    :param Mesh mesh: The Mesh object to use as the sampling surface.
    :param float surface_offset: The offset from the mesh surface (default=0).
    :param list pipelines: The list of pipelines that will process the spectrum measured
      by this observer (default=PowerPipeline1D()).
    :param kwargs: **kwargs from Observer1D and _ObserverBase

    .. code-block:: pycon

        >>> from raysect.primitive import Mesh
        >>> from raysect.optical import World
        >>> from raysect.optical.material import AbsorbingSurface
        >>> from raysect.optical.observer import MeshCamera, PowerPipeline1D, MonoAdaptiveSampler1D
        >>>
        >>> world = World()
        >>>
        >>> mesh = Mesh.from_file("my_mesh.rsm", material=AbsorbingSurface(), parent=world)
        >>>
        >>> power = PowerPipeline1D()
        >>> sampler = MonoAdaptiveSampler1D(power, fraction=0.2, ratio=25.0, min_samples=1000, cutoff=0.1)
        >>> camera = MeshCamera(mesh,
                                surface_offset=1e-6,  # launch rays 1mm off surface to avoid intersection with absorbing mesh
                                pipelines=[power],
                                frame_sampler=sampler,
                                parent=world,
                                spectral_bins=1,
                                min_wavelength=400,
                                max_wavelength=740,
                                pixel_samples=250)
        >>> camera.observe()
    """

    mesh: Mesh

    def __init__(
        self,
        mesh: Mesh,
        surface_offset: float | None = 0.0,
        frame_sampler: FrameSampler1D | None = ...,
        pipelines: list[Pipeline1D] | None = ...,
        parent: _NodeBase | None = None,
        transform: AffineMatrix3D | None = None,
        name: str | None = None,
        render_engine: RenderEngine | None = ...,
        pixel_samples: int = 1000,
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
    def collection_areas(self) -> NDArray[np.float64]: ...
    def collection_area(self, pixel: int) -> float:
        """
        The mesh camera's collection area in m^2.

        :rtype: float
        """
    @property
    def solid_angles(self) -> NDArray[np.float64]: ...
    def solid_angle(self, pixel: int) -> float:
        """
        The solid angle observed at each mesh triangle in steradians str.

        :rtype: float
        """
    @property
    def sensitivitys(self) -> NDArray[np.float64]: ...
    def sensitivity(self, pixel: int) -> float:
        """
        The mesh camera's sensitivity measured in units of per area per solid angle (m^-2 str^-1).

        :rtype: float
        """
