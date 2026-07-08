import numpy as np
from numpy.typing import ArrayLike, NDArray

from ....core.math import AffineMatrix3D
from ....core.scenegraph._nodebase import _NodeBase
from ... import Ray
from ..base import Observer2D, Pipeline2D
from ..sampler2d import FrameSampler2D

class OpenCVCamera(Observer2D):
    """
    An observer based on the OpenCV camera model.

    A simple analytic camera that uses calibrated camera parameters to re-generate the
    pixel vectors. The following parameters need to be supplied.

    * pinhole and barrel distortion terms :math:`(k_1, k_2, p_1, p_2, k_3)`.
    * camera matrix describing the focal lengths :math:`(f_x, f_y)` and
      optical centres :math:`(c_x, c_y)` in pixel coordinates.
    * R and T coordinate vectors defining the transformation coordinates.
    * pixel dimensions of the camera.

    See the OpenCV documentation `here
    <https://docs.opencv.org/2.4/doc/tutorials/calib3d/camera_calibration/camera_calibration.html>`_ and `here
    <https://docs.opencv.org/3.4.0/d9/d0c/group__calib3d.html>`_ for more details.

    Arguments and attributes are inherited from the base Observer2D sensor class.

    :param ndarray camera_matrix: focal lengths :math:`(f_x, f_y)` and optical centres :math:`(c_x, c_y)`
      in pixel coordinates.
    :param tuple distortion: tuple/list/array of pinhole and barrel distortion terms :math:`(k_1, k_2, p_1, p_2, k_3)`.
    :param tuple r_vector: R coordinate vector.
    :param tuple t_vector: T coordinate vector.
    :param tuple pixels: The pixel dimensions of the camera.
    :param FrameSampler2D frame_sampler: The frame sampling strategy (default=FullFrameSampler2D()).
    :param list pipelines: The list of pipelines that will process the spectrum measured
      at each pixel by the camera (default=RGBPipeline2D()).
    :param float etendue: The constant etendue factor applied to each pixel (default=1).
    :param kwargs: **kwargs and properties from Observer2D and _ObserverBase.
    """

    def __init__(
        self,
        camera_matrix: NDArray[np.float64],
        distortion: ArrayLike,
        r_vector: tuple[float, float, float],
        t_vector: tuple[float, float, float],
        pixels: tuple[int, int],
        frame_sampler: FrameSampler2D | None = ...,
        pipelines: list[Pipeline2D] | None = None,
        etendue: float = 1.0,
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
