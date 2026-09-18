from thorlabs_xa.interfaces.device_features.disconnect import Disconnect
from thorlabs_xa.native_sdks.native_functions import NativeFunctions

class DisconnectFeature(Disconnect):

    def __init__(self, device_handle: int, native_functions: NativeFunctions) -> None:

        self.device_handle = device_handle
        self.native_functions = native_functions

    def disconnect(self) -> None:

        self.native_functions.disconnect(self.device_handle)