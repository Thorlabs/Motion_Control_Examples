from typing import Protocol, runtime_checkable

from thorlabs_xa.shared.params import TLMC_PZIM_KcubeTriggerParams

@runtime_checkable
class KcubeTriggerParams(Protocol):

    def get_kcube_trigger_params(self, max_wait_in_milliseconds: int) -> TLMC_PZIM_KcubeTriggerParams:...

    def set_kcube_trigger_params(self, params: TLMC_PZIM_KcubeTriggerParams) -> None:...