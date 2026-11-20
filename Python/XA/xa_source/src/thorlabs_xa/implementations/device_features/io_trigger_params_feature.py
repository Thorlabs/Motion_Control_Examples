from thorlabs_xa.interfaces.device_features.io_trigger_params import IoTriggerParams
from thorlabs_xa.native_sdks.native_functions import NativeFunctions
from thorlabs_xa.shared.params import TLMC_IoTriggerParams

class IoTriggerParamsFeature(IoTriggerParams):

    def __init__(self, device_handle: int, native_functions: NativeFunctions) -> None:

        self.device_handle = device_handle
        self.native_functions = native_functions

    def get_io_trigger_params(self, max_wait_in_milliseconds: int) -> TLMC_IoTriggerParams:
        return self.native_functions.get_io_trigger_params(self.device_handle, max_wait_in_milliseconds)

    def set_io_trigger_params(self, params: TLMC_IoTriggerParams) -> None:
        self.native_functions.set_io_trigger_params(self.device_handle, params)
