from typing import Protocol, runtime_checkable

from thorlabs_xa.shared.params import TLMC_HomeParams

@runtime_checkable
class HomeParams(Protocol):

    def get_home_params(self, max_wait_in_milliseconds: int) -> TLMC_HomeParams: ...

    def set_home_params(self, params: TLMC_HomeParams): ...