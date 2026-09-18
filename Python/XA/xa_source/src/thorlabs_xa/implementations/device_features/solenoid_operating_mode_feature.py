from thorlabs_xa.interfaces.device_features.solenoid_operating_mode import SolenoidOperatingMode
from thorlabs_xa.native_sdks.native_functions import NativeFunctions

from thorlabs_xa.shared.enums import TLMC_SolenoidOperatingMode

class SolenoidOperatingModeFeature(SolenoidOperatingMode):

    def __init__(self, device_handle: int, native_functions: NativeFunctions) -> None:

        self.device_handle = device_handle
        self.native_functions = native_functions

    def get_solenoid_operating_mode(self, max_wait_in_milliseconds: int) -> TLMC_SolenoidOperatingMode:
        return self.native_functions.get_solenoid_operating_mode(self.device_handle, max_wait_in_milliseconds)

    def set_solenoid_operating_mode(self, mode: TLMC_SolenoidOperatingMode) -> None:
        self.native_functions.set_solenoid_operating_mode(self.device_handle, mode)