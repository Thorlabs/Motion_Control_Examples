from typing import Protocol, runtime_checkable
from thorlabs_xa.shared.params import TLMC_KcubePositionTriggerParams

@runtime_checkable
class KcubePositionTriggerParams(Protocol):

    def get_kcube_position_trigger_params(self, max_wait_in_milliseconds: int) -> TLMC_KcubePositionTriggerParams: ...

    def set_kcube_position_trigger_params(self, params: TLMC_KcubePositionTriggerParams) -> None: ...