from typing import Protocol, runtime_checkable
from thorlabs_xa.shared.enums import TLMC_CalibrationState
from thorlabs_xa.shared.params import *


@runtime_checkable
class Calibration(Protocol):

    
    def activate(self) -> None:
        pass

    
    def deactivate(self) -> None:
        pass

    
    def get_calibration_state(self, max_wait_in_milliseconds: int) -> TLMC_CalibrationState:
        pass
