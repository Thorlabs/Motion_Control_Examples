from typing import Protocol, runtime_checkable

from thorlabs_xa.shared.params import TLMC_ProfileModeParams

@runtime_checkable
class ProfileModeParams(Protocol):

    def get_profile_mode_params(self, max_wait_in_milliseconds: int) -> TLMC_ProfileModeParams: ...

    def set_profile_mode_params(self, params: TLMC_ProfileModeParams) -> None: ...