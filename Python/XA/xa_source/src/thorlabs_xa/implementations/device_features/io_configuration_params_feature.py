from thorlabs_xa.interfaces.device_features.io_configuration_params import IoConfigurationParams
from thorlabs_xa.native_sdks.native_functions import NativeFunctions
from thorlabs_xa.shared.enums import TLMC_IoPortNumber
from thorlabs_xa.shared.params import TLMC_IoConfigurationParams

class IoConfigurationParamsFeature(IoConfigurationParams):

    def __init__(self, device_handle: int, native_functions: NativeFunctions) -> None:

        self.device_handle = device_handle
        self.native_functions = native_functions

    def get_io_configuration_number_of_ports_supported(self) -> int:
        return self.native_functions.get_io_configuration_number_of_ports_supported(self.device_handle)

    def get_io_configuration_params(self, port_number: TLMC_IoPortNumber, max_wait_in_milliseconds: int) -> TLMC_IoConfigurationParams:
        return self.native_functions.get_io_configuration_params(self.device_handle, port_number, max_wait_in_milliseconds)

    def set_io_configuration_params(self, handle: int, port_number: TLMC_IoPortNumber, params: TLMC_IoConfigurationParams) -> None:   
        self.native_functions.set_io_configuration_params(self.device_handle, port_number, params)