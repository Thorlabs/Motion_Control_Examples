from typing import Protocol, runtime_checkable

from thorlabs_xa.shared.enums import TLMC_DigitalOutput

@runtime_checkable
class DigitalOutputStates(Protocol):

    def get_digital_output_states(self, max_wait_in_milliseconds: int) -> TLMC_DigitalOutput: ...

    def set_digital_output_states(self, params: TLMC_DigitalOutput): ...