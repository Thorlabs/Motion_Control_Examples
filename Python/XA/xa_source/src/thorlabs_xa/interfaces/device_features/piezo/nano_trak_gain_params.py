from typing import Protocol, runtime_checkable

from thorlabs_xa.shared.params import TLMC_PZ_NanoTrakGainParams

@runtime_checkable
class NanoTrakGainParams(Protocol):

    def get_nano_trak_gain_params(self, max_wait_in_milliseconds: int) -> TLMC_PZ_NanoTrakGainParams: ...

    def set_nano_trak_gain_params(self, params: TLMC_PZ_NanoTrakGainParams) -> None: ...