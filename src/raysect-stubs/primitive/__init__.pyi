"""Primitive shapes type stubs."""

from typing import Any

from ..core.math import AffineMatrix3D
from ..core.scenegraph import Node, Primitive

class Sphere(Primitive):
    radius: float

    def __init__(
        self,
        radius: float = ...,
        parent: Node | None = ...,
        transform: AffineMatrix3D | None = ...,
        material: Any | None = ...,
        name: str | None = ...,
    ) -> None: ...

class Box(Primitive):
    lower: tuple[float, float, float]
    upper: tuple[float, float, float]

    def __init__(
        self,
        lower: tuple[float, float, float] = ...,
        upper: tuple[float, float, float] = ...,
        parent: Node | None = ...,
        transform: AffineMatrix3D | None = ...,
        material: Any | None = ...,
        name: str | None = ...,
    ) -> None: ...

class Cylinder(Primitive):
    radius: float
    height: float

    def __init__(
        self,
        radius: float = ...,
        height: float = ...,
        parent: Node | None = ...,
        transform: AffineMatrix3D | None = ...,
        material: Any | None = ...,
        name: str | None = ...,
    ) -> None: ...
