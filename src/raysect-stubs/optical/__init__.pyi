"""Optical module type stubs."""

from typing import Any, TypeAlias

from ..core.math import Point3D, Vector3D

Wavelength: TypeAlias = float
Power: TypeAlias = float
RadiantPower: TypeAlias = float

class Spectrum:
    def __init__(self, wavelengths: Any = ..., values: Any = ...) -> None: ...
    def sample(self, wavelength: Wavelength) -> float: ...
    def integrate(
        self, min_wavelength: Wavelength = ..., max_wavelength: Wavelength = ...
    ) -> float: ...

class Ray:
    origin: Point3D
    direction: Vector3D
    min_wavelength: Wavelength
    max_wavelength: Wavelength

    def __init__(
        self,
        origin: Point3D = ...,
        direction: Vector3D = ...,
        min_wavelength: Wavelength = ...,
        max_wavelength: Wavelength = ...,
    ) -> None: ...

class SpectralFunction:
    def __call__(self, wavelength: Wavelength) -> float: ...
