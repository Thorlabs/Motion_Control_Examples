from thorlabs_xa.interfaces.device_features.current_loop_params import CurrentLoopParams

from thorlabs_xa.native_sdks.native_functions import NativeFunctions
from thorlabs_xa.shared.enums import TLMC_CurrentLoopScenario
from thorlabs_xa.shared.params import TLMC_CurrentLoopParams

class CurrentLoopParamsFeature(CurrentLoopParams):

    def __init__(self, device_handle: int, native_functions: NativeFunctions) -> None:
        self.device_handle = device_handle
        self.native_functions = native_functions

    def get_current_loop_params(self, scenario: TLMC_CurrentLoopScenario, max_wait_in_milliseconds: int) -> TLMC_CurrentLoopParams:
        return self.native_functions.get_current_loop_params(self.device_handle, scenario, max_wait_in_milliseconds)

    def set_current_loop_params(self, scenario: TLMC_CurrentLoopScenario, parameters: TLMC_CurrentLoopParams) -> None:
        self.native_functions.set_current_loop_params(self.device_handle, scenario, parameters)