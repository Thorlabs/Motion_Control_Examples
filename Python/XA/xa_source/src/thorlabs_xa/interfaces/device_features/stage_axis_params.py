from typing import Protocol, runtime_checkable

from thorlabs_xa.shared.params import TLMC_StageAxisParams

@runtime_checkable
class StageAxisParams(Protocol):

    def get_stage_axis_params(self, max_wait_in_milliseconds: int) -> TLMC_StageAxisParams: ...

    def set_stage_axis_params(self, params: TLMC_StageAxisParams) -> None: ...