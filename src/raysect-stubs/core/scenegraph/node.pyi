from ..math.affinematrix import AffineMatrix3D
from ._nodebase import _NodeBase  # pyright: ignore[reportPrivateUsage]

class Node(_NodeBase):
    """
    The scene-graph node class.

    The basic constituent of a scene-graph tree. Nodes can be linked together
    by parenting one Node to another to form a tree structure. Each node in a
    scene-graph represents a distinct co-ordinate system. An affine transform
    associated with each node describes the relationship between a node and its
    parent's coordinate system. By combining the transforms (and inverse
    transforms) along the path between two nodes in the tree, the direct
    transform between any two arbitrary nodes, and thus their co-ordinate
    systems, can be calculated. Using this transform it is then possible to
    transform vectors and points between the two co-ordinate systems.

    :param Node parent: Assigns the Node's parent to the specified scene-graph object.
    :param AffineMatrix3D transform: Sets the affine transform associated with the Node.
    :param str name: A string defining the node name.

    :ivar list children: A list of child nodes for which this node is the parent.
    :ivar dict meta: A dictionary for the storage of any extra user specified meta data.
    :ivar Node root: A reference to the root node of this node's scene-graph
      (i.e. the parent of all parents.
    """

    def __init__(self, parent: Node | None = None, transform: AffineMatrix3D | None = None, name: str | None = None) -> None: ...
    @property
    def parent(self) -> Node | None:
        """
        The parent of this node in the scenegraph.

        :rtype: Node
        """
    @parent.setter
    def parent(self, value: Node | None) -> None: ...
    @property
    def transform(self) -> AffineMatrix3D:
        """
        The transform for this node's coordinate system in relation to the parent node.

        :rtype: AffineMatrix3D
        """
    @transform.setter
    def transform(self, value: AffineMatrix3D) -> None: ...
    @property
    def name(self) -> str | None:
        """
        The name of this node.

        :rtype: str
        """
    @name.setter
    def name(self, value: str | None) -> None: ...
    def to(self, node: _NodeBase) -> AffineMatrix3D:
        """
        Returns an affine transform that, when applied to a vector or point,
        transforms the vector or point from the co-ordinate space of the calling
        node to the co-ordinate space of the target node.

        For example, if space B is translated +100 in x compared to space A and
        A.to(B) is called then the matrix returned would represent a translation
        of -100 in x. Applied to point (0,0,0) in A, this would produce the
        point (-100,0,0) in B as B is translated +100 in x compared to A.

        :param _NodeBase node: The target node.
        :return: An AffineMatrix3D describing the coordinate transform.
        :rtyoe: AffineMatrix3D
        """
    def to_local(self) -> AffineMatrix3D:
        """
        Returns an affine transform from world space into this nodes local
        coordinate space.

        :rtype: AffineMatrix3D
        """
    def to_root(self) -> AffineMatrix3D:
        """
        Returns an affine transform from local space into the parent node's
        coordinate space.

        :rtype: AffineMatrix3D
        """
