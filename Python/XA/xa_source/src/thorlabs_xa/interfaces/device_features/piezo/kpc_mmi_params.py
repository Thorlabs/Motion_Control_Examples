from typing import Protocol

from thorlabs_xa.shared.params import TLMC_PZ_KpcMmiParams

class KpcMmiParams(Protocol):

    def get_kpc_mmi_params(self, max_wait_in_milliseconds: int) -> TLMC_PZ_KpcMmiParams: ...

    def set_kpc_mmi_params(self, params: TLMC_PZ_KpcMmiParams) -> None: ...