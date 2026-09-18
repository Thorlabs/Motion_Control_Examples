from thorlabs_xa.interfaces.device_features.enable_state import EnableState
from thorlabs_xa.native_sdks.native_functions import NativeFunctions
from thorlabs_xa.shared.enums import TLMC_EnableState

class EnableStateFeature(EnableState):

    def __init__(self, device_handle: int, native_functions: NativeFunctions) -> None:

        self.device_handle = device_handle
        self.native_functions = native_functions

    def get_enable_state(self, max_wait_in_milliseconds: int) -> TLMC_EnableState:
        return self.native_functions.get_enable_state(self.device_handle, max_wait_in_milliseconds)

    def set_enable_state(self, enable_state: TLMC_EnableState) -> None:
        self.native_functions.set_enable_state(self.device_handle, enable_state)