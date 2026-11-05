from typing import Protocol, runtime_checkable

from thorlabs_xa.shared.params import TLMC_PZIM_LimitSwitchParams

@runtime_checkable
class LimitSwitchParams(Protocol):

    def get_limit_switch_params(self, max_wait_in_milliseconds: int) -> TLMC_PZIM_LimitSwitchParams:...

    def set_limit_switch_params(self, params: TLMC_PZIM_LimitSwitchParams) -> None:...