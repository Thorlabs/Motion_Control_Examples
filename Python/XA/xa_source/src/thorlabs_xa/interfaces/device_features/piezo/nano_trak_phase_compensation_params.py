from typing import Protocol, runtime_checkable

from thorlabs_xa.shared.params import TLMC_PZ_NanoTrakPhaseCompensationParams

@runtime_checkable
class NanoTrakPhaseCompensationParams(Protocol):

    def get_nano_trak_phase_compensation_params(self, max_wait_in_milliseconds: int) -> TLMC_PZ_NanoTrakPhaseCompensationParams: ...

    def set_nano_trak_phase_compensation_params(self, params: TLMC_PZ_NanoTrakPhaseCompensationParams) -> None: ...