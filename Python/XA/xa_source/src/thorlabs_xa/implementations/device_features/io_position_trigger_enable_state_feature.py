from thorlabs_xa.interfaces.device_features.io_position_trigger_enable_state import IoPositionTriggerEnableState
from thorlabs_xa.native_sdks.native_functions import NativeFunctions
from thorlabs_xa.shared.enums import TLMC_IoPositionTriggerEnableState

class IoPositionTriggerEnableStateFeature(IoPositionTriggerEnableState):

    def __init__(self, device_handle: int, native_functions: NativeFunctions) -> None:

        self.device_handle = device_handle
        self.native_functions = native_functions

    def get_io_position_trigger_enable_state(self, max_wait_in_milliseconds: int) -> TLMC_IoPositionTriggerEnableState:
        return self.native_functions.get_io_position_trigger_enable_state(self.device_handle, max_wait_in_milliseconds)

    def set_io_position_trigger_enable_state(self, enable_state: TLMC_IoPositionTriggerEnableState, max_wait_in_milliseconds: int) -> None:
        self.native_functions.set_io_position_trigger_enable_state(self.device_handle, enable_state, max_wait_in_milliseconds)
