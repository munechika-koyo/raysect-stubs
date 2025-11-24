def seed(d: int | None = None) -> None:
    """
    Seeds the random number generator with the specified integer.

    If a seed is not specified the generator is automatically re-seed using the
    system cryptographic random number generator (urandom).

    :param int d: Integer seed.

    .. code-block:: pycon

        >>> from raysect.core.math.random import seed
        >>> seed(1)
    """

def uniform() -> float:
    """
    Generate random doubles in range [0, 1).

    Values are uniformly distributed.

    :returns: Random double.

    .. code-block:: pycon

        >>> from raysect.core.math.random import uniform
        >>>
        >>> uniform()
        0.7151068954493792
        >>> uniform()
        0.21476630242370853
    """

def normal(mean: float, stddev: float) -> float:
    """
    Generates a normally distributed random number.

    The mean and standard deviation of the distribution must be specified.

    :param float mean: The distribution mean.
    :param float stddev: The distribution standard deviation.
    :returns: Random double.

    .. code-block:: pycon

        >>> from raysect.core.math.random import normal
        >>>
        >>> normal(0, 1)
        0.5775399543387388
        >>> normal(0, 1)
        -2.247813575930409
    """

def probability(prob: float) -> bool:
    """
    Samples from the Bernoulli distribution where P(True) = prob.

    For example, if probability is 0.8, this function will return True 80% of
    the time and False 20% of the time.

    Values of prob outside the [0, 1] range of probabilities will be clamped to
    the nearest end of the range [0, 1].

    :param double prob: A probability from [0, 1].
    :return: True or False.
    :rtype: bool

    .. code-block:: pycon

        >>> from raysect.core.math.random import probability
        >>>
        >>> probability(0.8)
        True
        >>> probability(0.8)
        True
    """
