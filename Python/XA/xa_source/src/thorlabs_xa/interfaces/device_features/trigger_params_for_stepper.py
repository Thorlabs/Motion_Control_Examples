from typing import Protocol, runtime_checkable
from thorlabs_xa.shared.params import TLMC_TriggerParamsForStepper

@runtime_checkable
class TriggerParamsForStepper(Protocol):

    def get_trigger_params_for_stepper(self, max_wai_in_milliseconds: int) -> TLMC_TriggerParamsForStepper: ...

    def set_trigger_params_for_stepper(self, params: TLMC_TriggerParamsForStepper) -> None: ...
