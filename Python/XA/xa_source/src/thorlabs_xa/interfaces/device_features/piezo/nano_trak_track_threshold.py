from typing import Protocol, runtime_checkable

from thorlabs_xa.shared.params import TLMC_PZ_NanoTrakTrackThresholdParams

@runtime_checkable
class NanoTrakTrackThreshold(Protocol):

    def get_nano_trak_track_threshold(self, max_wait_in_milliseconds: int) -> TLMC_PZ_NanoTrakTrackThresholdParams: ...

    def set_nano_trak_track_threshold(self, params: TLMC_PZ_NanoTrakTrackThresholdParams) -> None: ...
