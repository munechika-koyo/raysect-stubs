from numpy.typing import ArrayLike

from ..base import Function3D

class Discrete3DMesh(Function3D):
    """
    Discrete interpolator for data on a 3d ungridded tetrahedra mesh.

    The mesh is specified as a set of 3D vertices supplied as an Nx3 numpy
    array or a suitably sized sequence that can be converted to a numpy array.

    The mesh tetrahedra are defined with a Mx4 array where the four values are
    indices into the vertex array that specify the tetrahedra vertices. The
    mesh must not contain overlapping tetrahedra. Supplying a mesh with
    overlapping tetrahedra will result in undefined behaviour.

    A data array of length M, containing a value for each tetrahedra, holds the
    data to be interpolated across the mesh.

    By default, requesting a point outside the bounds of the mesh will cause
    a ValueError exception to be raised. If this is not desired the limit
    attribute (default True) can be set to False. When set to False, a default
    value will be returned for any point lying outside the mesh. The value
    return can be specified by setting the default_value attribute (default is
    0.0).

    To optimise the lookup of tetrahedra, the interpolator builds an
    acceleration structure (a KD-Tree) from the specified mesh data. Depending
    on the size of the mesh, this can be quite slow to construct. If the user
    wishes to interpolate a number of different data sets across the same mesh
    - for example: temperature and density data that are both defined on the
    same mesh - then the user can use the instance() method on an existing
    interpolator to create a new interpolator. The new interpolator will shares
    a copy of the internal acceleration data. The tetrahedra_data, limit and
    default_value can be customised for the new instance. See instance(). This
    will avoid the cost in memory and time of rebuilding an identical
    acceleration structure.

    :param ndarray vertex_coords: An array of vertex coordinates (x, y, z) with shape Nx3.
    :param ndarray tetrahedra: An array of vertex indices defining the mesh tetrahedra, with shape Mx4.
    :param ndarray tetrahedra_data: An array containing data for each tetrahedra of shape Mx1.
    :param bool limit: Raise an exception outside mesh limits - True (default) or False.
    :param float default_value: The value to return outside the mesh limits if limit is set to False.
    """

    def __init__(
        self,
        vertex_coords: ArrayLike,
        tetrahedra: ArrayLike,
        tetrahedra_data: ArrayLike,
        limit: bool = True,
        default_value: float = 0.0,
    ) -> None: ...
    @classmethod
    def instance(
        cls,
        instance: Discrete3DMesh,
        tetrahedra_data: ArrayLike | None = None,
        limit: bool | None = None,
        default_value: float | None = None,
    ) -> Discrete3DMesh: ...
