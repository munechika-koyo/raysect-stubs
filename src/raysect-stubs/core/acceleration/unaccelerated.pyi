from ..boundingbox import BoundingBox3D
from ..intersection import Intersection
from ..math import Point3D
from ..ray import Ray
from ..scenegraph.primitive import Primitive
from .accelerator import Accelerator
from .boundprimitive import BoundPrimitive

class Unaccelerated(Accelerator):
    primitives: list[BoundPrimitive]
    world_box: BoundingBox3D
    def __init__(self) -> None: ...
    def build(self, primitives: list[Primitive]) -> None: ...
    def hit(self, ray: Ray) -> Intersection | None: ...
    def contains(self, point: Point3D) -> list[Primitive]: ...
