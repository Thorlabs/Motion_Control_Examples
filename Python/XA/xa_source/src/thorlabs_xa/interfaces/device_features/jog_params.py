from typing import Protocol, runtime_checkable
from thorlabs_xa.shared.params import TLMC_JogParams

@runtime_checkable
class JogParams(Protocol):

    def get_jog_params(self, max_wait_in_milliseconds: int) -> TLMC_JogParams: ...

    def set_jog_params(self, params: TLMC_JogParams) -> None: ...