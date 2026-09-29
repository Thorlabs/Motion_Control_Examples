from typing import Protocol, runtime_checkable

from thorlabs_xa.shared.params import TLMC_PZIM_KcubeFeedbackSignalParams

@runtime_checkable
class KcubeFeedbackSignalParams(Protocol):

    def get_kcube_feedback_signal_params(self, max_wait_in_milliseconds: int) -> TLMC_PZIM_KcubeFeedbackSignalParams:...

    def set_kcube_feedback_signal_params(self, params: TLMC_PZIM_KcubeFeedbackSignalParams) -> None:...