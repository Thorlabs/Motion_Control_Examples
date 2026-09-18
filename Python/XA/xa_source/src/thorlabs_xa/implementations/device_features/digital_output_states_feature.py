from thorlabs_xa.interfaces.device_features.digital_output_states import DigitalOutputStates
from thorlabs_xa.native_sdks.native_functions import NativeFunctions

from thorlabs_xa.shared.enums import TLMC_DigitalOutput

class DigitalOutputStatesFeature(DigitalOutputStates):

    def __init__(self, device_handle: int, native_functions: NativeFunctions) -> None:

        self.device_handle = device_handle
        self.native_functions = native_functions

    def get_digital_output_states(self, max_wait_in_milliseconds: int) -> TLMC_DigitalOutput:

        return self.native_functions.get_digital_output_states(self.device_handle, max_wait_in_milliseconds)

    def set_digital_output_states(self, params: TLMC_DigitalOutput) -> None:

        self.native_functions.set_digital_output_states(self.device_handle, params)