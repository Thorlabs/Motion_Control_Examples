from typing import Protocol, runtime_checkable

from thorlabs_xa.shared.params import TLMC_PZ_NanoTrakCircleDiameterLookupTable

@runtime_checkable
class NanoTrakCircleDiameterLookupTable(Protocol):

    def get_nano_trak_circle_diameter_lookup_table(self, max_wait_in_milliseconds: int) -> TLMC_PZ_NanoTrakCircleDiameterLookupTable: ...

    def set_nano_trak_circle_diameter_lookup_table(self, params: TLMC_PZ_NanoTrakCircleDiameterLookupTable) -> None: ...