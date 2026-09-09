from thorlabs_xa.interfaces.device_features.calibration import Calibration
from thorlabs_xa.native_sdks.native_functions import NativeFunctions
from thorlabs_xa.shared.enums import TLMC_CalibrationState

class CalibrationFeature(Calibration):

    def __init__(self, device_handle: int, native_functions: NativeFunctions) -> None:
        self.device_handle = device_handle
        self.native_functions = native_functions

    def activate(self) -> None:
        self.native_functions.activate_calibration(self.device_handle)

    def deactivate(self) -> None:
        self.native_functions.deactivate_calibration(self.device_handle)

    def get_calibration_state(self, max_wait_in_milliseconds: int) -> TLMC_CalibrationState:
        return self.native_functions.get_calibration_state(self.device_handle, max_wait_in_milliseconds)