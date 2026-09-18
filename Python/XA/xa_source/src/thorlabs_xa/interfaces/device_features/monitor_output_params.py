from typing import Protocol, runtime_checkable

from thorlabs_xa.shared.params import TLMC_MonitorOutputParams

@runtime_checkable
class MonitorOutputParams(Protocol):

    def get_monitor_output_params(self, max_wait_in_milliseconds: int) -> TLMC_MonitorOutputParams:...

    def set_monitor_output_params(self, params: TLMC_MonitorOutputParams) -> None:...