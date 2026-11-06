from typing import Protocol, runtime_checkable
from thorlabs_xa.shared.enums import TLMC_CalibrationState

@runtime_checkable
class Calibration(Protocol):

    def activate(self) -> None: ...
    
    def deactivate(self) -> None: ...

    def get_calibration_state(self, max_wait_in_milliseconds: int) -> TLMC_CalibrationState: ...
