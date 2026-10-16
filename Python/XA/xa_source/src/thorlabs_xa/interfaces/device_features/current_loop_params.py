from typing import Protocol, runtime_checkable

from thorlabs_xa.shared.enums import TLMC_CurrentLoopScenario
from thorlabs_xa.shared.params import TLMC_CurrentLoopParams

@runtime_checkable
class CurrentLoopParams(Protocol):

    def get_current_loop_params(self, scenario: TLMC_CurrentLoopScenario, max_wait_in_milliseconds: int) -> TLMC_CurrentLoopParams: ...

    def set_current_loop_params(self, scenario: TLMC_CurrentLoopScenario, parameters: TLMC_CurrentLoopParams): ...