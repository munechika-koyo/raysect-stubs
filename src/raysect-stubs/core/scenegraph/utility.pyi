from ._nodebase import _NodeBase  # pyright: ignore[reportPrivateUsage]
from .node import Node
from .signal import ChangeSignal

class BridgeNode(Node):
    destination: _NodeBase
    """
    Specialised scene-graph root node that propagates geometry notifications.
    """
    def __init__(self, destination: _NodeBase) -> None: ...
    def _change(self, node: _NodeBase, signal: ChangeSignal) -> None:
        """
        Handles a scene-graph node change handler.

        Propagates change notifications to the specified node and it's
        scene-graph.
        """

def print_scenegraph(node: _NodeBase) -> None:
    """
    Pretty-prints a scene-graph.

    This function will print the scene-graph that contains the specified node.
    The specified node will be highlighted in the tree by post-fixing the node
    with the string: "[referring node]".

    :param Node node: The target node.

    .. code-block:: pycon

        >>> from raysect.core import Point3D, translate, print_scenegraph
        >>> from raysect.primitive import Cylinder, Sphere, Box
        >>> from raysect.optical import World
        >>>
        >>> world = World()
        >>>
        >>> cyl_x = Cylinder(1, 4.2, transform=translate(0, 0, -2.1), parent=world)
        >>> sphere = Sphere(2.0, parent=world)
        >>> cube = Box(Point3D(-1.5, -1.5, -1.5), Point3D(1.5, 1.5, 1.5), world)
        >>>
        >>> print_scenegraph(sphere)
        <World at 0x7f11eee98e08>
         |
         |_ <Cylinder at 0x7f11e40c9588>
         |
         |_ <Sphere at 0x7f11ec063678> [referring node]
         |
         |_ <Box at 0x7f11e40c9648>

    """

def _print_node(node: _NodeBase, indent: str, link: str, highlight: str) -> None:
    """
    Internal function called recursively to print a scene-graph.
    """
