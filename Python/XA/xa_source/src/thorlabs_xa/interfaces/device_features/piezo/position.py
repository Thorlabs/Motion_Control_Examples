from typing import Protocol, runtime_checkable

@runtime_checkable
class Position(Protocol):

    def get_position(self, max_wait_in_milliseconds: int) -> int: ...

    def set_position(self, position: int) -> None: ...