from abc import abstractmethod
from typing import Any

from ..math.affinematrix import AffineMatrix3D
from .signal import ChangeSignal

class _NodeBase:
    """
    The base class from which all scene-graph objects are derived.

    Defines the core attributes and common functionality of the scene-graph
    node objects.
    """

    _name: str | None
    _parent: _NodeBase | None
    children: list[_NodeBase]
    root: _NodeBase
    _transform: AffineMatrix3D
    _root_transform: AffineMatrix3D
    _root_transform_inverse: AffineMatrix3D
    _tract_modifications: bool

    meta: dict[Any, Any]

    def __init__(self, name: str | None = None) -> None: ...
    def __str__(self) -> str:
        """String representation."""
    def _check_parent(self, parent: _NodeBase) -> None:
        """
        Raises an exception if this node or its descendants are passed.

        The purpose of this function is to enforce the structure of the scene-
        graph. A scene-graph is logically a tree and so cannot contain cyclic
        references.
        """
    def _update(self) -> None:
        """
        Instructs the node to recalculate the root transforms for its section of
        the scene graph. Automatically registers/deregisters the node with the
        root node (if the methods are implemented). Propagates a reference to
        the root node through the tree.

        This method is called automatically when the scenegraph above this node
        changes or if the node transform or parent are modified. This method
        should never be called manually.
        """
    @abstractmethod
    def _register(self, node: _NodeBase) -> None:
        """
        When implemented by root nodes this method allows nodes in the
        scene-graph to register themselves with the root node for special
        handling.

        Virtual method call.

        For use in conjunction with _deregister()
        """
    @abstractmethod
    def _deregister(self, node: _NodeBase) -> None:
        """
        When implemented by root nodes this method allows nodes in the
        scene-graph to deregister themselves with the root node.

        Virtual method call.

        For use in conjunction with _register()
        """
    @abstractmethod
    def _change(self, node: _NodeBase, signal: ChangeSignal) -> None:
        """
        When implemented by root nodes this method allows nodes in the
        scene-graph to inform the root node of any change to scene-graph
        structure or to the nodes themselves.

        A ChangeSignal object specifying the nature of the change.

        Virtual method call.
        """
    @abstractmethod
    def _modified(self) -> None:
        """
        This method is called when a scene-graph change occurs that modifies
        the node's root transforms. This will occur if the node's transform is
        modified, a parent node's transform is modified or if the node's
        section of scene-graph is re-parented.

        Virtual method call.
        """
