from typing import Protocol, runtime_checkable

from thorlabs_xa.shared.enums import TLMC_OperatingMode

@runtime_checkable
class StatusMode(Protocol):

    def set_status_mode(self, operating_mode: TLMC_OperatingMode): ...