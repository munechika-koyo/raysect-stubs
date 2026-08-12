from ....core.math import AffineMatrix3D
from ....core.scenegraph import Primitive
from ....core.scenegraph._nodebase import _NodeBase
from ..base import Observer2D, Pipeline2D

class TargetedCCDArray(Observer2D):
    """
    An ideal CCD-like imaging sensor that preferentially targets a given list of primitives.

    The targeted CCD is a regular array of square pixels. Each pixel samples red, green
    and blue channels (behaves like a Foveon imaging sensor). The CCD sensor
    width is specified with the width parameter. The CCD height is calculated
    from the width and the number of vertical and horizontal pixels. The
    default width and sensor ratio approximates a 35mm camera sensor.

    The targeted CCD takes a list of target primitives. Each pixel will target the
    bounding spheres that encompass each target primitive. Therefore, for best performance,
    the target primitives should be split up such that their surfaces are closely wrapped
    by the bounding sphere.

    The sampling algorithm fires a proportion of rays at the targets, and a portion sampled
    from the full hemisphere. The proportion that is fired towards the targets is controlled
    with the targeted_path_prob attribute. By default this attribute is set to 0.9, i.e.
    90% of the rays are fired towards the targets.

    .. Warning..
       If the target probability is set to 1, rays will only be fired directly towards the
       targets. The user must ensure there are no sources of radiance outside of the
       targeted directions, otherwise they will not be sampled and the result will be biased.

    :param list targets: The list of primitives for targeted sampling.
    :param tuple pixels: A tuple of pixel dimensions for the camera (default=(720, 480)).
    :param float width: The CCD sensor x-width in metres (default=35mm).
    :param list pipelines: The list of pipelines that will process the spectrum measured
      at each pixel by the camera (default=RGBPipeline2D()).
    :param kwargs: **kwargs and properties from Observer2D and _ObserverBase.
    """

    def __init__(
        self,
        targets: list[Primitive],
        pixels: tuple[int, int] = (720, 480),
        width: float = 0.035,
        targeted_path_prob: float = 0.9,
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
    @property
    def targets(self) -> list[Primitive]:
        """
        The list of primitives this pixel will target for sampling.

        :rtype: list
        """
    @targets.setter
    def targets(self, value: list[Primitive]) -> None: ...
    @property
    def targeted_path_prob(self) -> float:
        """
        The probability that an individual sample will be fired at a target instead of a sample from the whole hemisphere.

        .. Warning..
           If the target probability is set to 1, rays will only be fired directly towards the targets. The user must
           ensure there are now sources of radiance outside of the targeted directions, otherwise they will not be
           sampled and the result will be biased.

        :rtype: float
        """
    @targeted_path_prob.setter
    def targeted_path_prob(self, value: float) -> None: ...
