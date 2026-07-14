from thorlabs_xa.interfaces.device_features.no_flash_programming import NoFlashProgramming
from thorlabs_xa.native_sdks.native_functions import NativeFunctions

class NoFlashProgrammingFeature(NoFlashProgramming):

    def __init__(self, device_handle: int, native_functions: NativeFunctions) -> None:

        self.device_handle = device_handle
        self.native_functions = native_functions

    def send_no_flash_programming(self) -> None:

        self.native_functions.send_no_flash_programming(self.device_handle)
