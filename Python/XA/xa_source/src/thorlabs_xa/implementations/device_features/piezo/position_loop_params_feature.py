from thorlabs_xa.interfaces.device_features.piezo.position_loop_params import PositionLoopParams
from thorlabs_xa.native_sdks.native_functions import NativeFunctions
from thorlabs_xa.shared.params import TLMC_PZ_PositionLoopParams

class PositionLoopParamsFeature(PositionLoopParams):

    def __init__(self, device_handle: int, native_functions: NativeFunctions) -> None:

        self.native_functions = native_functions
        self.device_handle = device_handle

    def get_position_loop_params(self, max_wait_in_milliseconds: int) -> TLMC_PZ_PositionLoopParams:

        return self.native_functions.pz_get_position_loop_params(self.device_handle, max_wait_in_milliseconds)

    def set_position_loop_params(self, params: TLMC_PZ_PositionLoopParams) -> None:

        self.native_functions.pz_set_position_loop_params(self.device_handle, params)