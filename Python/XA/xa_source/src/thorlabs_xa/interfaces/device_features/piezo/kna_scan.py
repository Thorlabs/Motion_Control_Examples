from typing import Protocol, runtime_checkable

from thorlabs_xa.shared.params import TLMC_PZ_KnaScanData

@runtime_checkable
class KnaScan(Protocol):

    def start_kna_scan(self) -> None: ...

    def stop_kna_scan(self) -> None: ...

    def get_kna_scan_data(self, max_wait_in_milliseconds: int) -> TLMC_PZ_KnaScanData: ...
