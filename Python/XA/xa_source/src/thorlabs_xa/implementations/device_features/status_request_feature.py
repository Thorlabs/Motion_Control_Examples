from thorlabs_xa.interfaces.device_features.status_request import StatusRequest
from thorlabs_xa.native_sdks.native_functions import NativeFunctions

class StatusRequestFeature(StatusRequest):

    def __init__(self, device_handle: int, native_functions: NativeFunctions):

        self.device_handle = device_handle
        self.native_functions = native_functions

    def request_status(self, max_wait_in_milliseconds: int):

        self.native_functions.request_status(self.device_handle, max_wait_in_milliseconds)