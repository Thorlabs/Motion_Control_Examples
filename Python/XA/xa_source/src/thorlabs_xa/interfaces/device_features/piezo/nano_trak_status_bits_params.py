from typing import Protocol, runtime_checkable

from thorlabs_xa.shared.params import TLMC_PZ_NanoTrakStatusBitsParams

@runtime_checkable
class NanoTrakStatusBitsParams(Protocol):

    def get_nano_trak_status_bits_params(self, max_wait_in_milliseconds: int) -> TLMC_PZ_NanoTrakStatusBitsParams: ...
