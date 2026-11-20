from typing import Protocol, runtime_checkable

from thorlabs_xa.shared.params import TLMC_PZIM_AbnormalMoveDetectionParams

@runtime_checkable
class AbnormalMoveDetectionParams(Protocol):

    def get_abnormal_move_detection_params(self, max_wait_in_milliseconds: int) -> TLMC_PZIM_AbnormalMoveDetectionParams:...

    def set_abnormal_move_detection_params(self, params: TLMC_PZIM_AbnormalMoveDetectionParams) -> None:...
