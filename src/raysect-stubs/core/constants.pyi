from .math import AffineMatrix3D, Point3D, Vector3D

# coordinate system vectors
UP = Vector3D(0, 1, 0)
"""Up direction Vector3D(0, 1, 0) in Raysect's right-handed coordinate system."""
DOWN = Vector3D(0, -1, 0)
"""Down direction Vector3D(0, -1, 0) in Raysect's right-handed coordinate system."""
LEFT = Vector3D(1, 0, 0)
"""Left direction Vector3D(1, 0, 0) in Raysect's right-handed coordinate system."""
RIGHT = Vector3D(-1, 0, 0)
"""Right direction Vector3D(-1, 0, 0) in Raysect's right-handed coordinate system."""
FORWARD = Vector3D(0, 0, 1)
"""Forward direction Vector3D(0, 0, 1) in Raysect's right-handed coordinate system."""
BACK = Vector3D(0, 0, -1)
"""Back direction Vector3D(0, 0, -1) in Raysect's right-handed coordinate system."""
ORIGIN = Point3D()
"""Origin point Point3D(0, 0, 0) in Raysect's right-handed coordinate system."""

# affine matrix representing no transform
NULL_TRANSFORM = AffineMatrix3D()
"""AffineMatrix3D() representing the null transform (no transformation)."""
