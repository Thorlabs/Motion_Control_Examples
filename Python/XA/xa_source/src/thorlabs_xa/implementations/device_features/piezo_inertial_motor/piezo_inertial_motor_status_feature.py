from thorlabs_xa.interfaces.device_features.piezo_inertial_motor.piezo_inertial_motor_status import PiezoInertialMotorStatus
from thorlabs_xa.native_sdks.native_functions import NativeFunctions

from thorlabs_xa.shared.params import TLMC_PZIM_Status

class PiezoInertialMotorStatusFeature(PiezoInertialMotorStatus):

    def __init__(self, device_handle: int, native_functions: NativeFunctions) -> None:

        self.device_handle = device_handle
        self.native_functions = native_functions

    def get_piezo_inertial_motor_status(self, max_wait_in_milliseconds: int) -> TLMC_PZIM_Status:

        return self.native_functions.pzim_get_status(self.device_handle, max_wait_in_milliseconds)
