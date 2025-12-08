from typing import Literal, overload

from ..point import Point3D

class SurfaceSampler3D:
    """
    Base class for an object that generates samples from a surface in 3D.
    """

    @overload
    def __call__(self, samples: None = None, pdf: Literal[False] = False) -> Point3D: ...
    @overload
    def __call__(self, samples: int, pdf: Literal[False] = False) -> list[Point3D]: ...
    @overload
    def __call__(self, samples: None = None, pdf: Literal[True] = True) -> tuple[Point3D, float]: ...
    @overload
    def __call__(self, samples: int, pdf: Literal[True] = True) -> list[tuple[Point3D, float]]: ...
    def __call__(self, samples: int | None = None, pdf: bool = False) -> Point3D | tuple[Point3D, float] | list[Point3D] | list[tuple[Point3D, float]]:
        """
        If samples is not provided, returns a single Point3D sample from
        the distribution. If samples is set to a value then a number of
        samples equal to the value specified is returned in a list.

        If pdf is set to True the Point3D sample is returned inside a tuple
        with its associated pdf value as the second element.

        :param int samples: Number of points to generate (default=None).
        :param bool pdf: Toggle for returning associated sample pdfs (default=False).
        :return: A Point3D, tuple or list.
        """

class DiskSampler3D(SurfaceSampler3D):
    """
    Generates Point3D samples from a disk centred in the x-y plane.

    :param double radius: The radius of the disk in metres (default=1).

    .. code-block:: pycon

        >>> from raysect.core.math import DiskSampler3D
        >>>
        >>> disk_sampler = DiskSampler3D()
        >>> disk_sampler(2)
        [Point3D(-0.8755314944066419, -0.36748751614554004, 0.0),
         Point3D(-0.7515341075950953, 0.15368157833817775, 0.0)]
    """

    radius: float
    area: float
    _area_inv: float

    def __init__(self, radius: float = 1.0) -> None: ...

class RectangleSampler3D(SurfaceSampler3D):
    """
    Generates Point3D samples from a rectangle centred in the x-y plane.

    :param double width: The width of the rectangle.
    :param double height: The height of the rectangle.

    .. code-block:: pycon

        >>> from raysect.core.math import RectangleSampler3D
        >>>
        >>> rectangle_sampler = RectangleSampler3D(width=3, height=3)
        >>> rectangle_sampler(2)
        [Point3D(0.8755185034767394, -1.4596971179451579, 0.0),
         Point3D(1.3514601271010727, 0.9710083493215418, 0.0)]
    """

    width: float
    height: float
    area: float
    _area_inv: float
    _width_offset: float
    _height_offset: float

    def __init__(self, width: float = 1.0, height: float = 1.0) -> None: ...

class TriangleSampler3D(SurfaceSampler3D):
    """
    Generates Point3D samples from a triangle in 3D space.

    :param Point3D v1: Triangle vertex 1.
    :param Point3D v2: Triangle vertex 2.
    :param Point3D v3: Triangle vertex 3.

    .. code-block:: pycon

        >>> from raysect.core.math import TriangleSampler3D
        >>>
        >>> tri_sampler = TriangleSampler3D(Point3D(0,0,0),
                                            Point3D(1,0,0),
                                            Point3D(1,1,0))
        >>> tri_sampler(2)
        [Point3D(0.9033819087428726, 0.053382913976399715, 0.0),
         Point3D(0.857350441035813, 0.4243360393025779, 0.0)]

    """

    v1: Point3D
    v2: Point3D
    v3: Point3D
    area: float
    _area_inv: float

    def __init__(self, v1: Point3D, v2: Point3D, v3: Point3D) -> None: ...
