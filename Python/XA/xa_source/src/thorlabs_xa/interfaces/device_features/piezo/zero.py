from typing import Protocol, runtime_checkable

@runtime_checkable
class Zero(Protocol):

    def set_zero(self, max_wait_in_milliseconds: int) -> None: ...