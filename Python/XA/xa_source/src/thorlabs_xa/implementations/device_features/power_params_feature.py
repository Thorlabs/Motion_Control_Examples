from thorlabs_xa.interfaces.device_features.power_params import PowerParams
from thorlabs_xa.native_sdks.native_functions import NativeFunctions
from thorlabs_xa.shared.params import TLMC_PowerParams

class PowerParamsFeature(PowerParams):

    def __init__(self, device_handle: int, native_functions: NativeFunctions):
        
        self.device_handle = device_handle
        self.native_functions = native_functions

    def get_power_params(self, max_wait_in_milliseconds: int) -> TLMC_PowerParams:
        return self.native_functions.get_power_params(self.device_handle, max_wait_in_milliseconds)

    def set_power_params(self, params: TLMC_PowerParams):
        self.native_functions.set_power_params(self.device_handle, params)
