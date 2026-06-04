from typing import Protocol, runtime_checkable

from thorlabs_xa.shared.params import TLMC_PZ_NanoTrakCircleHomePositionParams

@runtime_checkable
class NanoTrakCircleHomePosition(Protocol):

    def get_nano_trak_circle_home_position(self, max_wait_in_milliseconds: int) -> TLMC_PZ_NanoTrakCircleHomePositionParams: ...

    def set_nano_trak_circle_home_position(self, params: TLMC_PZ_NanoTrakCircleHomePositionParams) -> None: ...