from typing import Protocol, runtime_checkable

from thorlabs_xa.shared.params import TLMC_PZ_NanoTrakEEPROMParams

@runtime_checkable
class NanoTrakEEPROMParams(Protocol):

    def set_nano_trak_eeprom_params(self, params: TLMC_PZ_NanoTrakEEPROMParams) -> None: ...