from thorlabs_xa.interfaces.device_features.av_modes import AvModes
from thorlabs_xa.native_sdks.native_functions import NativeFunctions

from thorlabs_xa.shared.enums import TLMC_AvMode

class AvModesFeature(AvModes):

    def __init__(self, device_handle: int, native_functions: NativeFunctions) -> None:

        self.device_handle = device_handle
        self.native_functions = native_functions

    def get_av_modes(self, max_wait_in_milliseconds: int) -> TLMC_AvMode:
        return self.native_functions.get_av_modes(self.device_handle, max_wait_in_milliseconds)

    def set_av_modes(self, avModes : TLMC_AvMode) -> None:
        self.native_functions.set_av_modes(self.device_handle, avModes)