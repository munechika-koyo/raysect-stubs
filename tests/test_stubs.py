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
import numpy as np
from numpy.typing import NDArray
from raysect.core.math import AffineMatrix3D, Vector3D, Point3D, triangulate2d
from raysect.core.math.function.float import Constant1D as Scalar1D
from raysect.core.math.function.float import Constant2D as Scalar2D
from raysect.core.math.function.float import Constant3D as Scalar3D
from raysect.core.math.function.float.function1d.base import (
    AbsFunction1D,
    AddScalar1D,
    EqualsScalar1D,
    GreaterEqualsScalar1D,
    GreaterThanScalar1D,
    LessEqualsScalar1D,
    LessThanScalar1D,
    ModuloFunction1D,
    ModuloFunctionScalar1D,
    ModuloScalarFunction1D,
    NotEqualsScalar1D,
)
from raysect.core.math.function.vector3d import Constant1D as Vector1D
from raysect.core.math.function.vector3d import Constant2D as Vector2D
from raysect.core.math.function.vector3d import Constant3D as Vector3DField
from raysect.core.math.function.vector3d.function1d.base import MultiplyFunction1D as VectorMultiply1D
from raysect.core.math.function.vector3d.function2d.base import MultiplyFunction2D as VectorMultiply2D
from raysect.core.math.function.vector3d.function3d.base import MultiplyFunction3D as VectorMultiply3D
from typing_extensions import assert_type

v1 = Vector3D(1.0, 2.0, 3.0)
v2 = Vector3D(4.0, 5.0, 6.0)
p1 = Point3D(0.0, 0.0, 0.0)

# These should be valid operations
v3 = v1 + v2
v4 = v1 * 2.0
dot_product = v1.dot(v2)
cross_product = v1.cross(v2)
p2 = p1 + v1
assert_type(AffineMatrix3D() * v1, Vector3D)
assert_type(
    triangulate2d([[0.0, 0.0], [0.0, 1.0], [1.0, 1.0], [1.0, 0.0]]),
    NDArray[np.int32],
)
scalar1d = Scalar1D(2.0)
assert_type(scalar1d * Vector1D(v1), VectorMultiply1D)
assert_type(scalar1d - 1.0, AddScalar1D)
assert_type(3.0 % scalar1d, ModuloScalarFunction1D)
assert_type(scalar1d == 3.0, EqualsScalar1D)
assert_type(scalar1d != 3.0, NotEqualsScalar1D)
assert_type(scalar1d < 3.0, GreaterThanScalar1D)
assert_type(scalar1d <= 3.0, GreaterEqualsScalar1D)
assert_type(scalar1d > 3.0, LessThanScalar1D)
assert_type(scalar1d >= 3.0, LessEqualsScalar1D)
assert_type(abs(scalar1d), AbsFunction1D)
assert_type(AbsFunction1D(2.0), AbsFunction1D)
assert_type(
    pow(scalar1d, 2.0, 3.0),
    ModuloFunction1D | ModuloFunctionScalar1D,
)
assert_type(Scalar2D(2.0) * Vector2D(v1), VectorMultiply2D)
assert_type(Scalar3D(2.0) * Vector3DField(v1), VectorMultiply3D)
        """,
        ]
    )

    stdout, stderr, exit_status = result
    assert exit_status == 0, f"MyPy errors: {stdout}"


def test_invalid_math_operations():
    """Test that unsupported math operations are rejected."""
    result = api.run(
        [
            "--no-error-summary",
            "--show-error-codes",
            "-c",
            """
from raysect.core.math import AffineMatrix3D, Point2D

AffineMatrix3D() * Point2D()
        """,
        ]
    )

    stdout, stderr, exit_status = result
    assert not stderr
    assert exit_status == 1
    assert "[operator]" in stdout


def test_colour_conversion_buffers():
    """Test CIE XYZ sample buffer types."""
    result = api.run(
        [
            "--no-error-summary",
            "--show-error-codes",
            "-c",
            """
from typing_extensions import assert_type

from raysect.optical import Spectrum
from raysect.optical.colour import resample_ciexyz, spectrum_to_ciexyz

samples = resample_ciexyz(400.0, 700.0, 10)
assert_type(samples, memoryview)
assert_type(
    spectrum_to_ciexyz(Spectrum(400.0, 700.0, 10), samples),
    tuple[float, float, float],
)
        """,
        ]
    )

    stdout, stderr, exit_status = result
    assert not stderr
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
