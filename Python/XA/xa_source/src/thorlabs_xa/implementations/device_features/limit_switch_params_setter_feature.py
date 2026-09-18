from thorlabs_xa.interfaces.device_features.limit_switch_params_setter import LimitSwitchParamsSetter
from thorlabs_xa.native_sdks.native_functions import NativeFunctions
from thorlabs_xa.shared.params import TLMC_LimitSwitchParams

class LimitSwitchParamsSetterFeature(LimitSwitchParamsSetter):

    def __init__(self, device_handle: int, native_functions: NativeFunctions) -> None:

        self.device_handle = device_handle
        self.native_functions = native_functions

    def set_limit_switch_params(self, params: TLMC_LimitSwitchParams) -> None:
        
        self.native_functions.set_limit_switch_params(self.device_handle, params)