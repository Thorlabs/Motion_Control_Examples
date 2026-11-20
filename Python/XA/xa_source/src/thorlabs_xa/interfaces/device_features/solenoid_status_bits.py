from typing import Protocol, runtime_checkable

from thorlabs_xa.shared.enums import TLMC_SolenoidStatusBit

@runtime_checkable
class SolenoidStatusBits(Protocol):

    def get_solenoid_status_bits(self, max_wait_in_milliseconds: int) -> TLMC_SolenoidStatusBit:...