from typing import Protocol, runtime_checkable
from thorlabs_xa.shared.params import TLMC_KcubeIoTriggerParams

@runtime_checkable
class KcubeIoTriggerParams(Protocol):

    def get_kcube_io_trigger_params(self, max_wait_in_milliseconds: int) -> TLMC_KcubeIoTriggerParams: ...

    def set_kcube_io_trigger_params(self, params: TLMC_KcubeIoTriggerParams) -> None: ...