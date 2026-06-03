from thorlabs_xa.interfaces.device_features.digital_input_states import DigitalInputStates
from thorlabs_xa.native_sdks.native_functions import NativeFunctions
from thorlabs_xa.shared.enums import TLMC_DigitalInput

class DigitalInputStatesFeature(DigitalInputStates):

    def __init__(self, device_handle: int, native_functions: NativeFunctions) -> None:

        self.device_handle = device_handle
        self.native_functions = native_functions

    def get_digital_input_states(self, max_wait_in_milliseconds: int) -> TLMC_DigitalInput:
        return self.native_functions.get_digital_input_states(self.device_handle, max_wait_in_milliseconds)