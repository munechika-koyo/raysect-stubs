from numpy.typing import ArrayLike

from .....point import Point2D
from .....spatial.kdtree2d import KDTree2DCore

class MeshKDTree2D(KDTree2DCore):
    def __init__(self, vertices: ArrayLike, triangles: ArrayLike) -> None: ...
    def is_contained(self, point: Point2D) -> bool:
        """
        Traverses the kd-Tree to identify if the point is contained by an item.
        :param Point2D point: A Point2D object.
        :return: True if the point lies inside an item, false otherwise.
        """
