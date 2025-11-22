from ..core.constants import FORWARD, ORIGIN
from ..core.intersection import Intersection
from ..core.math import Point3D, Vector3D
from .ray import Ray
from .scenegraph.world import World
from .spectrum import Spectrum

class LoggingRay(Ray):
    log: list[Intersection]
    def __init__(
        self,
        origin: Point3D = ORIGIN,
        direction: Vector3D = FORWARD,
        min_wavelength: float = 375,
        max_wavelength: float = 785,
        bins: int = 40,
        max_distance: float = float("inf"),
        extinction_prob: float = 0.1,
        extinction_min_depth: int = 3,
        max_depth: int = 100,
        importance_sampling: bool = True,
        important_path_weight: float = 0.25,
    ) -> None: ...
    def trace(self, world: World, keep_alive: bool = False) -> Spectrum:
        """
        Traces a single ray path through the world.

        :param world: World object defining the scene.
        :param keep_alive: If true, disables Russian roulette termination of the ray.
        :return: A Spectrum object.
        """
    def spawn_daughter(self, origin: Point3D, direction: Vector3D) -> LoggingRay:
        """
        Spawns a new daughter of the ray.

        A daughter ray has the same spectral configuration as the source ray,
        however the ray depth is increased by 1.

        :param origin: A Point3D defining the ray origin.
        :param direction: A vector defining the ray direction.
        :return: A Ray object.
        """
    def copy(self, origin: Point3D | None = None, direction: Vector3D | None = None) -> LoggingRay: ...
    @property
    def path_vertices(self) -> list[Point3D]: ...
