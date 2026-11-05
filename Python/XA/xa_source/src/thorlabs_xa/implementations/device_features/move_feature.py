from thorlabs_xa.interfaces.device_features.move import Move
from thorlabs_xa.native_sdks.native_functions import NativeFunctions
from thorlabs_xa.shared.enums import TLMC_MoveMode

class MoveFeature(Move):
    
    def __init__(self, device_handle: int, native_functions: NativeFunctions) -> None:

        self.device_handle = device_handle
        self.native_functions = native_functions

    def move(self, move_mode: TLMC_MoveMode, params: int, max_wait_in_milliseconds: int) -> None:

        self.native_functions.move(self.device_handle, move_mode, params, max_wait_in_milliseconds)
