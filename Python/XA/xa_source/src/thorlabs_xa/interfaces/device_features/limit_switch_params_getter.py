
from typing import Protocol, runtime_checkable
from thorlabs_xa.shared.params import TLMC_LimitSwitchParams

@runtime_checkable
class LimitSwitchParamsGetter(Protocol):

    def get_limit_switch_params(self, max_wait_in_milliseconds: int) -> TLMC_LimitSwitchParams: ...