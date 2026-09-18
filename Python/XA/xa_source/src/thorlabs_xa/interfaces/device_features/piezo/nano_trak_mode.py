from typing import Protocol, runtime_checkable

from thorlabs_xa.shared.enums import TLMC_PZ_SetNanoTrakModeType
from thorlabs_xa.shared.params import TLMC_PZ_NanoTrakMode

@runtime_checkable
class NanoTrakMode(Protocol):

    def get_nano_trak_mode(self, max_wait_in_milliseconds: int) -> TLMC_PZ_NanoTrakMode: ...

    def set_nano_trak_mode(self, set_mode: TLMC_PZ_SetNanoTrakModeType) -> None: ...