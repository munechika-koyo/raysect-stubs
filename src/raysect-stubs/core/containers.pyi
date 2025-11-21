from collections.abc import Iterable, Iterator

class _Item:
    """
    Internal item class for holding individual LinkedList items with references to neighbors.

    :param _Item previous: Reference to the previous container item, will be None if this is the first item.
    :param object value: The object to be stored as this item value.
    :param _Item next_item: Reference to the next container item, will be None if this is the last item.
    """

    previous: _Item
    value: object
    next_item: _Item | None

    def __init__(self, previous: _Item, value: object, next_item: _Item | None = None) -> None: ...

class LinkedList:
    """
    Basic implementation of a Linked List for fast container operations in cython.

    :param object initial_items: Optional iterable for initialising container.

    :ivar int length: number of items in the container
    :ivar first: starting element of container
    :ivar last: final element of container
    """

    length: int
    first: _Item | None
    last: _Item | None

    def __init__(self, initial_items: Iterable[object] | None = None) -> None: ...
    def __getitem__(self, item: int) -> object: ...
    def __iter__(self) -> Iterator[object] | None: ...
    def is_empty(self) -> bool:
        """Returns True if the container is empty."""
    def add(self, value: object) -> None:
        """Add an item to the end of the container.

        :param object value: The item to add to the end of the container.
        """
    def add_items(self, iterable: Iterable[object]) -> None:
        """Extend this container with another iterable container.

        :param object iterable: Iterable object such as a list or ndarray with
          which to extend this container.
        """
    def get_index(self, index: int) -> object:
        """
        Get the item from the container at specified index.

        :param int index: requested item index
        """
    def insert(self, value: object, index: int) -> None:
        """
        Insert an item at the specified index.

        :param object value: item to insert
        :param int index: index at which to insert this item
        """
    def remove(self, index: int) -> object:
        """
        Remove and return the specified item from the container.

        :param int index: Index at which an item will be removed.
        :return: The object at the specified index position.
        """

class Stack(LinkedList):
    """
    Basic implementation of a Stack container for fast container operations in cython.
    Inherits attributes and methods from LinkedList.
    """

    def push(self, value: object) -> None:
        """Adds an item to the top of the stack

        :param object value: Object that will be pushed to top of the stack
        """
    def pop(self) -> object:
        """Removes and returns the most recently added item from the stack

        :rtype: object
        """

class Queue(LinkedList):
    """
    Basic implementation of a Queue container for fast container operations in cython.
    Inherits attributes and methods from LinkedList.
    """

    def next_in_queue(self) -> object:
        """Returns the next object in the queue

        :rtype: object
        """
