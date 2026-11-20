from typing import Protocol, runtime_checkable

from thorlabs_xa.shared.params import TLMC_UmcStatus

@runtime_checkable
class UmcStatus(Protocol):

    def get_umc_status(self, max_wait_in_milliseconds: int) -> TLMC_UmcStatus: ...