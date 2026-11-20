from thorlabs_xa.interfaces.device_features.piezo_inertial_motor.open_loop_move_params import OpenLoopMoveParams
from thorlabs_xa.native_sdks.native_functions import NativeFunctions
from thorlabs_xa.shared.params import TLMC_PZIM_OpenLoopMoveParams

class OpenLoopMoveParamsFeature(OpenLoopMoveParams):

    def __init__(self, device_handle: int, native_functions: NativeFunctions) -> None:

        self.device_handle = device_handle
        self.native_functions = native_functions

    def get_open_loop_move_params(self, max_wait_in_milliseconds: int) -> TLMC_PZIM_OpenLoopMoveParams:

        return self.native_functions.pzim_get_open_loop_move_params(self.device_handle, max_wait_in_milliseconds)

    def set_open_loop_move_params(self, params: TLMC_PZIM_OpenLoopMoveParams) -> None:

        self.native_functions.pzim_set_open_loop_move_params(self.device_handle, params)
