from thorlabs_xa.interfaces.device_features.firmware_version_info import FirmwareVersionInfo
from thorlabs_xa.native_sdks.native_functions import NativeFunctions
from thorlabs_xa.shared.params import TLMC_FirmwareVersion

class FirmwareVersionInfoFeature(FirmwareVersionInfo):

    def __init__(self, device_handle: int, native_functions: NativeFunctions) -> None:

        self.device_handle = device_handle
        self.native_functions = native_functions

    def get_firmware_version_info(self, max_wait_in_milliseconds: int) -> tuple [TLMC_FirmwareVersion, TLMC_FirmwareVersion]:

        return self.native_functions.get_firmware_version_info(self.device_handle, max_wait_in_milliseconds)