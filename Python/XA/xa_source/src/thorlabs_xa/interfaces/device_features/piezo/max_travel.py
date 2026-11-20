from typing import Protocol, runtime_checkable

@runtime_checkable
class MaxTravel(Protocol):

    def get_max_travel(self, max_wait_in_milliseconds: int) -> int: ...

    def set_max_travel(self, max_travel: int) -> None: ...