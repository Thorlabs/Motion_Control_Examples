from typing import Protocol, runtime_checkable

from thorlabs_xa.shared.enums import TLMC_SolenoidState

@runtime_checkable
class SolenoidState(Protocol):

    def get_solenoid_state(self, max_wait_in_milliseconds: int) -> TLMC_SolenoidState:...

    def set_solenoid_state(self, state: TLMC_SolenoidState) -> None:...