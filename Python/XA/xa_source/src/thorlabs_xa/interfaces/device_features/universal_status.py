from typing import Protocol, runtime_checkable
from thorlabs_xa.shared.params import TLMC_UniversalStatus

@runtime_checkable
class UniversalStatus(Protocol):

    def get_universal_status(self, max_wait_in_milliseconds: int) -> TLMC_UniversalStatus: ...