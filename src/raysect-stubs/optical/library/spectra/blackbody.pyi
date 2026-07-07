from ...spectralfunction import NumericallyIntegratedSF, SpectralFunction

class BlackBody(NumericallyIntegratedSF):
    """
    Generates a black body radiation spectrum.

    Implements Planck's Law to generate a black body spectrum for the given
    body temperature. The temperature must be supplied in Kelvin.

    An optional emissivity spectral function may be supplied. This function
    should return a value in the range [0, 1]. Values outside this range will
    be clamped.

    Averages and integrals are calculated using numerical integration, the step
    size of this integration can be controlled by the user. The default step
    size in 1 nm.

    :param temperature: The temperature in Kelvin.
    :param emissivity: Emissivity function (default=ConstantSF(1.0)).
    :param scale: Scales the spectra (default=1.0).
    :param sample_resolution: Numerical integration step size (default=1nm).
    """

    temperature: float
    scale: float
    emissivity: SpectralFunction

    def __init__(
        self,
        temperature: float,
        emissivity: SpectralFunction | None = None,
        scale: float = 1.0,
        sample_resolution: float = 1.0,
    ) -> None: ...
    def function(self, wavelength: float) -> float:
        """
        Planck's Law.

        :param wavelength: Wavelength in nm.
        :return: Spectral radiance (W/m^2/str/nm).
        """
