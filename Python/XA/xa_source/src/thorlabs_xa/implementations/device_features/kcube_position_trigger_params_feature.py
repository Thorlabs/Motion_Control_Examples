from thorlabs_xa.interfaces.device_features.kcube_position_trigger_params import KcubePositionTriggerParams
from thorlabs_xa.native_sdks.native_functions import NativeFunctions
from thorlabs_xa.shared.params import TLMC_KcubePositionTriggerParams

class KcubePositionTriggerParamsFeature(KcubePositionTriggerParams):

    def __init__(self, device_handle: int, native_functions: NativeFunctions) -> None:

        self.device_handle = device_handle
        self.native_functions = native_functions

    def get_kcube_position_trigger_params(self, max_wait_in_milliseconds: int) -> TLMC_KcubePositionTriggerParams:

        return self.native_functions.get_kcube_position_trigger_params(self.device_handle, max_wait_in_milliseconds)

    def set_kcube_position_trigger_params(self, params: TLMC_KcubePositionTriggerParams) -> None:

        self.native_functions.set_kcube_position_trigger_params(self.device_handle, params)
