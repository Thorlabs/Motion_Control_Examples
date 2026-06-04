from typing import Protocol, runtime_checkable
from thorlabs_xa.shared.params import TLMC_PZ_NanoTrakTnaIoSettings

@runtime_checkable
class NanoTrakTnaIoSettings(Protocol):

    def get_nano_trak_tna_io_settings(self, max_wait_in_milliseconds: int) -> TLMC_PZ_NanoTrakTnaIoSettings: ...

    def set_nano_trak_tna_io_settings(self, params: TLMC_PZ_NanoTrakTnaIoSettings) -> None: ...