from typing import Protocol

from thorlabs_xa.shared.params import TLMC_PZ_KpcIoSettingsParams

class KpcIoSettingsParams(Protocol):

    def get_io_settings_params(self, max_wait_in_milliseconds: int) -> TLMC_PZ_KpcIoSettingsParams: ...

    def set_io_settings_params(self, params: TLMC_PZ_KpcIoSettingsParams) -> None: ...