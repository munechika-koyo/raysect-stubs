from ..acceleration.kdtree import KDTree
from ..intersection import Intersection
from ..math import AffineMatrix3D, Point3D
from ..ray import Ray
from ._nodebase import _NodeBase  # pyright: ignore[reportPrivateUsage]
from .observer import Observer
from .primitive import Primitive
from .signal import ChangeSignal

class World(_NodeBase):
    """
    The root node of the scene-graph.

    The world node tracks all primitives and observers in the world. It maintains acceleration structures to speed up
    the ray-tracing calculations. The particular acceleration algorithm used is selectable. The default acceleration
    structure is a kd-tree.

    :param name: A string defining the node name.
    """
    def __init__(self, name: str | None = None) -> None: ...
    @property
    def accelerator(self) -> KDTree:
        """
        The acceleration structure used for this world's scene-graph.
        """
    @accelerator.setter
    def accelerator(self, value: KDTree) -> None: ...
    @property
    def name(self) -> str:
        """
        The name for this world node.

        :rtype: str
        """
    @name.setter
    def name(self, value: str) -> None: ...
    @property
    def primitives(self) -> list[Primitive]:
        """
        A list of all primitives registered with this world.

        :rtype: list
        """
    @property
    def observers(self) -> list[Observer]:
        """
        A list of all observers registered with this world.

        :rtype: list
        """
    def to(self, node: _NodeBase) -> AffineMatrix3D:
        """
        Returns an affine transform that, when applied to a vector or point,
        transforms the vector or point from the co-ordinate space of the calling
        node to the co-ordinate space of the target node.

        For example, if space B is translated +100 in x compared to space A and
        A.to(B) is called then the matrix returned would represent a translation
        of -100 in x. Applied to point (0,0,0) in A, this would produce the
        point (-100,0,0) in B as B is translated +100 in x compared to A.

        :param Node node: The target node.
        :return: An AffineMatrix3D describing the coordinate transform.
        :rtype: AffineMatrix3D
        """
    def hit(self, ray: Ray) -> Intersection:
        """
        Calculates the closest intersection of the Ray with the Primitives in
        the scene-graph, if such an intersection exists.

        If a hit occurs an Intersection object is returned which contains the
        mathematical details of the intersection. None is returned if the ray
        does not intersect any primitive.

        This method automatically rebuilds the Acceleration object that is used
        to optimise hit calculations - if a Primitive's geometry or a transform
        affecting a primitive has changed since the last call to hit() or
        contains(), the Acceleration structure used to optimise hit calculations
        is rebuilt to represent the new scene-graph state.

        :param Ray ray: The ray to test.
        :return: An Intersection object or None if no intersection occurs.
        :rtype: Intersection
        """
    def contains(self, point: Point3D) -> list[Primitive]:
        """
        Returns a list of Primitives that contain the specified point within
        their surface.

        An empty list is returned if no Primitives contain the Point3D.

        This method automatically rebuilds the Acceleration object that is used
        to optimise the contains calculation - if a Primitive's geometry or a
        transform affecting a primitive has changed since the last call to hit()
        or contains(), the Acceleration structure used to optimise the contains
        calculation is rebuilt to represent the new scene-graph state.

        :param Point3D point: The point to test.
        :return: A list containing all Primitives that enclose the Point3D.
        :rtype: list
        """
    def build_accelerator(self, force: bool = False) -> None:
        """
        This method manually triggers a rebuild of the Acceleration object.

        If the Acceleration object is already in a consistent state this method
        will do nothing unless the force keyword option is set to True.

        The Acceleration object is used to accelerate hit() and contains()
        calculations, typically using a spatial sub-division method. If changes are
        made to the scene-graph structure, transforms or to a primitive's
        geometry the acceleration structures may no longer represent the
        geometry of the scene and hence must be rebuilt. This process is
        usually performed automatically as part of the first call to hit() or
        contains() following a change in the scene-graph. As calculating these
        structures can take some time, this method provides the option of
        triggering a rebuild outside of hit() and contains() in case the user wants
        to be able to perform a benchmark without including the overhead of the
        Acceleration object rebuild.

        :param bool force: If set to True, forces rebuilding of acceleration structure.
        """
    def _register(self, node: _NodeBase) -> None:
        """
        Adds observers and primitives to the World's object tracking lists.
        """
    def _deregister(self, node: _NodeBase) -> None:
        """
        Removes observers and primitives from the World's object tracking lists.
        """
    def _change(self, node: _NodeBase, signal: ChangeSignal) -> None:
        """
        Notifies the World of a change to the scene-graph.

        This method must be called is a change occurs that may have invalidated
        any acceleration structures held by the World.

        The node on which the change occurs and a ChangeSignal must be
        provided. The ChangeSignal must specify the nature of the change to the
        scene-graph.

        The core World object only recognises the GEOMETRY signal. When a
        GEOMETRY signal is received, the world will be instructed to rebuild
        it's spatial acceleration structures on the next call to any method
        that interacts with the scene-graph geometry.
        """
