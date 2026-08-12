from typing import Any

from ....core.math import StatsArray2D
from ...spectrum import SpectralFunction
from ..base import Pipeline2D, PixelProcessor, SpectralSlice

_DEFAULT_PIPELINE_NAME: str = "Bayer Pipeline"
_DISPLAY_DPI: int = 100
_DISPLAY_SIZE: tuple[float, float] = (5.12, 5.12)

class BayerPipeline2D(Pipeline2D):
    """
    A 2D pipeline simulating a Bayer filter.

    Many commercial cameras use a Bayer filter for converting measured spectra into
    a 2D image of RGB values. The 2D sensor pixel array is covered with a mosaic of
    alternating red, green and blue filters. Thus each pixel in the array is only
    responsive to one of the colour filters simulating the response of the human eye.
    The final image is represented by a 2D grid of only red, green and blue values. The
    eye interpolates these values to create other colours. See
    `Wikipedia <https://en.wikipedia.org/wiki/Bayer_filter>`_ for more information.

    :param SpectralFunction red_filter: The spectral function representing the red pixel filter.
    :param SpectralFunction green_filter: The spectral function representing the green pixel filter.
    :param SpectralFunction blue_filter: The spectral function representing the blue pixel filter.
    :param bool display_progress: Toggles the display of live render progress (default=True).
    :param float display_update_time: Time in seconds between preview display
      updates (default=15 seconds).
    :param bool accumulate: Whether to accumulate samples with subsequent calls
      to observe() (default=True).
    :param bool display_auto_exposure: Toggles the use of automatic exposure of
      final images (default=True).
    :param float display_black_point: Lower clamp point for pixel to appear black
      (default=0.0).
    :param float display_white_point: Upper clamp point for pixel saturation
      (default=1.0).
    :param float display_unsaturated_fraction:  Fraction of pixels that must not
      be saturated. Display values will be scaled to satisfy this value
      (default=1.0).
    :param float display_gamma: Gamma exponent to account for non-linear response of
      display screens (default=2.2).
    :param str name: User friendly name for this pipeline (default="Bayer Pipeline").

    .. code-block:: pycon

        >>> from raysect.optical import InterpolatedSF
        >>> from raysect.optical.observer import BayerPipeline2D
        >>>
        >>> filter_red = InterpolatedSF([100, 650, 660, 670, 680, 800], [0, 0, 1, 1, 0, 0])
        >>> filter_green = InterpolatedSF([100, 530, 540, 550, 560, 800], [0, 0, 1, 1, 0, 0])
        >>> filter_blue = InterpolatedSF([100, 480, 490, 500, 510, 800], [0, 0, 1, 1, 0, 0])
        >>>
        >>> bayer = BayerPipeline2D(filter_red, filter_green, filter_blue,
                                    display_unsaturated_fraction=0.96, name="Bayer Filter")
    """

    name: str
    red_filter: SpectralFunction
    green_filter: SpectralFunction
    blue_filter: SpectralFunction
    display_progress: bool
    accumulate: bool
    frame: StatsArray2D
    display_persist_figure: bool

    def __init__(
        self,
        red_filter: SpectralFunction,
        green_filter: SpectralFunction,
        blue_filter: SpectralFunction,
        display_progress: bool = True,
        display_update_time: float = 15,
        accumulate: bool = True,
        display_auto_exposure: bool = True,
        display_black_point: float = 0.0,
        display_white_point: float = 1.0,
        display_unsaturated_fraction: float = 1.0,
        display_gamma: float = 2.2,
        name: str | None = None,
    ) -> None: ...
    @property
    def display_white_point(self) -> float:
        """
        Upper clamp point for pixel colour saturation.

        :rtype: float
        """
    @display_white_point.setter
    def display_white_point(self, value: float) -> None: ...
    @property
    def display_black_point(self) -> float:
        """
        Lower clamp point for pixel to appear black.

        :rtype: float
        """
    @display_black_point.setter
    def display_black_point(self, value: float) -> None: ...
    @property
    def display_gamma(self) -> float:
        r"""
        Power law exponent to approximate non-linear human eye response.

        Each pixel value will be raised to power gamma:

        .. math::

            V_{out} = V_{in}^{\gamma}

        For more information see `Wikipedia <https://en.wikipedia.org/wiki/Gamma_correction>`_.

        :rtype: float
        """
    @display_gamma.setter
    def display_gamma(self, value: float) -> None: ...
    @property
    def display_auto_exposure(self) -> bool:
        """
        Toggles the use of automatic exposure on final image.

        :rtype: bool
        """
    @display_auto_exposure.setter
    def display_auto_exposure(self, value: bool) -> None: ...
    @property
    def display_unsaturated_fraction(self) -> float:
        """
        Fraction of pixels that must not be saturated. Display values will
        be scaled to satisfy this value.

        :rtype: float
        """
    @display_unsaturated_fraction.setter
    def display_unsaturated_fraction(self, value: float) -> None: ...
    @property
    def display_update_time(self) -> float:
        """
        Time in seconds between preview display updates.

        :rtype: float
        """
    @display_update_time.setter
    def display_update_time(self, value: float) -> None: ...
    def initialise(
        self,
        pixels: tuple[int, int],
        pixel_samples: int,
        min_wavelength: float,
        max_wavelength: float,
        spectral_bins: int,
        spectral_slices: list[SpectralSlice],
        quiet: bool,
    ) -> None: ...
    def pixel_processor(self, x: int, y: int, slice_id: int) -> PixelProcessor: ...
    def update(self, x: int, y: int, slice_id: int, packed_result: tuple[Any, ...]) -> None: ...
    def finalise(self) -> None: ...
    def display(self) -> None:
        """
        Plot the RGB frame.
        """
    def save(self, filename: str) -> None:
        """
        Saves the display image to a png file.

        The current display settings (exposure, gamma, etc..) are used to
        process the image prior saving.

        :param str filename: Image path and filename.
        """
