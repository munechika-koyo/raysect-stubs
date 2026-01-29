import numpy as np
from numpy.typing import NDArray

from .spectralfunction import SpectralFunction

class Spectrum(SpectralFunction):
    """
    A class for working with spectra.

    Describes the distribution of light at each wavelength in units of radiance (W/m^2/str/nm).
    Spectral samples are regularly spaced over the wavelength range and lie in the centre of
    the wavelength bins.

    :param float min_wavelength: Lower wavelength bound for this spectrum
    :param float max_wavelength: Upper wavelength bound for this spectrum
    :param int bins: Number of samples to use over the spectral range

    .. code-block:: pycon

        >>> from raysect.optical import Spectrum
        >>>
        >>> spectrum = Spectrum(400, 720, 250)
    """

    min_wavelength: float
    max_wavelength: float
    bins: int
    delta_wavelength: float
    samples: NDArray[np.float64]

    def __init__(self, min_wavelength: float, max_wavelength: float, bins: int) -> None: ...
    @property
    def wavelengths(self) -> NDArray[np.float64]:
        """
        Wavelength array in nm

        :rtype: ndarray
        """

    def __len__(self) -> int:
        """
        The number of spectral bins

        :rtype: int
        """

    def is_compatible(self, min_wavelength: float, max_wavelength: float, bins: int) -> bool:
        """
        Returns True if the stored samples are consistent with the specified
        wavelength range and sample size.

        :param float min_wavelength: The minimum wavelength in nanometers
        :param float max_wavelength: The maximum wavelength in nanometers
        :param int bins: The number of bins.
        :return: True if the samples are compatible with the range/samples, False otherwise.
        :rtype: boolean
        """

    def average(self, min_wavelength: float, max_wavelength: float) -> float:
        """
        Finds the average number of spectral samples over the specified wavelength range.

        :param float min_wavelength: The minimum wavelength in nanometers
        :param float max_wavelength: The maximum wavelength in nanometers
        :return: Average radiance in W/m^2/str/nm
        :rtype: float

        .. code-block:: pycon

            >>> spectrum = ray.trace(world)
            >>> spectrum.average(400, 700)
            1.095030870970234
        """

    def integrate(self, min_wavelength: float, max_wavelength: float) -> float:
        """
        Calculates the integrated radiance over the specified spectral range.

        :param float min_wavelength: The minimum wavelength in nanometers
        :param float max_wavelength: The maximum wavelength in nanometers
        :return: Integrated radiance in W/m^2/str
        :rtype: float

        .. code-block:: pycon

            >>> spectrum = ray.trace(world)
            >>> spectrum.integrate(400, 700)
            328.50926129107023
        """

    def sample(self, min_wavelength: float, max_wavelength: float, bins: int) -> NDArray[np.float64]:
        """
        Re-sample this spectrum over a new spectral range.

        :param float min_wavelength: The minimum wavelength in nanometers
        :param float max_wavelength: The maximum wavelength in nanometers
        :param int bins: The number of spectral bins.
        :rtype: ndarray

        .. code-block:: pycon

            >>> spectrum
            <raysect.optical.spectrum.Spectrum at 0x7f56c22bd8b8>
            >>> spectrum.min_wavelength, spectrum.max_wavelength
            (375.0, 785.0)
            >>> sub_spectrum = spectrum.sample(450, 550, 100)
        """

    def is_zero(self) -> bool:
        """
        Can be used to determine if all the samples are zero.

        True if the spectrum is zero, False otherwise.

        :rtype: bool

        .. code-block:: pycon

            >>> spectrum = ray.trace(world)
            >>> spectrum.is_zero()
            False
        """

    def total(self) -> float:
        """
        Calculates the total radiance integrated over the whole spectral range.

        Returns radiance in W/m^2/str

        :rtype: float

        .. code-block:: pycon

            >>> spectrum = ray.trace(world)
            >>> spectrum.total()
            416.6978223103715
        """

    def to_photons(self) -> NDArray[np.float64]:
        """
        Converts the spectrum sample array from radiance W/m^2/str/nm to Photons/s/m^2/str/nm
        and returns the data in a numpy array.

        :rtype: ndarray

        .. code-block:: pycon

            >>> spectrum = ray.trace(world)
            >>> spectrum.to_photons()
            array([2.30744985e+17, 3.12842916e+17, ...])
        """

    def clear(self) -> None:
        """
        Resets the sample values in the spectrum to zero.
        """

    def new_spectrum(self, *args, **kwargs) -> Spectrum:
        """
        Returns a new Spectrum compatible with the same spectral settings.

        :rtype: Spectrum
        """

    def copy(self) -> Spectrum:
        """
        Returns a copy of the spectrum.

        :rtype: Spectrum
        """

def photon_energy(wavelength: float) -> float:
    """
    Returns the energy of a photon with the specified wavelength.

    :param float wavelength: Photon wavelength in nanometers.
    :return: Photon energy in Joules.
    :rtype: float
    """
