from typing import Protocol, runtime_checkable

from thorlabs_xa.shared.enums import TLMC_MoveMode

@runtime_checkable
class Move(Protocol):

    def move(self, move_mode: TLMC_MoveMode, params: int, max_wait_in_milliseconds: int): ...
