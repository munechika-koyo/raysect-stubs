from abc import abstractmethod
from typing import BinaryIO

from _typeshed import StrOrBytesPath

from ...boundingbox import BoundingBox2D
from ...math import Point2D

class Item2D:
    """
    Item2D class. Represents an item to place into the kd-tree.

    The id should be a unique integer value identifying an external object.
    For example the id could be the index into an array of polygon objects.
    The id values are stored in the kd-tree and returned by the hit() or
    contains() methods.

    A bounding box associated with the item defines the spatial extent of the
    item along each axis. This data is used to place the items in the tree.

    :param id: An integer item id.
    :param box: A BoundingBox2D object defining the item's spatial extent.
    """

    id: int
    box: BoundingBox2D
    def __init__(self, id: int, box: BoundingBox2D) -> None: ...

class KDTree2DCore:
    """
    Implements a 2D kd-tree for items with finite extents.

    This is a Cython abstract base class. It cannot be directly extended in
    Python due to the need to implement cdef methods _contains_leaf() and
     _hit_leaf(). Use the KDTree2D wrapper class if extending from Python.

    :param list items: A list of Items.
    :param int max_depth: The maximum tree depth (automatic if set to 0, default is 0).
    :param int min_items: The item count threshold for forcing creation of a new leaf node (default 1).
    :param double hit_cost: The relative computational cost of item hit evaluations vs kd-tree traversal (default 20.0).
    :param double empty_bonus: The bonus applied to node splits that generate empty leaves (default 0.2).
    """

    bounds: BoundingBox2D
    def __init__(self, items: list[Item2D], max_depth: int = 0, min_items: int = 1, hit_cost: float = 20.0, empty_bonux: float = 0.2) -> None: ...
    def is_contained(self, point: Point2D) -> bool:
        """
        Traverses the kd-Tree to identify if the point is contained by an any item.

        :param point: A Point2D object.
        :return: True if the point lies inside an item, false otherwise.
        """
    def items_containing(self, point: Point2D) -> list[int]:
        """
        Traverses the kd-Tree to find the items that contain the specified point.

        :param point: A Point2D object.
        :return: A list of ids (indices) of the items containing the point
        """
    def __dealloc__(self) -> None:
        """
        Frees the memory allocated to store the kd-Tree.
        """
    def save(self, file: BinaryIO | StrOrBytesPath) -> None: ...
    def load(self, file: BinaryIO | StrOrBytesPath) -> None: ...

class KDTree2D(KDTree2DCore):
    """
    Implements a 2D kd-tree for items with finite extents.

    This class cannot be used directly, it must be sub-classed. One or both of
    _hit_item() and _contains_item() must be implemented.

    :param list items: A list of Items.
    :param int max_depth: The maximum tree depth (automatic if set to 0, default is 0).
    :param int min_items: The item count threshold for forcing creation of a new leaf node (default 1).
    :param double hit_cost: The relative computational cost of item hit evaluations vs kd-tree traversal (default 20.0).
    :param double empty_bonus: The bonus applied to node splits that generate empty leaves (default 0.2).
    """

    @abstractmethod
    def _is_contained_items(self, item_ids: list[int], point: Point2D) -> bool:
        """
        Tests each item in the list to identify if any enclose the point.

        This is a virtual method and must be implemented in a derived class if
        the identification of an item enclosing a point is required. This method
        must return True is the point lies inside an item or False otherwise.

        Derived classes may need to wish to return additional information about
        the enclosing item(s). This can be done by setting object attributes
        prior to returning. Any attributes set when _hit_items() returns are
        guaranteed not to be further modified.

        :param item_ids: List of item ids.
        :param point: Point2D to evaluate.
        :return: True if the point lies inside an item, false otherwise.
        """
    @abstractmethod
    def _items_containing_items(self, item_ids: list[int], point: Point2D) -> list[int]:
        """
        Tests each item in the list to identify if they enclose the point.

        This is a virtual method and must be implemented in a derived class if
        the identification of items enclosing a point is required. This method
        must return a list of ids for the items that enclose the point. If no
        items enclose the point, an empty list must be returned.

        Derived classes may need to wish to return additional information about
        the enclosing items. This can be done by setting object attributes
        prior to returning the list. Any attributes set when _contains_items()
        returns are guaranteed not to be further modified.

        :param item_ids: List of item ids.
        :param point: Point2D to evaluate.
        :return: List of ids of the items containing the point.
        """
