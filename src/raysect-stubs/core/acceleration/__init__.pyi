"""Acceleration structures type stubs."""

from typing import Protocol

class Accelerator(Protocol):
    def build(self) -> None: ...

class KDTree:
    def __init__(self, max_depth: int = ..., min_items: int = ...) -> None: ...
    def build(self) -> None: ...
