from typing import Protocol, runtime_checkable
from thorlabs_xa.shared.params import TLMC_IoTriggerParams

@runtime_checkable
class IoTriggerParams(Protocol):

    def get_io_trigger_params(self, max_wait_in_milliseconds: int) -> TLMC_IoTriggerParams: ...

    def set_io_trigger_params(self, params: TLMC_IoTriggerParams) -> None: ...