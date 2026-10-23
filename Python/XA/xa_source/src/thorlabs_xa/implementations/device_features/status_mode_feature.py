from thorlabs_xa.interfaces.device_features.status_mode import StatusMode
from thorlabs_xa.native_sdks.native_functions import NativeFunctions
from thorlabs_xa.shared.enums import TLMC_OperatingMode

class StatusModeFeature(StatusMode):
    
    def __init__(self, device_handle: int, native_functions: NativeFunctions) -> None:

        self.device_handle = device_handle
        self.native_functions = native_functions

    def set_status_mode(self, operating_mode: TLMC_OperatingMode) -> None:

        self.native_functions.set_status_mode(self.device_handle, operating_mode)