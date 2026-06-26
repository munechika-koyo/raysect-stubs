import numpy as np
from numpy.typing import NDArray

from ....core.math import StatsArray3D
from ...spectrum import Spectrum
from ..base import Pipeline2D, PixelProcessor, SpectralSlice

_DEFAULT_PIPELINE_NAME: str = "RGBPipeline Pipeline"
_DISPLAY_DPI: int = 100
_DISPLAY_SIZE: tuple[float, float] = (5.12, 5.12)

class RGBPipeline2D(Pipeline2D):
    """
    2D pipeline of sRGB colour values.

    Converts the measured spectrum from each pixel into sRGB
    colour space values. See the colour module for more
    information. The RGBPipeline2D class is the workhorse
    pipeline for visualisation of scenes with Raysect and the
    default pipeline for most 2D observers.

    :param bool display_progress: Toggles the display of live render progress
      (default=True).
    :param float display_update_time: Time in seconds between preview display
      updates (default=15 seconds).
    :param bool accumulate: Whether to accumulate samples with subsequent calls
      to observe() (default=True).
    :param bool display_auto_exposure: Toggles the use of automatic exposure of
      final images (default=True).
    :param float display_sensitivity: The sensitivity of the camera, effectively
      inverse of the exposure time (default=1.0).
    :param float display_unsaturated_fraction: Fraction of pixels that must not
      be saturated. Display values will be scaled to satisfy this value
      (default=1.0).
    :param str name: User friendly name for this pipeline.
    """

    name: str
    display_progress: bool
    accumulate: bool
    xyz_frame: StatsArray3D
    display_persist_figure: bool

    def __init__(
        self,
        display_progress: bool = True,
        display_update_time: float = 15,
        accumulate: bool = True,
        display_auto_exposure: bool = True,
        display_sensitivity: float = 1.0,
        display_unsaturated_fraction: float = 1.0,
        name: str | None = None,
    ) -> None: ...
    @property
    def display_sensitivity(self) -> float:
        """
        The sensitivity of the camera, effectively inverse of the exposure time.

        :rtype: float
        """
    @display_sensitivity.setter
    def display_sensitivity(self, value: float) -> None: ...
    @property
    def display_auto_exposure(self) -> bool:
        """
        Toggles the use of automatic exposure of final images.

        :rtype: bool
        """
    @display_auto_exposure.setter
    def display_auto_exposure(self, value: bool) -> None: ...
    @property
    def display_unsaturated_fraction(self) -> float:
        """
        Fraction of pixels that must not be saturated. Display values will be
        scaled to satisfy this value.

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
    def update(self, x: int, y: int, slice_id: int, packed_result: tuple[NDArray[np.float64], NDArray[np.float64]]) -> None: ...
    def finalise(self) -> None: ...
    def _start_display(self) -> None:
        """
        Display live render.
        """
    def _update_display(self, x: int, y: int) -> None:
        """
        Update live render.
        """
    def _refresh_display(self) -> None:
        """
        Refreshes the display window (if active) and frame data is present.

        This method is called when display attributes are changed to refresh
        the display according to the new settings.
        """
    def _render_display(self, frame: StatsArray3D, status: str | None = None) -> None: ...
    def _generate_display_image(self, frame: StatsArray3D) -> NDArray[np.float64]: ...
    def _calculate_sensitivity(self, image: NDArray[np.float64]) -> float: ...
    def _generate_srgb_image(self, image: NDArray[np.float64]) -> NDArray[np.float64]: ...
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

class XYZPixelProcessor(PixelProcessor):
    """
    PixelProcessor that converts each pixel's spectrum into three
    XYZ colourspace values.
    """

    def __init__(self, resampled_xyz: NDArray[np.float64]) -> None: ...
    def reset(self) -> None: ...
    def add_sample(self, spectrum: Spectrum, sensitivity: float) -> None: ...
    def pack_results(self) -> tuple[NDArray[np.float64], NDArray[np.float64]]: ...
