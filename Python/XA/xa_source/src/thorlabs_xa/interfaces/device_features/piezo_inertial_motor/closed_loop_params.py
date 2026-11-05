from typing import Protocol, runtime_checkable

from thorlabs_xa.shared.params import TLMC_PZIM_ClosedLoopParams

@runtime_checkable
class ClosedLoopParams(Protocol):

    def get_closed_loop_params(self, max_wait_in_milliseconds: int) -> TLMC_PZIM_ClosedLoopParams:...

    def set_closed_loop_params(self, params: TLMC_PZIM_ClosedLoopParams) -> None:...
