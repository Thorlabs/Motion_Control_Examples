from typing import Protocol, runtime_checkable

from thorlabs_xa.shared.params import TLMC_PZ_NanoTrakCircleParams

@runtime_checkable
class NanoTrakCircleParams(Protocol):

    def get_nano_trak_circle_params(self, max_wait_in_milliseconds: int) -> TLMC_PZ_NanoTrakCircleParams: ...

    def set_nano_trak_circle_params(self, params: TLMC_PZ_NanoTrakCircleParams) -> None: ...