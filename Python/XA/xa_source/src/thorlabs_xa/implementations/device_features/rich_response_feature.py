from thorlabs_xa.interfaces.device_features.rich_response import RichResponse
from thorlabs_xa.native_sdks.native_functions import NativeFunctions
from thorlabs_xa.shared.params import TLMC_RichResponse

class RichResponseFeature(RichResponse):

    def __init__(self, device_handle: int, native_functions: NativeFunctions):

        self.device_handle = device_handle
        self.native_functions = native_functions

    def get_rich_response(self) -> TLMC_RichResponse:

        return self.native_functions.get_rich_response(self.device_handle)