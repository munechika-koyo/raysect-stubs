from abc import abstractmethod

import numpy as np
from numpy.typing import ArrayLike, NDArray

class SpectralFunction:
    """
    SpectralFunction abstract base class.

    A common interface for representing optical properties that are a function
    of wavelength. It provides methods for sampling, integrating and averaging
    a spectral function over specified wavelength ranges. The optical package
    uses SpectralFunctions to represent a number of different wavelength
    dependent optical properties, for example emission spectra, refractive
    indices and attenuation curves.

    Deriving classes must implement the integrate method.

    It is also recommended that subclasses implement __call__(). This should
    accept a single argument - wavelength - and return a single sample of the
    function at that wavelength. The units of wavelength are nanometers.

    A number of utility sub-classes exist to simplify SpectralFunction
    development.

    see also: NumericallyIntegratedSF, InterpolatedSF, ConstantSF, Spectrum
    """

    def __init__(self) -> None: ...
    def __call__(self, wavelength: float) -> float:
        """
        Evaluate the spectral function f(wavelength)

        :param float wavelength: Wavelength in nanometers.
        :rtype: float
        """

    @abstractmethod
    def evaluate(self, wavelength: float) -> float:
        """
        Evaluate the spectral function f(wavelength)

        :param float wavelength: Wavelength in nanometers.
        :rtype: float
        """

    @abstractmethod
    def integrate(self, min_wavelength: float, max_wavelength: float) -> float:
        """
        Calculates the integrated radiance over the specified spectral range.

        Virtual method, to be implemented in child classes.

        :param float min_wavelength: The minimum wavelength in nanometers
        :param float max_wavelength: The maximum wavelength in nanometers
        :return: Integrated radiance in W/m^2/str
        :rtype: float

        .. code-block:: pycon

            >>> spectrum = ray.trace(world)
            >>> spectrum.integrate(400, 700)
            328.50926129107023
        """

    def average(self, min_wavelength: float, max_wavelength: float) -> float:
        """
        Average radiance over the requested spectral range (W/m^2/sr/nm).

        Virtual method, to be implemented in child classes.

        :param float min_wavelength: lower wavelength for calculation
        :param float max_wavelength: upper wavelength for calculation
        :rtype: float

        .. code-block:: pycon

            >>> spectrum = ray.trace(world)
            >>> spectrum.average(400, 700)
            1.095030870970234
        """

    def sample(self, min_wavelength: float, max_wavelength: float, bins: int) -> NDArray[np.float64]:
        """
        Re-sample the spectral function with a new wavelength range and resolution.

        :param float min_wavelength: lower wavelength for calculation
        :param float max_wavelength: upper wavelength for calculation
        :param int bins: The number of spectral bins
        :rtype: ndarray

        .. code-block:: pycon

            >>> spectrum
            <raysect.optical.spectrum.Spectrum at 0x7f56c22bd8b8>
            >>> spectrum.min_wavelength, spectrum.max_wavelength
            (375.0, 785.0)
            >>> sub_spectrum = spectrum.sample(450, 550, 100)
        """

class NumericallyIntegratedSF(SpectralFunction):
    """
    Numerically integrates a supplied function.

    This abstract class provides an implementation of the integrate method that
    numerically integrates a supplied function (typically a non-integrable
    analytical function). The function to numerically integrate is supplied by
    sub-classing this class and implementing the function() method.

    The function is numerically sampled at regular intervals. A sampling
    resolution may be specified in the class constructor (default: 1 sample/nm).

    :param double sample_resolution: The numerical sampling resolution in nanometers.
    """

    sample_resolution: float

    def __init__(self, sample_resolution: float = 1.0) -> None: ...
    def evaluate(self, wavelength: float) -> float:
        """
        Evaluate the spectral function f(wavelength)

        :param float wavelength: Wavelength in nanometers.
        :rtype: float
        """

    def integrate(self, min_wavelength: float, max_wavelength: float) -> float:
        """
        Calculates the integrated radiance over the specified spectral range.

        :param float min_wavelength: The minimum wavelength in nanometers
        :param float max_wavelength: The maximum wavelength in nanometers
        :return: Integrated radiance in W/m^2/str
        :rtype: float
        """

    @abstractmethod
    def function(self, wavelength: float) -> float:
        """
        Function to numerically integrate.

        This is a virtual method and must be implemented through sub-classing.

        :param double wavelength: Wavelength in nanometers.
        :return: Function value at the specified wavelength.
        """

class InterpolatedSF(SpectralFunction):
    """
    Linearly interpolated spectral function.

    Spectral function defined by samples of regular or irregular spacing, ends
    are extrapolated. You must set the ends to zero if you want the function to
    go to zero at the edges!

    wavelengths and samples will be sorted during initialisation.

    If normalise is set to True the data is rescaled so the integrated area
    of the spectral function over the full range of the input data is
    normalised to 1.0.

    :param object wavelengths: 1D array of wavelengths in nanometers.
    :param object samples: 1D array of spectral samples.
    :param bool normalise: True/false toggle for whether to normalise the
      spectral function so its integral equals 1.

    .. code-block:: pycon

        >>> from raysect.optical import InterpolatedSF
        >>>
        >>> # defining a set of spectral filters
        >>> filter_red = InterpolatedSF([100, 650, 660, 670, 680, 800], [0, 0, 1, 1, 0, 0])
        >>> filter_green = InterpolatedSF([100, 530, 540, 550, 560, 800], [0, 0, 1, 1, 0, 0])
        >>> filter_blue = InterpolatedSF([100, 480, 490, 500, 510, 800], [0, 0, 1, 1, 0, 0])
    """

    def __init__(
        self,
        wavelengths: ArrayLike,
        samples: ArrayLike,
        normalise: bool = False,
    ) -> None: ...
    def evaluate(self, wavelength: float) -> float:
        """
        Evaluate the spectral function f(wavelength)

        :param float wavelength: Wavelength in nanometers.
        :rtype: float
        """

    def integrate(self, min_wavelength: float, max_wavelength: float) -> float:
        """
        Calculates the integrated radiance over the specified spectral range.

        :param float min_wavelength: The minimum wavelength in nanometers
        :param float max_wavelength: The maximum wavelength in nanometers
        :return: Integrated radiance in W/m^2/str
        :rtype: float
        """

class ConstantSF(SpectralFunction):
    """
    Constant value spectral function

    :param float value: Constant radiance value

    .. code-block:: pycon

        >>> from raysect.optical import ConstantSF
        >>>
        >>> unity_spectral_function = ConstantSF(1.0)
    """

    value: float

    def __init__(self, value: float) -> None: ...
    def evaluate(self, wavelength: float) -> float:
        """
        Evaluate the spectral function f(wavelength)

        :param float wavelength: Wavelength in nanometers.
        :rtype: float
        """

    def integrate(self, min_wavelength: float, max_wavelength: float) -> float:
        """
        Calculates the integrated radiance over the specified spectral range.

        :param float min_wavelength: The minimum wavelength in nanometers
        :param float max_wavelength: The maximum wavelength in nanometers
        :return: Integrated radiance in W/m^2/str
        :rtype: float
        """

    def average(self, min_wavelength: float, max_wavelength: float) -> float:
        """
        Average radiance over the requested spectral range (W/m^2/sr/nm).

        :param float min_wavelength: lower wavelength for calculation
        :param float max_wavelength: upper wavelength for calculation
        :rtype: float
        """

    def sample(self, min_wavelength: float, max_wavelength: float, bins: int) -> NDArray[np.float64]:
        """
        Re-sample the spectral function with a new wavelength range and resolution.

        :param float min_wavelength: lower wavelength for calculation
        :param float max_wavelength: upper wavelength for calculation
        :param int bins: The number of spectral bins
        :rtype: ndarray
        """
