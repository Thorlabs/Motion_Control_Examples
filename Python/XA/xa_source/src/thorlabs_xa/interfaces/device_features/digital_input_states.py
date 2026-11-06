from typing import Protocol, runtime_checkable

from thorlabs_xa.shared.enums import TLMC_DigitalInput

@runtime_checkable
class DigitalInputStates(Protocol):

    def get_digital_input_states(self, max_wait_in_milliseconds: int) -> TLMC_DigitalInput: ...