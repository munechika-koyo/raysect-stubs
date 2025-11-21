from .scenegraph.primitive import Primitive

class Material:
    """
    A base class for all Material classes.
    """

    primitives: list[Primitive] = []

    def __init__(self) -> None: ...
    def notify_material_change(self) -> None:
        """
        Notifies any connected scene-graph root of a change to the material.

        The notification informs the root node that any caching structures used
        to accelerate ray-tracing calculations are now potentially invalid and
        must be recalculated, taking the new material properties into account.
        """
