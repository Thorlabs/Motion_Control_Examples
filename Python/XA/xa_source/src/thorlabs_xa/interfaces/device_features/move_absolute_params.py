from typing import Protocol, runtime_checkable

from thorlabs_xa.shared.params import TLMC_MoveAbsoluteParams

@runtime_checkable
class MoveAbsoluteParams(Protocol):

    def get_move_absolute_params(self, max_wait_in_milliseconds: int) -> TLMC_MoveAbsoluteParams: ...

    def set_move_absolute_params(self, params: TLMC_MoveAbsoluteParams) -> None: ...