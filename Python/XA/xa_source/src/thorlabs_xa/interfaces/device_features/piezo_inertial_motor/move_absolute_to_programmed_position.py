from typing import Protocol, runtime_checkable

@runtime_checkable
class MoveAbsoluteToProgrammedPosition(Protocol):

    def move_absolute_to_programmed_position(self, max_wait_in_milliseconds: int) -> None: ...
