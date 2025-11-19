"""Scenegraph module type stubs."""

from typing import Any

from ..math import AffineMatrix3D, Point3D, Vector3D

class Node:
    name: str | None
    parent: Node | None
    children: list[Node]
    transform: AffineMatrix3D

    def __init__(
        self,
        parent: Node | None = ...,
        transform: AffineMatrix3D | None = ...,
        name: str | None = ...,
    ) -> None: ...
    def add_child(self, child: Node) -> None: ...
    def remove_child(self, child: Node) -> None: ...

class World(Node):
    def __init__(self, name: str | None = ...) -> None: ...

class Primitive(Node):
    def __init__(
        self,
        parent: Node | None = ...,
        transform: AffineMatrix3D | None = ...,
        material: Any | None = ...,
        name: str | None = ...,
    ) -> None: ...
