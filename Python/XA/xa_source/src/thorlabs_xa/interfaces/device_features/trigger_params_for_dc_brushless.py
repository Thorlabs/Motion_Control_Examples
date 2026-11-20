from typing import Protocol, runtime_checkable
from thorlabs_xa.shared.params import TLMC_TriggerParamsForDcBrushless

@runtime_checkable
class TriggerParamsForDcBrushless(Protocol):
    
    def get_trigger_params_for_dc_brushless(self, max_wait_in_milliseconds: int) -> TLMC_TriggerParamsForDcBrushless: ...

    def set_trigger_params_for_dc_brushless(self, params: TLMC_TriggerParamsForDcBrushless) -> None:...
