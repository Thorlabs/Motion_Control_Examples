from typing import Protocol, runtime_checkable

from thorlabs_xa.shared.enums import TLMC_SolenoidOperatingMode

@runtime_checkable
class SolenoidOperatingMode(Protocol):

    def get_solenoid_operating_mode(self, max_wait_in_milliseconds: int) -> TLMC_SolenoidOperatingMode:...

    def set_solenoid_operating_mode(self, mode: TLMC_SolenoidOperatingMode) -> None:...