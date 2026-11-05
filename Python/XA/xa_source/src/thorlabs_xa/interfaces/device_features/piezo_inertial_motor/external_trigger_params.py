from typing import Protocol, runtime_checkable

from thorlabs_xa.shared.params import TLMC_PZIM_ExternalTriggerParams

@runtime_checkable
class ExternalTriggerParams(Protocol):

    def get_external_trigger_params(self, max_wait_in_milliseconds: int) -> TLMC_PZIM_ExternalTriggerParams:...

    def set_external_trigger_params(self, params: TLMC_PZIM_ExternalTriggerParams) -> None:...
