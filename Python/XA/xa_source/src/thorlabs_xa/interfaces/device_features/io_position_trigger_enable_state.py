from typing import Protocol, runtime_checkable

from thorlabs_xa.shared.enums import TLMC_IoPositionTriggerEnableState

@runtime_checkable
class IoPositionTriggerEnableState(Protocol):

    def get_io_position_trigger_enable_state(self, max_wait_in_milliseconds: int) -> TLMC_IoPositionTriggerEnableState: ...

    def set_io_position_trigger_enable_state(self, enable_state: TLMC_IoPositionTriggerEnableState, max_wait_in_milliseconds: int) -> None: ...