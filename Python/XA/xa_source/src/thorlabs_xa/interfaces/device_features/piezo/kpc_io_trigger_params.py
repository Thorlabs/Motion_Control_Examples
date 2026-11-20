from typing import Protocol, runtime_checkable

from thorlabs_xa.shared.params import TLMC_PZ_KpcIoTriggerParams

@runtime_checkable
class KpcIoTriggerParams(Protocol):

    def get_io_trigger_params(self, max_wait_in_milliseconds: int) -> TLMC_PZ_KpcIoTriggerParams: ...

    def set_io_trigger_params(self, params: TLMC_PZ_KpcIoTriggerParams) -> None: ...