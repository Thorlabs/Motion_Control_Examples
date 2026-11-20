from typing import Protocol, runtime_checkable

from thorlabs_xa.shared.params import TLMC_PZ_Status

@runtime_checkable
class PiezoStatus(Protocol):

    def get_piezo_status(self, max_wait_in_milliseconds: int) ->  TLMC_PZ_Status: ...