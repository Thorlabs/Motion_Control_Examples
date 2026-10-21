from thorlabs_xa.interfaces.device_features.move_sync_array import MoveSyncArray

from thorlabs_xa.native_sdks.native_functions import NativeFunctions

from thorlabs_xa.shared.params import TLMC_MoveSyncArray

class MoveSyncArrayFeature(MoveSyncArray):

    def __init__(self, device_handle: int, native_functions: NativeFunctions) -> None:

        self.device_handle = device_handle
        self.native_functions = native_functions

    def set_move_sync_array(self, parameters: TLMC_MoveSyncArray) -> None:

        self.native_functions.set_move_sync_array(self.device_handle, parameters)