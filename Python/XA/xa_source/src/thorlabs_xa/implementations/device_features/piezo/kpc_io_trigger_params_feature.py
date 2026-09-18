from thorlabs_xa.interfaces.device_features.piezo.kpc_io_trigger_params import KpcIoTriggerParams
from thorlabs_xa.native_sdks.native_functions import NativeFunctions
from thorlabs_xa.shared.params import TLMC_PZ_KpcIoTriggerParams

class KpcIoTriggerParamsFeature(KpcIoTriggerParams):

    def __init__(self, device_handle: int, native_functions: NativeFunctions) -> None:

        self.device_handle = device_handle
        self.native_functions = native_functions

    def get_io_trigger_params(self, max_wait_in_milliseconds: int) -> TLMC_PZ_KpcIoTriggerParams:

        return self.native_functions.pz_get_kpc_io_trigger_params(self.device_handle, max_wait_in_milliseconds)
    
    def set_io_trigger_params(self, params: TLMC_PZ_KpcIoTriggerParams) -> None:

        self.native_functions.pz_set_kpc_io_trigger_params(self.device_handle, params)