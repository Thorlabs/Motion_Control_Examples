from typing import Protocol, runtime_checkable

from thorlabs_xa.shared.params import TLMC_GeneralMoveParams

@runtime_checkable
class GeneralMoveParams(Protocol):

    def get_general_move_params(self, max_wait_in_milliseconds: int) -> TLMC_GeneralMoveParams: ...

    def set_general_move_params(self, params: TLMC_GeneralMoveParams) -> None: ...