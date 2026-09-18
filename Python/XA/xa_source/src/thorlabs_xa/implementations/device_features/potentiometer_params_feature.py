from thorlabs_xa.interfaces.device_features.potentiometer_params import PotentiometerParams
from thorlabs_xa.native_sdks.native_functions import NativeFunctions
from thorlabs_xa.shared.params import TLMC_PotentiometerParams

class PotentiometerParamsFeature(PotentiometerParams):

    def __init__(self, device_handle: int, native_functions: NativeFunctions):

        self.device_handle = device_handle
        self.native_functions = native_functions

    def get_potentiometer_params(self, max_wait_in_milliseconds: int) -> TLMC_PotentiometerParams:
        return self.native_functions.get_potentiometer_params(self.device_handle, max_wait_in_milliseconds)

    def set_potentiometer_params(self, params: TLMC_PotentiometerParams):
        self.native_functions.set_potentiometer_params(self.device_handle, params)
