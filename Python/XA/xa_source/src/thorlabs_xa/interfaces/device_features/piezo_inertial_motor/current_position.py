from typing import Protocol, runtime_checkable

@runtime_checkable
class CurrentPosition(Protocol):

    def get_current_position(self, max_wait_in_milliseconds: int) -> int: ...
