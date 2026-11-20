from typing import Protocol, runtime_checkable

from thorlabs_xa.shared.params import TLMC_SolenoidStatus

@runtime_checkable
class SolenoidStatus(Protocol):

    def get_solenoid_status(self, max_wait_in_milliseconds: int) -> TLMC_SolenoidStatus:...
