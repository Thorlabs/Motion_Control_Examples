from typing import Protocol, runtime_checkable

from thorlabs_xa.shared.enums import TLMC_KcubeMmiLockState

@runtime_checkable
class KcubeMmiLock(Protocol):

    def get_kcube_mmi_lock_state(self, max_wait_in_milliseconds: int) -> TLMC_KcubeMmiLockState: ...

    def set_kcube_mmi_lock_state(self, lock_state: TLMC_KcubeMmiLockState) -> None: ...