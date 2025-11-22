from abc import abstractmethod

from .node import Node

class Observer(Node):
    """
    A scene-graph class for observing the world.

    An observer class is intended to launch rays and sample the world. This is a base class and the observe function
    must be implemented by a deriving class. This object is the fundamental abstraction for items such as cameras,
    fibre optics and other sampling objects.
    """
    @abstractmethod
    def observe(self) -> None:
        """
        Virtual method - to be implemented by derived classes.

        Triggers the exploration of the scene by emitting rays according to
        the model defined by the derived class implementing the method.
        """
