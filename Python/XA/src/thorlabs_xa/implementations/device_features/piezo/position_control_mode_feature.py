from thorlabs_xa.interfaces.device_features.piezo.position_control_mode import PositionControlMode
from thorlabs_xa.native_sdks.native_functions import NativeFunctions
from thorlabs_xa.shared.enums import TLMC_PZ_PositionControlMode

class PositionControlModeFeature(PositionControlMode):

    def __init__(self, device_handle: int, native_functions: NativeFunctions) -> None:

        self.device_handle = device_handle
        self.native_functions = native_functions

    def get_position_control_mode(self, max_wait_in_milliseconds: int) -> TLMC_PZ_PositionControlMode:

        return self.native_functions.pz_get_position_control_mode(self.device_handle, max_wait_in_milliseconds)

    def set_position_control_mode(self, control_mode: TLMC_PZ_PositionControlMode) -> None:
        
        self.native_functions.pz_set_position_control_mode(self.device_handle, control_mode)