from typing import Protocol, runtime_checkable

from thorlabs_xa.shared.params import TLMC_LcdMoveParams

@runtime_checkable
class LcdMoveParams(Protocol):

    def get_lcd_move_params(self, max_wait_in_milliseconds: int) -> TLMC_LcdMoveParams: ...

    def set_lcd_move_params(self, params: TLMC_LcdMoveParams) -> None: ...