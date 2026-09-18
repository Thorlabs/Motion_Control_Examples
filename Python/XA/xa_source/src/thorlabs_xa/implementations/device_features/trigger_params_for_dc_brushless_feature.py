from thorlabs_xa.interfaces.device_features.trigger_params_for_dc_brushless import TriggerParamsForDcBrushless
from thorlabs_xa.native_sdks.native_functions import NativeFunctions
from thorlabs_xa.shared.params import TLMC_TriggerParamsForDcBrushless

class TriggerParamsForDcBrushlessFeature(TriggerParamsForDcBrushless):

    def __init__(self, device_handle: int, native_functions: NativeFunctions):

        self.device_handle = device_handle
        self.native_functions = native_functions

    def get_trigger_params_for_dc_brushless(self, max_wait_in_milliseconds: int) -> TLMC_TriggerParamsForDcBrushless:

        return self.native_functions.get_trigger_params_for_dc_brushless(self.device_handle, max_wait_in_milliseconds)

    def set_trigger_params_for_dc_brushless(self, params: TLMC_TriggerParamsForDcBrushless) -> None:
            
        self.native_functions.set_trigger_params_for_dc_brushless(self.device_handle, params)
