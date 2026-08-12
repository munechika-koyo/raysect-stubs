from numpy.typing import ArrayLike

from ..base import Function2D

class Interpolator2DMesh(Function2D):
    """
    Linear interpolator for data on a 2d ungridded tri-poly mesh.

    The mesh is specified as a set of 2D vertices supplied as an Nx2 numpy
    array or a suitably sized sequence that can be converted to a numpy array.

    The mesh triangles are defined with a Mx3 array where the three values are
    indices into the vertex array that specify the triangle vertices. The
    mesh must not contain overlapping triangles. Supplying a mesh with
    overlapping triangles will result in undefined behaviour.

    A data array of length N, containing a value for each vertex, holds the
    data to be interpolated across the mesh.

    By default, requesting a point outside the bounds of the mesh will cause
    a ValueError exception to be raised. If this is not desired the limit
    attribute (default True) can be set to False. When set to False, a default
    value will be returned for any point lying outside the mesh. The value
    return can be specified by setting the default_value attribute (default is
    0.0).

    To optimise the lookup of triangles, the interpolator builds an
    acceleration structure (a KD-Tree) from the specified mesh data. Depending
    on the size of the mesh, this can be quite slow to construct. If the user
    wishes to interpolate a number of different data sets across the same mesh
    - for example: temperature and density data that are both defined on the
    same mesh - then the user can use the instance() method on an existing
    interpolator to create a new interpolator. The new interpolator will shares
    a copy of the internal acceleration data. The vertex_data, limit and
    default_value can be customised for the new instance. See instance(). This
    will avoid the cost in memory and time of rebuilding an identical
    acceleration structure.

    :param ndarray vertex_coords: An array of vertex coordinates (x, y) with shape Nx2.
    :param ndarray vertex_data: An array containing data for each vertex of shape Nx1.
    :param ndarray triangles: An array of vertex indices defining the mesh triangles, with shape Mx3.
    :param bool limit: Raise an exception outside mesh limits - True (default) or False.
    :param float default_value: The value to return outside the mesh limits if limit is set to False.
    """

    def __init__(
        self,
        vertex_coords: ArrayLike,
        vertex_data: ArrayLike,
        triangles: ArrayLike,
        limit: bool = True,
        default_value: float = 0.0,
    ) -> None: ...
    @classmethod
    def instance(
        cls,
        instance: Interpolator2DMesh,
        vertex_data: ArrayLike | None = None,
        limit: bool | None = None,
        default_value: float | None = None,
    ) -> Interpolator2DMesh:
        """
        Creates a new interpolator instance from an existing interpolator instance.

        The new interpolator instance will share the same internal acceleration
        data as the original interpolator. The vertex_data, limit and default_value
        settings of the new instance can be redefined by setting the appropriate
        attributes. If any of the attributes are set to None (default) then the
        value from the original interpolator will be copied.

        This method should be used if the user has multiple sets of vertex_data
        that lie on the same mesh geometry. Using this methods avoids the
        repeated rebuilding of the mesh acceleration structures by sharing the
        geometry data between multiple interpolator objects.

        :param Interpolator2DMesh instance: Interpolator2DMesh object.
        :param ndarray vertex_data: An array containing data for each vertex of shape Nx1 (default None).
        :param bool limit: Raise an exception outside mesh limits - True (default) or False (default None).
        :param float default_value: The value to return outside the mesh limits if limit is set to False (default None).
        :return: An Interpolator2DMesh object.
        :rtype: Interpolator2DMesh
        """
