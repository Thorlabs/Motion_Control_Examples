from typing import Protocol, runtime_checkable

from thorlabs_xa.shared.params import TLMC_ButtonParams

@runtime_checkable
class ButtonParams(Protocol):

    def get_button_params(self, max_wait_in_milliseconds: int) -> TLMC_ButtonParams: ...

    def set_button_params(self, params: TLMC_ButtonParams): ...