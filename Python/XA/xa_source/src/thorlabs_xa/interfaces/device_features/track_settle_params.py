from typing import Protocol, runtime_checkable

from thorlabs_xa.shared.params import TLMC_TrackSettleParams

@runtime_checkable
class TrackSettleParams(Protocol):

    def get_track_settle_params(self, max_wait_in_milliseconds: int) -> TLMC_TrackSettleParams: ...

    def set_track_settle_params(self, params: TLMC_TrackSettleParams): ...