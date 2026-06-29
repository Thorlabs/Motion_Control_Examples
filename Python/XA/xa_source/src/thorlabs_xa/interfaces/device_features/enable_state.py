from typing import Protocol, runtime_checkable

from thorlabs_xa.shared.enums import TLMC_EnableState

@runtime_checkable
class EnableState(Protocol):

    def get_enable_state(self, max_wait_in_milliseconds: int) -> TLMC_EnableState: ...

    def set_enable_state(self, enable_state: TLMC_EnableState) -> None: ...