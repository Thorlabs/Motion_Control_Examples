from typing import Protocol, runtime_checkable

from thorlabs_xa.shared.params import TLMC_AdcInputs

@runtime_checkable
class AdcInputs(Protocol):

    def get_adc_inputs(self, max_wait_in_milliseconds: int) -> TLMC_AdcInputs: ...