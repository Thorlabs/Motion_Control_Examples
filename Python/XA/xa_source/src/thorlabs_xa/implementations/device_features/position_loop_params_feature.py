from thorlabs_xa.interfaces.device_features.position_loop_params import PositionLoopParams
from thorlabs_xa.native_sdks.native_functions import NativeFunctions
from thorlabs_xa.shared.enums import TLMC_PositionLoopScenario
from thorlabs_xa.shared.params import TLMC_PositionLoopParams

class PositionLoopParamsFeature(PositionLoopParams):

    def __init__(self, device_handle: int, native_functions: NativeFunctions) -> None:

        self.device_handle = device_handle
        self.native_functions = native_functions

    def get_position_loop_params(self, scenario: TLMC_PositionLoopScenario, max_wait_in_milliseconds: int) -> TLMC_PositionLoopParams:

        return self.native_functions.get_position_loop_params(self.device_handle, scenario, max_wait_in_milliseconds)
    
    def set_position_loop_params(self, scenario: TLMC_PositionLoopScenario, params: TLMC_PositionLoopParams) -> None:

        self.native_functions.set_position_loop_params(self.device_handle, scenario, params)