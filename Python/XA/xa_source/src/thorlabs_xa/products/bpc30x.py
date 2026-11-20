from typing import List

from thorlabs_xa.interfaces.device_feature_groups.bpc30x_feature_group import Bpc30xFeatureGroup

from thorlabs_xa.interfaces.device_features.digital_output_states import DigitalOutputStates
from thorlabs_xa.interfaces.device_features.disconnect import Disconnect
from thorlabs_xa.interfaces.device_features.firmware_version_info import FirmwareVersionInfo
from thorlabs_xa.interfaces.device_features.hardware_info import HardwareInfo
from thorlabs_xa.interfaces.device_features.rack_identify import RackIdentify
from thorlabs_xa.interfaces.device_features.load_params import LoadParams
from thorlabs_xa.interfaces.device_features.rack_bay_occupied_state import RackBayOccupiedState
from thorlabs_xa.interfaces.device_features.settings import Settings

from thorlabs_xa.native_sdks.native_functions import NativeFunctions
from thorlabs_xa.shared.params import TLMC_DeviceInfo

from thorlabs_xa.shared.enums import TLMC_DigitalOutput, TLMC_RackBayNumber, TLMC_RackBayOccupiedState, TLMC_SettingStringFormat
from thorlabs_xa.shared.params import TLMC_FirmwareVersion, TLMC_HardwareInfo, TLMC_Setting
from thorlabs_xa.shared.device import Device

class Bpc30x(Device,
        DigitalOutputStates,
        Disconnect,
        FirmwareVersionInfo,
        HardwareInfo,
        LoadParams,
        RackBayOccupiedState,
        RackIdentify,
        Settings):

    def __init__(self, device_handle: int, device_info: TLMC_DeviceInfo, feature_group: Bpc30xFeatureGroup, native_functions: NativeFunctions) -> None:

        super().__init__(device_handle, device_info, native_functions)

        self.feature_group = feature_group

    def get_digital_output_states(self, max_wait_in_milliseconds: int) -> TLMC_DigitalOutput:

        return self.feature_group.digital_output_states_feature.get_digital_output_states(max_wait_in_milliseconds)

    def set_digital_output_states(self, params: TLMC_DigitalOutput) -> None:

        self.feature_group.digital_output_states_feature.set_digital_output_states(params)

    def disconnect(self) -> None:

        self.feature_group.disconnect_feature.disconnect()

    def get_firmware_version_info(self, max_wait_in_milliseconds: int) -> tuple[TLMC_FirmwareVersion, TLMC_FirmwareVersion]:

        return self.feature_group.firmware_version_info_feature.get_firmware_version_info(max_wait_in_milliseconds)

    def get_hardware_info(self, max_wait_in_milliseconds: int) -> TLMC_HardwareInfo:

        return self.feature_group.hardware_info_feature.get_hardware_info(max_wait_in_milliseconds)

    def load_params(self) -> None:

        self.feature_group.load_params_feature.load_params()

    def rack_identify(self, channel: int) -> None:

        self.feature_group.rack_identify_feature.rack_identify(channel)

    def get_rack_bay_occupied_state(self, bay_number: TLMC_RackBayNumber, max_wait_in_milliseconds: int) -> TLMC_RackBayOccupiedState:

        return self.feature_group.rack_bay_occupied_state_feature.get_rack_bay_occupied_state(bay_number, max_wait_in_milliseconds)

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