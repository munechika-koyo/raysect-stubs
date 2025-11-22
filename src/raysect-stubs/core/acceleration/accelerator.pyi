from abc import abstractmethod

from ..intersection import Intersection
from ..math import Point3D
from ..ray import Ray
from ..scenegraph.primitive import Primitive

class Accelerator:
    @abstractmethod
    def build(self, primitives: list[Primitive]) -> None: ...
    @abstractmethod
    def hit(self, ray: Ray) -> Intersection | None: ...
    @abstractmethod
    def contains(self, point: Point3D) -> list[Primitive]: ...
