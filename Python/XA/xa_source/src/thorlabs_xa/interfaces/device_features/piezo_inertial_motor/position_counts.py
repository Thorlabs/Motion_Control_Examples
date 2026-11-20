from typing import Protocol, runtime_checkable

from thorlabs_xa.shared.params import TLMC_PZIM_PositionCounts

@runtime_checkable
class PositionCounts(Protocol):

    def get_position_counts(self, max_wait_in_milliseconds: int) -> TLMC_PZIM_PositionCounts:...

    def set_position_counts(self, params: TLMC_PZIM_PositionCounts) -> None:...