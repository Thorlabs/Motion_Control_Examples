from thorlabs_xa.interfaces.device_features.kcube_mmi_params import KcubeMmiParams
from thorlabs_xa.native_sdks.native_functions import NativeFunctions
from thorlabs_xa.shared.params import TLMC_KcubeMmiParams

class KcubeMmiParamsFeature(KcubeMmiParams):

    def __init__(self, device_handle: int, native_functions: NativeFunctions) -> None:

        self.device_handle = device_handle
        self.native_functions = native_functions

    def get_kcube_mmi_params(self, max_wait_in_milliseconds: int) -> TLMC_KcubeMmiParams:
        return self.native_functions.get_kcube_mmi_params(self.device_handle, max_wait_in_milliseconds)

    def set_kcube_mmi_params(self, params: TLMC_KcubeMmiParams) -> None:
        self.native_functions.set_kcube_mmi_params(self.device_handle, params)
