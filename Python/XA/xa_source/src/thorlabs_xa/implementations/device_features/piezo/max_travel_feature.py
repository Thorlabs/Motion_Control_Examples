from thorlabs_xa.interfaces.device_features.piezo.max_travel import MaxTravel
from thorlabs_xa.native_sdks.native_functions import NativeFunctions

class MaxTravelFeature(MaxTravel):

    def __init__(self, device_handle: int, native_functions: NativeFunctions) -> None:

        self.device_handle = device_handle
        self.native_functions = native_functions

    def get_max_travel(self, max_wait_in_milliseconds: int) -> int:

        return self.native_functions.pz_get_max_travel(self.device_handle, max_wait_in_milliseconds)

    def set_max_travel(self, max_travel: int) -> None:

        self.native_functions.pz_set_max_travel(self.device_handle, max_travel)