import numpy as np
from numpy.typing import NDArray

from .....core.math import StatsArray1D, StatsArray2D, StatsArray3D
from .... import Spectrum
from ...base.pipeline import Pipeline0D, Pipeline1D, Pipeline2D
from ...base.processor import PixelProcessor
from ...base.slice import SpectralSlice

_DEFAULT_PIPELINE_NAME: str = "Spectral Power Pipeline"
_DISPLAY_DPI: int = 100
_DISPLAY_SIZE: tuple[float, float] = (8, 6)

class SpectralPowerPipeline0D(Pipeline0D):
    """
    A basic spectral power pipeline for 0D observers (W/nm).

    The mean spectral power for the observer is stored along with the associated
    error on each wavelength bin.

    Spectral values and errors are available through the self.frame attribute.

    :param bool accumulate: Whether to accumulate samples with subsequent calls
      to observe() (default=True).
    :param str name: User friendly name for this pipeline.
    """

    name: str
    accumulate: bool
    samples: StatsArray1D
    bins: int
    min_wavelength: float
    max_wavelength: float
    delta_wavelength: float
    wavelengths: NDArray[np.float64]
    display_progress: bool

    def __init__(
        self,
        accumulate: bool = True,
        name: str = _DEFAULT_PIPELINE_NAME,
        display_progress: bool = True,
    ) -> None: ...
    def initialise(
        self,
        min_wavelength: float,
        max_wavelength: float,
        spectral_bins: int,
        spectral_slices: list[SpectralSlice],
        quiet: bool,
    ) -> None: ...
    def pixel_processor(self, slice_id: int) -> PixelProcessor: ...
    def update(  # pyrefly: ignore [bad-override-param-name]
        self,
        slice_id: int,
        packed_result: tuple[NDArray[np.float64], NDArray[np.float64]],
        pixel_samples: int,
    ) -> None: ...
    def finalise(self) -> None: ...
    def display(self) -> None: ...

class SpectralPowerPipeline1D(Pipeline1D):
    """
    A basic spectral power pipeline for 1D observers (W/nm).

    The mean spectral power for each pixel is stored along with the associated
    error on each wavelength bin in a 1D frame object.

    Spectral values and errors are available through the self.frame attribute.

    :param bool accumulate: Whether to accumulate samples with subsequent calls
      to observe() (default=True).
    :param str name: User friendly name for this pipeline.
    """

    name: str
    accumulate: bool
    frame: StatsArray2D
    bins: int
    min_wavelength: float
    max_wavelength: float
    delta_wavelength: float
    wavelengths: NDArray[np.float64]

    def __init__(
        self,
        accumulate: bool = True,
        name: str = _DEFAULT_PIPELINE_NAME,
    ) -> None: ...
    def initialise(self, pixels: int, pixel_samples: int, min_wavelength: float, max_wavelength: float, spectral_bins: int, spectral_slices: list[SpectralSlice], quiet: bool) -> None: ...
    def pixel_processor(self, pixel: int, slice_id: int) -> SpectralPowerPixelProcessor: ...
    def update(self, pixel: int, slice_id: int, packed_result: tuple[NDArray[np.float64], NDArray[np.float64]]) -> None: ...
    def finalise(self) -> None: ...
    def display_pixel(self, pixel: int) -> None: ...

class SpectralPowerPipeline2D(Pipeline2D):
    """
    A basic spectral power pipeline for 2D observers (W/nm).

    The mean spectral power for each pixel is stored along with the associated
    error on each wavelength bin in a 2D frame object.

    Spectral values and errors are available through the self.frame attribute.

    :param bool accumulate: Whether to accumulate samples with subsequent calls
      to observe() (default=True).
    :param str name: User friendly name for this pipeline.
    """

    name: str
    accumulate: bool
    frame: StatsArray3D
    bins: int
    min_wavelength: float
    max_wavelength: float
    delta_wavelength: float
    wavelengths: NDArray[np.float64]

    def __init__(
        self,
        accumulate: bool = True,
        name: str = _DEFAULT_PIPELINE_NAME,
    ) -> None: ...
    def initialise(self, pixels: tuple[int, int], pixel_samples: int, min_wavelength: float, max_wavelength: float, spectral_bins: int, spectral_slices: list[SpectralSlice], quiet: bool) -> None: ...
    def pixel_processor(self, x: int, y: int, slice_id: int) -> SpectralPowerPixelProcessor: ...
    def update(self, x: int, y: int, slice_id: int, packed_result: tuple[NDArray[np.float64], NDArray[np.float64]]) -> None: ...
    def finalise(self) -> None: ...
    def display_pixel(self, x: int, y: int) -> None: ...

class SpectralPowerPixelProcessor(PixelProcessor):
    """
    PixelProcessor that stores the spectral power observed by each pixel.
    """

    def __init__(self, slice: SpectralSlice) -> None: ...
    def add_sample(self, spectrum: Spectrum, sensitivity: float) -> None: ...
    def pack_results(self) -> tuple[NDArray[np.float64], NDArray[np.float64]]: ...
