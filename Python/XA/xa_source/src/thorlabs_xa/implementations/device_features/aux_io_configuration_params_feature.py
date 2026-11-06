from thorlabs_xa.interfaces.device_features.aux_io_configuration_params import AuxIoConfigurationParams
from thorlabs_xa.native_sdks.native_functions import NativeFunctions
from thorlabs_xa.shared.enums import TLMC_AuxIoPortMode, TLMC_AuxIoPortNumber

class AuxIoConfigurationParamsFeature(AuxIoConfigurationParams):

    def __init__(self, device_handle: int, native_functions: NativeFunctions) -> None:
        self.device_handle = device_handle
        self.native_functions = native_functions

    def get_aux_io_port_mode(self, port_number: TLMC_AuxIoPortNumber, max_wait_in_milliseconds: int) -> TLMC_AuxIoPortMode:
        return self.native_functions.get_aux_io_port_mode(self.device_handle, port_number, max_wait_in_milliseconds)

    def set_aux_io_port_mode(self, port_number: TLMC_AuxIoPortNumber, port_mode: TLMC_AuxIoPortMode) -> None:
        self.native_functions.set_aux_io_port_mode(self.device_handle, port_number, port_mode)

    def get_aux_io_software_states(self, max_wait_in_milliseconds: int) -> int:
        return self.native_functions.get_aux_io_software_states(self.device_handle, max_wait_in_milliseconds)

    def set_aux_io_software_states(self, software_states: int) -> None:
        self.native_functions.set_aux_io_software_states(self.device_handle, software_states)