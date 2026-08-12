from ....core import Primitive
from ....core.math import AffineMatrix3D, Point3D, Vector3D
from ... import Ray, Spectrum, World
from ..material import NullVolume

class HomogeneousVolumeEmitter(NullVolume):
    """
    Base class for homogeneous volume emitters.

    Total power output of the light from each point is constant,
    but not necessarily isotropic.

    The deriving class must implement the emission_function() method.
    """

    def __init__(self) -> None: ...
    def evaluate_volume(
        self,
        spectrum: Spectrum,
        world: World,
        ray: Ray,
        primitive: Primitive,
        start_point: Point3D,
        end_point: Point3D,
        world_to_primitive: AffineMatrix3D,
        primitive_to_world: AffineMatrix3D,
    ) -> Spectrum: ...
    def emission_function(
        self,
        direction: Vector3D,
        spectrum: Spectrum,
        world: World,
        ray: Ray,
        primitive: Primitive,
        world_to_primitive: AffineMatrix3D,
        primitive_to_world: AffineMatrix3D,
    ) -> Spectrum:
        """
        The emission function for the material.

        This is a virtual method and must be implemented in a sub class.

        :param Vector3D direction: The emission direction vector in local coordinates.
        :param Spectrum spectrum: Spectrum measured so far along ray path. Add your emission
          to this spectrum, don't override it.
        :param World world: The world scene-graph.
        :param Ray ray: The ray being traced.
        :param Primitive primitive: The geometric primitive to which this material belongs
          (i.e. a cylinder or a mesh).
        :param AffineMatrix3D world_to_primitive: Affine matrix defining the coordinate
          transform from world space to the primitive's local space.
        :param AffineMatrix3D primitive_to_world: Affine matrix defining the coordinate
          transform from the primitive's local space to world space.
        """
