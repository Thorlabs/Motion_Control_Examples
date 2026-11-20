from thorlabs_xa.interfaces.device_features.move_sync_params import MoveSyncParams

from thorlabs_xa.native_sdks.native_functions import NativeFunctions

from thorlabs_xa.shared.params import TLMC_MoveSyncParams

class MoveSyncParamsFeature(MoveSyncParams):

    def __init__(self, device_handle: int, native_functions: NativeFunctions) -> None:

        self.device_handle = device_handle
        self.native_functions = native_functions

    def set_move_sync_params(self, parameters: TLMC_MoveSyncParams) -> None:

        self.native_functions.set_move_sync_params(self.device_handle, parameters)