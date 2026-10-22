from thorlabs_xa.interfaces.device_features.general_move_params import GeneralMoveParams
from thorlabs_xa.native_sdks.native_functions import NativeFunctions
from thorlabs_xa.shared.params import TLMC_GeneralMoveParams

class GeneralMoveParamsFeature(GeneralMoveParams):

    def __init__(self, device_handle: int, native_functions: NativeFunctions) -> None:

        self.device_handle = device_handle
        self.native_functions = native_functions

    def get_general_move_params(self, max_wait_in_milliseconds: int) -> TLMC_GeneralMoveParams:
        
        return self.native_functions.get_general_move_params(self.device_handle, max_wait_in_milliseconds)

    def set_general_move_params(self, params: TLMC_GeneralMoveParams) -> None:

        self.native_functions.set_general_move_params(self.device_handle, params)