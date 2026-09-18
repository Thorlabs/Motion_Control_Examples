from typing import Protocol, runtime_checkable

from thorlabs_xa.shared.params import TLMC_SolenoidCycleParams

@runtime_checkable
class SolenoidCycleParams(Protocol):

    def get_solenoid_cycle_params(self, max_wait_in_milliseconds: int) -> TLMC_SolenoidCycleParams:...

    def set_solenoid_cycle_params(self, solenoid_cycle_params : TLMC_SolenoidCycleParams) -> None:...