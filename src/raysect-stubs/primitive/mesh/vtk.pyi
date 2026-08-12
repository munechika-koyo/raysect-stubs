from typing import Any, Literal

from numpy.typing import ArrayLike

from .mesh import Mesh

VTK_AUTOMATIC: Literal["auto"] = "auto"
VTK_ASCII: Literal["ascii"] = "ascii"
VTK_BINARY: Literal["binary"] = "binary"

class VTKHandler:
    @classmethod
    def import_vtk(
        cls,
        filename: str,
        scaling: float = 1.0,
        mode: Literal["auto", "ascii", "binary"] = VTK_AUTOMATIC,
        **kwargs: Any,
    ) -> Mesh:
        """
        Create a mesh instance from a VTK mesh data file (.vtk).

        .. warning ::
           Currently only supports VTK DataFile v2.0 and unstructured grid data with
           3 element (triangular) cells.

        :param str filename: Mesh file path.
        :param double scaling: Scale the mesh by this factor (default=1.0).
        :param str mode: The file format to load: 'ascii', 'binary', 'auto' (default='auto').
        :param kwargs: Accepts optional keyword arguments from the Mesh class.
        :rtype: Mesh
        """
    @classmethod
    def export_vtk(
        cls,
        mesh: Mesh,
        filename: str,
        triangle_data: dict[str, ArrayLike] | None = None,
        vertex_data: dict[str, ArrayLike] | None = None,
        mode: Literal["ascii", "binary"] = VTK_ASCII,
    ) -> None:
        """
        Write a mesh instance to a vtk mesh file (.vtk) with optional cell and point data.

        :param Mesh mesh: The Raysect mesh instance to write as VTK.
        :param str filename: Mesh file path.
        :param dict triangle_data: A dictionary of triangle face datasets to be saved along with the
          mesh. The dictionary keys will be the variable names. Each array must be 1D with length
          equal to the number of triangles in the mesh.
        :param dict vertex_data: A dictionary of vertex datasets to be saved along with the
          mesh. The dictionary keys will be the variable names. Each array must be 1D with length
          equal to the number of vertices in the mesh.
        :param str mode: The file format to write: 'ascii' or 'binary' (default='ascii').
        """

def import_vtk(
    filename: str,
    scaling: float = 1.0,
    mode: Literal["auto", "ascii", "binary"] = VTK_AUTOMATIC,
    **kwargs: Any,
) -> Mesh:
    """
    Create a mesh instance from a VTK mesh data file (.vtk).

    .. warning ::
       Currently only supports VTK DataFile v2.0 and unstructured grid data with
       3 element (triangular) cells.

    :param str filename: Mesh file path.
    :param double scaling: Scale the mesh by this factor (default=1.0).
    :param str mode: The file format to load: 'ascii', 'binary', 'auto' (default='auto').
    :param kwargs: Accepts optional keyword arguments from the Mesh class.
    :rtype: Mesh
    """

def export_vtk(
    mesh: Mesh,
    filename: str,
    triangle_data: dict[str, ArrayLike] | None = None,
    vertex_data: dict[str, ArrayLike] | None = None,
    mode: Literal["ascii", "binary"] = VTK_ASCII,
) -> None:
    """
    Write a mesh instance to a vtk mesh file (.vtk) with optional cell and point data.

    :param Mesh mesh: The Raysect mesh instance to write as VTK.
    :param str filename: Mesh file path.
    :param dict triangle_data: A dictionary of triangle face datasets to be saved along with the
      mesh. The dictionary keys will be the variable names. Each array must be 1D with length
      equal to the number of triangles in the mesh.
    :param dict vertex_data: A dictionary of vertex datasets to be saved along with the
      mesh. The dictionary keys will be the variable names. Each array must be 1D with length
      equal to the number of vertices in the mesh.
    :param str mode: The file format to write: 'ascii' or 'binary' (default='ascii').
    """
