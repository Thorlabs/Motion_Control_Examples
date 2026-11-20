from typing import Protocol, runtime_checkable

from thorlabs_xa.shared.params import TLMC_LcdDisplayParams

@runtime_checkable
class LcdDisplayParams(Protocol):

    def get_lcd_display_params(self, max_wait_in_milliseconds: int) -> TLMC_LcdDisplayParams: ...

    def set_lcd_display_params(self, params: TLMC_LcdDisplayParams) -> None: ...