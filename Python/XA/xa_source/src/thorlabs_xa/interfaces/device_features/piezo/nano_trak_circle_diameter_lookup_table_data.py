from typing import Protocol, runtime_checkable

from thorlabs_xa.shared.params import TLMC_PZ_NanoTrakCircleDiameterLookupTableData

@runtime_checkable
class NanoTrakCircleDiameterLookupTableData(Protocol):

    def get_nano_trak_circle_diameter_lookup_table_data(self, max_wait_in_milliseconds: int) -> TLMC_PZ_NanoTrakCircleDiameterLookupTableData: ...

    def set_nano_trak_circle_diameter_lookup_table_data(self, params: TLMC_PZ_NanoTrakCircleDiameterLookupTableData) -> None: ...