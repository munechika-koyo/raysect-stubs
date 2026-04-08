from ... import Spectrum

class PixelProcessor:
    """
    Base class for pixel processors.

    To optimally use computing resources, observers may use parallel processes
    to sample the world.

    Raysect observers launch multiple worker processes to sample the world, these
    processes send their results back to a single process that combines them into
    a frame.

    In order to distribute the processing of the returned spectra, it is
    necessary to perform the data processing on each worker.

    Each worker is given a pixel id and a number of spectral samples to collect
    for that pixel. The worker launches a ray to collect a sample and a spectrum is
    returned. When a spectrum is obtained, the worker calls add_sample() on each
    pixel processor associated with the pipelines attached to the observer. The pixel
    processor processes the spectrum and accumulates the results in its internal buffer.

    When the pixel samples are complete the worker calls pack_results() on each pixel
    processor. These results are sent back to the process handling the frame assembly.

    """

    def add_sample(self, spectrum: Spectrum, sensitivity: float) -> None:
        """
        Processes a spectrum and adds it to internal buffer.

        This is a virtual method and must be implemented in a sub class.

        :param Spectrum spectrum: The sampled spectrum.
        :param float sensitivity: The pixel sensitivity.
        """

    def pack_results(self) -> tuple:
        """
        Packs the contents of the internal buffer.

        This method must return a tuple. The contents and length of the tuple are entirely
        defined by the needs of the pipeline.

        This is a virtual method and must be implemented in a sub class.

        :rtype: tuple
        """
