from abc import abstractmethod

from ....core import Primitive
from ....core.math import AffineMatrix3D, Point3D, Vector3D
from ... import Ray, Spectrum, World
from ...material.material import NullSurface

class VolumeIntegrator:
    """
    Base class for integrators in InhomogeneousVolumeEmitter materials.

    The deriving class must implement the integrate() method.
    """

    @abstractmethod
    def integrate(
        self,
        spectrum: Spectrum,
        world: World,
        ray: Ray,
        primitive: Primitive,
        material: InhomogeneousVolumeEmitter,
        start_point: Point3D,
        end_point: Point3D,
        world_to_primitive: AffineMatrix3D,
        primitive_to_world: AffineMatrix3D,
    ) -> Spectrum:
        """
        Performs a customised integration of the emission through a volume emitter.

        This is a virtual method and must be implemented in a sub class.

        :param Spectrum spectrum: Spectrum measured so far along ray path. Add your emission
          to this spectrum, don't override it.
        :param World world: The world scene-graph.
        :param Ray ray: The ray being traced.
        :param Primitive primitive: The geometric primitive to which this material belongs
          (i.e. a cylinder or a mesh).
        :param InhomogeneousVolumeEmitter material: The material whose emission needs to be
          integrated.
        :param Point3D start_point: The start point for integration in world space.
        :param Point3D end_point: The end point for integration in world space.
        :param AffineMatrix3D world_to_primitive: Affine matrix defining the coordinate
          transform from world space to the primitive's local space.
        :param AffineMatrix3D primitive_to_world: Affine matrix defining the coordinate
          transform from the primitive's local space to world space.
        """

class NumericalIntegrator(VolumeIntegrator):
    """
    A basic implementation of the trapezium integration scheme for volume emitters.

    :param float step: The step size for numerical integration in metres.
    :param int min_samples: The minimum number of samples to use over integration
      range (default=5).
    """

    _step: float
    _min_samples: float
    def __init__(self, step: float, min_samples: float) -> None: ...
    @property
    def step(self) -> float: ...
    @step.setter
    def step(self, value: float) -> None: ...
    @property
    def min_samples(self) -> float: ...
    @min_samples.setter
    def min_samples(self, value: float) -> None: ...
    def integrate(
        self,
        spectrum: Spectrum,
        world: World,
        ray: Ray,
        primitive: Primitive,
        material: InhomogeneousVolumeEmitter,
        start_point: Point3D,
        end_point: Point3D,
        world_to_primitive: AffineMatrix3D,
        primitive_to_world: AffineMatrix3D,
    ) -> Spectrum: ...

class InhomogeneousVolumeEmitter(NullSurface):
    """
    Base class for inhomogeneous volume emitters.

    The integration technique can be changed by the user, but defaults to
    a basic numerical integration scheme.

    The deriving class must implement the emission_function() method.

    :param VolumeIntegrator integrator: Integration object, defaults to
      NumericalIntegrator(step=0.01, min_samples=5).
    """

    integrator: VolumeIntegrator
    importance: float = 1.0

    def __init__(self, integrator: VolumeIntegrator | None = None) -> None: ...
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
        point: Point3D,
        direction: Vector3D,
        spectrum: Spectrum,
        world: World,
        ray: Ray,
        primitive: Primitive,
        world_to_primitive: AffineMatrix3D,
        primitive_to_world: AffineMatrix3D,
    ) -> Spectrum:
        """
        The emission function for the material at a given sample point.

        This is a virtual method and must be implemented in a sub class.

        :param Point3D point: Requested sample point in local coordinates.
        :param Vector3D direction: The emission direction in local coordinates.
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
