from typing import Protocol, runtime_checkable

@runtime_checkable
class NanoTrakCircleDiameter(Protocol):

    def set_nano_trak_circle_diameter(self, circle_diameter: int) -> None: ...