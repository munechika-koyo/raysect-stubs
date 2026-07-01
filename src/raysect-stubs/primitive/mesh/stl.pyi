from typing import Literal

from .mesh import Mesh

STL_AUTOMATIC = "auto"
STL_ASCII = "ascii"
STL_BINARY = "binary"

class STLHandler:
    @classmethod
    def import_stl(
        cls,
        filename: str,
        scaling: float = 1.0,
        mode: Literal["auto", "ascii", "binary"] = STL_AUTOMATIC,
        **kwargs,
    ) -> Mesh:
        """
        Create a mesh instance from a STereoLithography (STL) mesh file (.stl).

        Some engineering meshes are exported in different units (mm for example)
        whereas Raysect units are in m. Applying a scale factor of 0.001 would
        convert the mesh into m for use in Raysect.

        :param str filename: Mesh file path.
        :param double scaling: Scale the mesh by this factor (default=1.0).
        :param str mode: The file format to load: 'ascii', 'binary', 'auto' (default='auto').
        :param kwargs: Accepts optional keyword arguments from the Mesh class.
        :rtype: Mesh

        .. code-block:: pycon

            >>> from raysect.optical import World, translate, rotate, ConstantSF, Sellmeier, Dielectric
            >>> from raysect.primitive import import_stl
            >>>
            >>> world = World()
            >>>
            >>> diamond = Dielectric(Sellmeier(0.3306, 4.3356, 0.0, 0.1750**2, 0.1060**2, 0.0),
            >>>                      ConstantSF(1.0))
            >>>
            >>> mesh = import_stl("my_mesh.stl", scaling=1, mode='binary', parent=world,
            >>>                   transform=translate(0, 0, 0)*rotate(165, 0, 0), material=diamond)
        """
    @classmethod
    def export_stl(
        cls,
        mesh: Mesh,
        filename: str,
        mode: Literal["ascii", "binary"] = STL_BINARY,
    ) -> None:
        """
        Write a mesh instance to a STereoLithography (STL) mesh file (.stl).

        :param Mesh mesh: The Raysect mesh instance to write to STL.
        :param str filename: Mesh file path.
        :param str mode: The file format to write: 'ascii' or 'binary' (default='binary').

        .. code-block:: pycon

            >>> mesh
            <raysect.primitive.mesh.mesh.Mesh at 0x7f2c09eac2e8>
            >>> from raysect.primitive import export_stl
            >>> export_stl(mesh, 'my_mesh.stl', mode='ascii')

        """

def import_stl(
    filename: str,
    scaling: float = 1.0,
    mode: Literal["auto", "ascii", "binary"] = STL_AUTOMATIC,
    **kwargs,
) -> Mesh:
    """
    Create a mesh instance from a STereoLithography (STL) mesh file (.stl).

    Some engineering meshes are exported in different units (mm for example)
    whereas Raysect units are in m. Applying a scale factor of 0.001 would
    convert the mesh into m for use in Raysect.

    :param str filename: Mesh file path.
    :param double scaling: Scale the mesh by this factor (default=1.0).
    :param str mode: The file format to load: 'ascii', 'binary', 'auto' (default='auto').
    :param kwargs: Accepts optional keyword arguments from the Mesh class.
    :rtype: Mesh

    .. code-block:: pycon

        >>> from raysect.optical import World, translate, rotate, ConstantSF, Sellmeier, Dielectric
        >>> from raysect.primitive import import_stl
        >>>
        >>> world = World()
        >>>
        >>> diamond = Dielectric(Sellmeier(0.3306, 4.3356, 0.0, 0.1750**2, 0.1060**2, 0.0),
        >>>                      ConstantSF(1.0))
        >>>
        >>> mesh = import_stl("my_mesh.stl", scaling=1, mode='binary', parent=world,
        >>>                   transform=translate(0, 0, 0)*rotate(165, 0, 0), material=diamond)
    """

def export_stl(
    mesh: Mesh,
    filename: str,
    mode: Literal["ascii", "binary"] = STL_BINARY,
) -> None:
    """
    Write a mesh instance to a STereoLithography (STL) mesh file (.stl).

    :param Mesh mesh: The Raysect mesh instance to write to STL.
    :param str filename: Mesh file path.
    :param str mode: The file format to write: 'ascii' or 'binary' (default='binary').

    .. code-block:: pycon

        >>> mesh
        <raysect.primitive.mesh.mesh.Mesh at 0x7f2c09eac2e8>
        >>> from raysect.primitive import export_stl
        >>> export_stl(mesh, 'my_mesh.stl', mode='ascii')

    """
