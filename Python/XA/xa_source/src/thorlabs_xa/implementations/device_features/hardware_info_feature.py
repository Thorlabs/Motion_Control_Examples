from thorlabs_xa.interfaces.device_features.hardware_info import HardwareInfo
from thorlabs_xa.native_sdks.native_functions import NativeFunctions
from thorlabs_xa.shared.params import TLMC_HardwareInfo

class HardwareInfoFeature(HardwareInfo):

    def __init__(self, device_handle: int, native_functions: NativeFunctions) -> None:

        self.device_handle = device_handle
        self.native_functions = native_functions

    def get_hardware_info(self, max_wait_in_milliseconds: int) -> TLMC_HardwareInfo:

        return self.native_functions.get_hardware_info(self.device_handle, max_wait_in_milliseconds)