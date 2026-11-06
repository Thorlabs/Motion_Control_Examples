from typing import List

from thorlabs_xa.interfaces.device_feature_groups.ksc101_feature_group import Ksc101FeatureGroup

from thorlabs_xa.interfaces.device_features.av_modes import AvModes
from thorlabs_xa.interfaces.device_features.disconnect import Disconnect
from thorlabs_xa.interfaces.device_features.enable_state import EnableState
from thorlabs_xa.interfaces.device_features.firmware_version_info import FirmwareVersionInfo
from thorlabs_xa.interfaces.device_features.hardware_info import HardwareInfo
from thorlabs_xa.interfaces.device_features.identify import Identify
from thorlabs_xa.interfaces.device_features.kcube_io_trigger_params import KcubeIoTriggerParams
from thorlabs_xa.interfaces.device_features.kcube_mmi_params import KcubeMmiParams
from thorlabs_xa.interfaces.device_features.load_params import LoadParams
from thorlabs_xa.interfaces.device_features.persist_params import PersistParams
from thorlabs_xa.interfaces.device_features.rich_response import RichResponse
from thorlabs_xa.interfaces.device_features.settings import Settings
from thorlabs_xa.interfaces.device_features.solenoid_cycle_params import SolenoidCycleParams
from thorlabs_xa.interfaces.device_features.solenoid_interlock_mode import SolenoidInterlockMode
from thorlabs_xa.interfaces.device_features.solenoid_operating_mode import SolenoidOperatingMode
from thorlabs_xa.interfaces.device_features.solenoid_state import SolenoidState
from thorlabs_xa.interfaces.device_features.solenoid_status import SolenoidStatus
from thorlabs_xa.interfaces.device_features.solenoid_status_bits import SolenoidStatusBits
from thorlabs_xa.interfaces.device_features.status_items import StatusItems
from thorlabs_xa.interfaces.device_features.status_mode import StatusMode
from thorlabs_xa.interfaces.device_features.status_request import StatusRequest

from thorlabs_xa.native_sdks.native_functions import NativeFunctions
from thorlabs_xa.shared.params import TLMC_DeviceInfo

from thorlabs_xa.shared.enums import TLMC_EnableState, TLMC_AvMode, TLMC_OperatingMode, TLMC_ParameterGroupId, TLMC_SettingStringFormat, TLMC_SolenoidInterlockMode, TLMC_SolenoidOperatingMode, TLMC_SolenoidState, TLMC_SolenoidStatusBit, TLMC_StatusItemId
from thorlabs_xa.shared.params import TLMC_FirmwareVersion, TLMC_HardwareInfo, TLMC_KcubeIoTriggerParams, TLMC_KcubeMmiParams, TLMC_RichResponse, TLMC_Setting, TLMC_SolenoidCycleParams, TLMC_SolenoidStatus, TLMC_StatusItem
from thorlabs_xa.shared.device import Device

class Ksc101(Device,
        AvModes,
        Disconnect,
        EnableState,
        FirmwareVersionInfo,
        HardwareInfo,
        Identify,
        KcubeIoTriggerParams,
        KcubeMmiParams,
        LoadParams,
        PersistParams,
        RichResponse,
        Settings,
        SolenoidCycleParams,
        SolenoidInterlockMode,
        SolenoidOperatingMode,
        SolenoidState,
        SolenoidStatus,
        SolenoidStatusBits,
        StatusItems,
        StatusMode,
        StatusRequest):

    def __init__(self, device_handle: int, device_info: TLMC_DeviceInfo, feature_group: Ksc101FeatureGroup, native_functions: NativeFunctions) -> None:

        super().__init__(device_handle, device_info, native_functions)

        self.feature_group = feature_group

    def get_av_modes(self, max_wait_in_milliseconds: int) -> TLMC_AvMode:

        return self.feature_group.av_modes_feature.get_av_modes(max_wait_in_milliseconds)

    def set_av_modes(self, avModes: TLMC_AvMode) -> None:

        self.feature_group.av_modes_feature.set_av_modes(avModes)

    def disconnect(self) -> None:

        self.feature_group.disconnect_feature.disconnect()

    def get_enable_state(self, max_wait_in_milliseconds: int) -> TLMC_EnableState:

        return self.feature_group.enable_state_feature.get_enable_state(max_wait_in_milliseconds)

    def set_enable_state(self, enable_state: TLMC_EnableState) -> None:

        self.feature_group.enable_state_feature.set_enable_state(enable_state)

    def get_firmware_version_info(self, max_wait_in_milliseconds: int) -> tuple[TLMC_FirmwareVersion, TLMC_FirmwareVersion]:

        return self.feature_group.firmware_version_info_feature.get_firmware_version_info(max_wait_in_milliseconds)

    def get_hardware_info(self, max_wait_in_milliseconds: int) -> TLMC_HardwareInfo:

        return self.feature_group.hardware_info_feature.get_hardware_info(max_wait_in_milliseconds)

    def identify(self) -> None:

        self.feature_group.identify_feature.identify()

    def get_kcube_io_trigger_params(self, max_wait_in_milliseconds: int) -> TLMC_KcubeIoTriggerParams:

        return self.feature_group.kcube_io_trigger_params_feature.get_kcube_io_trigger_params(max_wait_in_milliseconds)

    def set_kcube_io_trigger_params(self, params: TLMC_KcubeIoTriggerParams) -> None:

        self.feature_group.kcube_io_trigger_params_feature.set_kcube_io_trigger_params(params)

    def get_kcube_mmi_params(self, max_wait_in_milliseconds: int) -> TLMC_KcubeMmiParams:

        return self.feature_group.kcube_mmi_params_feature.get_kcube_mmi_params(max_wait_in_milliseconds)

    def set_kcube_mmi_params(self, params: TLMC_KcubeMmiParams) -> None:

        self.feature_group.kcube_mmi_params_feature.set_kcube_mmi_params(params)

    def load_params(self) -> None:

        self.feature_group.load_params_feature.load_params()

    def persist_params(self, parameter_group_id: TLMC_ParameterGroupId) -> None:

        self.feature_group.persist_params_feature.persist_params(parameter_group_id)

    def get_rich_response(self) -> TLMC_RichResponse:

        return self.feature_group.rich_response_feature.get_rich_response()

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

    def get_solenoid_cycle_params(self, max_wait_in_milliseconds: int) -> TLMC_SolenoidCycleParams:

        return self.feature_group.solenoid_cycle_params_feature.get_solenoid_cycle_params(max_wait_in_milliseconds)

    def set_solenoid_cycle_params(self, solenoid_cycle_params: TLMC_SolenoidCycleParams) -> None:

        self.feature_group.solenoid_cycle_params_feature.set_solenoid_cycle_params(solenoid_cycle_params)

    def get_solenoid_interlock_mode(self, max_wait_in_milliseconds: int) -> TLMC_SolenoidInterlockMode:

        return self.feature_group.solenoid_interlock_mode_feature.get_solenoid_interlock_mode(max_wait_in_milliseconds)

    def set_solenoid_interlock_mode(self, interlock_mode: TLMC_SolenoidInterlockMode) -> None:

        self.feature_group.solenoid_interlock_mode_feature.set_solenoid_interlock_mode(interlock_mode)

    def get_solenoid_operating_mode(self, max_wait_in_milliseconds: int) -> TLMC_SolenoidOperatingMode:

        return self.feature_group.solenoid_operating_mode_feature.get_solenoid_operating_mode(max_wait_in_milliseconds)

    def set_solenoid_operating_mode(self, mode: TLMC_SolenoidOperatingMode) -> None:

        self.feature_group.solenoid_operating_mode_feature.set_solenoid_operating_mode(mode)

    def get_solenoid_state(self, max_wait_in_milliseconds: int) -> TLMC_SolenoidState:

        return self.feature_group.solenoid_state_feature.get_solenoid_state(max_wait_in_milliseconds)

    def set_solenoid_state(self, state: TLMC_SolenoidState) -> None:

        self.feature_group.solenoid_state_feature.set_solenoid_state(state)

    def get_solenoid_status(self, max_wait_in_milliseconds: int) -> TLMC_SolenoidStatus:

        return self.feature_group.solenoid_status_feature.get_solenoid_status(max_wait_in_milliseconds)

    def get_solenoid_status_bits(self, max_wait_in_milliseconds: int) -> TLMC_SolenoidStatusBit:

        return self.feature_group.solenoid_status_bits_feature.get_solenoid_status_bits(max_wait_in_milliseconds)

    def get_status_item(self, status_item_id: TLMC_StatusItemId) -> TLMC_StatusItem:

        return self.feature_group.status_items_feature.get_status_item(status_item_id)

    def get_status_item_count(self) -> int:

        return self.feature_group.status_items_feature.get_status_item_count()

    def get_status_items(self, start_index: int, number_of_items: int) -> List[TLMC_StatusItem]:

        return self.feature_group.status_items_feature.get_status_items(start_index, number_of_items)

    def set_status_mode(self, operating_mode: TLMC_OperatingMode) -> None:

        self.feature_group.status_mode_feature.set_status_mode(operating_mode)

    def request_status(self, max_wait_in_milliseconds: int) -> None:

        self.feature_group.status_request_feature.request_status(max_wait_in_milliseconds)