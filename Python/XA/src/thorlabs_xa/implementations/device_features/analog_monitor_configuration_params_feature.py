from thorlabs_xa.interfaces.device_features.analog_monitor_configuration_params import AnalogMonitorConfigurationParams as AnalogMonitorConfigurationParamsABC

from thorlabs_xa.native_sdks.native_functions import NativeFunctions
from thorlabs_xa.shared.enums import TLMC_AnalogMonitorNumber
from thorlabs_xa.shared.params import TLMC_AnalogMonitorConfigurationParams

class AnalogMonitorConfigurationParamsFeature(AnalogMonitorConfigurationParamsABC):

    def __init__(self, device_handle: int, native_functions: NativeFunctions) -> None:
        self.device_handle = device_handle
        self.native_functions = native_functions

    def get_analog_monitor_configuration_params(self, monitor_number: TLMC_AnalogMonitorNumber, max_wait_in_milliseconds: int) -> TLMC_AnalogMonitorConfigurationParams:
        return self.native_functions.get_analog_monitor_configuration_params(self.device_handle, monitor_number, max_wait_in_milliseconds)
    
    def set_analog_monitor_configuration_params(self, monitor_number: TLMC_AnalogMonitorNumber, params: TLMC_AnalogMonitorConfigurationParams):
        self.native_functions.set_analog_monitor_configuration_params(self.device_handle, monitor_number, params)