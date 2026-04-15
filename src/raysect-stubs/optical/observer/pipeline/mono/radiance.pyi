from ....spectralfunction import ConstantSF, SpectralFunction
from ....spectrum import Spectrum
from ...base.processor import PixelProcessor
from .power import PowerPipeline0D, PowerPipeline1D, PowerPipeline2D

_DEFAULT_PIPELINE_NAME: str = "Radiance Pipeline"
_DISPLAY_DPI: int = 100
_DISPLAY_SIZE: tuple[float, float] = (512 / _DISPLAY_DPI, 512 / _DISPLAY_DPI)

CONSTANTSF = ConstantSF(1.0)

class RadiancePipeline0D(PowerPipeline0D):
    """
    A radiance pipeline for 0D observers.

    The raw spectrum collected by the observer is multiplied by a spectra filter
    and integrated to give to total radiance collected (W/str/m^2).

    The measured value and error are accessed at self.value.mean and self.value.error
    respectively.

    :param SpectralFunction filter: A filter function to be multiplied with the
     measured spectrum.
    :param bool accumulate:
    :param str name: User friendly name for this pipeline.
    """

    def __init__(
        self,
        filter: SpectralFunction | None = CONSTANTSF,
        accumulate: bool = True,
        name: str = _DEFAULT_PIPELINE_NAME,
    ) -> None: ...
    def pixel_processor(self, slice_id: int) -> PixelProcessor: ...
    def finalise(self) -> None: ...

class RadiancePipeline1D(PowerPipeline1D):
    """
    A radiance pipeline for 1D observers.

    The raw spectrum collected at each pixel by the observer is multiplied by
    a spectral filter and integrated to give to total radiance collected at that
    pixel (W/str/m^2).

    The measured value and error for each pixel are accessed at self.frame.mean
    and self.frame.error respectively.

    :param SpectralFunction filter: A filter function to be multiplied with the
     measured spectrum.
    :param bool accumulate: Whether to accumulate samples with subsequent calls
      to observe() (default=True).
    :param str name: User friendly name for this pipeline.
    """

    def __init__(
        self,
        filter: SpectralFunction | None = CONSTANTSF,
        accumulate: bool = True,
        name: str = _DEFAULT_PIPELINE_NAME,
    ) -> None: ...
    def pixel_processor(self, pixel: int, slice_id: int) -> PixelProcessor: ...

class RadiancePipeline2D(PowerPipeline2D):
    """
    A radiance pipeline for 2D observers.

    The raw spectrum collected at each pixel by the observer is multiplied by
    a spectral filter and integrated to give to total radiance collected at that
    pixel (W/str/m^2).

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
    def pixel_processor(self, x: int, y: int, slice_id: int) -> PixelProcessor: ...

class RadiancePixelProcessor(PixelProcessor):
    """
    PixelProcessor that converts each pixel's spectrum into total radiance by
    integrating over the spectrum.
    """

    def __init__(self, filter: memoryview) -> None: ...
    def reset(self) -> None: ...
    def add_sample(self, spectrum: Spectrum, sensitivity: float) -> None: ...
    def pack_results(self) -> tuple[float, float]: ...
