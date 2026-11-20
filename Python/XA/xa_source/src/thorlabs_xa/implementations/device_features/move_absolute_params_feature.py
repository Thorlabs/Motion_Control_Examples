from thorlabs_xa.interfaces.device_features.move_absolute_params import MoveAbsoluteParams
from thorlabs_xa.native_sdks.native_functions import NativeFunctions
from thorlabs_xa.shared.params import TLMC_MoveAbsoluteParams

class MoveAbsoluteParamsFeature(MoveAbsoluteParams):

    def __init__(self, device_handle: int, native_functions: NativeFunctions) -> None:

        self.native_functions = native_functions
        self.device_handle = device_handle

    def get_move_absolute_params(self, max_wait_in_milliseconds: int) -> TLMC_MoveAbsoluteParams:

        return self.native_functions.get_move_absolute_params(self.device_handle, max_wait_in_milliseconds)

    def set_move_absolute_params(self, params: TLMC_MoveAbsoluteParams) -> None:

        self.native_functions.set_move_absolute_params(self.device_handle, params)
