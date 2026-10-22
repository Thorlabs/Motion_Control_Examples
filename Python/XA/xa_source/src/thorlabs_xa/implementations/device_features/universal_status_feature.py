from thorlabs_xa.interfaces.device_features.universal_status import UniversalStatus
from thorlabs_xa.native_sdks.native_functions import NativeFunctions
from thorlabs_xa.shared.params import TLMC_UniversalStatus

class UniversalStatusFeature(UniversalStatus):

    def __init__(self, device_handle: int, native_functions: NativeFunctions):

        self.device_handle = device_handle
        self.native_functions = native_functions

    def get_universal_status(self, max_wait_in_milliseconds: int) -> TLMC_UniversalStatus:

        return self.native_functions.get_universal_status(self.device_handle, max_wait_in_milliseconds)