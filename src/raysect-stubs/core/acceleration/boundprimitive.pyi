from ..boundingbox import BoundingBox3D
from ..scenegraph.primitive import Primitive

class BoundPrimitive:
    box: BoundingBox3D
    primitive: Primitive
    def __init__(self, primitive: Primitive) -> None: ...
