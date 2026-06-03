from typing import Protocol, runtime_checkable

@runtime_checkable
class NanoTrakCircleToHomePosition(Protocol):

    def nano_trak_circle_to_home_position(self) -> None: ...