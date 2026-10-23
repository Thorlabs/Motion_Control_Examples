from typing import Protocol, runtime_checkable

from thorlabs_xa.shared.params import TLMC_PZ_NanoTrakTiaRangeParams

@runtime_checkable
class NanoTrakTiaRangeParams(Protocol):

    def get_nano_trak_tia_range_params(self, max_wait_in_milliseconds: int) -> TLMC_PZ_NanoTrakTiaRangeParams: ...

    def set_nano_trak_tia_range_params(self, params: TLMC_PZ_NanoTrakTiaRangeParams) -> None: ...
