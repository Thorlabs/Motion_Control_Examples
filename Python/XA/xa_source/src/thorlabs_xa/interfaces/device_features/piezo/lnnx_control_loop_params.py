from typing import Protocol, runtime_checkable

from thorlabs_xa.shared.params import TLMC_PZ_LnnxControlLoopParams

@runtime_checkable
class LnnxControlLoopParams(Protocol):

    def get_control_loop_params(self, max_wait_in_milliseconds: int) -> TLMC_PZ_LnnxControlLoopParams:...

    def set_control_loop_params(self, params: TLMC_PZ_LnnxControlLoopParams) -> None:...