from thorlabs_xa.interfaces.device_features.stage_axis_params import StageAxisParams
from thorlabs_xa.native_sdks.native_functions import NativeFunctions
from thorlabs_xa.shared.params import TLMC_StageAxisParams

class StageAxisParamsFeature(StageAxisParams):

    def __init__(self, device_handle: int, native_functions: NativeFunctions):

        self.device_handle = device_handle
        self.native_functions = native_functions

    def get_stage_axis_params(self, max_wait_in_milliseconds: int) -> TLMC_StageAxisParams:
        return self.native_functions.get_stage_axis_params(self.device_handle, max_wait_in_milliseconds)

    def set_stage_axis_params(self, params: TLMC_StageAxisParams) -> None:
        self.native_functions.set_stage_axis_params(self.device_handle, params)
