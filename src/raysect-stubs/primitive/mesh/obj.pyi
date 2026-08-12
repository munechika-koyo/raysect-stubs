from typing import Any

from .mesh import Mesh

class OBJHandler:
    @classmethod
    def import_obj(cls, filename: str, scaling: float = 1.0, **kwargs: Any) -> Mesh:
        """
        Create a mesh instance from a Wavefront OBJ mesh file (.obj).

        :param str filename: Mesh file path.
        :param double scaling: Scale the mesh by this factor (default=1.0).
        :param kwargs: Accepts optional keyword arguments from the Mesh class.
        :rtype: Mesh

        .. code-block:: pycon

            >>> from raysect.optical import World, translate, rotate, ConstantSF, Sellmeier, Dielectric
            >>> from raysect.primitive import import_obj
            >>>
            >>> world = World()
            >>>
            >>> diamond = Dielectric(Sellmeier(0.3306, 4.3356, 0.0, 0.1750**2, 0.1060**2, 0.0),
            >>>                      ConstantSF(1.0))
            >>>
            >>> bunny_mesh = import_obj("resources/stanford_bunny.obj", scaling=1, parent=world,
            >>>                         transform=translate(0, 0, 0)*rotate(165, 0, 0), material=diamond)
        """
    @classmethod
    def export_obj(cls, mesh: Mesh, filename: str) -> None:
        """
        Write a mesh instance to a Wavefront OBJ (.obj) mesh file.

        :param Mesh mesh: The Raysect mesh instance to write to OBJ.
        :param str filename: Mesh file path.

        .. code-block:: pycon

            >>> bunny_mesh
            <raysect.primitive.mesh.mesh.Mesh at 0x7f2c09eac2e8>
            >>> from raysect.primitive import export_obj
            >>> export_obj(bunny_mesh, 'my_mesh.obj')
        """

def import_obj(filename: str, scaling: float = 1.0, **kwargs: Any) -> Mesh:
    """
    Create a mesh instance from a Wavefront OBJ mesh file (.obj).

    :param str filename: Mesh file path.
    :param double scaling: Scale the mesh by this factor (default=1.0).
    :param kwargs: Accepts optional keyword arguments from the Mesh class.
    :rtype: Mesh

    .. code-block:: pycon

        >>> from raysect.optical import World, translate, rotate, ConstantSF, Sellmeier, Dielectric
        >>> from raysect.primitive import import_obj
        >>>
        >>> world = World()
        >>>
        >>> diamond = Dielectric(Sellmeier(0.3306, 4.3356, 0.0, 0.1750**2, 0.1060**2, 0.0),
        >>>                      ConstantSF(1.0))
        >>>
        >>> bunny_mesh = import_obj("resources/stanford_bunny.obj", scaling=1, parent=world,
        >>>                         transform=translate(0, 0, 0)*rotate(165, 0, 0), material=diamond)
    """

def export_obj(mesh: Mesh, filename: str) -> None:
    """
    Write a mesh instance to a Wavefront OBJ (.obj) mesh file.

    :param Mesh mesh: The Raysect mesh instance to write to OBJ.
    :param str filename: Mesh file path.

    .. code-block:: pycon

        >>> bunny_mesh
        <raysect.primitive.mesh.mesh.Mesh at 0x7f2c09eac2e8>
        >>> from raysect.primitive import export_obj
        >>> export_obj(bunny_mesh, 'my_mesh.obj')
    """
