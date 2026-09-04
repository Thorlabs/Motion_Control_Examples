from thorlabs_xa.interfaces.device_features.stop import Stop
from thorlabs_xa.native_sdks.native_functions import NativeFunctions
from thorlabs_xa.shared.enums import TLMC_StopMode

class StopFeature(Stop):

    def __init__(self, device_handle: int, native_functions: NativeFunctions):

        self.device_handle = device_handle
        self.native_functions = native_functions

    def stop(self, stop_mode: TLMC_StopMode, max_wait_in_milliseconds: int) -> None:

        self.native_functions.stop(self.device_handle, stop_mode, max_wait_in_milliseconds)
