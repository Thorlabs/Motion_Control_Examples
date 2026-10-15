from thorlabs_xa.interfaces.device_features.piezo_inertial_motor.kcube_io_trigger_params import KcubeIoTriggerParams
from thorlabs_xa.native_sdks.native_functions import NativeFunctions

from thorlabs_xa.shared.params import TLMC_PZIM_KcubeIoTriggerParams

class KcubeIoTriggerParamsFeature(KcubeIoTriggerParams):

    def __init__(self, device_handle: int, native_functions: NativeFunctions) -> None:

        self.device_handle = device_handle
        self.native_functions = native_functions

    def get_kcube_io_trigger_params(self, max_wait_in_milliseconds: int) -> TLMC_PZIM_KcubeIoTriggerParams:

        return self.native_functions.pzim_get_kcube_io_trigger_params(self.device_handle, max_wait_in_milliseconds)

    def set_kcube_io_trigger_params(self, params: TLMC_PZIM_KcubeIoTriggerParams) -> None:

        self.native_functions.pzim_set_kcube_io_trigger_params(self.device_handle, params)