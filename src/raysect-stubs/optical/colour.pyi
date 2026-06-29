import numpy as np
from numpy.typing import NDArray

from .spectralfunction import InterpolatedSF
from .spectrum import Spectrum

ciexyz_wavelength_samples: NDArray[np.float64]
ciexyz_y_samples: NDArray[np.float64]
ciexyz_x_samples: NDArray[np.float64]
ciexyz_z_samples: NDArray[np.float64]
ciexyz_x: InterpolatedSF
ciexyz_y: InterpolatedSF
ciexyz_z: InterpolatedSF
d65_wavelength_samples: NDArray[np.float64]
d65_white_samples: NDArray[np.float64]
d65_white: InterpolatedSF

def resample_ciexyz(min_wavelength: float, max_wavelength: float, bins: int) -> NDArray[np.float64]:
    """
    Pre-calculates samples of XYZ sensitivity curves over desired spectral range.

    Returns ndarray of shape [N, 3] where the last dimension (0, 1, 2) corresponds
    to (X, Y, Z).

    :param float min_wavelength: Lower wavelength bound on spectrum
    :param float max_wavelength: Upper wavelength bound on spectrum
    :param int bins: Number of spectral bins in spectrum
    :rtype: memoryview
    """

def spectrum_to_ciexyz(spectrum: Spectrum, resampled_xyz: memoryview | None = None) -> tuple[float, float, float]:
    """
    Calculates a tuple of CIE X, Y, Z values from an input spectrum

    :param Spectrum spectrum: Spectrum to process
    :param memoryview resampled_xyz: Pre-calculated XYZ sensitivity curves optimised
      for this spectral range (default=None).
    :rtype: tuple
    """

def ciexyy_to_ciexyz(cx: float, cy: float, Y: float) -> tuple[float, float, float]:
    """
    Performs conversion from CIE xyY to CIE XYZ colour space

    Returns a tuple of (X, Y, Z)

    :param float cx: chromaticity x
    :param float cy: chromaticity y
    :param float y: tristimulus Y
    :rtype: tuple
    """

def ciexyz_to_ciexyy(x: float, y: float, z: float) -> tuple[float, float, float]:
    """
    Performs conversion from CIE XYZ to CIE xyY colour space

    Returns a tuple of (cx, cy, Y)

    :param float x: tristimulus X
    :param float y: tristimulus y
    :param float z: tristimulus Z
    :rtype: tuple
    """

def ciexyz_to_srgb(x: float, y: float, z: float) -> tuple[float, float, float]:
    """
    Convert CIE XYZ values to sRGB colour space.

    x, y, z in range [0, 1]
    r, g, b in range [0, 1]

    :param float x: tristimulus X
    :param float y: tristimulus y
    :param float z: tristimulus Z
    :rtype: tuple
    """

def srgb_to_ciexyz(r: float, g: float, b: float) -> tuple[float, float, float]:
    """
    Convert sRGB values to CIE XYZ colour space.

    r, g, b in range [0, 1]
    x, y, z in range [0, 1]

    :param float r: Red value
    :param float g: Green value
    :param float b: Blue value
    :rtype: tuple
    """
