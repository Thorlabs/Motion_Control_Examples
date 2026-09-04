from typing import Protocol, runtime_checkable

from thorlabs_xa.shared.enums import TLMC_AnalogMonitorNumber
from thorlabs_xa.shared.params import TLMC_AnalogMonitorConfigurationParams

@runtime_checkable
class AnalogMonitorConfigurationParams(Protocol):

    def get_analog_monitor_configuration_params(self, monitor_number: TLMC_AnalogMonitorNumber, max_wait_in_milliseconds: int) -> TLMC_AnalogMonitorConfigurationParams: ...
    def set_analog_monitor_configuration_params(self, monitor_number: TLMC_AnalogMonitorNumber, params: TLMC_AnalogMonitorConfigurationParams): ...