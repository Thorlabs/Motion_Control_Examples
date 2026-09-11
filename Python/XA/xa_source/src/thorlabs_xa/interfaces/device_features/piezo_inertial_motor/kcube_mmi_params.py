from typing import Protocol, runtime_checkable

from thorlabs_xa.shared.params import TLMC_PZIM_KcubeMmiParams

@runtime_checkable
class KcubeMmiParams(Protocol):

    def get_kcube_mmi_params(self, max_wait_in_milliseconds: int) -> TLMC_PZIM_KcubeMmiParams:...

    def set_kcube_mmi_params(self, params: TLMC_PZIM_KcubeMmiParams) -> None:...