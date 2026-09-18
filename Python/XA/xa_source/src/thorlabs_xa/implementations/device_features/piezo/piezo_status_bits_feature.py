from thorlabs_xa.interfaces.device_features.piezo.piezo_status_bits import PiezoStatusBits
from thorlabs_xa.native_sdks.native_functions import NativeFunctions
from thorlabs_xa.shared.enums import TLMC_PZ_StatusBit

class PiezoStatusBitsFeature(PiezoStatusBits):

    def __init__(self, device_handle: int, native_functions: NativeFunctions) -> None:

        self.device_handle = device_handle
        self.native_functions = native_functions

    def get_piezo_status_bits(self, max_wait_in_milliseconds: int) -> TLMC_PZ_StatusBit:

        return self.native_functions.pz_get_status_bits(self.device_handle, max_wait_in_milliseconds)