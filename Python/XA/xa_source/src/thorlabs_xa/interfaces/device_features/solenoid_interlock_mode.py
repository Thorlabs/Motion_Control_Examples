from typing import Protocol, runtime_checkable

from thorlabs_xa.shared.enums import TLMC_SolenoidInterlockMode

@runtime_checkable
class SolenoidInterlockMode(Protocol):

    def get_solenoid_interlock_mode(self, max_wait_in_milliseconds: int) -> TLMC_SolenoidInterlockMode:...

    def set_solenoid_interlock_mode(self, interlock_mode: TLMC_SolenoidInterlockMode) -> None:...