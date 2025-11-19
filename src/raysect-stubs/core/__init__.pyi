"""Core module type stubs."""

from typing import Any, Optional, TypeAlias, Union

Number: TypeAlias = int | float

# Re-exports from core submodules
from .acceleration import *
from .math import *
from .scenegraph import *
