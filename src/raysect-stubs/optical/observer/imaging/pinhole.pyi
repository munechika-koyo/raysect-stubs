from ....core.math import AffineMatrix3D
from ....core.scenegraph._nodebase import _NodeBase
from ..base import Observer2D, Pipeline2D
from ..sampler2d import FrameSampler2D

class PinholeCamera(Observer2D):
    """
    An observer that models an idealised pinhole camera.

    A simple camera that launches rays from the observer\'s origin point over a
    specified field of view.

    :param tuple pixels: A tuple of pixel dimensions for the camera (default=(720, 480)).
    :param float fov: The field of view of the camera in degrees (default=45 degrees).
    :param float sensitivity: The sensitivity of each pixel (default=1.0)
    :param FrameSampler2D frame_sampler: The frame sampling strategy, defaults to adaptive
      sampling (i.e. extra samples for noisier pixels).
    :param list pipelines: The list of pipelines that will process the spectrum measured
      at each pixel by the camera (default=RGBPipeline2D()).
    :param kwargs: **kwargs and properties from Observer2D and _ObserverBase.

    .. code-block:: pycon

        >>> from raysect.core import translate
        >>> from raysect.optical import World
        >>> from raysect.optical.observer import PinholeCamera, PowerPipeline2D
        >>>
        >>> power = PowerPipeline2D(display_unsaturated_fraction=0.96, name="Unfiltered")
        >>>
        >>> camera = PinholeCamera((512, 512), parent=world, pipelines=[power])
        >>> camera.transform = translate(0, 0, -3.3)
        >>> camera.pixel_samples = 250
        >>> camera.spectral_bins = 15
        >>>
        >>> camera.observe()
    """

    def __init__(
        self,
        pixels: tuple[int, int],
        fov: float = 45.0,
        sensitivity: float = 1.0,
        frame_sampler: FrameSampler2D | None = ...,
        pipelines: list[Pipeline2D] | None = None,
        parent: _NodeBase | None = None,
        transform: AffineMatrix3D | None = None,
        name: str | None = None,
    ) -> None: ...
    @property
    def fov(self) -> float:
        """
        The field of view of the camera in degrees.

        :rtype: float
        """
    @fov.setter
    def fov(self, value: float) -> None: ...
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
