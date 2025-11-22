from abc import abstractmethod

from ...core.intersection import Intersection
from ...core.material import Material as CoreMaterial
from ...core.math import AffineMatrix3D, Normal3D, Point3D, Vector3D
from ...core.scenegraph import Primitive
from ..ray import Ray
from ..scenegraph import World
from ..spectrum import Spectrum

class Material(CoreMaterial):
    """
    Base class for optical material classes.

    Derived classes must implement the evaluate_surface() and evaluate_volume() methods.
    """
    def __init__(self) -> None: ...
    @property
    def importance(self) -> float:
        """
        Importance sampling weight for this material.

        Only effective if importance sampling is turned on.

        :rtype: float
        """
    @abstractmethod
    def evaluate_surface(
        self,
        world: World,
        ray: Ray,
        primitive: Primitive,
        hit_point: Point3D,
        exiting: bool,
        inside_point: Point3D,
        outside_point: Point3D,
        normal: Normal3D,
        world_to_primitive: AffineMatrix3D,
        primitive_to_world: AffineMatrix3D,
        intersection: Intersection,
    ) -> Spectrum:
        """
        Virtual method for evaluating the spectrum at a material surface.

        :param World world: The world scenegraph belonging to this material.
        :param Ray ray: The ray incident at the material surface.
        :param Primitive primitive: The geometric shape the holds this material
          (i.e. mesh, cylinder, etc.).
        :param Point3D hit_point: The point where the ray is incident on the
          primitive surface.
        :param bool exiting: Boolean toggle indicating if this ray is exiting or
          entering the material surface (True means ray is exiting).
        :param Point3D inside_point:
        :param Point3D outside_point:
        :param Normal3D normal: The surface normal vector at location of hit_point.
        :param AffineMatrix3D world_to_primitive: Affine matrix defining transformation
          from world space to local primitive space.
        :param AffineMatrix3D primitive_to_world: Affine matrix defining transformation
          from local primitive space to world space.
        :param Intersection intersection: The full ray-primitive intersection object.
        """
    @abstractmethod
    def evaluate_volume(
        self,
        world: World,
        ray: Ray,
        primitive: Primitive,
        hit_point: Point3D,
        exiting: bool,
        inside_point: Point3D,
        outside_point: Point3D,
        normal: Normal3D,
        world_to_primitive: AffineMatrix3D,
        primitive_to_world: AffineMatrix3D,
        intersection: Intersection,
    ) -> Spectrum:
        """
        Virtual method for evaluating the spectrum emitted/absorbed along the rays trajectory
        through a material surface.


        :param Spectrum spectrum: The spectrum already accumulated along the ray path.
          Don't overwrite this array, add the materials emission/absorption to the existing
          spectrum.
        :param World world: The world scenegraph belonging to this material.
        :param Ray ray: The ray incident at the material surface.
        :param Primitive primitive: The geometric shape the holds this material
          (i.e. mesh, cylinder, etc.).
        :param Point3D start_point: The starting point of the ray's trajectory
          through the material.
        :param Point3D end_point: The end point of the ray's trajectory through
          the material.
        :param AffineMatrix3D world_to_primitive: Affine matrix defining transformation
          from world space to local primitive space.
        :param AffineMatrix3D primitive_to_world: Affine matrix defining transformation
          from local primitive space to world space.
        """

class NullSurface(Material):
    """
    A base class for materials that have volume properties such as emission/absorption
    but no surface properties (e.g. a plasma). This material will launch a new ray after
    the initial ray has transited the material primitive's volume. evaluate_volume() must be
    implemented by the deriving class.
    """

    def evaluate_surface(
        self,
        world: World,
        ray: Ray,
        primitive: Primitive,
        hit_point: Point3D,
        exiting: bool,
        inside_point: Point3D,
        outside_point: Point3D,
        normal: Normal3D,
        world_to_primitive: AffineMatrix3D,
        primitive_to_world: AffineMatrix3D,
        intersection: Intersection,
    ) -> Spectrum: ...

class NullVolume(Material):
    """
    A base class for materials that have surface properties such as reflection
    but no volume properties (e.g. a metallic mirror). evaluate_surface() must be
    implemented by the deriving class.
    """
    def evaluate_volume(
        self,
        world: World,
        ray: Ray,
        primitive: Primitive,
        hit_point: Point3D,
        exiting: bool,
        inside_point: Point3D,
        outside_point: Point3D,
        normal: Normal3D,
        world_to_primitive: AffineMatrix3D,
        primitive_to_world: AffineMatrix3D,
        intersection: Intersection,
    ) -> Spectrum: ...

class NullMaterial(Material):
    """
    A perfectly transparent material.

    Behaves as if nothing is present, doesn't perturb the ray trajectories at all.
    Useful for logging ray trajectories and designating areas of interest that may
    not correspond to a physical material (i.e. a slit / aperture).
    """
    def evaluate_surface(
        self,
        world: World,
        ray: Ray,
        primitive: Primitive,
        hit_point: Point3D,
        exiting: bool,
        inside_point: Point3D,
        outside_point: Point3D,
        normal: Normal3D,
        world_to_primitive: AffineMatrix3D,
        primitive_to_world: AffineMatrix3D,
        intersection: Intersection,
    ) -> Spectrum: ...
    def evaluate_volume(
        self,
        world: World,
        ray: Ray,
        primitive: Primitive,
        hit_point: Point3D,
        exiting: bool,
        inside_point: Point3D,
        outside_point: Point3D,
        normal: Normal3D,
        world_to_primitive: AffineMatrix3D,
        primitive_to_world: AffineMatrix3D,
        intersection: Intersection,
    ) -> Spectrum: ...

class DiscreteBSDF(Material):
    """
    A base class for materials implementing a discrete BSDF.
    """
    def evaluate_surface(
        self,
        world: World,
        ray: Ray,
        primitive: Primitive,
        hit_point: Point3D,
        exiting: bool,
        inside_point: Point3D,
        outside_point: Point3D,
        normal: Normal3D,
        world_to_primitive: AffineMatrix3D,
        primitive_to_world: AffineMatrix3D,
        intersection: Intersection,
    ) -> Spectrum: ...
    @abstractmethod
    def evaluate_shading(
        self,
        world: World,
        ray: Ray,
        s_incoming: Vector3D,
        w_reflection_origin: Point3D,
        w_transmission_origin: Point3D,
        back_face: bool,
        world_to_surface: AffineMatrix3D,
        surface_to_world: AffineMatrix3D,
        intersection: Intersection,
    ) -> Spectrum: ...

class ContinuousBSDF(Material):
    """
    A base class for materials implementing a continuous BSDF.
    """

    def evaluate_surface(
        self,
        world: World,
        ray: Ray,
        primitive: Primitive,
        hit_point: Point3D,
        exiting: bool,
        inside_point: Point3D,
        outside_point: Point3D,
        normal: Normal3D,
        world_to_primitive: AffineMatrix3D,
        primitive_to_world: AffineMatrix3D,
        intersection: Intersection,
    ) -> Spectrum: ...
    @abstractmethod
    def pdf(self, s_incoming: Vector3D, s_outgoing: Vector3D, back_face: bool) -> float: ...
    @abstractmethod
    def sample(self, s_incoming: Vector3D, back_face: bool) -> Vector3D: ...
    @abstractmethod
    def evaluate_shading(
        self,
        world: World,
        ray: Ray,
        s_incoming: Vector3D,
        s_outgoing: Vector3D,
        w_reflection_origin: Point3D,
        w_transmission_origin: Point3D,
        back_face: bool,
        world_to_surface: AffineMatrix3D,
        surface_to_world: AffineMatrix3D,
        intersection: Intersection,
    ) -> Spectrum: ...
    @abstractmethod
    def bsdf(self, s_incident: Vector3D, s_reflected: Vector3D, wavelength: float) -> float:
        """
        Returns the surface bi-directional scattering distribution function (BSDF).

        The BSDF is calculated for the given wavelength, incoming and outgoing surface space directions.

        :param Vector3D s_incident: The surface space incident vector, :math:`\\omega_i`.
        :param Vector3D s_reflected: The surface space reflected vector, :math:`\\omega_o`.
        :param float wavelength: The wavelength :math:`\\lambda` at which to perform the BSDF evaluation.
        :return: The BSDF value, :math:`BSDF(\\omega_i, \\omega_o, \\lambda)`
        """
