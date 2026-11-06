from thorlabs_xa.interfaces.device_features.piezo.slew_rate_params import SlewRateParams
from thorlabs_xa.native_sdks.native_functions import NativeFunctions

from thorlabs_xa.shared.params import TLMC_PZ_SlewRateParams

class SlewRateParamsFeature(SlewRateParams):

    def __init__(self, device_handle: int, native_functions: NativeFunctions) -> None:

        self.device_handle = device_handle
        self.native_functions = native_functions

    def get_slew_rate_params(self, max_wait_in_milliseconds: int) -> TLMC_PZ_SlewRateParams:
        return self.native_functions.pz_get_slew_rate_params(self.device_handle, max_wait_in_milliseconds)

    def set_slew_rate_params(self, parameters: TLMC_PZ_SlewRateParams) -> None:
        self.native_functions.pz_set_slew_rate_params(self.device_handle, parameters)