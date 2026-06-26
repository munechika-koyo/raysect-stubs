from typing import Literal

import numpy
from numpy.typing import NDArray

from .base.sampler import FrameSampler2D
from .pipeline.mono import PowerPipeline2D, RadiancePipeline2D
from .pipeline.rgb import RGBPipeline2D
from .pipeline.spectral import SpectralPowerPipeline2D, SpectralRadiancePipeline2D

class FullFrameSampler2D(FrameSampler2D):
    """
    Evenly samples the full 2D frame or its masked fragment.

    :param np.ndarray mask: The image mask array (default=None). A 2D boolean array with
      the same shape as the frame. The tasks are generated only for those pixels for which
      the mask is True.
    """

    def __init__(self, mask: NDArray | None = None) -> None: ...
    @property
    def mask(self) -> NDArray[numpy.bool_]: ...
    @mask.setter
    def mask(self, value: NDArray) -> None: ...
    def generate_tasks(self, pixels: tuple[int, int]) -> list[tuple[int, int]]: ...

class MonoAdaptiveSampler2D(FrameSampler2D):
    """
    FrameSampler that dynamically adjusts a camera's pixel samples based on the noise
    level in each pixel's power value.

    Pixels that have high noise levels will receive extra samples until the desired
    noise threshold is achieve across the whole image.

    :param PowerPipeline2D pipeline: The specific power pipeline to use for feedback control.
    :param float fraction: The fraction of frame (or its masked fragment) pixels to receive
      extra sampling (default=0.2).
    :param float ratio: The maximum allowable ratio between the maximum and minimum number of
      samples obtained for the pixels of the same observer (default=10).
      The sampler will generate additional tasks for pixels with the least number of samples
      in order to keep this ratio below a given value.
    :param int min_samples: Minimum number of pixel samples across the image
      (or its masked fragment) before turning on adaptive sampling (default=1000).
    :param double cutoff: Normalised noise threshold at which extra sampling will be aborted and
      rendering will complete (default=0.0). The standard error is normalised to 1 so that a
      cutoff of 0.01 corresponds to 1% standard error.
    :param np.ndarray mask: The image mask array (default=None). A 2D boolean array with
      the same shape as the frame. The tasks are generated only for those pixels for which
      the mask is True. If not provided, the all-true mask will be created during the first call
      of generate_tasks().
    """

    def __init__(
        self,
        pipeline: PowerPipeline2D | RadiancePipeline2D,
        fraction: float = 0.2,
        ratio: float = 10.0,
        min_samples: int = 1000,
        cutoff: float = 0.0,
        mask: NDArray | None = None,
    ) -> None: ...
    @property
    def pipeline(self) -> PowerPipeline2D | RadiancePipeline2D: ...
    @pipeline.setter
    def pipeline(self, value: PowerPipeline2D | RadiancePipeline2D) -> None: ...
    @property
    def fraction(self) -> float: ...
    @fraction.setter
    def fraction(self, value: float) -> None: ...
    @property
    def ratio(self) -> float: ...
    @ratio.setter
    def ratio(self, value: float) -> None: ...
    @property
    def min_samples(self) -> int: ...
    @min_samples.setter
    def min_samples(self, value: int) -> None: ...
    @property
    def cutoff(self) -> float: ...
    @cutoff.setter
    def cutoff(self, value: float) -> None: ...
    @property
    def mask(self) -> NDArray[numpy.bool_]: ...
    @mask.setter
    def mask(self, value: NDArray) -> None: ...
    def generate_tasks(self, pixels: tuple[int, int]) -> list[tuple[int, int]]: ...
    def _full_frame(self, pixels: tuple[int, int]) -> list[tuple[int, int]]: ...

class SpectralAdaptiveSampler2D(FrameSampler2D):
    """
    FrameSampler that dynamically adjusts a camera's pixel samples based on the noise
    level in each pixel's power value.

    Pixels that have high noise levels will receive extra samples until the desired
    noise threshold is achieve across the whole image.

    :param SpectralPowerPipeline2D pipeline: The specific power pipeline to use for feedback control.
    :param float fraction: The fraction of frame (or its masked fragment) pixels to receive
      extra sampling (default=0.2).
    :param float ratio: The maximum allowable ratio between the maximum and minimum number of
      samples obtained for the pixels of the same observer (default=10).
      The sampler will generate additional tasks for pixels with the least number of samples
      in order to keep this ratio below a given value.
    :param int min_samples: Minimum number of pixel samples across the image
      (or its masked fragment) before turning on adaptive sampling (default=1000).
    :param double cutoff: Normalised noise threshold at which extra sampling will be aborted and
      rendering will complete (default=0.0). The standard error is normalised to 1 so that a
      cutoff of 0.01 corresponds to 1% standard error.
    :param str reduction_method: A method for obtaining spectral-average value of normalised
      error of a pixel from spectral array of errors (default='percentile').
       - `reduction_method='weighted'`: the error of a pixel is calculated as power-weighted
         average of the spectral errors,
       - `reduction_method='mean'`: the error of a pixel is calculated as a mean
         of the spectral errors excluding spectral bins with zero power,
       - `reduction_method='percentile'`: the error of a pixel is calculated as a user-defined
         percentile of the spectral errors excluding spectral bins with zero power.
       - `reduction_method='power_percentile'`: the error of a pixel is calculated as the highest
         spectral error among a given percentage of spectral bins with the highest spectral power.
    :param double percentile: Used only if `reduction_method='percentile'` or
      `reduction_method='power_percentile'` (default=100).
       - `reduction_method='percentile'`: If `percentile=x`, extra sampling will be aborted
         if x% of spectral bins of each pixel have normalised errors lower than `cutoff`.
       - `reduction_method='power_percentile'`: If `percentile=x`, extra sampling will be aborted
         if x% of spectral bins with the highest spectral power all have normalised errors lower
         than `cutoff`.
    """

    def __init__(
        self,
        pipeline: SpectralPowerPipeline2D | SpectralRadiancePipeline2D,
        fraction: float = 0.2,
        ratio: float = 10.0,
        min_samples: int = 1000,
        cutoff: float = 0.0,
        reduction_method: Literal["weighted", "mean", "percentile", "power_percentile"] = "percentile",
        percentile: float = 100.0,
        mask: NDArray | None = None,
    ) -> None: ...
    @property
    def pipeline(self) -> SpectralPowerPipeline2D | SpectralRadiancePipeline2D: ...
    @pipeline.setter
    def pipeline(self, value: SpectralPowerPipeline2D | SpectralRadiancePipeline2D) -> None: ...
    @property
    def fraction(self) -> float: ...
    @fraction.setter
    def fraction(self, value: float) -> None: ...
    @property
    def ratio(self) -> float: ...
    @ratio.setter
    def ratio(self, value: float) -> None: ...
    @property
    def min_samples(self) -> int: ...
    @min_samples.setter
    def min_samples(self, value: int) -> None: ...
    @property
    def cutoff(self) -> float: ...
    @cutoff.setter
    def cutoff(self, value: float) -> None: ...
    @property
    def reduction_method(self) -> str: ...
    @reduction_method.setter
    def reduction_method(self, value: Literal["weighted", "mean", "percentile", "power_percentile"]) -> None: ...
    @property
    def percentile(self) -> float: ...
    @percentile.setter
    def percentile(self, value: float) -> None: ...
    @property
    def mask(self) -> NDArray[numpy.bool_]: ...
    @mask.setter
    def mask(self, value: NDArray) -> None: ...
    def generate_tasks(self, pixels: tuple[int, int]) -> list[tuple[int, int]]: ...
    def _full_frame(self, pixels: tuple[int, int]) -> list[tuple[int, int]]: ...

class RGBAdaptiveSampler2D(FrameSampler2D):
    """
    FrameSampler that dynamically adjusts a camera's pixel samples based on the noise
    level in each RGB pixel value.

    Pixels that have high noise levels will receive extra samples until the desired
    noise threshold is achieve across the whole image.

    :param RGBPipeline2D pipeline: The specific RGB pipeline to use for feedback control.
    :param float fraction: The fraction of frame (or its masked fragment) pixels to receive
      extra sampling (default=0.2).
    :param float ratio: The maximum allowable ratio between the maximum and minimum number of
      samples obtained for the pixels of the same observer (default=10).
      The sampler will generate additional tasks for pixels with the least number of samples
      in order to keep this ratio below a given value.
    :param int min_samples: Minimum number of pixel samples across the image
      (or its masked fragment) before turning on adaptive sampling (default=1000).
    :param double cutoff: Noise threshold at which extra sampling will be aborted and
      rendering will complete (default=0.0).
    :param np.ndarray mask: The image mask array (default=None). A 2D boolean array with
      the same shape as the frame. The tasks are generated only for those pixels for which
      the mask is True. If not provided, the all-true mask will be created during the first call
      of generate_tasks().
    """

    def __init__(
        self,
        pipeline: RGBPipeline2D,
        fraction: float = 0.2,
        ratio: float = 10.0,
        min_samples: int = 1000,
        cutoff: float = 0.0,
        mask: NDArray | None = None,
    ) -> None: ...
    @property
    def pipeline(self) -> RGBPipeline2D: ...
    @pipeline.setter
    def pipeline(self, value: RGBPipeline2D) -> None: ...
    @property
    def fraction(self) -> float: ...
    @fraction.setter
    def fraction(self, value: float) -> None: ...
    @property
    def ratio(self) -> float: ...
    @ratio.setter
    def ratio(self, value: float) -> None: ...
    @property
    def min_samples(self) -> int: ...
    @min_samples.setter
    def min_samples(self, value: int) -> None: ...
    @property
    def cutoff(self) -> float: ...
    @cutoff.setter
    def cutoff(self, value: float) -> None: ...
    @property
    def mask(self) -> NDArray[numpy.bool_]: ...
    @mask.setter
    def mask(self, value: NDArray) -> None: ...
    def generate_tasks(self, pixels: tuple[int, int]) -> list[tuple[int, int]]: ...
    def _full_frame(self, pixels: tuple[int, int]) -> list[tuple[int, int]]: ...
