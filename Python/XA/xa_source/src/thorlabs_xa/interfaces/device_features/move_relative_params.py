from typing import Protocol, runtime_checkable

from thorlabs_xa.shared.params import TLMC_MoveRelativeParams

@runtime_checkable
class MoveRelativeParams(Protocol):

    def get_move_relative_params(self, max_wait_in_milliseconds: int) -> TLMC_MoveRelativeParams: ...

    def set_move_relative_params(self, params: TLMC_MoveRelativeParams) -> None: ...
