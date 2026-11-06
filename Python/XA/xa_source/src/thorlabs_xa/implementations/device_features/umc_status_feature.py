from thorlabs_xa.interfaces.device_features.umc_status import UmcStatus
from thorlabs_xa.native_sdks.native_functions import NativeFunctions
from thorlabs_xa.shared.params import TLMC_UmcStatus

class UmcStatusFeature(UmcStatus):

    def __init__(self, device_handle: int, native_functions: NativeFunctions):

        self.device_handle = device_handle
        self.native_functions = native_functions

    def get_umc_status(self, max_wait_in_milliseconds: int) -> TLMC_UmcStatus:

        return self.native_functions.get_umc_status(self.device_handle, max_wait_in_milliseconds)