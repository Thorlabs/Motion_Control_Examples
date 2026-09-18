from thorlabs_xa.interfaces.device_features.piezo.nano_trak_mode import NanoTrakMode
from thorlabs_xa.native_sdks.native_functions import NativeFunctions
from thorlabs_xa.shared.enums import TLMC_PZ_SetNanoTrakModeType
from thorlabs_xa.shared.params import TLMC_PZ_NanoTrakMode

class NanoTrakModeFeature(NanoTrakMode):

    def __init__(self, device_handle: int, native_functions: NativeFunctions) -> None:

        self.device_handle = device_handle
        self.native_functions = native_functions

    def get_nano_trak_mode(self, max_wait_in_milliseconds: int) -> TLMC_PZ_NanoTrakMode:
        return self.native_functions.pz_get_nano_trak_mode(self.device_handle, max_wait_in_milliseconds)

    def set_nano_trak_mode(self, set_mode: TLMC_PZ_SetNanoTrakModeType) -> None:
        self.native_functions.pz_set_nano_trak_mode(self.device_handle, set_mode)