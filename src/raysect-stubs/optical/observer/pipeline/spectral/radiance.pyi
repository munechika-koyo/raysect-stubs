import numpy as np
from numpy.typing import NDArray

from ....spectrum import Spectrum
from ...base.slice import SpectralSlice
from .power import SpectralPowerPipeline0D, SpectralPowerPipeline1D, SpectralPowerPipeline2D, SpectralPowerPixelProcessor

_DEFAULT_PIPELINE_NAME: str = "Spectral Radiance Pipeline"
_DISPLAY_DPI: int = 100
_DISPLAY_SIZE: tuple[float, float] = (8, 6)

class SpectralRadiancePipeline0D(SpectralPowerPipeline0D):
    """
    A basic spectral radiance pipeline for 0D observers (W/str/m^2/nm).

    The mean spectral radiance for the observer is stored along with the associated
    error on each wavelength bin.

    Spectral values and errors are available through the self.frame attribute.

    :param bool accumulate: Whether to accumulate samples with subsequent calls
      to observe() (default=True).
    :param str name: User friendly name for this pipeline.
    """

    def __init__(
        self,
        accumulate: bool = True,
        name: str = _DEFAULT_PIPELINE_NAME,
        display_progress: bool = True,
    ) -> None: ...
    def pixel_processor(self, slice_id: int) -> SpectralRadiancePixelProcessor: ...
    def _render_display(self) -> None: ...
    def to_spectrum(self) -> Spectrum:
        """
        Returns the mean spectral radiance in a Spectrum() object.
        """

class SpectralRadiancePipeline1D(SpectralPowerPipeline1D):
    """
    A basic spectral radiance pipeline for 1D observers (W/str/m^2/nm).

    The mean spectral radiance for each pixel is stored along with the associated
    error on each wavelength bin in a 1D frame object.

    Spectral values and errors are available through the self.frame attribute.

    :param bool accumulate: Whether to accumulate samples with subsequent calls
      to observe() (default=True).
    :param str name: User friendly name for this pipeline.
    """

    def __init__(
        self,
        accumulate: bool = True,
        name: str = _DEFAULT_PIPELINE_NAME,
    ) -> None: ...
    def pixel_processor(self, pixel: int, slice_id: int) -> SpectralRadiancePixelProcessor: ...
    def display_pixel(self, pixel: int) -> None: ...
    def to_spectrum(self, pixel: int) -> Spectrum:
        """
        Returns the mean spectral radiance of pixel in a Spectrum() object.
        """

class SpectralRadiancePipeline2D(SpectralPowerPipeline2D):
    """
    A basic spectral radiance pipeline for 2D observers (W/str/m^2/nm).

    The mean spectral radiance for each pixel is stored along with the associated
    error on each wavelength bin in a 2D frame object.

    Spectral values and errors are available through the self.frame attribute.

    :param bool accumulate: Whether to accumulate samples with subsequent calls
      to observe() (default=True).
    :param str name: User friendly name for this pipeline.
    """

    def __init__(
        self,
        accumulate: bool = True,
        name: str = _DEFAULT_PIPELINE_NAME,
    ) -> None: ...
    def pixel_processor(self, x: int, y: int, slice_id: int) -> SpectralRadiancePixelProcessor: ...
    def display_pixel(self, x: int, y: int) -> None: ...
    def to_spectrum(self, x: int, y: int) -> Spectrum:
        """
        Returns the mean spectral radiance of pixel (x, y) in a Spectrum() object.
        """

class SpectralRadiancePixelProcessor(SpectralPowerPixelProcessor):
    """
    PixelProcessor that stores the spectral radiance observed by each pixel.
    """

    def __init__(self, slice: SpectralSlice) -> None: ...
    def add_sample(self, spectrum: Spectrum, sensitivity: float) -> None: ...
    def pack_results(self) -> tuple[NDArray[np.float64], NDArray[np.float64]]: ...
