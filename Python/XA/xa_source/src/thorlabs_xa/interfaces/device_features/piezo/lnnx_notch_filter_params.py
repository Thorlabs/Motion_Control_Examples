from typing import Protocol, runtime_checkable

from thorlabs_xa.shared.params import TLMC_PZ_LnnxNotchFilterParams

@runtime_checkable
class LnnxNotchFilterParams(Protocol):

    def get_notch_filter_params(self, max_wait_in_milliseconds: int) -> TLMC_PZ_LnnxNotchFilterParams:...

    def set_notch_filter_params(self, params: TLMC_PZ_LnnxNotchFilterParams) -> None:...