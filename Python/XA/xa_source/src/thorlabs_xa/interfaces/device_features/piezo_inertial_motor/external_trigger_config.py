from typing import Protocol, runtime_checkable

from thorlabs_xa.shared.params import TLMC_PZIM_ExternalTriggerConfig

@runtime_checkable
class ExternalTriggerConfig(Protocol):

    def get_external_trigger_config(self, max_wait_in_milliseconds: int) -> TLMC_PZIM_ExternalTriggerConfig:...

    def set_external_trigger_config(self, params: TLMC_PZIM_ExternalTriggerConfig) -> None:...
