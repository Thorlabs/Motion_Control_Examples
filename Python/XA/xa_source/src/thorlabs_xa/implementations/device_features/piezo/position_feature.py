from thorlabs_xa.interfaces.device_features.piezo.position import Position
from thorlabs_xa.native_sdks.native_functions import NativeFunctions

class PositionFeature(Position):

    def __init__(self, device_handle: int, native_functions: NativeFunctions) -> None:

        self.device_handle = device_handle
        self.native_functions = native_functions

    def get_position(self, max_wait_in_milliseconds: int) -> int:

        return self.native_functions.pz_get_position(self.device_handle, max_wait_in_milliseconds)

    def set_position(self, position: int) -> None:

        self.native_functions.pz_set_position(self.device_handle, position)