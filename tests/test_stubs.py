"""Tests for raysect stubs."""

from mypy import api


def test_basic_import_stubs():
    """Test that basic imports work with stubs."""
    result = api.run(
        [
            "--no-error-summary",
            "--show-error-codes",
            "-c",
            """
import raysect
from raysect.core.math import Vector3D, Point3D
from raysect.core.scenegraph import World, Node
from raysect.primitive import Sphere
from raysect.optical import Ray, Spectrum

# Test basic usage
world = World()
vector = Vector3D(1.0, 2.0, 3.0)
point = Point3D(0.0, 0.0, 0.0)
sphere = Sphere(radius=1.0, parent=world)
        """,
        ]
    )

    stdout, stderr, exit_status = result
    assert exit_status == 0, f"MyPy errors: {stdout}"


def test_math_operations():
    """Test math operations type checking."""
    result = api.run(
        [
            "--no-error-summary",
            "--show-error-codes",
            "-c",
            """
from raysect.core.math import Vector3D, Point3D

v1 = Vector3D(1.0, 2.0, 3.0)
v2 = Vector3D(4.0, 5.0, 6.0)
p1 = Point3D(0.0, 0.0, 0.0)

# These should be valid operations
v3 = v1 + v2
v4 = v1 * 2.0
dot_product = v1.dot(v2)
cross_product = v1.cross(v2)
p2 = p1 + v1
        """,
        ]
    )

    stdout, stderr, exit_status = result
    assert exit_status == 0, f"MyPy errors: {stdout}"


def test_private_subclass_extension_hooks():
    """Test that protected Python extension hooks carry override type information."""
    result = api.run(
        [
            "--no-error-summary",
            "--show-error-codes",
            "-c",
            """
from typing_extensions import override

from raysect.core.math import Point3D
from raysect.core.math.spatial import KDTree3D
from raysect.core.ray import Ray as CoreRay
from raysect.core.scenegraph import Node
from raysect.optical import Ray
from raysect.optical.observer import Observer2D

class CustomNode(Node):
    @override
    def _modified(self) -> None:
        pass

class CustomKDTree(KDTree3D):
    @override
    def _trace_items(self, item_ids: list[int], ray: CoreRay, max_range: float) -> bool:
        return False

    @override
    def _items_containing_items(self, item_ids: list[int], point: Point3D) -> list[int]:
        return []

class CustomObserver(Observer2D):
    @override
    def _generate_rays(self, x: int, y: int, template: Ray, ray_count: int) -> list[tuple[Ray, float]]:
        return []

    @override
    def _pixel_sensitivity(self, x: int, y: int) -> float:
        return 1.0
        """,
        ]
    )

    stdout, stderr, exit_status = result
    assert exit_status == 0, f"MyPy errors: {stdout}"


if __name__ == "__main__":
    test_basic_import_stubs()
    test_math_operations()
    print("All stub tests passed!")
