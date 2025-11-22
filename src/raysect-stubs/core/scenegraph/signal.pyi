class ChangeSignal:
    """
    Scene-graph change signal class.

    All scene-graph signals must be unique instances of this class.
    """
    def __init__(self, name: str) -> None: ...
    def __repr__(self) -> str: ...

GEOMETRY: ChangeSignal
MATERIAL: ChangeSignal
