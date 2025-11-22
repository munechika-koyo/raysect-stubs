from ...core.math import Point3D, Vector3D
from ...core.scenegraph._nodebase import _NodeBase  # pyright: ignore[reportPrivateUsage]
from ...core.scenegraph.primitive import Primitive
from ...core.scenegraph.signal import ChangeSignal
from ...core.scenegraph.world import World as CoreWorld

MATERIAL: ChangeSignal

class ImportanceError(Exception): ...

class ImportanceManager:
    """
    Specialist class for managing sampling of important primitives.
    """
    def __init__(self, primitives: list[Primitive]) -> None: ...
    def sample(self, origin: Point3D) -> Vector3D:
        """
        Sample a random important primitive weighted by their importance weight.

        :param Point3D origin: The point from which to sample.
        :return: The vector along which to sample.
        :rtype: Vector3D
        """
    def pdf(self, origin: Point3D, direction: Vector3D) -> float:
        """
        Calculates the value of the PDF for the specified sample point and direction.

        :param Point3D origin: The point from which to sample.
        :param Vector3D direction: The sample direction.
        :rtype: float
        """
    def has_primitives(self) -> bool:
        """
        Returns true if any primitives in this scene-graph have an importance weighting.

        :rtype: bool
        """

class World(CoreWorld):
    """
    The root node of the optical scene-graph.

    Inherits a lot of functionality and attributes from the core World object.

    The world node tracks all primitives and observers in the world. It maintains acceleration structures to speed up
    the ray-tracing calculations. The particular acceleration algorithm used is selectable. The default acceleration
    structure is a kd-tree.

    :param name: A string defining the node name.
    """

    def __init__(self, name: str | None = None) -> None: ...
    def build_importance(self, force: bool = False) -> None:
        """
        This method manually triggers a rebuild of the importance manager object.

        If the importance manager object is already in a consistent state this method
        will do nothing unless the force keyword option is set to True.

        :param bint force: If set to True, forces rebuilding of acceleration structure.
        """
    def _change(self, node: _NodeBase, signal: ChangeSignal) -> None:
        """
        Notifies the World of a change to the scene-graph.

        This method must be called if a change occurs that may have invalidated
        any acceleration structures held by the World, and also the important primitives
        list maintained be the importance manager.

        The node on which the change occurs and a ChangeSignal must be
        provided. The ChangeSignal must specify the nature of the change.

        The optical World object only recognises the MATERIAL signal. When a
        MATERIAL signal is received, the ImportanceManager is rebuilt to reflect
        changes to the important primitive list and their respective weights.
        """
    def important_direction_sample(self, origin: Point3D) -> Vector3D:
        """
        Get a sample direction of an important primitive.

        :param Point3D origin: The point from which to sample.
        :return: The vector along which to sample.
        :rtype: Vector3D
        """
    def important_direction_pdf(self, origin: Point3D, direction: Vector3D) -> float:
        """
        Calculates the value of the PDF for the specified sample point and direction.

        :param Point3D origin: The point from which to sample.
        :param Vector3D direction: The sample direction.
        :rtype: float
        """
    def has_important_primitives(self) -> bool:
        """
        Returns true if any primitives in this scene-graph have an importance weighting.

        :rtype: bool
        """
