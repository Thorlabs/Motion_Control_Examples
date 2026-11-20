from typing import Protocol, runtime_checkable

from thorlabs_xa.shared.enums import TLMC_AvMode

@runtime_checkable
class AvModes(Protocol):

    def get_av_modes(self, max_wait_in_milliseconds: int) -> TLMC_AvMode:...

    def set_av_modes(self, avModes : TLMC_AvMode) -> None:...