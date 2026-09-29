from typing import Protocol, runtime_checkable

from thorlabs_xa.shared.params import TLMC_StepperLoopParams

@runtime_checkable
class StepperLoopParams(Protocol):

    def get_stepper_loop_params(self, max_wait_in_milliseconds: int) -> TLMC_StepperLoopParams: ...

    def set_stepper_loop_params(self, params: TLMC_StepperLoopParams) -> None: ...