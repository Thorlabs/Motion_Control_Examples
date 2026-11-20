from typing import Protocol, runtime_checkable

from thorlabs_xa.shared.params import TLMC_PZIM_StageSelectParams

@runtime_checkable
class StageSelectParams(Protocol):

    def set_stage_select_params(self, params: TLMC_PZIM_StageSelectParams) -> None:...