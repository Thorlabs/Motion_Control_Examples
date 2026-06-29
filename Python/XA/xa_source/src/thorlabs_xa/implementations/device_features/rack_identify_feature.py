from thorlabs_xa.interfaces.device_features.rank_identify import RackIdentify
from thorlabs_xa.native_sdks.native_functions import NativeFunctions

class RackIdentifyFeature(RackIdentify):

    def __init__(self, device_handle: int, native_functions: NativeFunctions):

        self.device_handle = device_handle
        self.native_functions = native_functions

    def rack_identify(self, channel: int) -> None:

        self.native_functions.rack_identify(self.device_handle, channel)