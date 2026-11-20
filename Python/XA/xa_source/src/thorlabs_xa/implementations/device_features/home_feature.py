from thorlabs_xa.interfaces.device_features.home import Home
from thorlabs_xa.native_sdks.native_functions import NativeFunctions

class HomeFeature(Home):
    def __init__(self, device_handle: int, native_functions: NativeFunctions) -> None:
        self.device_handle = device_handle
        self.native_functions = native_functions

    def home(self, max_wait_in_milliseconds: int) -> None:
        self.native_functions.home(self.device_handle, max_wait_in_milliseconds)
