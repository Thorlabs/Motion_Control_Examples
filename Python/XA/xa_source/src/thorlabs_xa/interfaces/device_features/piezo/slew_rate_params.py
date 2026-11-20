from typing import Protocol, runtime_checkable

from thorlabs_xa.shared.params import TLMC_PZ_SlewRateParams

@runtime_checkable
class SlewRateParams(Protocol):

    def get_slew_rate_params(self, max_wait_in_milliseconds: int) -> TLMC_PZ_SlewRateParams:...

    def set_slew_rate_params(self, parameters: TLMC_PZ_SlewRateParams) -> None:...