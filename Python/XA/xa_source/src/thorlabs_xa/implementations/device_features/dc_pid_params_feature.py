from thorlabs_xa.interfaces.device_features.dc_pid_params import DcPidParams

from thorlabs_xa.native_sdks.native_functions import NativeFunctions
from thorlabs_xa.shared.params import TLMC_DcPidParams

class DcPidParamsFeature(DcPidParams):

    def __init__(self, device_handle: int, native_functions: NativeFunctions) -> None:
        self.device_handle = device_handle
        self.native_functions = native_functions

    def get_dc_pid_params(self, max_wait_in_milliseconds: int) -> TLMC_DcPidParams:
        return self.native_functions.get_dc_pid_params(self.device_handle, max_wait_in_milliseconds)

    def set_dc_pid_params(self, parameters: TLMC_DcPidParams) -> None:
        self.native_functions.set_dc_pid_params(self.device_handle, parameters)