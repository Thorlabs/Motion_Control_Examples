from thorlabs_xa.interfaces.device_features.yes_flash_programming import YesFlashProgramming
from thorlabs_xa.native_sdks.native_functions import NativeFunctions

class YesFlashProgrammingFeature(YesFlashProgramming):

    def __init__(self, device_handle: int, native_functions: NativeFunctions):

        self.device_handle = device_handle
        self.native_functions = native_functions

    def send_yes_flash_programming(self):

        self.native_functions.send_yes_flash_programming(self.device_handle)
