from typing import List

from thorlabs_xa.implementations.device_feature_groups.pdxc3_subchannel_feature_group import Pdxc3SubchannelFeatureGroup
from thorlabs_xa.interfaces.device_feature_groups.pdxc3_feature_group import Pdxc3FeatureGroup

from thorlabs_xa.interfaces.device_features.disconnect import Disconnect
from thorlabs_xa.interfaces.device_features.firmware_version_info import FirmwareVersionInfo
from thorlabs_xa.interfaces.device_features.hardware_info import HardwareInfo
from thorlabs_xa.interfaces.device_features.identify import Identify
from thorlabs_xa.interfaces.device_features.load_params import LoadParams
from thorlabs_xa.interfaces.device_features.move_sync_array import MoveSyncArray
from thorlabs_xa.interfaces.device_features.move_sync_params import MoveSyncParams
from thorlabs_xa.interfaces.device_features.move_sync_start import MoveSyncStart
from thorlabs_xa.interfaces.device_features.settings import Settings
from thorlabs_xa.interfaces.device_features.status_mode import StatusMode

from thorlabs_xa.native_sdks.native_functions import NativeFunctions
from thorlabs_xa.products.pdxc3_subchannel import Pdxc3Subchannel
from thorlabs_xa.shared.get_subchannel import GetSubchannel
from thorlabs_xa.shared.params import TLMC_DeviceInfo

from thorlabs_xa.shared.enums import TLMC_OperatingMode, TLMC_SettingStringFormat
from thorlabs_xa.shared.params import TLMC_FirmwareVersion, TLMC_HardwareInfo, TLMC_MoveSyncArray, TLMC_MoveSyncParams, TLMC_MoveSyncStartParams, TLMC_Setting
from thorlabs_xa.shared.device import Device
from thorlabs_xa.shared.subchannel import Subchannel

class Pdxc3(Device,
        GetSubchannel,
        Disconnect,
        FirmwareVersionInfo,
        HardwareInfo,
        Identify,
        LoadParams,
        MoveSyncArray,
        MoveSyncParams,
        MoveSyncStart,
        Settings,
        StatusMode):

    _SUBCHANNEL_COUNT = 3

    def __init__(self, device_handle: int, device_info: TLMC_DeviceInfo, feature_group: Pdxc3FeatureGroup, native_functions: NativeFunctions) -> None:

        super().__init__(device_handle, device_info, native_functions)

        self.feature_group = feature_group
        self._subchannels: dict[int, Pdxc3Subchannel] = {}
        self._init_subchannels(native_functions)

    def _init_subchannels(self, native_functions: NativeFunctions) -> None:
        for channel_number in range(1, self._SUBCHANNEL_COUNT + 1):
            subchannel_handle = native_functions.get_channel(self._device_handle, channel_number)
            feature_group = Pdxc3SubchannelFeatureGroup(subchannel_handle, native_functions)
            subchannel = Pdxc3Subchannel(
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

    def identify(self) -> None:

        self.feature_group.identify_feature.identify()

    def load_params(self) -> None:

        self.feature_group.load_params_feature.load_params()

    def set_move_sync_array(self, parameters: TLMC_MoveSyncArray) -> None:

        self.feature_group.move_sync_array_feature.set_move_sync_array(parameters)

    def set_move_sync_params(self, parameters: TLMC_MoveSyncParams) -> None:

        self.feature_group.move_sync_params_feature.set_move_sync_params(parameters)

    def move_sync_start(self, parameters: TLMC_MoveSyncStartParams) -> None:

        self.feature_group.move_sync_start_feature.move_sync_start(parameters)

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

    def set_status_mode(self, operating_mode: TLMC_OperatingMode) -> None:

        self.feature_group.status_mode_feature.set_status_mode(operating_mode)