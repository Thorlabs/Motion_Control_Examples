from thorlabs_xa.interfaces.device_features.position_counter import PositionCounter
from thorlabs_xa.native_sdks.native_functions import NativeFunctions

class PositionCounterFeature(PositionCounter):

    def __init__(self, device_handle: int, native_functions: NativeFunctions) -> None:

        self.device_handle = device_handle
        self.native_functions = native_functions

    def get_position_counter(self, max_wait_in_milliseconds: int) -> int:

        return self.native_functions.get_position_counter(self.device_handle, max_wait_in_milliseconds)

    def set_position_counter(self, new_position_counter: int) -> None:
            
        self.native_functions.set_position_counter(self.device_handle, new_position_counter)