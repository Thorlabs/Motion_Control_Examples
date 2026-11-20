from thorlabs_xa.interfaces.device_features.piezo_inertial_motor.move_stop import MoveStop
from thorlabs_xa.native_sdks.native_functions import NativeFunctions
from thorlabs_xa.shared.enums import TLMC_StopMode

class MoveStopFeature(MoveStop):

    def __init__(self, device_handle: int, native_functions: NativeFunctions) -> None:

        self.device_handle = device_handle
        self.native_functions = native_functions

    def move_stop(self, stop_mode: TLMC_StopMode, max_wait_in_milliseconds: int) -> None:
        self.native_functions.stop(self.device_handle, stop_mode, max_wait_in_milliseconds)
