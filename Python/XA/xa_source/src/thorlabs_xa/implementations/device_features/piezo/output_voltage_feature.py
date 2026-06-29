from thorlabs_xa.interfaces.device_features.piezo.output_voltage import OutputVoltage
from thorlabs_xa.native_sdks.native_functions import NativeFunctions

class OutputVoltageFeature(OutputVoltage):

    def __init__(self, device_handle: int, native_functions: NativeFunctions) -> None:

        self.native_functions = native_functions
        self.device_handle = device_handle

    def get_output_voltage(self, max_wait_in_milliseconds: int) -> int:

        return self.native_functions.pz_get_output_voltage(self.device_handle, max_wait_in_milliseconds)

    def set_output_voltage(self, output_voltage: int) -> None:

        self.native_functions.pz_set_output_voltage(self.device_handle, output_voltage)