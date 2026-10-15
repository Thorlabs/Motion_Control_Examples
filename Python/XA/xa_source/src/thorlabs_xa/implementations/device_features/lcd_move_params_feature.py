from thorlabs_xa.interfaces.device_features.lcd_move_params import LcdMoveParams
from thorlabs_xa.native_sdks.native_functions import NativeFunctions
from thorlabs_xa.shared.params import TLMC_LcdMoveParams

class LcdMoveParamsFeature(LcdMoveParams):

    def __init__(self, device_handle: int, native_functions: NativeFunctions) -> None:

        self.device_handle = device_handle
        self.native_functions = native_functions

    def get_lcd_move_params(self, max_wait_in_milliseconds: int) -> TLMC_LcdMoveParams:
        return self.native_functions.get_lcd_move_params(self.device_handle, max_wait_in_milliseconds)

    def set_lcd_move_params(self, params: TLMC_LcdMoveParams) -> None:
        self.native_functions.set_lcd_move_params(self.device_handle, params)
