from typing import Protocol, runtime_checkable

from thorlabs_xa.shared.params import TLMC_PZIM_DriveOperationsParams

@runtime_checkable
class DriveOperationsParams(Protocol):

    def get_drive_operations_params(self, max_wait_in_milliseconds: int) -> TLMC_PZIM_DriveOperationsParams:...

    def set_drive_operations_params(self, params: TLMC_PZIM_DriveOperationsParams) -> None:...