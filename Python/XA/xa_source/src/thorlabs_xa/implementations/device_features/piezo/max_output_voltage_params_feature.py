from thorlabs_xa.interfaces.device_features.piezo.max_output_voltage_params import MaxOutputVoltageParams
from thorlabs_xa.native_sdks.native_functions import NativeFunctions
from thorlabs_xa.shared.params import TLMC_PZ_MaxOutputVoltageParams

class MaxOutputVoltageParamsFeature(MaxOutputVoltageParams):

    def __init__(self, device_handle: int, native_functions: NativeFunctions) -> None:

        self.device_handle = device_handle
        self.native_functions = native_functions

    def get_max_output_voltage_params(self, max_wait_in_milliseconds: int) -> TLMC_PZ_MaxOutputVoltageParams:

        return self.native_functions.pz_get_max_output_voltage_params(self.device_handle, max_wait_in_milliseconds)
    
    def set_max_output_voltage(self, max_output_voltage: int) -> None:

        self.native_functions.pz_set_max_output_voltage(self.device_handle, max_output_voltage)