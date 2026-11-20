from typing import Protocol, runtime_checkable

from thorlabs_xa.shared.params import TLMC_PowerParams

@runtime_checkable
class PowerParams(Protocol):

    def get_power_params(self, max_wait_in_milliseconds: int) -> TLMC_PowerParams: ...

    def set_power_params(self, params: TLMC_PowerParams) -> None: ...