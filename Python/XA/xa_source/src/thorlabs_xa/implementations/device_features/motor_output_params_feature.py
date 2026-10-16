from thorlabs_xa.interfaces.device_features.motor_output_params import MotorOutputParams
from thorlabs_xa.native_sdks.native_functions import NativeFunctions
from thorlabs_xa.shared.params import TLMC_MotorOutputParams

class MotorOutputParamsFeature(MotorOutputParams):

    def __init__(self, device_handle: int, native_functions: NativeFunctions) -> None:

        self.device_handle = device_handle
        self.native_functions = native_functions

    def get_motor_output_params(self, max_wait_in_milliseconds: int) -> TLMC_MotorOutputParams:

        return self.native_functions.get_motor_output_params(self.device_handle, max_wait_in_milliseconds)

    def set_motor_output_params(self, params: TLMC_MotorOutputParams) -> None:

        self.native_functions.set_motor_output_params(self.device_handle, params)
