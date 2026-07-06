from ....core.math import AffineMatrix3D
from ....core.scenegraph._nodebase import _NodeBase
from ... import Ray
from ..base import Observer2D, Pipeline2D
from ..sampler2d import FrameSampler2D

class OrthographicCamera(Observer2D):
    """
    A camera observing an orthogonal (orthographic) projection of the scene,
    avoiding perspective effects.

    :param tuple pixels: A tuple of pixel dimensions for the camera (default=(720, 480)).
    :param double width: width of the orthographic area to observe in meters,
      the height is deduced from the 'pixels' attribute.
    :param float sensitivity: The sensitivity of each pixel (default=1.0)
    :param FrameSampler2D frame_sampler: The frame sampling strategy
      (default=FullFrameSampler2D()).
    :param list pipelines: The list of pipelines that will process the spectrum measured
      at each pixel by the camera (default=RGBPipeline2D()).
    :param kwargs: **kwargs and properties from Observer2D and _ObserverBase.
    """

    def __init__(
        self,
        pixels: tuple[int, int],
        width: float = 1.0,
        sensitivity: float = 1.0,
        frame_sampler: FrameSampler2D | None = ...,
        pipelines: list[Pipeline2D] | None = None,
        parent: _NodeBase | None = None,
        transform: AffineMatrix3D | None = None,
        name: str | None = None,
    ) -> None: ...
    @property
    def width(self) -> float:
        """
        The width of the orthographic area to observe in meters, the height is
        deduced from the 'pixels' attribute.

        :rtype: float
        """
    @width.setter
    def width(self, value: float) -> None: ...
    @property
    def pixels(self) -> tuple[int, int]:
        """
        Tuple describing the pixel dimensions for this observer (nx, ny), i.e. (512, 512).

        :rtype: tuple
        """
    @pixels.setter
    def pixels(self, value: tuple[int, int]) -> None: ...
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
