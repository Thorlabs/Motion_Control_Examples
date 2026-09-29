from typing import Protocol, runtime_checkable

from thorlabs_xa.shared.enums import TLMC_PZ_NanoTrakFeedbackSource

@runtime_checkable
class NanoTrakFeedbackSource(Protocol):
    def get_nano_trak_feedback_source(self, max_wait_in_milliseconds: int) -> TLMC_PZ_NanoTrakFeedbackSource:...
    def set_nano_trak_feedback_source(self, params: TLMC_PZ_NanoTrakFeedbackSource) -> None:...