from typing import Protocol, runtime_checkable
from thorlabs_xa.shared.enums import TLMC_PZ_StatusBit

@runtime_checkable
class PiezoStatusBits(Protocol):

    def get_piezo_status_bits(self, max_wait_in_milliseconds: int) -> TLMC_PZ_StatusBit: ...