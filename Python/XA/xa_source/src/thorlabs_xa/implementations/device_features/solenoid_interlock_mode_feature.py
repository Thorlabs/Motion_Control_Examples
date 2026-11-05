from thorlabs_xa.interfaces.device_features.solenoid_interlock_mode import SolenoidInterlockMode
from thorlabs_xa.native_sdks.native_functions import NativeFunctions

from thorlabs_xa.shared.enums import TLMC_SolenoidInterlockMode

class SolenoidInterlockModeFeature(SolenoidInterlockMode):

    def __init__(self, device_handle: int, native_functions: NativeFunctions) -> None:

        self.device_handle = device_handle
        self.native_functions = native_functions

    def get_solenoid_interlock_mode(self, max_wait_in_milliseconds: int) -> TLMC_SolenoidInterlockMode:
        return self.native_functions.get_solenoid_interlock_mode(self.device_handle, max_wait_in_milliseconds)

    def set_solenoid_interlock_mode(self, interlock_mode: TLMC_SolenoidInterlockMode) -> None:
        self.native_functions.set_solenoid_interlock_mode(self.device_handle, interlock_mode)