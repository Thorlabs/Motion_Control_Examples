from typing import Protocol, runtime_checkable
from thorlabs_xa.shared.params import TLMC_VelocityParams

@runtime_checkable
class VelocityParams(Protocol):

    def get_velocity_params(self, max_wait_in_milliseconds: int) -> TLMC_VelocityParams: ...

    def set_velocity_params(self, params: TLMC_VelocityParams) -> None: ...