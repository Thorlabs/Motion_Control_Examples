from thorlabs_xa.interfaces.device_features.home_params import HomeParams
from thorlabs_xa.native_sdks.native_functions import NativeFunctions
from thorlabs_xa.shared.params import TLMC_HomeParams

class HomeParamsFeature(HomeParams):

    def __init__(self, device_handle: int, native_functions: NativeFunctions) -> None:
        self.device_handle = device_handle
        self.native_functions = native_functions

    def get_home_params(self, max_wait_in_milliseconds: int) -> TLMC_HomeParams:
        
        return self.native_functions.get_home_params(self.device_handle, max_wait_in_milliseconds)

    def set_home_params(self, params: TLMC_HomeParams) -> None:

        self.native_functions.set_home_params(self.device_handle, params)
