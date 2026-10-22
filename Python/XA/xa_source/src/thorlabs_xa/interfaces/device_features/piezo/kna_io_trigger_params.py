from typing import Protocol, runtime_checkable

from thorlabs_xa.shared.params import TLMC_PZ_KnaIoTriggerParams

@runtime_checkable
class KnaIoTriggerParams(Protocol):

    def get_kna_io_trigger_params(self, max_wait_in_milliseconds: int) -> TLMC_PZ_KnaIoTriggerParams: ...

    def set_kna_io_trigger_params(self, params: TLMC_PZ_KnaIoTriggerParams) -> None: ...
