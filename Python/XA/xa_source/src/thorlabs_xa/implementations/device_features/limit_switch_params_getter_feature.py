from thorlabs_xa.interfaces.device_features.limit_switch_params_getter import LimitSwitchParamsGetter
from thorlabs_xa.native_sdks.native_functions import NativeFunctions
from thorlabs_xa.shared.params import TLMC_LimitSwitchParams

class LimitSwitchParamsGetterFeature(LimitSwitchParamsGetter):

    def __init__(self, device_handle: int, native_functions: NativeFunctions) -> None:

        self.device_handle = device_handle
        self.native_functions = native_functions

    def get_limit_switch_params(self, max_wait_in_milliseconds: int) -> TLMC_LimitSwitchParams:

        return self.native_functions.get_limit_switch_params(self.device_handle, max_wait_in_milliseconds)