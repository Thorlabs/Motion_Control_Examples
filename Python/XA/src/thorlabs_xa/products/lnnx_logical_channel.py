from typing import List

from thorlabs_xa.interfaces.device_feature_groups.lnnx_logical_channel_feature_group import LnnxLogicalChannelFeatureGroup
from thorlabs_xa.native_sdks.native_functions import NativeFunctions
from thorlabs_xa.shared.device import Device
from thorlabs_xa.shared.enums import TLMC_EnableState, TLMC_OperatingMode, TLMC_PZ_PositionControlMode, TLMC_PZ_StatusBit, TLMC_ScaleType, TLMC_SettingStringFormat, TLMC_StatusItemId, TLMC_Unit
from thorlabs_xa.shared.params import TLMC_DeviceInfo, TLMC_FirmwareVersion, TLMC_HardwareInfo, TLMC_PZ_MaxOutputVoltageParams, TLMC_PZ_OutputVoltageControlSourceParams, TLMC_PZ_Status, TLMC_Setting, TLMC_StatusItem

from thorlabs_xa.interfaces.device_features.enable_state import EnableState
from thorlabs_xa.interfaces.device_features.firmware_version_info import FirmwareVersionInfo
from thorlabs_xa.interfaces.device_features.hardware_info import HardwareInfo
from thorlabs_xa.interfaces.device_features.identify import Identify
from thorlabs_xa.interfaces.device_features.piezo.max_output_voltage_params import MaxOutputVoltageParams
from thorlabs_xa.interfaces.device_features.piezo.max_travel import MaxTravel
from thorlabs_xa.interfaces.device_features.piezo.output_voltage import OutputVoltage
from thorlabs_xa.interfaces.device_features.piezo.output_voltage_control_source_params import OutputVoltageControlSourceParams
from thorlabs_xa.interfaces.device_features.piezo.piezo_status import PiezoStatus
from thorlabs_xa.interfaces.device_features.piezo.piezo_status_bits import PiezoStatusBits
from thorlabs_xa.interfaces.device_features.piezo.position import Position
from thorlabs_xa.interfaces.device_features.piezo.position_control_mode import PositionControlMode
from thorlabs_xa.interfaces.device_features.restore_factory_defaults import RestoreFactoryDefaults
from thorlabs_xa.interfaces.device_features.settings import Settings
from thorlabs_xa.interfaces.device_features.status_items import StatusItems
from thorlabs_xa.interfaces.device_features.status_mode import StatusMode
from thorlabs_xa.interfaces.device_features.unit_converter import UnitConverter
from thorlabs_xa.interfaces.device_features.piezo.zero import Zero

class LnnxLogicalChannel(Device,
    EnableState,
    FirmwareVersionInfo,
    HardwareInfo,
    Identify,
    MaxOutputVoltageParams,
    MaxTravel,
    OutputVoltage,
    OutputVoltageControlSourceParams,
    PiezoStatus,
    PiezoStatusBits,
    Position,
    PositionControlMode,
    RestoreFactoryDefaults,
    Settings,
    StatusItems,
    StatusMode,
    UnitConverter,
    Zero):
    """
    Thorlabs Low Noise NanoTrak Piezo Controller channel.
    """

    def __init__(self, device_handle: int, device_info: TLMC_DeviceInfo, feature_group: LnnxLogicalChannelFeatureGroup, native_functions: NativeFunctions) -> None:

        super().__init__(device_handle, device_info, native_functions)
        self.feature_group = feature_group

    def get_enable_state(self, max_wait_in_milliseconds: int) -> TLMC_EnableState:
        return self.feature_group.enable_state_feature.get_enable_state(max_wait_in_milliseconds)

    def set_enable_state(self, enable_state: TLMC_EnableState) -> None:
        self.feature_group.enable_state_feature.set_enable_state(enable_state)

    def get_firmware_version_info(self, max_wait_in_milliseconds: int) -> tuple [TLMC_FirmwareVersion, TLMC_FirmwareVersion]:
        return self.feature_group.firmware_version_info_feature.get_firmware_version_info(max_wait_in_milliseconds)

    def get_hardware_info(self, max_wait_in_milliseconds: int) -> TLMC_HardwareInfo:
        return self.feature_group.hardware_info_feature.get_hardware_info(max_wait_in_milliseconds)

    def identify(self) -> None:
        self.feature_group.identify_feature.identify()

    def get_max_output_voltage_params(self, max_wait_in_milliseconds: int) -> TLMC_PZ_MaxOutputVoltageParams:
        return self.feature_group.max_output_voltage_params_feature.get_max_output_voltage_params(max_wait_in_milliseconds)

    def set_max_output_voltage(self, max_output_voltage: int) -> None:
        self.feature_group.max_output_voltage_params_feature.set_max_output_voltage(max_output_voltage)

    def get_max_travel(self, max_wait_in_milliseconds: int) -> int:
        return self.feature_group.max_travel_feature.get_max_travel(max_wait_in_milliseconds)

    def set_max_travel(self, max_travel: int) -> None:
        self.feature_group.max_travel_feature.set_max_travel(max_travel)

    def get_position(self, max_wait_in_milliseconds: int) -> int:
        return self.feature_group.position_feature.get_position(max_wait_in_milliseconds)

    def set_position(self, position: int) -> None:
        self.feature_group.position_feature.set_position(position)

    def get_output_voltage(self, max_wait_in_milliseconds: int) -> int:
        return self.feature_group.output_voltage_feature.get_output_voltage(max_wait_in_milliseconds)

    def set_output_voltage(self, output_voltage: int) -> None:
        self.feature_group.output_voltage_feature.set_output_voltage(output_voltage)

    def get_output_voltage_control_source_params(self, max_wait_in_milliseconds: int) -> TLMC_PZ_OutputVoltageControlSourceParams:
        return self.feature_group.output_voltage_control_source_params_feature.get_output_voltage_control_source_params(max_wait_in_milliseconds)

    def set_output_voltage_control_source_params(self, params: TLMC_PZ_OutputVoltageControlSourceParams) -> None:
        self.feature_group.output_voltage_control_source_params_feature.set_output_voltage_control_source_params(params)

    def get_piezo_status(self, max_wait_in_milliseconds: int) -> TLMC_PZ_Status:
        return self.feature_group.piezo_status_feature.get_piezo_status(max_wait_in_milliseconds)

    def get_piezo_status_bits(self, max_wait_in_milliseconds: int) -> TLMC_PZ_StatusBit:
        return self.feature_group.piezo_status_bits_feature.get_piezo_status_bits(max_wait_in_milliseconds)

    def get_position_control_mode(self, max_wait_in_milliseconds: int) -> TLMC_PZ_PositionControlMode:
        return self.feature_group.position_control_mode_feature.get_position_control_mode(max_wait_in_milliseconds)

    def set_position_control_mode(self, control_mode: TLMC_PZ_PositionControlMode) -> None:
        self.feature_group.position_control_mode_feature.set_position_control_mode(control_mode)

    def restore_factory_defaults(self) -> None:
        self.feature_group.restore_factory_defaults_feature.restore_factory_defaults()

    def get_setting(self, settings_name: str, max_wait_in_milliseconds: int) -> TLMC_Setting:
        return self.feature_group.settings_feature.get_setting(settings_name, max_wait_in_milliseconds);

    def get_settings_items(self) -> List[TLMC_Setting]:
        return self.feature_group.settings_feature.get_settings_items()

    def get_settings(self, setting_string_format: TLMC_SettingStringFormat, include_read_only_items: bool) -> str:
        return self.feature_group.settings_feature.get_settings(setting_string_format, include_read_only_items)

    def set_settings_from_string(self, settings: str) -> None:
        self.feature_group.settings_feature.set_settings(settings)

    def get_setting_discrete_values(self, settings_name: str) -> str:
        return self.feature_group.settings_feature.get_setting_discrete_values(settings_name)

    def get_status_item(self, status_item_id: TLMC_StatusItemId) -> TLMC_StatusItem:
        return self.feature_group.status_items_feature.get_status_item(status_item_id)
    
    def get_status_item_count(self) -> int:
        return self.feature_group.status_items_feature.get_status_item_count()

    def get_status_items(self, start_index: int, number_of_items: int) -> List[TLMC_StatusItem]:
        return self.feature_group.status_items_feature.get_status_items(start_index, number_of_items)

    def set_status_mode(self, operating_mode: TLMC_OperatingMode) -> None:
        self.feature_group.status_mode_feature.set_status_mode(operating_mode)

    def convert_from_device_units_to_physical(self, scale_type: TLMC_ScaleType, device_value: int) -> tuple [float, TLMC_Unit]:
        return self.feature_group.unit_converter_feature.convert_from_device_units_to_physical(scale_type, device_value)
    
    def convert_from_physical_to_device(self, scale_type: TLMC_ScaleType, unit: TLMC_Unit, physical_value: int) -> int:
        return self.feature_group.unit_converter_feature.convert_from_physical_to_device(scale_type, unit, physical_value)

    def get_preferred_physical_unit(self, scale_type: TLMC_ScaleType) -> TLMC_Unit:
        return self.feature_group.unit_converter_feature.get_preferred_physical_unit(scale_type)

    def set_zero(self, max_wait_in_milliseconds: int) -> None:
        return self.feature_group.zero_feature.set_zero(max_wait_in_milliseconds)