from typing import Protocol, runtime_checkable

from thorlabs_xa.shared.params import TLMC_PZ_NanoTrakStatus

@runtime_checkable
class NanoTrakStatus(Protocol):

    def get_nano_trak_status(self, max_wait_in_milliseconds: int) -> TLMC_PZ_NanoTrakStatus: ...