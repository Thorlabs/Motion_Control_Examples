from thorlabs_xa.interfaces.device_features.piezo_inertial_motor.amplifier_output_params import AmplifierOutputParams
from thorlabs_xa.native_sdks.native_functions import NativeFunctions
from thorlabs_xa.shared.params import TLMC_PZIM_AmplifierOutputParams

class AmplifierOutputParamsFeature(AmplifierOutputParams):

    def __init__(self, device_handle: int, native_functions: NativeFunctions) -> None:

        self.device_handle = device_handle
        self.native_functions = native_functions

    def get_amplifier_output_params(self, max_wait_in_milliseconds: int) -> TLMC_PZIM_AmplifierOutputParams:

        return self.native_functions.pzim_get_amplifier_output_params(self.device_handle, max_wait_in_milliseconds)

    def set_amplifier_output_params(self, params: TLMC_PZIM_AmplifierOutputParams) -> None:

        self.native_functions.pzim_set_amplifier_output_params(self.device_handle, params)
