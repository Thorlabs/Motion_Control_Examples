from typing import Protocol, runtime_checkable

from thorlabs_xa.shared.enums import TLMC_PositionLoopScenario
from thorlabs_xa.shared.params import TLMC_PositionLoopParams

@runtime_checkable
class PositionLoopParams(Protocol):

    def get_position_loop_params(self, scenario: TLMC_PositionLoopScenario, max_wait_in_milliseconds: int) -> TLMC_PositionLoopParams: ...

    def set_position_loop_params(self, scenario: TLMC_PositionLoopScenario, params: TLMC_PositionLoopParams) -> None: ...