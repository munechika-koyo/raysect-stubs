from ....core.math import AffineMatrix3D
from ....core.scenegraph._nodebase import _NodeBase
from ... import Ray
from ..base import Observer2D, Pipeline2D

class CCDArray(Observer2D):
    """
    An observer that models an idealised CCD-like imaging sensor.

    The CCD is a regular array of square pixels. Each pixel samples red, green
    and blue channels (behaves like a Foveon imaging sensor). The CCD sensor
    width is specified with the width parameter. The CCD height is calculated
    from the width and the number of vertical and horizontal pixels. The
    default width and sensor ratio approximates a 35mm camera sensor.

    :param tuple pixels: A tuple of pixel dimensions for the camera (default=(720, 480)).
    :param float width: The CCD sensor x-width in metres (default=35mm).
    :param list pipelines: The list of pipelines that will process the spectrum measured
      at each pixel by the camera (default=RGBPipeline2D()).
    :param kwargs: **kwargs and properties from Observer2D and _ObserverBase.
    """

    def __init__(
        self,
        pixels: tuple[int, int] = (720, 480),
        width: float = 0.035,
        parent: _NodeBase | None = None,
        transform: AffineMatrix3D | None = None,
        name: str | None = None,
        pipelines: list[Pipeline2D] | None = None,
    ) -> None: ...
    @property
    def pixels(self) -> tuple[int, int]: ...
    @pixels.setter
    def pixels(self, value: tuple[int, int]) -> None: ...
    @property
    def width(self) -> float:
        """
        The CCD sensor x-width in metres.

        :rtype: float
        """
    @width.setter
    def width(self, value: float) -> None: ...
    def _generate_rays(self, x: int, y: int, template: Ray, ray_count: int) -> list[tuple[Ray, float]]: ...
    def _pixel_sensitivity(self, x: int, y: int) -> float: ...
