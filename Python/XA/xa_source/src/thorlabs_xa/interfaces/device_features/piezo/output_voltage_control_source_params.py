from typing import Protocol, runtime_checkable

from thorlabs_xa.shared.params import TLMC_PZ_OutputVoltageControlSourceParams

@runtime_checkable
class OutputVoltageControlSourceParams(Protocol):

    def get_output_voltage_control_source_params(self, max_wait_in_milliseconds: int) -> TLMC_PZ_OutputVoltageControlSourceParams: ...

    def set_output_voltage_control_source_params(self, params: TLMC_PZ_OutputVoltageControlSourceParams) -> None: ...
