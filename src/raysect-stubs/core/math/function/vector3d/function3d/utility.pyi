from .base import Function3D, _ScalarOperand3D

class FloatToVector3DFunction3D(Function3D):
    """
    Combines three float.Function3D objects to produce a vector3d.Function3D.

    The three float.Function3D objects correspond to the x, y and z components
    of the resulting vector object.

    :param float.Function3D x_function: the Vx(x, y, z) 3d function.
    :param float.Function3D y_function: the Vy(x, y, z) 3d function.
    :param float.Function3D z_function: the Vz(x, y, z) 3d function.

    .. code-block:: pycon

       >>> from raysect.core.math.function.float import Sqrt3D, Exp3D, Arg3D
       >>> from raysect.core.math.function.vector3d import FloatToVector3DFunction3D
       >>>
       >>> vx = 1  # Will be auto-wrapped to Constant3D(1)
       >>> vy = Arg3D('y')
       >>> vz = Sqrt3D(Arg3D('x'))
       >>>
       >>> fv = FloatToVector3DFunction3D(vx, vy, vz)
       >>> fv(4.0, 6.2)
       Vector3D(1.0, 6.2, 2.0)
    """

    def __init__(self, x_function: _ScalarOperand3D, y_function: _ScalarOperand3D, z_function: _ScalarOperand3D) -> None: ...
