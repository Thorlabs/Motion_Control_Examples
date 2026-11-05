from thorlabs_xa.native_sdks.native_functions import NativeFunctions

from thorlabs_xa.shared.params import TLMC_AdcInputs
from thorlabs_xa.interfaces.device_features.adc_inputs import AdcInputs

class AdcInputsFeature(AdcInputs):

    def __init__(self, device_handle: int, native_functions: NativeFunctions) -> None:
        self.native_functions = native_functions
        self.device_handle = device_handle

    def get_adc_inputs(self, max_wait_in_milliseconds: int) -> TLMC_AdcInputs:
        return self.native_functions.get_adc_inputs(self.device_handle, max_wait_in_milliseconds)