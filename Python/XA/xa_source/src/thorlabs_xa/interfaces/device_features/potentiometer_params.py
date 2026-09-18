from typing import Protocol, runtime_checkable

from thorlabs_xa.shared.params import TLMC_PotentiometerParams

@runtime_checkable
class PotentiometerParams(Protocol):

    def get_potentiometer_params(self, max_wait_in_milliseconds: int) -> TLMC_PotentiometerParams: ...

    def set_potentiometer_params(self, params: TLMC_PotentiometerParams): ...
