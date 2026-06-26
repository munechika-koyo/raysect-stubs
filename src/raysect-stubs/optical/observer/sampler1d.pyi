from typing import Literal

from .base.sampler import FrameSampler1D
from .pipeline.mono import PowerPipeline1D, RadiancePipeline1D
from .pipeline.spectral import SpectralPowerPipeline1D, SpectralRadiancePipeline1D

class FullFrameSampler1D(FrameSampler1D):
    def generate_tasks(self, pixels: int) -> list[tuple[int]]: ...

class MonoAdaptiveSampler1D(FrameSampler1D):
    """
    FrameSampler that dynamically adjusts a camera's pixel samples based on the noise
    level in each pixel's power value.

    Pixels that have high noise levels will receive extra samples until the desired
    noise threshold is achieve across the whole image.

    :param PowerPipeline1D pipeline: The specific power pipeline to use for feedback control.
    :param float fraction: The fraction of frame pixels to receive extra sampling
      (default=0.2).
    :param float ratio: The maximum allowable ratio between the maximum and minimum number of
      samples obtained for the pixels of the same observer (default=10).
      The sampler will generate additional tasks for pixels with the least number of samples
      in order to keep this ratio below a given value.
    :param int min_samples: Minimum number of pixel samples across the image before
      turning on adaptive sampling (default=1000).
    :param double cutoff: Normalised noise threshold at which extra sampling will be aborted and
      rendering will complete (default=0.0). The standard error is normalised to 1 so that a
      cutoff of 0.01 corresponds to 1% standard error.
    """

    def __init__(
        self,
        pipeline: PowerPipeline1D | RadiancePipeline1D,
        fraction: float = 0.2,
        ratio: float = 10.0,
        min_samples: int = 1000,
        cutoff: float = 0.0,
    ): ...
    @property
    def pipeline(self) -> PowerPipeline1D | RadiancePipeline1D: ...
    @pipeline.setter
    def pipeline(self, value: PowerPipeline1D | RadiancePipeline1D) -> None: ...
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
    def generate_tasks(self, pixels: int) -> list[tuple[int]]: ...
    def _full_frame(self, pixels: int) -> list[tuple[int]]: ...

class SpectralAdaptiveSampler1D(FrameSampler1D):
    """
    FrameSampler that dynamically adjusts a camera's pixel samples based on the noise
    level in each pixel's power value.

    Pixels that have high noise levels will receive extra samples until the desired
    noise threshold is achieve across the whole image.

    :param SpectralPowerPipeline1D pipeline: The specific spectral power pipeline to use
      for feedback control.
    :param float fraction: The fraction of frame pixels to receive extra sampling
      (default=0.2).
    :param float ratio: The maximum allowable ratio between the maximum and minimum number of
      samples obtained for the pixels of the same observer (default=10).
      The sampler will generate additional tasks for pixels with the least number of samples
      in order to keep this ratio below a given value.
    :param int min_samples: Minimum number of pixel samples across the image before
      turning on adaptive sampling (default=1000).
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
        pipeline: SpectralPowerPipeline1D | SpectralRadiancePipeline1D,
        fraction: float = 0.2,
        ratio: float = 10.0,
        min_samples: int = 1000,
        cutoff: float = 0.0,
        reduction_method: Literal["weighted", "mean", "percentile", "power_percentile"] = "percentile",
        percentile: float = 100.0,
    ) -> None: ...
    @property
    def pipeline(self) -> SpectralPowerPipeline1D | SpectralRadiancePipeline1D: ...
    @pipeline.setter
    def pipeline(self, value: SpectralPowerPipeline1D | SpectralRadiancePipeline1D) -> None: ...
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
    def generate_tasks(self, pixels: int) -> list[tuple[int]]: ...
    def _full_frame(self, pixels: int) -> list[tuple[int]]: ...
