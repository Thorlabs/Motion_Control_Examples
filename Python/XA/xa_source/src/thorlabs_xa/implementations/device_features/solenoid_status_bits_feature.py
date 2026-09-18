from thorlabs_xa.interfaces.device_features.solenoid_status_bits import SolenoidStatusBits
from thorlabs_xa.native_sdks.native_functions import NativeFunctions

from thorlabs_xa.shared.enums import TLMC_SolenoidStatusBit

class SolenoidStatusBitsFeature(SolenoidStatusBits):

    def __init__(self, device_handle: int, native_functions: NativeFunctions) -> None:

        self.device_handle = device_handle
        self.native_functions = native_functions

    def get_solenoid_status_bits(self, max_wait_in_milliseconds: int) -> TLMC_SolenoidStatusBit:
        return self.native_functions.get_solenoid_status_bits(self.device_handle, max_wait_in_milliseconds)