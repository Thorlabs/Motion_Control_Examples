from typing import Protocol, runtime_checkable

from thorlabs_xa.shared.params import TLMC_PZIM_Status

@runtime_checkable
class PiezoInertialMotorStatus(Protocol):

    def get_piezo_inertial_motor_status(self, max_wait_in_milliseconds: int) -> TLMC_PZIM_Status: ...
