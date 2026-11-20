from thorlabs_xa.interfaces.device_features.bow_index import BowIndex
from thorlabs_xa.native_sdks.native_functions import NativeFunctions
from thorlabs_xa.shared.enums import TLMC_BowIndex

class BowIndexFeature(BowIndex):

    def __init__(self, device_handle: int, native_functions: NativeFunctions) -> None:
        self.device_handle = device_handle
        self.native_functions = native_functions

    def get_bow_index(self, max_wait_in_milliseconds: int) -> TLMC_BowIndex:
        return self.native_functions.get_bow_index(self.device_handle, max_wait_in_milliseconds)

    def set_bow_index(self, bow_index: TLMC_BowIndex) -> None:
        self.native_functions.set_bow_index(self.device_handle, bow_index)