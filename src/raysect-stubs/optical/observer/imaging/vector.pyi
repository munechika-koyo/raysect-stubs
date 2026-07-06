import numpy as np
from numpy.typing import NDArray

from ....core.math import AffineMatrix3D
from ....core.scenegraph._nodebase import _NodeBase
from ... import Ray
from ..base import Observer2D, Pipeline2D
from ..sampler2d import FrameSampler2D

class VectorCamera(Observer2D):
    """
    An observer that uses a specified set of pixel vectors.

    A simple camera that uses calibrated vectors for each pixel to sample the scene.
    Arguments and attributes are inherited from the base Observer2D sensor class.

    :param np.ndarray pixel_origins: Numpy array of Point3Ds describing the origin points
      of each pixel. Must have same shape as the pixel dimensions.
    :param np.ndarray pixel_directions: Numpy array of Vector3Ds describing the sampling
      direction vectors of each pixel. Must have same shape as the pixel dimensions.
    :param float sensitivity: The sensitivity of each pixel (default=1.0)
    :param FrameSampler2D frame_sampler: The frame sampling strategy (default=FullFrameSampler2D()).
    :param list pipelines: The list of pipelines that will process the spectrum measured
      at each pixel by the camera (default=RGBPipeline2D()).
    :param kwargs: **kwargs and properties from Observer2D and _ObserverBase.
    """

    def __init__(
        self,
        pixel_origins: NDArray[np.float64],
        pixel_directions: NDArray[np.float64],
        frame_sampler: FrameSampler2D | None = None,
        pipelines: list[Pipeline2D] | None = None,
        sensitivity: float | None = None,
        parent: _NodeBase | None = None,
        transform: AffineMatrix3D | None = None,
        name: str | None = None,
    ) -> None: ...
    @property
    def sensitivity(self) -> float:
        """
        The sensitivity applied to each pixel.

        If sensitivity=1.0 all spectral units are in radiance.

        :rtype: float
        """
    @sensitivity.setter
    def sensitivity(self, value: float) -> None: ...
    def _generate_rays(self, x: int, y: int, template: Ray, ray_count: int) -> list[tuple[Ray, float]]: ...
    def _pixel_sensitivity(self, x: int, y: int) -> float: ...
