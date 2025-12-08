from ..base import Function

class Vector3DFunction(Function):
    """
    The base class of all functions that return a Vector3D.

    All functions that return a Vector3D derive from this class.
    """
    def __repr__(self) -> str: ...
