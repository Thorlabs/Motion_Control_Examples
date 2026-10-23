from typing import Protocol, runtime_checkable

from thorlabs_xa.shared.params import TLMC_PZ_PositionLoopParams

@runtime_checkable
class PositionLoopParams(Protocol):

    def get_position_loop_params(self, max_wait_in_milliseconds: int) -> TLMC_PZ_PositionLoopParams: ...

    def set_position_loop_params(self, params: TLMC_PZ_PositionLoopParams) -> None: ...