from thorlabs_xa.interfaces.device_features.profile_mode_params import ProfileModeParams
from thorlabs_xa.native_sdks.native_functions import NativeFunctions
from thorlabs_xa.shared.params import TLMC_ProfileModeParams

class ProfileModeParamsFeature(ProfileModeParams):

    def __init__(self, device_handle: int, native_functions: NativeFunctions):

        self.device_handle = device_handle
        self.native_functions = native_functions

    def get_profile_mode_params(self, max_wait_in_milliseconds: int) -> TLMC_ProfileModeParams:
        return self.native_functions.get_profile_mode_params(self.device_handle, max_wait_in_milliseconds)

    def set_profile_mode_params(self, params: TLMC_ProfileModeParams):
        self.native_functions.set_profile_mode_params(self.device_handle, params)
