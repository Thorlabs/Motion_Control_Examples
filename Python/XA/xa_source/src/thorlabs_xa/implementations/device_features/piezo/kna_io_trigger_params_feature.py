from thorlabs_xa.interfaces.device_features.piezo.kna_io_trigger_params import KnaIoTriggerParams
from thorlabs_xa.native_sdks.native_functions import NativeFunctions
from thorlabs_xa.shared.params import TLMC_PZ_KnaIoTriggerParams

class KnaIoTriggerParamsFeature(KnaIoTriggerParams):

    def __init__(self, device_handle: int, native_functions: NativeFunctions) -> None:

        self.device_handle = device_handle
        self.native_functions = native_functions

    def get_kna_io_trigger_params(self, max_wait_in_milliseconds: int) -> TLMC_PZ_KnaIoTriggerParams:

        return self.native_functions.pz_get_kna_io_trigger_params(self.device_handle, max_wait_in_milliseconds)

    def set_kna_io_trigger_params(self, params: TLMC_PZ_KnaIoTriggerParams) -> None:

        self.native_functions.pz_set_kna_io_trigger_params(self.device_handle, params)
