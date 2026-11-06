from typing import Protocol, runtime_checkable

from thorlabs_xa.shared.params import TLMC_PZIM_ClosedLoopMoveParams

@runtime_checkable
class ClosedLoopMoveParams(Protocol):

    def get_closed_loop_move_params(self, max_wait_in_milliseconds: int) -> TLMC_PZIM_ClosedLoopMoveParams:...

    def set_closed_loop_move_params(self, params: TLMC_PZIM_ClosedLoopMoveParams) -> None:...
