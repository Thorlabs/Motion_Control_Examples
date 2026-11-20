from thorlabs_xa.interfaces.device_features.universal_status_bits import UniversalStatusBits
from thorlabs_xa.native_sdks.native_functions import NativeFunctions
from thorlabs_xa.shared.params import TLMC_UniversalStatusBit

class UniversalStatusBitsFeature(UniversalStatusBits):

    def __init__(self, device_handle: int, native_functions: NativeFunctions):

        self.device_handle = device_handle
        self.native_functions = native_functions

    def get_universal_status_bits(self, max_wait_in_milliseconds: int) -> TLMC_UniversalStatusBit:

        return self.native_functions.get_universal_status_bits(self.device_handle, max_wait_in_milliseconds)