from thorlabs_xa.interfaces.device_features.piezo_inertial_motor.external_trigger_config import ExternalTriggerConfig
from thorlabs_xa.native_sdks.native_functions import NativeFunctions
from thorlabs_xa.shared.params import TLMC_PZIM_ExternalTriggerConfig

class ExternalTriggerConfigFeature(ExternalTriggerConfig):

    def __init__(self, device_handle: int, native_functions: NativeFunctions) -> None:

        self.device_handle = device_handle
        self.native_functions = native_functions

    def get_external_trigger_config(self, max_wait_in_milliseconds: int) -> TLMC_PZIM_ExternalTriggerConfig:

        return self.native_functions.pzim_get_external_trigger_config(self.device_handle, max_wait_in_milliseconds)

    def set_external_trigger_config(self, params: TLMC_PZIM_ExternalTriggerConfig) -> None:

        self.native_functions.pzim_set_external_trigger_config(self.device_handle, params)
