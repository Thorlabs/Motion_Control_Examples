from thorlabs_xa.interfaces.device_features.piezo.output_voltage_control_source_params import OutputVoltageControlSourceParams
from thorlabs_xa.native_sdks.native_functions import NativeFunctions
from thorlabs_xa.shared.params import TLMC_PZ_OutputVoltageControlSourceParams

class OutputVoltageControlSourceParamsFeature(OutputVoltageControlSourceParams):

    def __init__(self, device_handle: int, native_functions: NativeFunctions) -> None:

        self.device_handle = device_handle
        self.native_functions = native_functions

    def get_output_voltage_control_source_params(self, max_wait_in_milliseconds: int) -> TLMC_PZ_OutputVoltageControlSourceParams:

        return self.native_functions.pz_get_output_voltage_control_source_params(self.device_handle, max_wait_in_milliseconds)

    def set_output_voltage_control_source_params(self, params: TLMC_PZ_OutputVoltageControlSourceParams) -> None:

        self.native_functions.pz_set_output_voltage_control_source_params(self.device_handle, params)