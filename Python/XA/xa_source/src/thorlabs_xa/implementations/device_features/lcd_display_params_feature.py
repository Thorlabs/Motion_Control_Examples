from thorlabs_xa.interfaces.device_features.lcd_display_params import LcdDisplayParams
from thorlabs_xa.native_sdks.native_functions import NativeFunctions
from thorlabs_xa.shared.params import TLMC_LcdDisplayParams

class LcdDisplayParamsFeature(LcdDisplayParams):

    def __init__(self, device_handle: int, native_functions: NativeFunctions) -> None:

        self.device_handle = device_handle
        self.native_functions = native_functions

    def get_lcd_display_params(self, max_wait_in_milliseconds: int) -> TLMC_LcdDisplayParams:
        return self.native_functions.get_lcd_display_params(self.device_handle, max_wait_in_milliseconds)

    def set_lcd_display_params(self, params: TLMC_LcdDisplayParams) -> None:
        self.native_functions.set_lcd_display_params(self.device_handle, params)