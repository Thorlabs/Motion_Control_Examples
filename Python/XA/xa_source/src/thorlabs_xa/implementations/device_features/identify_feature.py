from thorlabs_xa.interfaces.device_features.identify import Identify

from thorlabs_xa.native_sdks.native_functions import NativeFunctions

class IdentifyFeature(Identify):

    def __init__(self, device_handle: int, native_functions: NativeFunctions) -> None:

        self.device_handle = device_handle
        self.native_functions = native_functions

    def identify(self) -> None:

        return self.native_functions.identify(self.device_handle)