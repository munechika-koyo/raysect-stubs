"""Tests for raysect stubs."""

import pytest
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


if __name__ == "__main__":
    test_basic_import_stubs()
    test_math_operations()
    print("All stub tests passed!")
