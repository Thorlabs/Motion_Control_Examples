from thorlabs_xa.interfaces.device_features.solenoid_status import SolenoidStatus
from thorlabs_xa.native_sdks.native_functions import NativeFunctions

from thorlabs_xa.shared.params import TLMC_SolenoidStatus

class SolenoidStatusFeature(SolenoidStatus):

    def __init__(self, device_handle: int, native_functions: NativeFunctions) -> None:

        self.device_handle = device_handle
        self.native_functions = native_functions

    def get_solenoid_status(self, max_wait_in_milliseconds: int) -> TLMC_SolenoidStatus:
        return self.native_functions.get_solenoid_status(self.device_handle, max_wait_in_milliseconds)
