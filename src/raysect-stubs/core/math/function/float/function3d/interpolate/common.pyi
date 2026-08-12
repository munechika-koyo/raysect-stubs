from numpy.typing import ArrayLike

from .....point import Point3D
from .....spatial.kdtree3d import KDTree3DCore

class MeshKDTree3D(KDTree3DCore):
    def __init__(self, vertices: ArrayLike, tetrahedra: ArrayLike) -> None: ...
    def is_contained(self, point: Point3D) -> bool: ...
