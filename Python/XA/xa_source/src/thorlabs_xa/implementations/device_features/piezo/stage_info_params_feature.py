from thorlabs_xa.interfaces.device_features.piezo.stage_info_params import StageInfoParams
from thorlabs_xa.native_sdks.native_functions import NativeFunctions

from thorlabs_xa.shared.params import TLMC_PZ_StageInfoParams

class StageInfoParamsFeature(StageInfoParams):

    def __init__(self, device_handle: int, native_functions: NativeFunctions) -> None:

        self.device_handle = device_handle
        self.native_functions = native_functions

    def get_stage_info_params(self, max_wait_in_milliseconds: int) -> TLMC_PZ_StageInfoParams:

        return self.native_functions.pz_get_stage_info_params(self.device_handle, max_wait_in_milliseconds)