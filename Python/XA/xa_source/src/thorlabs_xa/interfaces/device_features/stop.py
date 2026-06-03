from typing import Protocol, runtime_checkable
from thorlabs_xa.shared.enums import TLMC_StopMode

@runtime_checkable
class Stop(Protocol):

    def stop(self, stop_mode: TLMC_StopMode, max_wait_in_milliseconds: int) -> None: ...
