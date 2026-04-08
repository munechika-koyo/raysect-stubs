class FrameSampler1D:
    """
    Base class for 1D frame samplers.
    """

    def generate_tasks(self, pixels: int) -> list[tuple[int]]:
        """
        Generates a list of tuples that selects the pixels to render.

        Must return a list of tuples where each tuple contains the id of a pixel
        to render. For example:

            tasks = [(1,), (5,), (512,), ...]

        This is a virtual method and must be implemented in a sub class.

        :param int pixels: The number of pixels in the frame.
        :rtype: list
        """

class FrameSampler2D:
    """
    Base class for 2D frame samplers.
    """

    def generate_tasks(self, pixels: tuple[int, int]) -> list[tuple[int, int]]:
        """
        Generates a list of tuples that selects the pixels to render.

        Must return a list of tuples where each tuple contains the id of a pixel
        to render. For example:

            tasks = [(1, 10), (5, 53), (512, 354), ...]

        This is a virtual method and must be implemented in a sub class.

        :param tuple pixels: Contains the (x, y) pixel dimensions of the frame.
        :rtype: list
        """
