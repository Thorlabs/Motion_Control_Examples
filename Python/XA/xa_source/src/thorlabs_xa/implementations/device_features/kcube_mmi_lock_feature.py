from thorlabs_xa.interfaces.device_features.kcube_mmi_lock import KcubeMmiLock
from thorlabs_xa.native_sdks.native_functions import NativeFunctions
from thorlabs_xa.shared.enums import TLMC_KcubeMmiLockState

class KcubeMmiLockFeature(KcubeMmiLock):

    def __init__(self, device_handle: int, native_functions: NativeFunctions) -> None:

        self.device_handle = device_handle
        self.native_functions = native_functions

    def get_kcube_mmi_lock_state(self, max_wait_in_milliseconds: int) -> TLMC_KcubeMmiLockState:
        return self.native_functions.get_kcube_mmi_lock_state(self.device_handle, max_wait_in_milliseconds)

    def set_kcube_mmi_lock_state(self, lock_state: TLMC_KcubeMmiLockState) -> None:
        self.native_functions.set_kcube_mmi_lock_state(self.device_handle, lock_state)
