class SpectralSlice:
    offset: int
    bins: int
    total_bins: int
    min_wavelength: float
    max_wavelength: float
    total_min_wavelength: float
    total_max_wavelength: float

    def __init__(
        self,
        min_wavelength: float,
        max_wavelength: float,
        bins: int,
        slice_bins: int,
        slice_offset: int,
    ) -> None: ...
