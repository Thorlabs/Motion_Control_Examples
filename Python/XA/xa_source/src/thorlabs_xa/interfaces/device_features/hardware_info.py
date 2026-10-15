from typing import Protocol, runtime_checkable

from thorlabs_xa.shared.params import TLMC_HardwareInfo

@runtime_checkable
class HardwareInfo(Protocol):

    def get_hardware_info(self, max_wait_in_milliseconds: int) -> TLMC_HardwareInfo: ...