from typing import Protocol, runtime_checkable

from thorlabs_xa.shared.params import TLMC_PZ_MaxOutputVoltageParams

@runtime_checkable
class MaxOutputVoltageParams(Protocol):

    def get_max_output_voltage_params(self, max_wait_in_milliseconds: int) -> TLMC_PZ_MaxOutputVoltageParams: ...

    def set_max_output_voltage(self, max_output_voltage: int) -> None: ...