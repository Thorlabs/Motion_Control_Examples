from typing import Protocol, runtime_checkable

from thorlabs_xa.shared.params import TLMC_LimitSwitchParams

@runtime_checkable
class LimitSwitchParamsSetter(Protocol):

    def set_limit_switch_params(self, params: TLMC_LimitSwitchParams) -> None: ...