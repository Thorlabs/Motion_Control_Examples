from typing import List

from thorlabs_xa.implementations.device_feature_groups.kim101_subchannel_feature_group import Kim101SubchannelFeatureGroup
from thorlabs_xa.interfaces.device_feature_groups.kim101_feature_group import Kim101FeatureGroup

from thorlabs_xa.interfaces.device_features.disconnect import Disconnect
from thorlabs_xa.interfaces.device_features.firmware_version_info import FirmwareVersionInfo
from thorlabs_xa.interfaces.device_features.hardware_info import HardwareInfo
from thorlabs_xa.interfaces.device_features.piezo_inertial_motor.kcube_channel_enable import KcubeChannelEnable
from thorlabs_xa.interfaces.device_features.piezo_inertial_motor.stage_select_params import StageSelectParams
from thorlabs_xa.interfaces.device_features.load_params import LoadParams
from thorlabs_xa.interfaces.device_features.settings import Settings
from thorlabs_xa.interfaces.device_features.status_mode import StatusMode

from thorlabs_xa.native_sdks.native_functions import NativeFunctions
from thorlabs_xa.products.kim101_subchannel import Kim101Subchannel
from thorlabs_xa.shared.get_subchannel import GetSubchannel
from thorlabs_xa.shared.params import TLMC_DeviceInfo, TLMC_PZIM_StageSelectParams

from thorlabs_xa.shared.enums import TLMC_PZIM_KcubeChannelEnableMode, TLMC_OperatingMode, TLMC_SettingStringFormat
from thorlabs_xa.shared.params import TLMC_FirmwareVersion, TLMC_HardwareInfo, TLMC_Setting
from thorlabs_xa.shared.device import Device
from thorlabs_xa.shared.subchannel import Subchannel

class Kim101(Device,
        GetSubchannel,
        Disconnect,
        FirmwareVersionInfo,
        HardwareInfo,
        KcubeChannelEnable,
        LoadParams,
        Settings,
        StageSelectParams,
        StatusMode):

    _SUBCHANNEL_COUNT = 4

    def __init__(self, device_handle: int, device_info: TLMC_DeviceInfo, feature_group: Kim101FeatureGroup, native_functions: NativeFunctions) -> None:

        super().__init__(device_handle, device_info, native_functions)

        self.feature_group = feature_group
        self._subchannels: dict[int, Kim101Subchannel] = {}
        self._init_subchannels(native_functions)

    def _init_subchannels(self, native_functions: NativeFunctions) -> None:
        for channel_number in range(1, self._SUBCHANNEL_COUNT + 1):
            subchannel_handle = native_functions.get_channel(self._device_handle, channel_number)
            feature_group = Kim101SubchannelFeatureGroup(subchannel_handle, native_functions)
            subchannel = Kim101Subchannel(
                subchannel_handle, channel_number, feature_group, native_functions
            )
            subchannel.set_parent_device_identity(
                self.device_id,
                self.device_type,
            )
            self._subchannels[channel_number] = subchannel

    def get_subchannel(self, subchannel_number: int) -> Subchannel:
        subchannel = self._subchannels.get(subchannel_number)
        if subchannel is None:
            raise ValueError(f"Subchannel number {subchannel_number} is not available on this device.")
        return subchannel

    def get_all_subchannels(self) -> List[Subchannel]:
        return list(self._subchannels.values())

    def disconnect(self) -> None:

        self.feature_group.disconnect_feature.disconnect()

    def get_firmware_version_info(self, max_wait_in_milliseconds: int) -> tuple[TLMC_FirmwareVersion, TLMC_FirmwareVersion]:

        return self.feature_group.firmware_version_info_feature.get_firmware_version_info(max_wait_in_milliseconds)

    def get_hardware_info(self, max_wait_in_milliseconds: int) -> TLMC_HardwareInfo:

        return self.feature_group.hardware_info_feature.get_hardware_info(max_wait_in_milliseconds)

    def get_kcube_channel_enable(self, max_wait_in_milliseconds: int) -> TLMC_PZIM_KcubeChannelEnableMode:

        return self.feature_group.kcube_channel_enable_feature.get_kcube_channel_enable(max_wait_in_milliseconds)

    def set_kcube_channel_enable(self, channelMode: TLMC_PZIM_KcubeChannelEnableMode) -> None:

        self.feature_group.kcube_channel_enable_feature.set_kcube_channel_enable(channelMode)

    def load_params(self) -> None:

        self.feature_group.load_params_feature.load_params()

    def get_setting(self, settings_name: str, max_wait_in_milliseconds: int) -> TLMC_Setting:

        return self.feature_group.settings_feature.get_setting(settings_name, max_wait_in_milliseconds)

    def get_setting_discrete_values(self, settings_name: str) -> str:

        return self.feature_group.settings_feature.get_setting_discrete_values(settings_name)

    def get_settings(self, setting_string_format: TLMC_SettingStringFormat, include_read_only_items: bool) -> str:

        return self.feature_group.settings_feature.get_settings(setting_string_format, include_read_only_items)

    def get_settings_items(self) -> List[TLMC_Setting]:

        return self.feature_group.settings_feature.get_settings_items()

    def set_settings(self, settings: str) -> None:

        self.feature_group.settings_feature.set_settings(settings)

    def set_stage_select_params(self, params: TLMC_PZIM_StageSelectParams) -> None:

        self.feature_group.stage_select_params_feature.set_stage_select_params(params)

    def set_status_mode(self, operating_mode: TLMC_OperatingMode) -> None:

        self.feature_group.status_mode_feature.set_status_mode(operating_mode)