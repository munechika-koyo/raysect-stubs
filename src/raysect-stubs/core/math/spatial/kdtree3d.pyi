from abc import abstractmethod
from typing import BinaryIO

from _typeshed import StrOrBytesPath

from ...boundingbox import BoundingBox3D
from ...ray import Ray
from ..point import Point3D

class Item3D:
    """
    Item3D class. Represents an item to place into the kd-tree.

    The id should be a unique integer value identifying an external object.
    For example the id could be the index into an array of polygon objects.
    The id values are stored in the kd-tree and returned by the hit() or
    contains() methods.

    A bounding box associated with the item defines the spatial extent of the
    item along each axis. This data is used to place the items in the tree.

    :param id: An integer item id.
    :param box: A BoundingBox3D object defining the item's spatial extent.
    """

    id: int
    box: BoundingBox3D
    def __init__(self, id: int, box: BoundingBox3D) -> None: ...

class KDTree3DCore:
    """
    Implements a 3D kd-tree for items with finite extents.

    This is a Cython abstract base class. It cannot be directly extended in
    Python due to the need to implement cdef methods _items_containing_leaf() and
     _trace_leaf(). Use the KDTree3D wrapper class if extending from Python.

    :param items: A list of Items.
    :param max_depth: The maximum tree depth (automatic if set to 0, default is 0).
    :param min_items: The item count threshold for forcing creation of a new leaf node (default 1).
    :param hit_cost: The relative computational cost of item hit evaluations vs kd-tree traversal (default 20.0).
    :param empty_bonus: The bonus applied to node splits that generate empty leaves (default 0.2).
    """

    bounds: BoundingBox3D
    def __init__(self, items: list[Item3D], max_depth: int = 0, min_items: int = 1, hit_cost: float = 20.0, empty_bonus: float = 0.2) -> None: ...
    def is_contained(self, point: Point3D) -> bool:
        """
        Traverses the kd-Tree to identify if the point is contained by an any item.

        :param point: A Point3D object.
        :return: True if the point lies inside an item, false otherwise.
        """
    def trace(self, ray: Ray) -> bool:
        """
        Traverses the kd-Tree to find the first intersection with an item stored in the tree.

        This method returns True is an item is hit and False otherwise.

        :param ray: A Ray object.
        :return: True is an intersection occurs, false otherwise.
        """
    def items_containing(self, point: Point3D) -> list[int]:
        """
        Starts contains traversal of the kd-Tree.
        Traverses the kd-Tree to find the items that contain the specified point.

        :param point: A Point3D object.
        :return: A list of ids (indices) of the items containing the point
        """
    def __dealloc__(self) -> None:
        """
        Frees the memory allocated to store the kd-Tree.
        """
    def save(self, file: BinaryIO | StrOrBytesPath) -> None: ...
    def load(self, file: BinaryIO | StrOrBytesPath) -> None: ...

class KDTree3D(KDTree3DCore):
    """
    Implements a 3D kd-tree for items with finite extents.

    This class cannot be used directly, it must be sub-classed. One or both of
    _trace_item() and _items_containing_item() must be implemented.

    :param items: A list of Items.
    :param max_depth: The maximum tree depth (automatic if set to 0, default is 0).
    :param min_items: The item count threshold for forcing creation of a new leaf node (default 1).
    :param hit_cost: The relative computational cost of item hit evaluations vs kd-tree traversal (default 20.0).
    :param empty_bonus: The bonus applied to node splits that generate empty leaves (default 0.2).
    """
    @abstractmethod
    def _trace_items(self, item_ids: list[int], ray: Ray, max_range: float) -> bool:
        """
        Tests each item to identify if an intersection occurs.

        This is a virtual method and must be implemented in a derived class if
        ray intersections are to be identified. This method must return True
        if an intersection is found and False otherwise.

        Derived classes may need to return information about the intersection.
        This can be done by setting object attributes prior to returning True.
        The kd-Tree search algorithm stops as soon as the first leaf is
        identified that contains an intersection. Any attributes set when
        _trace_items() returns True are guaranteed not to be further modified.

        :param item_ids: List of item ids.
        :param ray: Ray object.
        :param max_range: The maximum intersection search range.
        :return: True is a hit occurs, false otherwise.
        """
    @abstractmethod
    def _items_containing_items(self, item_ids: list[int], point: Point3D) -> list[int]:
        """
        Tests each item in the list to identify if they enclose the point.

        This is a virtual method and must be implemented in a derived class if
        the identification of items enclosing a point is required. This method
        must return a list of ids for the items that enclose the point. If no
        items enclose the point, an empty list must be returned.

        Derived classes may need to wish to return additional information about
        the enclosing items. This can be done by setting object attributes
        prior to returning the list. Any attributes set when
        _items_containing_items() returns are guaranteed not to be further
        modified.

        :param item_ids: List of item ids.
        :param point: Point3D to evaluate.
        :return: List of ids of the items containing the point.
        """
