from typing import Self

import numpy as np
from _typeshed import StrOrBytesPath, SupportsRead, SupportsWrite
from numpy.typing import NDArray

from ...core.boundingbox import BoundingBox3D
from ...core.intersection import Intersection
from ...core.material import Material
from ...core.math import AffineMatrix3D, Normal3D, Point3D
from ...core.math.spatial.kdtree3d import KDTree3DCore
from ...core.ray import Ray
from ...core.scenegraph import Primitive
from ...core.scenegraph._nodebase import _NodeBase

DEFAULT_AFFINEMATRIX = AffineMatrix3D()
DEFAULT_MATERIAL = Material()

class MeshIntersection(Intersection):
    """
    Describes the result of a ray-primitive intersection with a Mesh primitive.

    :param Ray ray: The incident ray object (world space).
    :param double ray_distance: The distance of the intersection along the ray path.
    :param Primitive primitive: The intersected primitive object.
    :param Point3D hit_point: The point of intersection between the ray and the primitive (primitive local space).
    :param Point3D inside_point: The interior ray launch point (primitive local space).
    :param Point3D outside_point: The exterior ray launch point (primitive local space).
    :param Normal3D normal: The surface normal (primitive local space)
    :param bool exiting: True if the ray is exiting the surface, False otherwise.
    :param AffineMatrix3D world_to_primitive: A world to primitive local transform matrix.
    :param AffineMatrix3D primitive_to_world: A primitive local to world transform matrix.

    :ivar bool exiting: True if the ray is exiting the surface, False otherwise.
    :ivar Point3D hit_point: The point of intersection between the ray and the primitive
      (primitive local space).
    :ivar Point3D inside_point: The interior ray launch point (primitive local space).
    :ivar Normal3D normal: The surface normal (primitive local space).
    :ivar Point3D outside_point: The exterior ray launch point (primitive local space).
    :ivar Primitive primitive: The primitive object that was intersected by the Ray.
    :ivar AffineMatrix3D primitive_to_world: The primitive's local to world transform matrix.
    :ivar Ray ray: The incident ray object (world space).
    :ivar double ray_distance: The distance of the intersection along the ray path.
    :ivar AffineMatrix3D world_to_primitive: A world to primitive local transform matrix.
    :ivar int triangle: The index of the triangle intersected.
    :ivar float u: The barycentric coordinate U of the intersection.
    :ivar float v: The barycentric coordinate V of the intersection.
    :ivar float w: The barycentric coordinate W of the intersection.
    """

    triangle: np.int32
    u: float
    v: float
    w: float

    def __init__(
        self,
        ray: Ray,
        ray_distance: float,
        primitive: Primitive,
        hit_point: Point3D,
        inside_point: Point3D,
        outside_point: Point3D,
        normal: Normal3D,
        exiting: bool,
        world_to_primitive: AffineMatrix3D,
        primitive_to_world: AffineMatrix3D,
        triangle: np.int32,
        u: float,
        v: float,
        w: float,
    ) -> None: ...

class MeshData(KDTree3DCore):
    """
    Holds the mesh data and acceleration structures.

    The Mesh primitive is a thin wrapper around a MeshData object. This
    arrangement simplifies mesh instancing and the load/dump methods.

    :param object vertices: A list/array or triangle vertices with shape Nx3,
      where N is the number of vertices.
    :param object triangles: A list/array of triangles with shape Nx3 or Nx6
      where N is the number of triangles in the mesh. For each triangle there
      must be three integers identifying the triangle's vertices in the vertices
      array. If vertex normals are present then three additional integers
      specify the triangle's vertex normals in the normals array.
    :param object normals: Optional array of triangle normals (default=None).
    :param bool smoothing: Turns on smoothing of triangle surface normals when
      calculating ray intersections (default=True).
    :param bool closed: Whether this mesh should be treated as a closed surface,
      i.e. no holes. (default=True)
    :param bool tolerant: Toggles filtering out of degenerate triangles
      (default=True).
    :param bool flip_normals: Inverts the direction of the surface normals (default=False).
    :param int max_depth: Maximum kd-Tree depth for this mesh (automatic if set to
      0, default=0).
    :param int min_items: The item count threshold for forcing creation of a
      new leaf node in the kdTree (default=1).
    :param double hit_cost: The relative computational cost of item hit evaluations
      vs kd-tree traversal (default=20.0).
    :param double empty_bonus: The bonus applied to node splits that generate empty
      kd-Tree leaves (default=0.2).
    """

    closed: bool
    smoothing: bool

    def __init__(
        self,
        vertices: object,
        triangles: object,
        normals: object = None,
        smoothing: bool = True,
        closed: bool = True,
        tolerant: bool = True,
        flip_normals: bool = False,
        max_depth: int = 0,
        min_items: int = 1,
        hit_cost: float = 20.0,
        empty_bonus: float = 0.2,
    ) -> None: ...
    @property
    def vertices(self) -> NDArray[np.float32]: ...
    @property
    def triangles(self) -> NDArray[np.int32]: ...
    @property
    def vertex_normals(self) -> NDArray[np.float32] | None: ...
    @property
    def face_normals(self) -> NDArray[np.float32]: ...
    def vertex(self, index: int) -> Point3D:
        """
        Returns the specified vertex.

        :param index: The vertex index.
        :return: A Point3D object.
        """
    def triangle(self, index: int) -> NDArray[np.int32]:
        """
        Returns the specified triangle.

        The returned data will either be a 3 or 6 element numpy array. The
        first three element are the triangle's vertex indices. If present, the
        last three elements are the triangle's vertex normal indices.

        :param index: The triangle index.
        :return: A numpy array.
        """
    def vertex_normal(self, index: int) -> Normal3D:
        """
        Returns the specified vertex normal.

        :param index: The vertex normal's index.
        :return: A Normal3D object.
        """
    def face_normal(self, index: int) -> Normal3D:
        """
        Returns the specified face normal.

        :param index: The face normal's index.
        :return: A Normal3D object.
        """
    def trace(self, ray: Ray) -> bool: ...
    def calc_intersection(self, ray: Ray) -> Intersection: ...
    def contains(self, p: Point3D) -> bool:
        """
        Tests if a point is contained by the mesh.

        Note, this method assumes the mesh is closed. Any open/closed mesh test
        must be performed externally (this is generally quicker as coordinate
        transforms etc... can be skipped if the mesh is open).

        :param p: Local space Point3D.
        :return: True if mesh contains point, False otherwise.
        """
    def bounding_box(self, to_world: AffineMatrix3D) -> BoundingBox3D:
        """
        Returns a bounding box that encloses the mesh.

        The box is padded by a small margin to reduce the risk of numerical
        accuracy problems between the mesh and box representations following
        coordinate transforms.

        :param to_world: Local to world space transform matrix.
        :return: A BoundingBox3D object.
        """
    def save(self, file: StrOrBytesPath | SupportsWrite[bytes]) -> None:
        """
        Save the mesh's kd-Tree representation to a binary Raysect mesh file (.rsm).

        :param object file: File stream or string file name to save state.
        """
    def load(self, file: StrOrBytesPath | SupportsRead[bytes]) -> None:
        """
        Load a mesh with its kd-Tree representation from Raysect mesh binary file (.rsm).

        :param object file: File stream or string file name to save state.
        """
    @classmethod
    def from_file(cls, file: StrOrBytesPath | SupportsRead[bytes]) -> Self:
        """
        Load a mesh with its kd-Tree representation from Raysect mesh binary file (.rsm).

        :param object file: File stream or string file name to save state.
        """

class Mesh(Primitive):
    """
    This primitive defines a polyhedral surface with triangular faces.

    To define a new mesh, a list of vertices and triangles must be supplied.
    A set of vertex normals, used for smoothing calculations may also be
    provided.

    The mesh vertices are supplied as an Nx3 list/array of floating point
    values. For each Vertex, x, y and z coordinates must be supplied. e.g.

        vertices = [[0.0, 0.0, 1.0], [1.0, 0.0, 0.0], ...]

    Vertex normals are similarly defined. Note that vertex normals must be
    correctly normalised.

    The triangle array is either Mx3 or Mx6 - Mx3 if only vertices are defined
    or Mx6 if both vertices and vertex normals are defined. Triangles are
    defined by indexing into the vertex and vertex normal arrays. i.e:

        triangles = [[v1, v2, v3, n1, n2, n3], ...]

    where v1, v2, v3 are the vertex array indices specifying the triangle\'s
    vertices and n1, n2, n3 are the normal array indices specifying the
    triangle\'s surface normals at each vertex location. Where normals are
    not defined, n1, n2 and n3 are omitted.

    The mesh may be an open surface (which does not enclose a volume) or a
    closed surface (which defines a volume). The nature of the mesh must be
    specified using the closed argument. If closed is True (default) then the
    mesh must be watertight and the face normals must be facing so they point
    out of the volume. If the mesh is open then closed must be set to False.
    Incorrectly setting the closed argument may result in undefined behaviour,
    depending on the application of the ray-tracer.

    If vertex normals are defined for some or all of the triangles of the mesh
    then normal interpolation may be enabled for the mesh. For optical models
    this will result in a (suitably defined) mesh appearing smooth rather than
    faceted. If the triangles do not have vertex normals defined, the smoothing
    argument is ignored.

    An alternate option for creating a new mesh is to create an instance of an
    existing mesh. An instance is a "clone" of the original mesh. Mesh instances
    hold references to the internal data of the target mesh, they are therefore
    very memory efficient (particularly for detailed meshes) compared to
    creating a new mesh from scratch. A new instance of a mesh can be created
    using the instance() method.

    If a mesh contains degenerate triangles (common for meshes generated from
    CAD models), enable tolerant mode to automatically remove them during mesh
    initialisation. A degenerate triangle is one where two or more vertices are
    coincident or all the vertices lie on the same line. Degenerate triangles
    will produce rendering error if encountered even though they are
    "infinitesimally" thin. A ray can still intersect them if they perfectly
    align as the triangle edges are treated as part of the triangle surface).

    The kdtree_* arguments are tuning parameters for the kd-tree construction.
    For more information see the documentation of KDTree3D. The default values
    should result in efficient construction of the mesh\'s internal kd-tree.
    Generally there is no need to modify these parameters unless the memory
    used by the kd-tree must be controlled. This may occur if very large meshes
    are used.

    :param object vertices: An N x 3 list of vertices.
    :param object triangles: An M x 3 or N x 6 list of vertex/normal indices
      defining the mesh triangles.
    :param object normals: An K x 3 list of vertex normals or None (default=None).
    :param bool smoothing: True to enable normal interpolation (default=True).
    :param bool closed: True is the mesh defines a closed volume (default=True).
    :param bool tolerant: Mesh will automatically correct meshes with degenerate
      triangles if set to True (default=True).
    :param bool flip_normals: Inverts the direction of the surface normals (default=False).
    :param int kdtree_max_depth: The maximum tree depth (automatic if set to 0, default=0).
    :param int kdtree_min_items: The item count threshold for forcing creation of
      a new leaf node (default=1).
    :param double kdtree_hit_cost: The relative computational cost of item hit
      evaluations vs kd-tree traversal (default=20.0).
    :param double kdtree_empty_bonus: The bonus applied to node splits that
      generate empty leaves (default=0.2).
    :param Node parent: Attaches the mesh to the specified scene-graph
      node (default=None).
    :param AffineMatrix3D transform: The co-ordinate transform between
      the mesh and its parent (default=unity matrix).
    :param Material material: The surface/volume material
      (default=Material() instance).
    :param str name: A human friendly name to identity the mesh in the
      scene-graph (default="").

    :ivar MeshData data: A class instance containing all the mesh data.
    """

    data: MeshData

    def __init__(
        self,
        vertices: object,
        triangles: object,
        normals: object = None,
        smoothing: bool = True,
        closed: bool = True,
        tolerant: bool = True,
        flip_normals: bool = False,
        kdtree_max_depth: int = -1,
        kdtree_min_items: int = 1,
        kdtree_hit_cost: float = 5.0,
        kdtree_empty_bonus: float = 0.25,
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
    ) -> Self: ...
    def hit(self, ray: Ray) -> Intersection | None:
        """
        Returns the first intersection with the mesh surface.

        If an intersection occurs this method will return an Intersection
        object. The Intersection object will contain the details of the
        ray-surface intersection, such as the surface normal and intersection
        point.

        If no intersection occurs None is returned.

        :param ray: A world-space ray.
        :return: An Intersection or None.
        """
    def next_intersection(self) -> Intersection | None:
        """
        Returns the next intersection of the ray with the mesh along the ray
        path.

        This method may only be called following a call to hit(). If the ray
        has further intersections with the mesh, these may be obtained by
        repeatedly calling the next_intersection() method. Each call to
        next_intersection() will return the next ray-mesh intersection
        along the ray's path. If no further intersections are found or
        intersections lie outside the ray parameters then next_intersection()
        will return None.

        :return: An Intersection or None.
        """
    def contains(self, point: Point3D) -> bool:
        """
        Identifies if the point lies in the volume defined by the mesh.

        If a mesh is open, this method will always return False.

        This method will fail if the face normals of the mesh triangles are not
        oriented to be pointing out of the volume surface.

        :param point: The point to test.
        :return: True if the point lies in the volume, False otherwise.
        """
    def bounding_box(self) -> BoundingBox3D:
        """
        Returns a world space bounding box that encloses the mesh.

        The box is padded by a small margin to reduce the risk of numerical
        accuracy problems between the mesh and box representations following
        coordinate transforms.

        :return: A BoundingBox3D object.
        """
    def save(self, file: StrOrBytesPath | SupportsWrite[bytes]) -> None:
        """
        Saves the mesh to the specified file object or filename.

        The mesh in written in RaySect Mesh (RSM) format. The RSM format
        contains the mesh geometry and the mesh acceleration structures.

        :param file: File object or string path.

        .. code-block:: pycon

            >>> mesh
            <raysect.primitive.mesh.mesh.Mesh at 0x7f2c09eac2e8>
            >>> mesh.save("my_mesh.rsm")

        """
    def load(self, file: StrOrBytesPath | SupportsRead[bytes]) -> None:
        """
        Loads the mesh specified by a file object or filename.

        The mesh must be stored in a RaySect Mesh (RSM) format file. RSM files
        are created with the Mesh save() method.

        :param file: File object or string path.
        """
    @classmethod
    def from_file(
        cls,
        file: StrOrBytesPath | SupportsRead[bytes],
        parent: _NodeBase | None = None,
        transform: AffineMatrix3D = DEFAULT_AFFINEMATRIX,
        material: Material = DEFAULT_MATERIAL,
        name: str = "",
    ) -> Self:
        """
        Instances a new Mesh using data from a file object or filename.

        The mesh must be stored in a RaySect Mesh (RSM) format file. RSM files
        are created with the Mesh save() method.

        :param object file: File object or string path.
        :param Node parent: Attaches the mesh to the specified scene-graph node.
        :param AffineMatrix3D transform: The co-ordinate transform between the mesh and its parent.
        :param Material material: The surface/volume material.
        :param str name: A human friendly name to identity the mesh in the scene-graph.

        .. code-block:: pycon

            >>> from raysect.optical import World, translate, rotate, ConstantSF, Sellmeier, Dielectric
            >>> from raysect.primitive import Mesh
            >>>
            >>> world = World()
            >>>
            >>> diamond = Dielectric(Sellmeier(0.3306, 4.3356, 0.0, 0.1750**2, 0.1060**2, 0.0), ConstantSF(1.0))
            >>>
            >>> mesh = Mesh.from_file("my_mesh.rsm", parent=world, material=diamond,
            >>>                       transform=translate(0, 0, 0)*rotate(165, 0, 0))

        """
