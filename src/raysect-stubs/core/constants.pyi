from .math import AffineMatrix3D, Point3D, Vector3D

# coordinate system vectors
UP = Vector3D(0, 1, 0)
DOWN = Vector3D(0, -1, 0)
LEFT = Vector3D(1, 0, 0)
RIGHT = Vector3D(-1, 0, 0)
FORWARD = Vector3D(0, 0, 1)
BACK = Vector3D(0, 0, -1)
ORIGIN = Point3D()

# affine matrix representing no transform
NULL_TRANSFORM = AffineMatrix3D()
