from thorlabs_xa.interfaces.device_features.piezo.nano_trak_status import NanoTrakStatus
from thorlabs_xa.native_sdks.native_functions import NativeFunctions
from thorlabs_xa.shared.params import TLMC_PZ_NanoTrakStatus

class NanoTrakStatusFeature(NanoTrakStatus):

    def __init__(self, device_handle: int, native_functions: NativeFunctions) -> None:

        self.device_handle = device_handle
        self.native_functions = native_functions

    def get_nano_trak_status(self, max_wait_in_milliseconds: int) -> TLMC_PZ_NanoTrakStatus:
        
        return self.native_functions.pz_get_nano_trak_status(self.device_handle, max_wait_in_milliseconds)