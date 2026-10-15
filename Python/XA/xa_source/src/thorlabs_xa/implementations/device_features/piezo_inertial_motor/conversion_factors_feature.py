from thorlabs_xa.interfaces.device_features.piezo_inertial_motor.conversion_factors import ConversionFactors
from thorlabs_xa.native_sdks.native_functions import NativeFunctions

class ConversionFactorsFeature(ConversionFactors):

    def __init__(self, device_handle: int, native_functions: NativeFunctions) -> None:

        self.device_handle = device_handle
        self.native_functions = native_functions

    def get_conversion_factors(self, max_wait_in_milliseconds: int) -> int:
        return self.native_functions.pzim_get_conversion_factors(self.device_handle, max_wait_in_milliseconds)
