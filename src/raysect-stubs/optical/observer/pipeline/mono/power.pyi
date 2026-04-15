import numpy as np
from numpy.typing import NDArray

from .....core.math import StatsArray1D, StatsArray2D, StatsBin
from ....spectralfunction import ConstantSF, SpectralFunction
from ....spectrum import Spectrum
from ...base.pipeline import Pipeline0D, Pipeline1D, Pipeline2D
from ...base.processor import PixelProcessor
from ...base.slice import SpectralSlice

_DEFAULT_PIPELINE_NAME: str = "Power Pipeline"
_DISPLAY_DPI: int = 100
_DISPLAY_SIZE: tuple[float, float] = (5.12, 5.12)

CONSTANTSF = ConstantSF(1.0)

class PowerPipeline0D(Pipeline0D):
    """
    A power pipeline for 0D observers.

    The raw spectrum collected by the observer is multiplied by a spectra filter
    and integrated to give to total power collected.

    The measured value and error are accessed at self.value.mean and self.value.error
    respectively.

    :param SpectralFunction filter: A filter function to be multiplied with the
     measured spectrum.
    :param bool accumulate:
    :param str name: User friendly name for this pipeline.
    """

    name: str
    filter: SpectralFunction
    accumulate: bool
    value: StatsBin

    def __init__(
        self,
        filter: SpectralFunction | None = CONSTANTSF,
        accumulate: bool = True,
        name: str = _DEFAULT_PIPELINE_NAME,
    ) -> None: ...
    def initialise(
        self,
        min_wavelength: float,
        max_wavelength: float,
        spectral_bins: int,
        spectral_slices: list,
        quiet: bool,
    ) -> None: ...
    def pixel_processor(self, slice_id: int) -> PowerPixelProcessor: ...
    def update(self, slice_id: int, packed_result: tuple[float, float], samples: int) -> None: ...
    def finalise(self) -> None: ...

class PowerPipeline1D(Pipeline1D):
    """
    A power pipeline for 1D observers.

    The raw spectrum collected at each pixel by the observer is multiplied by
    a spectral filter and integrated to give to total power collected at that
    pixel.

    The measured value and error for each pixel are accessed at self.frame.mean
    and self.frame.error respectively.

    :param SpectralFunction filter: A filter function to be multiplied with the
     measured spectrum.
    :param bool accumulate: Whether to accumulate samples with subsequent calls
      to observe() (default=True).
    :param str name: User friendly name for this pipeline.
    """

    name: str
    filter: SpectralFunction
    accumulate: bool
    frame: StatsArray1D

    def __init__(
        self,
        filter: SpectralFunction | None = CONSTANTSF,
        accumulate: bool = True,
        name: str = _DEFAULT_PIPELINE_NAME,
    ) -> None: ...
    def initialise(
        self,
        pixels: int,
        pixel_samples: int,
        min_wavelength: float,
        max_wavelength: float,
        spectral_bins: int,
        spectral_slices: list[SpectralSlice],
        quiet: bool,
    ) -> None: ...
    def pixel_processor(self, pixel: int, slice_id: int) -> PowerPixelProcessor: ...
    def update(self, pixel: int, slice_id: int, packed_result: tuple[float, float]) -> None: ...
    def finalise(self) -> None: ...

class PowerPipeline2D(Pipeline2D):
    """
    A power pipeline for 2D observers.

    The raw spectrum collected at each pixel by the observer is multiplied by
    a spectral filter and integrated to give to total power collected at that
    pixel.

    The measured value and error for each pixel are accessed at self.frame.mean and self.frame.error
    respectively.

    :param SpectralFunction filter: A filter function to be multiplied with the
     measured spectrum.
    :param bool display_progress: Toggles the display of live render progress
      (default=True).
    :param float display_update_time: Time in seconds between preview display
      updates (default=15 seconds).
    :param bool accumulate: Whether to accumulate samples with subsequent calls
      to observe() (default=True).
    :param bool display_auto_exposure: Toggles the use of automatic exposure of
      final images (default=True).
    :param float display_black_point:
    :param float display_white_point:
    :param float display_unsaturated_fraction: Fraction of pixels that must not
      be saturated. Display values will be scaled to satisfy this value
      (default=1.0).
    :param float display_gamma:
    :param str name: User friendly name for this pipeline.
    """

    name: str
    filter: SpectralFunction
    display_progress: bool
    accumulate: bool
    frame: StatsArray2D
    display_persist_figure: bool

    def __init__(
        self,
        filter: SpectralFunction | None = CONSTANTSF,
        display_progress: bool = True,
        display_update_time: float = 15.0,
        accumulate: bool = True,
        display_auto_exposure: bool = True,
        display_black_point: float = 0.0,
        display_white_point: float = 1.0,
        display_unsaturated_fraction: float = 1.0,
        display_gamma: float = 2.2,
        name: str = _DEFAULT_PIPELINE_NAME,
    ) -> None: ...
    @property
    def display_white_point(self) -> float: ...
    @display_white_point.setter
    def display_white_point(self, value: float) -> None: ...
    @property
    def display_black_point(self) -> float: ...
    @display_black_point.setter
    def display_black_point(self, value: float) -> None: ...
    @property
    def display_gamma(self) -> float: ...
    @display_gamma.setter
    def display_gamma(self, value: float) -> None: ...
    @property
    def display_auto_exposure(self) -> bool: ...
    @display_auto_exposure.setter
    def display_auto_exposure(self, value: bool) -> None: ...
    @property
    def display_unsaturated_fraction(self) -> float: ...
    @display_unsaturated_fraction.setter
    def display_unsaturated_fraction(self, value: float) -> None: ...
    @property
    def display_update_time(self) -> float: ...
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
    def pixel_processor(self, x: int, y: int, slice_id: int) -> PowerPixelProcessor: ...
    def update(self, x: int, y: int, slice_id: int, packed_result: tuple[float, float]) -> None: ...
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
    def _render_display(self, frame: StatsArray2D, status: str | None = None): ...
    def _generate_display_image(self, frame: StatsArray2D) -> NDArray[np.float64]: ...
    def _calculate_white_point(self, image: NDArray[np.float64]) -> float: ...
    def display(self) -> None: ...
    def save(self, filename: str) -> None:
        """
        Saves the display image to a png file.

        The current display settings (exposure, gamma, etc..) are used to
        process the image prior saving.

        :param str filename: Image path and filename.
        """

class PowerPixelProcessor(PixelProcessor):
    """
    PixelProcessor that converts each pixel's spectrum into total power by
    integrating over the spectrum and multiplying the resulting radiance
    value by the pixel's sensitivity.
    """

    def __init__(self, filter: memoryview) -> None: ...
    def reset(self) -> None: ...
    def add_sample(self, spectrum: Spectrum, sensitivity: float) -> None: ...
    def pack_results(self) -> tuple[float, float]: ...
