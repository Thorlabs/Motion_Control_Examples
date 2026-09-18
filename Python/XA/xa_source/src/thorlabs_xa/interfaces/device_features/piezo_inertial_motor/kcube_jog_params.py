from typing import Protocol, runtime_checkable

from thorlabs_xa.shared.params import TLMC_PZIM_KcubeJogParams

@runtime_checkable
class KcubeJogParams(Protocol):

    def get_kcube_jog_params(self, max_wait_in_milliseconds: int) -> TLMC_PZIM_KcubeJogParams:...

    def set_kcube_jog_params(self, params: TLMC_PZIM_KcubeJogParams) -> None:...