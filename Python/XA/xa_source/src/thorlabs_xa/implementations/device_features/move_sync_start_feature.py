from thorlabs_xa.interfaces.device_features.move_sync_start import MoveSyncStart

from thorlabs_xa.native_sdks.native_functions import NativeFunctions

from thorlabs_xa.shared.params import TLMC_MoveSyncStartParams

class MoveSyncStartFeature(MoveSyncStart):

    def __init__(self, device_handle: int, native_functions: NativeFunctions) -> None:

        self.device_handle = device_handle
        self.native_functions = native_functions

    def move_sync_start(self, parameters: TLMC_MoveSyncStartParams) -> None:

        self.native_functions.move_sync_start(self.device_handle, parameters)