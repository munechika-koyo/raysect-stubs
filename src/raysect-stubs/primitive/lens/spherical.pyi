"""
Basic spherical lens primitives.
"""

from ...core.material import Material
from ...core.math import AffineMatrix3D
from ...core.scenegraph._nodebase import _NodeBase
from ..utility import EncapsulatedPrimitive

class BiConvex(EncapsulatedPrimitive):
    """
    A bi-convex spherical lens primitive.

    A lens consisting of two convex spherical surfaces aligned on a common
    axis. The two surfaces sit at either end of a cylindrical barrel that is
    aligned to lie along the z-axis.

    The two lens surfaces are referred to as front and back respectively. The
    back surface is the negative surface most on the z-axis, while the front
    surface is the positive most surface on the z-axis. The centre of the back
    surface lies on z=0 and with the lens extending along the +ve z direction.

    :param diameter: The diameter of the lens body.
    :param center_thickness: The thickness of the lens measured along the lens axis.
    :param front_curvature: The radius of curvature of the front surface.
    :param back_curvature: The radius of curvature of the back surface.
    :param parent: Assigns the Node's parent to the specified scene-graph object.
    :param transform: Sets the affine transform associated with the Node.
    :param material: An object representing the material properties of the primitive.
    :param name: A string defining the node name.
    """

    diameter: float
    center_thickness: float
    edge_thickness: float
    front_thickness: float
    back_thickness: float
    front_curvature: float
    back_curvature: float

    def __init__(
        self,
        diameter: float,
        center_thickness: float,
        front_curvature: float,
        back_curvature: float,
        parent: _NodeBase | None = None,
        transform: AffineMatrix3D | None = None,
        material: Material | None = None,
        name: str | None = None,
    ) -> None: ...
    def instance(
        self,
        parent: _NodeBase | None = None,
        transform: AffineMatrix3D | None = None,
        material: Material | None = None,
        name: str | None = None,
    ) -> BiConvex: ...

class BiConcave(EncapsulatedPrimitive):
    """
    A bi-concave spherical lens primitive.

    A lens consisting of two concave spherical surfaces aligned on a common
    axis. The two surfaces sit at either end of a cylindrical barrel that is
    aligned to lie along the z-axis.

    The two lens surfaces are referred to as front and back respectively. The
    back surface is the negative surface most on the z-axis, while the front
    surface is the positive most surface on the z-axis. The centre of the back
    surface lies on z=0 and with the lens extending along the +ve z direction.

    :param diameter: The diameter of the lens body.
    :param center_thickness: The thickness of the lens measured along the lens axis.
    :param front_curvature: The radius of curvature of the front surface.
    :param back_curvature: The radius of curvature of the back surface.
    :param parent: Assigns the Node's parent to the specified scene-graph object.
    :param transform: Sets the affine transform associated with the Node.
    :param material: An object representing the material properties of the primitive.
    :param name: A string defining the node name.
    """

    diameter: float
    center_thickness: float
    edge_thickness: float
    front_thickness: float
    back_thickness: float
    front_curvature: float
    back_curvature: float

    def __init__(
        self,
        diameter: float,
        center_thickness: float,
        front_curvature: float,
        back_curvature: float,
        parent: _NodeBase | None = None,
        transform: AffineMatrix3D | None = None,
        material: Material | None = None,
        name: str | None = None,
    ) -> None: ...
    def instance(
        self,
        parent: _NodeBase | None = None,
        transform: AffineMatrix3D | None = None,
        material: Material | None = None,
        name: str | None = None,
    ) -> BiConcave: ...

class PlanoConvex(EncapsulatedPrimitive):
    """
    A plano-convex spherical lens primitive.

    A lens consisting of a convex spherical surface and a plane (flat) surface,
    aligned on a common axis. The two surfaces sit at either end of a
    cylindrical barrel that is aligned to lie along the z-axis.

    The two lens surfaces are referred to as front and back respectively. The
    back surface is the plane surface, it is the negative surface most on the
    z-axis. The front surface is the spherical surface, it is the positive most
    surface on the z-axis. The back (plane) surface lies on z=0 with the lens
    extending along the +ve z direction.

    :param diameter: The diameter of the lens body.
    :param center_thickness: The thickness of the lens measured along the lens axis.
    :param curvature: The radius of curvature of the spherical front surface.
    :param parent: Assigns the Node's parent to the specified scene-graph object.
    :param transform: Sets the affine transform associated with the Node.
    :param material: An object representing the material properties of the primitive.
    :param name: A string defining the node name.
    :return:
    """

    diameter: float
    center_thickness: float
    edge_thickness: float
    curve_thickness: float
    curvature: float

    def __init__(
        self,
        diameter: float,
        center_thickness: float,
        curvature: float,
        parent: _NodeBase | None = None,
        transform: AffineMatrix3D | None = None,
        material: Material | None = None,
        name: str | None = None,
    ) -> None: ...
    def instance(
        self,
        parent: _NodeBase | None = None,
        transform: AffineMatrix3D | None = None,
        material: Material | None = None,
        name: str | None = None,
    ) -> PlanoConvex: ...

class PlanoConcave(EncapsulatedPrimitive):
    """
    A plano-concave spherical lens primitive.

    A lens consisting of a concave spherical surface and a plane (flat)
    surface, aligned on a common axis. The two surfaces sit at either end of a
    cylindrical barrel that is aligned to lie along the z-axis.

    The two lens surfaces are referred to as front and back respectively. The
    back surface is the plane surface, it is the negative surface most on the
    z-axis. The front surface is the spherical surface, it is the positive most
    surface on the z-axis. The back (plane) surface lies on z=0 with the lens
    extending along the +ve z direction.

    :param diameter: The diameter of the lens body.
    :param center_thickness: The thickness of the lens measured along the lens axis.
    :param curvature: The radius of curvature of the spherical front surface.
    :param parent: Assigns the Node's parent to the specified scene-graph object.
    :param transform: Sets the affine transform associated with the Node.
    :param material: An object representing the material properties of the primitive.
    :param name: A string defining the node name.
    :return:
    """

    diameter: float
    center_thickness: float
    edge_thickness: float
    curve_thickness: float
    curvature: float

    def __init__(
        self,
        diameter: float,
        center_thickness: float,
        curvature: float,
        parent: _NodeBase | None = None,
        transform: AffineMatrix3D | None = None,
        material: Material | None = None,
        name: str | None = None,
    ) -> None: ...
    def instance(
        self,
        parent: _NodeBase | None = None,
        transform: AffineMatrix3D | None = None,
        material: Material | None = None,
        name: str | None = None,
    ) -> PlanoConcave: ...

class Meniscus(EncapsulatedPrimitive):
    """
    A meniscus spherical lens primitive.

    A lens consisting of a concave and a convex spherical surface aligned on a
    common axis. The two surfaces sit at either end of a cylindrical barrel
    that is aligned to lie along the z-axis.

    The two lens surfaces are referred to as front and back respectively. The
    back surface is concave, it is the negative surface most on the z-axis. The
    front surface is convex, it is the positive most surface on the z-axis. The
    centre of the back surface lies on z=0 and with the lens extending along
    the +ve z direction.

    :param diameter: The diameter of the lens body.
    :param center_thickness: The thickness of the lens measured along the lens axis.
    :param front_curvature: The radius of curvature of the front (convex) surface.
    :param back_curvature: The radius of curvature of the back (concave) surface.
    :param parent: Assigns the Node's parent to the specified scene-graph object.
    :param transform: Sets the affine transform associated with the Node.
    :param material: An object representing the material properties of the primitive.
    :param name: A string defining the node name.
    """

    diameter: float
    center_thickness: float
    edge_thickness: float
    front_thickness: float
    back_thickness: float
    front_curvature: float
    back_curvature: float

    def __init__(
        self,
        diameter: float,
        center_thickness: float,
        front_curvature: float,
        back_curvature: float,
        parent: _NodeBase | None = None,
        transform: AffineMatrix3D | None = None,
        material: Material | None = None,
        name: str | None = None,
    ) -> None: ...
    def instance(
        self,
        parent: _NodeBase | None = None,
        transform: AffineMatrix3D | None = None,
        material: Material | None = None,
        name: str | None = None,
    ) -> Meniscus: ...
