from thorlabs_xa.interfaces.device_features.piezo.lnnx_control_loop_params import LnnxControlLoopParams
from thorlabs_xa.native_sdks.native_functions import NativeFunctions
from thorlabs_xa.shared.params import TLMC_PZ_LnnxControlLoopParams

class LnnxControlLoopParamsFeature(LnnxControlLoopParams):

    def __init__(self, device_handle: int, native_functions: NativeFunctions) -> None:

        self.device_handle = device_handle
        self.native_functions = native_functions

    def get_control_loop_params(self, max_wait_in_milliseconds: int) -> TLMC_PZ_LnnxControlLoopParams:
        
        return self.native_functions.pz_get_lnnx_control_loop_params(self.device_handle, max_wait_in_milliseconds)

    def set_control_loop_params(self, params: TLMC_PZ_LnnxControlLoopParams) -> None:

        self.native_functions.pz_set_lnnx_control_loop_params(self.device_handle, params)