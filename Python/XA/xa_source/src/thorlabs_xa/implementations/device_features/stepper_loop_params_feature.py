from thorlabs_xa.interfaces.device_features.stepper_loop_params import StepperLoopParams
from thorlabs_xa.native_sdks.native_functions import NativeFunctions
from thorlabs_xa.shared.params import TLMC_StepperLoopParams

class StepperLoopParamsFeature(StepperLoopParams):

    def __init__(self, device_handle: int, native_functions: NativeFunctions):

        self.device_handle = device_handle
        self.native_functions = native_functions

    def get_stepper_loop_params(self, max_wait_in_milliseconds: int) -> TLMC_StepperLoopParams:

        return self.native_functions.get_stepper_loop_params(self.device_handle, max_wait_in_milliseconds)

    def set_stepper_loop_params(self, params: TLMC_StepperLoopParams):

        self.native_functions.set_stepper_loop_params(self.device_handle, params)
