from thorlabs_xa.interfaces.device_features.piezo_inertial_motor.kcube_channel_enable import KcubeChannelEnable
from thorlabs_xa.native_sdks.native_functions import NativeFunctions

from thorlabs_xa.shared.enums import TLMC_PZIM_KcubeChannelEnableMode

class KcubeChannelEnableFeature(KcubeChannelEnable):

    def __init__(self, device_handle: int, native_functions: NativeFunctions) -> None:

        self.device_handle = device_handle
        self.native_functions = native_functions

    def get_kcube_channel_enable(self, max_wait_in_milliseconds: int) -> TLMC_PZIM_KcubeChannelEnableMode:
        return self.native_functions.pzim_get_kcube_channel_enable_mode(self.device_handle, max_wait_in_milliseconds)

    def set_kcube_channel_enable(self, channelMode : TLMC_PZIM_KcubeChannelEnableMode) -> None:
        self.native_functions.pzim_set_kcube_channel_enable_mode(self.device_handle, channelMode)