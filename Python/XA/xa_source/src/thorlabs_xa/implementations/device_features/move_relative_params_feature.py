from thorlabs_xa.interfaces.device_features.move_relative_params import MoveRelativeParams
from thorlabs_xa.native_sdks.native_functions import NativeFunctions
from thorlabs_xa.shared.params import TLMC_MoveRelativeParams

class MoveRelativeParamsFeature(MoveRelativeParams):

    def __init__(self, device_handle: int, native_functions: NativeFunctions) -> None:

        self.device_handle = device_handle
        self.native_functions = native_functions

    def get_move_relative_params(self, max_wait_in_milliseconds: int) -> TLMC_MoveRelativeParams:

      return self.native_functions.get_move_relative_params(self.device_handle, max_wait_in_milliseconds)

    def set_move_relative_params(self, params: TLMC_MoveRelativeParams) -> None:

        self.native_functions.set_move_relative_params(self.device_handle, params)
