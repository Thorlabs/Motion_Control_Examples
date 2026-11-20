from typing import Protocol, runtime_checkable
from thorlabs_xa.shared.params import TLMC_StepperStatus

@runtime_checkable
class StepperStatus(Protocol):

    def get_stepper_status(self, max_wait_in_milliseconds: int) -> TLMC_StepperStatus: ...
