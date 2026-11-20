from typing import Protocol, runtime_checkable

@runtime_checkable
class PositionCounter(Protocol):

    def get_position_counter(self, max_wait_in_milliseconds: int) -> int: ...

    def set_position_counter(self, new_position_counter: int) -> None: ...