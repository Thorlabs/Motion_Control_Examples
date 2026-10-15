from thorlabs_xa.interfaces.device_features.solenoid_state import SolenoidState
from thorlabs_xa.native_sdks.native_functions import NativeFunctions

from thorlabs_xa.shared.enums import TLMC_SolenoidState

class SolenoidStateFeature(SolenoidState):

    def __init__(self, device_handle: int, native_functions: NativeFunctions) -> None:

        self.device_handle = device_handle
        self.native_functions = native_functions

    def get_solenoid_state(self, max_wait_in_milliseconds: int) -> TLMC_SolenoidState:
        return self.native_functions.get_solenoid_state(self.device_handle, max_wait_in_milliseconds)

    def set_solenoid_state(self, state: TLMC_SolenoidState) -> None:
        self.native_functions.set_solenoid_state(self.device_handle, state)