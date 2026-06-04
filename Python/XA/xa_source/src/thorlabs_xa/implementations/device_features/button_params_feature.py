from thorlabs_xa.interfaces.device_features.button_params import ButtonParams

from thorlabs_xa.native_sdks.native_functions import NativeFunctions
from thorlabs_xa.shared.params import TLMC_ButtonParams

class ButtonParamsFeature(ButtonParams):

    def __init__(self, device_handle: int, native_functions: NativeFunctions) -> None:
        self.device_handle = device_handle
        self.native_functions = native_functions

    def get_button_params(self, max_wait_in_milliseconds: int) -> TLMC_ButtonParams:
        return self.native_functions.get_button_params(self.device_handle, max_wait_in_milliseconds)

    def set_button_params(self, params: TLMC_ButtonParams) -> None:
        self.native_functions.set_button_params(self.device_handle, params)