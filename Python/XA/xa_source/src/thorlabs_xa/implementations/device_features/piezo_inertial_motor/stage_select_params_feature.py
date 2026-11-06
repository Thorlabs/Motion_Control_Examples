from thorlabs_xa.interfaces.device_features.piezo_inertial_motor.stage_select_params import StageSelectParams
from thorlabs_xa.native_sdks.native_functions import NativeFunctions

from thorlabs_xa.shared.params import TLMC_PZIM_StageSelectParams

class StageSelectParamsFeature(StageSelectParams):

    def __init__(self, device_handle: int, native_functions: NativeFunctions) -> None:

        self.device_handle = device_handle
        self.native_functions = native_functions

    def set_stage_select_params(self, params: TLMC_PZIM_StageSelectParams) -> None:

        self.native_functions.pzim_set_stage_select_params(self.device_handle, params)