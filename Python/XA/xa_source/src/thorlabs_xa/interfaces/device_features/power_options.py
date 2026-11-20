from typing import Protocol, runtime_checkable

from thorlabs_xa.shared.enums import TLMC_PowerOptions

@runtime_checkable
class PowerOptions(Protocol):

    def get_power_options(self, max_wait_in_milliseconds: int) -> TLMC_PowerOptions:...

    def set_power_options(self, power_options: TLMC_PowerOptions) -> None:...