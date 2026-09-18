from thorlabs_xa.interfaces.device_features.trigger_params_for_stepper import TriggerParamsForStepper
from thorlabs_xa.native_sdks.native_functions import NativeFunctions
from thorlabs_xa.shared.params import TLMC_TriggerParamsForStepper

class TriggerParamsForStepperFeature(TriggerParamsForStepper):

    def __init__(self, device_handle: int, native_functions: NativeFunctions):

        self.device_handle = device_handle
        self.native_functions = native_functions

    def get_trigger_params_for_stepper(self, max_wai_in_milliseconds: int) -> TLMC_TriggerParamsForStepper:

        return self.native_functions.get_trigger_params_for_stepper(self.device_handle, max_wai_in_milliseconds)

    def set_trigger_params_for_stepper(self, params: TLMC_TriggerParamsForStepper) -> None:

        self.native_functions.set_trigger_params_for_stepper(self.device_handle, params)
