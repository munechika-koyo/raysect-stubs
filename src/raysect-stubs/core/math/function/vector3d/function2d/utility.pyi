from .base import Function2D, _ScalarOperand2D

class FloatToVector3DFunction2D(Function2D):
    """
    Combines three float.Function2D objects to produce a vector3d.Function2D.

    The three float.Function2D objects correspond to the x, y and z components
    of the resulting vector object.

    :param float.Function2D x_function: the Vx(x, y) 2d function.
    :param float.Function2D y_function: the Vy(x, y) 2d function.
    :param float.Function2D z_function: the Vz(x, y) 2d function.

    .. code-block:: pycon

       >>> from raysect.core.math.function.float import Sqrt2D, Exp2D, Arg2D
       >>> from raysect.core.math.function.vector3d import FloatToVector3DFunction2D
       >>>
       >>> vx = 1  # Will be auto-wrapped to Constant2D(1)
       >>> vy = Arg2D('y')
       >>> vz = Sqrt2D(Arg2D('x'))
       >>>
       >>> fv = FloatToVector3DFunction2D(vx, vy, vz)
       >>> fv(4.0, 6.2)
       Vector3D(1.0, 6.2, 2.0)
    """

    def __init__(self, x_function: _ScalarOperand2D, y_function: _ScalarOperand2D, z_function: _ScalarOperand2D) -> None: ...
