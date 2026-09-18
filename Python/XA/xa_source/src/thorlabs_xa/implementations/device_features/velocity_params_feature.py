from thorlabs_xa.interfaces.device_features.velocity_params import VelocityParams
from thorlabs_xa.native_sdks.native_functions import NativeFunctions
from thorlabs_xa.shared.params import TLMC_VelocityParams

class VelocityParamsFeature(VelocityParams):

    def __init__(self, device_handle: int, native_functions: NativeFunctions) -> None:

        self.device_handle = device_handle
        self.native_functions = native_functions

    def get_velocity_params(self, max_wait_in_milliseconds: int) -> TLMC_VelocityParams:

        return self.native_functions.get_velocity_params(self.device_handle, max_wait_in_milliseconds)

    def set_velocity_params(self, params: TLMC_VelocityParams) -> None:

        self.native_functions.set_velocity_params(self.device_handle, params)
