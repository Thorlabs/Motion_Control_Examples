from typing import Protocol, runtime_checkable

from thorlabs_xa.shared.params import TLMC_PZ_NanoTrakRangeParams

@runtime_checkable
class NanoTrakRangeParams(Protocol):

    def get_nano_trak_range_params(self, max_wait_in_milliseconds: int) -> TLMC_PZ_NanoTrakRangeParams: ...

    def set_nano_trak_range_params(self, params: TLMC_PZ_NanoTrakRangeParams) -> None: ...