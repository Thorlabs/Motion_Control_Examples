from typing import Protocol, runtime_checkable

from thorlabs_xa.shared.enums import TLMC_PZ_PositionControlMode

@runtime_checkable
class PositionControlMode(Protocol):

    def get_position_control_mode(self, max_wait_in_milliseconds: int) -> TLMC_PZ_PositionControlMode: ...

    def set_position_control_mode(self, control_mode: TLMC_PZ_PositionControlMode) -> None: ...