from typing import Protocol, runtime_checkable

from thorlabs_xa.shared.enums import TLMC_MoveDirection

@runtime_checkable
class MoveJog(Protocol):

    def move_jog(self, direction: TLMC_MoveDirection, max_wait_in_milliseconds: int) -> None: ...
