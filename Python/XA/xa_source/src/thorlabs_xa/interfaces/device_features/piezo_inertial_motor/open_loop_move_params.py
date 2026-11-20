from typing import Protocol, runtime_checkable

from thorlabs_xa.shared.params import TLMC_PZIM_OpenLoopMoveParams

@runtime_checkable
class OpenLoopMoveParams(Protocol):

    def get_open_loop_move_params(self, max_wait_in_milliseconds: int) -> TLMC_PZIM_OpenLoopMoveParams:...

    def set_open_loop_move_params(self, params: TLMC_PZIM_OpenLoopMoveParams) -> None:...
