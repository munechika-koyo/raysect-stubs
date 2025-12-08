from numpy import float64, int32
from numpy.typing import NDArray

class StatsBin:
    """
    Class for storing a single numerical sampling result and its associated statistics.

    :ivar float mean: The mean value of the samples.
    :ivar float variance: The variance of the collected samples.
    :ivar int samples: The total number of samples in the set.
    """

    mean: float
    variance: float
    samples: int
    def __init__(self) -> None: ...
    def clear(self) -> None:
        """
        Erase the current statistics stored in this StatsBin.
        """
    def copy(self) -> StatsBin:
        """
        Instantiate a new StatsBin object with the same statistical results.
        """
    def add_sample(self, sample: float) -> None:
        """
        Add a single sample to this StatsBin.

        :param float sample: The sample value to be added.
        """
    def combine_samples(self, mean: float, variance: float, sample_count: int) -> None:
        """
        Combine the statistics from another set of samples with the results already stored in this StatsBin.

        :param float mean: The mean of the new samples
        :param float variance: The variance of the new samples
        :param int sample_count: The number of new samples that were taken.
        """
    def error(self) -> float:
        """
        Compute the standard error of this sample distribution.
        """

class StatsArray1D:
    """
    Class for storing a 1D array of sampling results and their associated statistics.

    :param int length: The length of the 1D samples array.

    :ivar ndarray mean: The mean value of the samples.
    :ivar ndarray variance: The variance of the collected samples.
    :ivar ndarray samples: The total number of samples in the set.
    :ivar int length: The length of the 1D samples array.
    """

    mean: NDArray[float64]
    variance: NDArray[float64]
    samples: NDArray[int32]
    length: int

    def __init__(self, length: int) -> None: ...
    @property
    def shape(self) -> tuple[int]:
        """
        The numpy style array shape of the underlying StatsArray.
        """
    def clear(self) -> None:
        """
        Erase the current statistics stored in this StatsArray.
        """
    def copy(self) -> StatsArray1D:
        """
        Instantiate a new StatsArray1D object with the same statistical results.
        """
    def add_sample(self, x: int, sample: float) -> None:
        """
        Add a single sample to the StatsArray1D element x.

        :param int x: The position index where the sample should be added.
        :param float sample: The sample value to be added.
        """
    def combine_samples(self, x: int, mean: float, variance: float, sample_count: int) -> None:
        """
        Combine the statistics from a given set of samples with the results already stored in
        this StatsArray at index position x.

        :param int x: The index position where these results are to be added.
        :param float mean: The mean of the new samples
        :param float variance: The variance of the new samples
        :param int sample_count: The number of new samples that were taken.
        """
    def error(self, x: int) -> float:
        """
        Compute the standard error of the results at index position x.

        :param int x: The index position at which to compute the standard error.
        """
    def errors(self) -> NDArray[float64]:
        """
        Compute the standard errors of all the results stored in this StatsArray.

        :rtype: ndarray
        """

class StatsArray2D:
    """
    Class for storing a 2D array of sampling results and their associated statistics.

    :param int nx: The number of array samples along the x direction.
    :param int ny: The number of array samples along the y direction.

    :ivar ndarray mean: The mean value of the samples.
    :ivar ndarray variance: The variance of the collected samples.
    :ivar ndarray samples: The total number of samples in the set.
    :ivar int nx: The number of array samples along the x direction.
    :ivar int ny: The number of array samples along the y direction.
    """

    mean: NDArray[float64]
    variance: NDArray[float64]
    samples: NDArray[int32]
    nx: int
    ny: int
    def __init__(self, nx: int, ny: int) -> None: ...
    @property
    def shape(self) -> tuple[int, int]:
        """
        The numpy style array shape of the underlying StatsArray.
        """
    def clear(self) -> None:
        """
        Erase the current statistics stored in this StatsArray.
        """
    def copy(self) -> StatsArray2D:
        """
        Instantiate a new StatsArray2D object with the same statistical results.
        """
    def add_sample(self, x: int, y: int, sample: float) -> None:
        """
        Add a single sample to the StatsArray2D results stored at element x, y.

        :param int x: The x position index where the sample should be added.
        :param int y: The y position index where the sample should be added.
        :param float sample: The sample value to be added.
        """
    def combine_samples(self, x: int, y: int, mean: float, variance: float, sample_count: int) -> None:
        """
        Combine the statistics from a given set of samples with the results already stored in
        this StatsArray at index position x, y.

        :param int x: The x index position where these results are to be added.
        :param int y: The y index position where these results are to be added.
        :param float mean: The mean of the new samples
        :param float variance: The variance of the new samples
        :param int sample_count: The number of new samples that were taken.
        """
    def error(self, x: int, y: int) -> float:
        """
        Compute the standard error of the results at index position x, y.

        :param int x: The x index position at which to compute the standard error.
        :param int y: The y index position at which to compute the standard error.
        """
    def errors(self) -> NDArray[float64]:
        """
        Compute the standard errors of all the results stored in this StatsArray.

        :rtype: ndarray
        """

class StatsArray3D:
    """
    Class for storing a 3D array of sampling results and their associated statistics.

    :param int nx: The number of array samples along the x direction.
    :param int ny: The number of array samples along the y direction.
    :param int nz: The number of array samples along the z direction.

    :ivar ndarray mean: The mean value of the samples.
    :ivar ndarray variance: The variance of the collected samples.
    :ivar ndarray samples: The total number of samples in the set.
    :ivar int nx: The number of array samples along the x direction.
    :ivar int ny: The number of array samples along the y direction.
    :ivar int nz: The number of array samples along the z direction.
    """

    mean: NDArray[float64]
    variance: NDArray[float64]
    samples: NDArray[int32]
    nx: int
    ny: int
    nz: int
    def __init__(self, nx: int, ny: int, nz: int) -> None: ...
    @property
    def shape(self) -> tuple[int, int, int]:
        """
        The numpy style array shape of the underlying StatsArray.
        """
    def clear(self) -> None:
        """
        Erase the current statistics stored in this StatsArray.
        """
    def copy(self) -> StatsArray3D:
        """
        Instantiate a new StatsArray3D object with the same statistical results.
        """
    def add_sample(self, x: int, y: int, z: int, sample: float) -> None:
        """
        Add a single sample to the StatsArray3D results stored at element x, y, z.

        :param int x: The x position index where the sample should be added.
        :param int y: The y position index where the sample should be added.
        :param int z: The z position index where the sample should be added.
        :param float sample: The sample value to be added.
        """
    def combine_samples(self, x: int, y: int, z: int, mean: float, variance: float, sample_count: int) -> None:
        """
        Combine the statistics from a given set of samples with the results already stored in
        this StatsArray at index position x, y, z.

        :param int x: The x index position where these results are to be added.
        :param int y: The y index position where these results are to be added.
        :param int z: The z index position where these results are to be added.
        :param float mean: The mean of the new samples
        :param float variance: The variance of the new samples
        :param int sample_count: The number of new samples that were taken.
        """
    def error(self, x: int, y: int, z: int) -> float:
        """
        Compute the standard error of the results at index position x, y, z.

        :param int x: The x index position at which to compute the standard error.
        :param int y: The y index position at which to compute the standard error.
        :param int z: The z index position at which to compute the standard error.
        """
    def errors(self) -> NDArray[float64]:
        """
        Compute the standard errors of all the results stored in this StatsArray.

        :rtype: ndarray
        """
