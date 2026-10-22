from typing import Protocol, runtime_checkable

from thorlabs_xa.shared.params import TLMC_PZ_KnaMmiParams

@runtime_checkable
class KnaMmiParams(Protocol):

    def get_kna_mmi_params(self, max_wait_in_milliseconds: int) -> TLMC_PZ_KnaMmiParams: ...

    def set_kna_mmi_params(self, params: TLMC_PZ_KnaMmiParams) -> None: ...
