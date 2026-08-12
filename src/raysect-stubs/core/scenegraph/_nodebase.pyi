from typing import Any

from .signal import ChangeSignal

class _NodeBase:
    """
    The base class from which all scene-graph objects are derived.

    Defines the core attributes and common functionality of the scene-graph
    node objects.
    """

    children: list[_NodeBase]
    root: _NodeBase
    meta: dict[Any, Any]

    def __init__(self, name: str | None = None) -> None: ...
    def __str__(self) -> str:
        """String representation."""
    def _register(self, node: _NodeBase) -> None:
        """
        When implemented by root nodes this method allows nodes in the
        scene-graph to register themselves with the root node for special
        handling.

        Virtual method call.

        For use in conjunction with _deregister()
        """
    def _deregister(self, node: _NodeBase) -> None:
        """
        When implemented by root nodes this method allows nodes in the
        scene-graph to deregister themselves with the root node.

        Virtual method call.

        For use in conjunction with _register()
        """
    def _change(self, node: _NodeBase, change: ChangeSignal) -> None:
        """
        When implemented by root nodes this method allows nodes in the
        scene-graph to inform the root node of any change to scene-graph
        structure or to the nodes themselves.

        A ChangeSignal object specifying the nature of the change.

        Virtual method call.
        """
    def _modified(self) -> None:
        """
        This method is called when a scene-graph change occurs that modifies
        the node's root transforms. This will occur if the node's transform is
        modified, a parent node's transform is modified or if the node's
        section of scene-graph is re-parented.

        Virtual method call.
        """
