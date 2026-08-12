from .base import Function1D, _ScalarOperand1D

class FloatToVector3DFunction1D(Function1D):
    """
    Combines three float.Function1D objects to produce a vector3d.Function1D.

    The three float.Function1D objects correspond to the x, y and z components
    of the resulting vector object.

    :param float.Function1D x_function: the Vx(x) 1d function.
    :param float.Function1D y_function: the Vy(x) 1d function.
    :param float.Function1D z_function: the Vz(x) 1d function.

    .. code-block:: pycon

       >>> from raysect.core.math.function.float import Sqrt1D, Exp1D, Arg1D
       >>> from raysect.core.math.function.vector3d import FloatToVector3DFunction1D
       >>>
       >>> vx = 1  # Will be auto-wrapped to Constant1D(1)
       >>> vy = Arg1D('y')
       >>> vz = Sqrt1D(Arg1D('x'))
       >>>
       >>> fv = FloatToVector3DFunction1D(vx, vy, vz)
       >>> fv(4.0, 6.2)
       Vector3D(1.0, 6.2, 2.0)
    """

    def __init__(self, x_function: _ScalarOperand1D, y_function: _ScalarOperand1D, z_function: _ScalarOperand1D) -> None: ...
