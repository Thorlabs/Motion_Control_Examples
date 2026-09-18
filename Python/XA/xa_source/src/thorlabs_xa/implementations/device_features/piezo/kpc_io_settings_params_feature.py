from thorlabs_xa.interfaces.device_features.piezo.kpc_io_settings_params import KpcIoSettingsParams
from thorlabs_xa.native_sdks.native_functions import NativeFunctions
from thorlabs_xa.shared.params import TLMC_PZ_KpcIoSettingsParams

class KpcIoSettingsParamsFeature(KpcIoSettingsParams):

    def __init__(self, device_handle: int, native_functions: NativeFunctions) -> None:

        self.device_handle = device_handle
        self.native_functions = native_functions

    def get_io_settings_params(self, max_wait_in_milliseconds: int) -> TLMC_PZ_KpcIoSettingsParams:

        return self.native_functions.pz_get_kpc_io_settings_params(self.device_handle, max_wait_in_milliseconds)
    
    def set_io_settings_params(self, params: TLMC_PZ_KpcIoSettingsParams) -> None:

        self.native_functions.pz_set_kpc_io_settings_params(self.device_handle, params)