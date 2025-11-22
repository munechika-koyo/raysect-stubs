from ..acceleration.accelerator import Accelerator
from ..intersection import Intersection
from ..math import Point3D
from ..math.spatial.kdtree3d import KDTree3DCore
from ..ray import Ray
from ..scenegraph.primitive import Primitive

class _PrimitiveKDTree(KDTree3DCore):
    def __init__(self, primitives: list[Primitive], max_depth: int = 0, min_items: int = 1, hit_cost: float = 80.0, empty_bonus: float = 0.2) -> None: ...

class KDTree(Accelerator):
    _kdtree: _PrimitiveKDTree
    def build(self, primitives: list[Primitive]) -> None: ...
    def hit(self, ray: Ray) -> Intersection | None: ...
    def contains(self, point: Point3D) -> list[Primitive]: ...
