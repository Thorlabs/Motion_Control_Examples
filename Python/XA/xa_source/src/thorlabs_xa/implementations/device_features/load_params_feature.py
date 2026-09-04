from thorlabs_xa.interfaces.device_features.load_params import LoadParams
from thorlabs_xa.native_sdks.native_functions import NativeFunctions

class LoadParamsFeature(LoadParams):

    def __init__(self, device_handle: int, native_functions: NativeFunctions) -> None:
        self.native_functions = native_functions
        self.device_handle = device_handle

    def load_params(self) -> None:
        self.native_functions.load_params(self.device_handle)