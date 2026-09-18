from thorlabs_xa.interfaces.device_features.piezo.zero import Zero
from thorlabs_xa.native_sdks.native_functions import NativeFunctions

class ZeroFeature(Zero):

    def __init__(self, device_handle: int, native_functions: NativeFunctions):

        self.device_handle = device_handle
        self.native_functions = native_functions

    def set_zero(self, max_wait_in_milliseconds: int):

        self.native_functions.pz_set_zero(self.device_handle, max_wait_in_milliseconds)