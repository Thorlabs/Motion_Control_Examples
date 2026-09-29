from typing import Protocol, runtime_checkable

from thorlabs_xa.shared.params import TLMC_PZ_StageInfoParams

@runtime_checkable
class StageInfoParams(Protocol):

    def get_stage_info_params(self, max_wait_in_milliseconds: int) -> TLMC_PZ_StageInfoParams:...