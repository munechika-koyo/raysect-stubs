from ..core.boundingbox import BoundingBox3D
from ..core.intersection import Intersection
from ..core.material import Material
from ..core.math import AffineMatrix3D, Point3D
from ..core.ray import Ray
from ..core.scenegraph import Primitive
from ..core.scenegraph._nodebase import _NodeBase

class EncapsulatedPrimitive(Primitive):
    """
    allows developers to hide primitive attributes from users

    where the primitive dimensions are defined by a wrapper e.g. CSG biconvex lens - two spheres and a cylinder with dimensiosn defineds by blah blah...

    can only be used to encapsulate a single primitive, any attached children will be removed automatically
    (they would be ignored anyway)

    :param Primitive:
    :return:
    """

    def __init__(
        self,
        primitive: Primitive,
        parent: _NodeBase | None = None,
        transform: AffineMatrix3D | None = None,
        material: Material | None = None,
        name: str | None = None,
    ) -> None: ...
    def hit(self, ray: Ray) -> Intersection | None: ...
    def next_intersection(self) -> Intersection | None: ...
    def contains(self, point: Point3D) -> bool: ...
    def bounding_box(self) -> BoundingBox3D: ...
