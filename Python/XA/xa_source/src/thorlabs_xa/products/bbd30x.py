from typing import List

from thorlabs_xa.interfaces.device_feature_groups.bbd30x_feature_group import Bbd30xFeatureGroup

from thorlabs_xa.interfaces.device_features.analog_monitor_configuration_params import AnalogMonitorConfigurationParams
from thorlabs_xa.interfaces.device_features.aux_io_configuration_params import AuxIoConfigurationParams
from thorlabs_xa.interfaces.device_features.digital_input_states import DigitalInputStates
from thorlabs_xa.interfaces.device_features.digital_output_states import DigitalOutputStates
from thorlabs_xa.interfaces.device_features.disconnect import Disconnect
from thorlabs_xa.interfaces.device_features.firmware_version_info import FirmwareVersionInfo
from thorlabs_xa.interfaces.device_features.hardware_info import HardwareInfo
from thorlabs_xa.interfaces.device_features.io_configuration_params import IoConfigurationParams
from thorlabs_xa.interfaces.device_features.lcd_display_params import LcdDisplayParams
from thorlabs_xa.interfaces.device_features.load_params import LoadParams
from thorlabs_xa.interfaces.device_features.move_sync_array import MoveSyncArray
from thorlabs_xa.interfaces.device_features.move_sync_params import MoveSyncParams
from thorlabs_xa.interfaces.device_features.move_sync_start import MoveSyncStart
from thorlabs_xa.interfaces.device_features.persist_params import PersistParams
from thorlabs_xa.interfaces.device_features.rack_identify import RackIdentify
from thorlabs_xa.interfaces.device_features.rack_bay_occupied_state import RackBayOccupiedState
from thorlabs_xa.interfaces.device_features.settings import Settings

from thorlabs_xa.native_sdks.native_functions import NativeFunctions
from thorlabs_xa.shared.params import TLMC_DeviceInfo

from thorlabs_xa.shared.enums import TLMC_AnalogMonitorNumber, TLMC_AuxIoPortMode, TLMC_AuxIoPortNumber, TLMC_DigitalInput, TLMC_DigitalOutput, TLMC_IoPortNumber, TLMC_ParameterGroupId, TLMC_RackBayNumber, TLMC_RackBayOccupiedState, TLMC_SettingStringFormat
from thorlabs_xa.shared.params import TLMC_AnalogMonitorConfigurationParams, TLMC_FirmwareVersion, TLMC_HardwareInfo, TLMC_IoConfigurationParams, TLMC_LcdDisplayParams, TLMC_MoveSyncArray, TLMC_MoveSyncParams, TLMC_MoveSyncStartParams, TLMC_Setting
from thorlabs_xa.shared.device import Device

class Bbd30x(Device,
        AnalogMonitorConfigurationParams,
        AuxIoConfigurationParams,
        DigitalInputStates,
        DigitalOutputStates,
        Disconnect,
        FirmwareVersionInfo,
        HardwareInfo,
        IoConfigurationParams,
        LcdDisplayParams,
        LoadParams,
        MoveSyncArray,
        MoveSyncParams,
        MoveSyncStart,
        PersistParams,
        RackIdentify,
        RackBayOccupiedState,
        Settings):

    def __init__(self, device_handle: int, device_info: TLMC_DeviceInfo, feature_group: Bbd30xFeatureGroup, native_functions: NativeFunctions) -> None:

        super().__init__(device_handle, device_info, native_functions)

        self.feature_group = feature_group

    def get_analog_monitor_configuration_params(self, monitor_number: TLMC_AnalogMonitorNumber, max_wait_in_milliseconds: int) -> TLMC_AnalogMonitorConfigurationParams:

        return self.feature_group.analog_monitor_configuration_params_feature.get_analog_monitor_configuration_params(monitor_number, max_wait_in_milliseconds)

    def set_analog_monitor_configuration_params(self, monitor_number: TLMC_AnalogMonitorNumber, params: TLMC_AnalogMonitorConfigurationParams) -> None:

        self.feature_group.analog_monitor_configuration_params_feature.set_analog_monitor_configuration_params(monitor_number, params)

    def get_aux_io_port_mode(self, port_number: TLMC_AuxIoPortNumber, max_wait_in_milliseconds: int) -> TLMC_AuxIoPortMode:

        return self.feature_group.aux_io_configuration_params_feature.get_aux_io_port_mode(port_number, max_wait_in_milliseconds)

    def get_aux_io_software_states(self, max_wait_in_milliseconds: int) -> int:

        return self.feature_group.aux_io_configuration_params_feature.get_aux_io_software_states(max_wait_in_milliseconds)

    def set_aux_io_port_mode(self, port_number: TLMC_AuxIoPortNumber, port_mode: TLMC_AuxIoPortMode) -> None:

        self.feature_group.aux_io_configuration_params_feature.set_aux_io_port_mode(port_number, port_mode)

    def set_aux_io_software_states(self, software_states: int) -> None:

        self.feature_group.aux_io_configuration_params_feature.set_aux_io_software_states(software_states)

    def get_digital_input_states(self, max_wait_in_milliseconds: int) -> TLMC_DigitalInput:

        return self.feature_group.digital_input_states_feature.get_digital_input_states(max_wait_in_milliseconds)

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

    def get_io_configuration_number_of_ports_supported(self) -> int:

        return self.feature_group.io_configuration_params_feature.get_io_configuration_number_of_ports_supported()

    def get_io_configuration_params(self, port_number: TLMC_IoPortNumber, max_wait_in_milliseconds: int) -> TLMC_IoConfigurationParams:

        return self.feature_group.io_configuration_params_feature.get_io_configuration_params(port_number, max_wait_in_milliseconds)

    def set_io_configuration_params(self, handle: int, port_number: TLMC_IoPortNumber, params: TLMC_IoConfigurationParams) -> None:

        self.feature_group.io_configuration_params_feature.set_io_configuration_params(handle, port_number, params)

    def get_lcd_display_params(self, max_wait_in_milliseconds: int) -> TLMC_LcdDisplayParams:

        return self.feature_group.lcd_display_params_feature.get_lcd_display_params(max_wait_in_milliseconds)

    def set_lcd_display_params(self, params: TLMC_LcdDisplayParams) -> None:

        self.feature_group.lcd_display_params_feature.set_lcd_display_params(params)

    def load_params(self) -> None:

        self.feature_group.load_params_feature.load_params()

    def set_move_sync_array(self, parameters: TLMC_MoveSyncArray) -> None:

        self.feature_group.move_sync_array_feature.set_move_sync_array(parameters)

    def set_move_sync_params(self, parameters: TLMC_MoveSyncParams) -> None:

        self.feature_group.move_sync_params_feature.set_move_sync_params(parameters)

    def move_sync_start(self, parameters: TLMC_MoveSyncStartParams) -> None:

        self.feature_group.move_sync_start_feature.move_sync_start(parameters)

    def persist_params(self, parameter_group_id: TLMC_ParameterGroupId) -> None:

        self.feature_group.persist_params_feature.persist_params(parameter_group_id)

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