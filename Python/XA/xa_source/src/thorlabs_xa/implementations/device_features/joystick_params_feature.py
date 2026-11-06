from thorlabs_xa.interfaces.device_features.joystick_params import JoystickParams
from thorlabs_xa.native_sdks.native_functions import NativeFunctions
from thorlabs_xa.shared.params import TLMC_JoystickParams

class JoystickParamsFeature(JoystickParams):

    def __init__(self, device_handle: int, native_functions: NativeFunctions) -> None:

        self.device_handle = device_handle
        self.native_functions = native_functions

    def get_joystick_params(self, max_wait_in_milliseconds: int) -> TLMC_JoystickParams:
        return self.native_functions.get_joystick_params(self.device_handle, max_wait_in_milliseconds)

    def set_joystick_params(self, params: TLMC_JoystickParams) -> None:
        self.native_functions.set_joystick_params(self.device_handle, params)
