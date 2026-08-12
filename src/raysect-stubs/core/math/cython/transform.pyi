"""
Cython utility functions for generating coordinate transforms.

These functions can not be called from Python directly.

.. WARNING:: For speed, none of these functions perform any type or bounds
   checking. Supplying malformed data may result in data corruption or a
   segmentation fault.
"""
