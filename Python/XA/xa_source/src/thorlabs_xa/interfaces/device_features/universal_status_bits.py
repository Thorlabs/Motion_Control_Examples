from typing import Protocol, runtime_checkable
from thorlabs_xa.shared.params import TLMC_UniversalStatusBit

@runtime_checkable
class UniversalStatusBits(Protocol):

    def get_universal_status_bits(self, max_wait_in_milliseconds: int) -> TLMC_UniversalStatusBit: ...