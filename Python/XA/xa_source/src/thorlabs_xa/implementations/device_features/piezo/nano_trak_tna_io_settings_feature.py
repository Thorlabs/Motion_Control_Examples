from thorlabs_xa.interfaces.device_features.piezo.nano_trak_tna_io_settings import NanoTrakTnaIoSettings
from thorlabs_xa.native_sdks.native_functions import NativeFunctions
from thorlabs_xa.shared.params import TLMC_PZ_NanoTrakTnaIoSettings

class NanoTrakTnaIoSettingsFeature(NanoTrakTnaIoSettings):

    def __init__(self, device_handle: int, native_functions: NativeFunctions) -> None:

        self.device_handle = device_handle
        self.native_functions = native_functions

    def get_nano_trak_tna_io_settings(self, max_wait_in_milliseconds: int) -> TLMC_PZ_NanoTrakTnaIoSettings:
        
        return self.native_functions.pz_get_nano_trak_tna_io_settings(self.device_handle, max_wait_in_milliseconds)

    def set_nano_trak_tna_io_settings(self, params: TLMC_PZ_NanoTrakTnaIoSettings) -> None:

        self.native_functions.pz_set_nano_trak_tna_io_settings(self.device_handle, params)