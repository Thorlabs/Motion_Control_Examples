from typing import List

from thorlabs_xa.interfaces.device_feature_groups.kpc101_feature_group import Kpc101FeatureGroup
from thorlabs_xa.interfaces.device_features.connected_product import ConnectedProduct
from thorlabs_xa.interfaces.device_features.digital_output_states import DigitalOutputStates
from thorlabs_xa.interfaces.device_features.disconnect import Disconnect
from thorlabs_xa.interfaces.device_features.enable_state import EnableState
from thorlabs_xa.interfaces.device_features.firmware_version_info import FirmwareVersionInfo
from thorlabs_xa.interfaces.device_features.hardware_info import HardwareInfo
from thorlabs_xa.interfaces.device_features.identify import Identify
from thorlabs_xa.interfaces.device_features.kcube_mmi_lock import KcubeMmiLock
from thorlabs_xa.interfaces.device_features.load_params import LoadParams
from thorlabs_xa.interfaces.device_features.persist_params import PersistParams
from thorlabs_xa.interfaces.device_features.piezo.kpc_io_settings_params import KpcIoSettingsParams
from thorlabs_xa.interfaces.device_features.piezo.kpc_io_trigger_params import KpcIoTriggerParams
from thorlabs_xa.interfaces.device_features.piezo.kpc_mmi_params import KpcMmiParams
from thorlabs_xa.interfaces.device_features.piezo.max_travel import MaxTravel
from thorlabs_xa.interfaces.device_features.piezo.output_voltage import OutputVoltage
from thorlabs_xa.interfaces.device_features.piezo.output_voltage_control_source_params import OutputVoltageControlSourceParams
from thorlabs_xa.interfaces.device_features.piezo.output_waveform import OutputWaveform
from thorlabs_xa.interfaces.device_features.piezo.output_waveform_params_getter import OutputWaveformParamsGetter
from thorlabs_xa.interfaces.device_features.piezo.piezo_status import PiezoStatus
from thorlabs_xa.interfaces.device_features.piezo.piezo_status_bits import PiezoStatusBits
from thorlabs_xa.interfaces.device_features.piezo.position import Position
from thorlabs_xa.interfaces.device_features.piezo.position_control_mode import PositionControlMode
from thorlabs_xa.interfaces.device_features.piezo.position_loop_params import PositionLoopParams
from thorlabs_xa.interfaces.device_features.piezo.zero import Zero
from thorlabs_xa.interfaces.device_features.restore_factory_defaults import RestoreFactoryDefaults
from thorlabs_xa.interfaces.device_features.rich_response import RichResponse
from thorlabs_xa.interfaces.device_features.settings import Settings
from thorlabs_xa.interfaces.device_features.status_items import StatusItems
from thorlabs_xa.interfaces.device_features.status_mode import StatusMode
from thorlabs_xa.interfaces.device_features.status_request import StatusRequest
from thorlabs_xa.interfaces.device_features.unit_converter import UnitConverter

from thorlabs_xa.native_sdks.native_functions import NativeFunctions

from thorlabs_xa.shared.device import Device
from thorlabs_xa.shared.enums import TLMC_DigitalOutput, TLMC_EnableState, TLMC_KcubeMmiLockState, TLMC_OperatingMode, TLMC_PZ_PositionControlMode, TLMC_PZ_StatusBit, TLMC_ParameterGroupId, TLMC_ScaleType, TLMC_SettingStringFormat, TLMC_StatusItemId, TLMC_Unit
from thorlabs_xa.shared.params import TLMC_ConnectedProductInfo, TLMC_DeviceInfo, TLMC_FirmwareVersion, TLMC_HardwareInfo, TLMC_PZ_KpcIoSettingsParams, TLMC_PZ_KpcIoTriggerParams, TLMC_PZ_KpcMmiParams, TLMC_PZ_OutputVoltageControlSourceParams, TLMC_PZ_OutputWaveformLoopTableSample, TLMC_PZ_OutputWaveformParams, TLMC_PZ_PositionLoopParams, TLMC_PZ_Status, TLMC_RichResponse, TLMC_Setting, TLMC_StatusItem


class Kpc101(Device,
            ConnectedProduct,
            DigitalOutputStates,
            Disconnect,
            EnableState,
            FirmwareVersionInfo,
            HardwareInfo,
            Identify,
            KcubeMmiLock,
            KpcIoSettingsParams,
            KpcIoTriggerParams,
            KpcMmiParams,
            LoadParams,
            MaxTravel,
            OutputVoltage,
            OutputVoltageControlSourceParams,
            OutputWaveform,
            OutputWaveformParamsGetter,
            PersistParams,
            PiezoStatus,
            PiezoStatusBits,
            PositionLoopParams,
            Position,
            PositionControlMode,
            RestoreFactoryDefaults,
            RichResponse,
            Settings,
            StatusItems,
            StatusRequest,
            StatusMode,
            UnitConverter,
            Zero):
    """
    Thorlabs Kcube Piezo Controller With Strain Gauge. 
    """
    def __init__(self, device_handle: int, device_info: TLMC_DeviceInfo, feature_group: Kpc101FeatureGroup, native_functions: NativeFunctions) -> None:

        super().__init__(device_handle, device_info, native_functions)

        self.feature_group = feature_group

    def get_connected_product_info(self) -> TLMC_ConnectedProductInfo:
        return self.feature_group.connected_product_feature.get_connected_product_info()

    def get_supported_connected_products(self) -> List[str]:
        return self.feature_group.connected_product_feature.get_supported_connected_products()

    def set_connected_product(self, product_name: str) -> None:
        self.feature_group.connected_product_feature.set_connected_product(product_name)

    def set_connected_product_info(self, product_info: TLMC_ConnectedProductInfo) -> None:
        self.feature_group.connected_product_feature.set_connected_product_info(product_info)

    def get_digital_output_states(self, max_wait_in_milliseconds: int) -> TLMC_DigitalOutput:
        return self.feature_group.digital_output_states_feature.get_digital_output_states(max_wait_in_milliseconds)

    def set_digital_output_states(self, params: TLMC_DigitalOutput) -> None:
        self.feature_group.digital_output_states_feature.set_digital_output_states(params)

    def disconnect(self) -> None:
        self.feature_group.disconnect_feature.disconnect()

    def get_enable_state(self, max_wait_in_milliseconds: int) -> TLMC_EnableState:
        return self.feature_group.enable_state_feature.get_enable_state(max_wait_in_milliseconds)

    def set_enable_state(self, enable_state: TLMC_EnableState) -> None:
        self.feature_group.enable_state_feature.set_enable_state(enable_state)

    def get_firmware_version_info(self, max_wait_in_milliseconds: int) -> tuple [TLMC_FirmwareVersion, TLMC_FirmwareVersion]:
        return self.feature_group.firmware_version_info_feature.get_firmware_version_info(max_wait_in_milliseconds)

    def get_hardware_info(self, max_wait_in_milliseconds: int) -> TLMC_HardwareInfo:
        return self.feature_group.hardware_version_info_feature.get_hardware_info(max_wait_in_milliseconds)

    def identify(self) -> None:
        self.feature_group.identify_feature.identify()

    def get_kcube_mmi_lock_state(self, max_wait_in_milliseconds: int) -> TLMC_KcubeMmiLockState:
        return self.feature_group.kcube_mmi_lock_feature.get_kcube_mmi_lock_state(max_wait_in_milliseconds)

    def set_kcube_mmi_lock_state(self, lock_state: TLMC_KcubeMmiLockState) -> None:
        self.feature_group.kcube_mmi_lock_feature.set_kcube_mmi_lock_state(lock_state)

    def get_io_settings_params(self, max_wait_in_milliseconds: int) -> TLMC_PZ_KpcIoSettingsParams:
        return self.feature_group.kpc_io_settings_params_feature.get_io_settings_params(max_wait_in_milliseconds)

    def set_io_settings_params(self, params: TLMC_PZ_KpcIoSettingsParams) -> None:
        return self.feature_group.kpc_io_settings_params_feature.set_io_settings_params(params)

    def get_io_trigger_params(self, max_wait_in_milliseconds: int) -> TLMC_PZ_KpcIoTriggerParams:
        return self.feature_group.kpc_io_trigger_params_feature.get_io_trigger_params(max_wait_in_milliseconds)

    def set_io_trigger_params(self, params: TLMC_PZ_KpcIoTriggerParams) -> None:
        return self.feature_group.kpc_io_trigger_params_feature.set_io_trigger_params(params)

    def get_kpc_mmi_params(self, max_wait_in_milliseconds: int) -> TLMC_PZ_KpcMmiParams:
        return self.feature_group.kpc_mmi_params_feature.get_kpc_mmi_params(max_wait_in_milliseconds)

    def set_kpc_mmi_params(self, params: TLMC_PZ_KpcMmiParams) -> None:
        return self.feature_group.kpc_mmi_params_feature.set_kpc_mmi_params(params)

    def load_params(self) -> None:
        self.feature_group.load_params_feature.load_params()

    def get_max_travel(self, max_wait_in_milliseconds: int) -> int:
        return self.feature_group.max_travel_feature.get_max_travel(max_wait_in_milliseconds)

    def set_max_travel(self, max_travel: int) -> None:
        self.feature_group.max_travel_feature.set_max_travel(max_travel)

    def get_output_voltage(self, max_wait_in_milliseconds: int) -> int:
        return self.feature_group.output_voltage_feature.get_output_voltage(max_wait_in_milliseconds)

    def set_output_voltage(self, output_voltage: int) -> None:
        self.feature_group.output_voltage_feature.set_output_voltage(output_voltage)

    def get_output_voltage_control_source_params(self, max_wait_in_milliseconds: int) -> TLMC_PZ_OutputVoltageControlSourceParams:
        return self.feature_group.output_voltage_control_source_params_feature.get_output_voltage_control_source_params(max_wait_in_milliseconds)

    def set_output_voltage_control_source_params(self, params: TLMC_PZ_OutputVoltageControlSourceParams) -> None:
        self.feature_group.output_voltage_control_source_params_feature.set_output_voltage_control_source_params(params)

    def set_output_waveform_params(self, params: TLMC_PZ_OutputWaveformParams) -> None:
        self.feature_group.output_waveform_feature.set_output_waveform_params(params)

    def set_output_waveform_lookup_table_sample_params(self, params: TLMC_PZ_OutputWaveformLoopTableSample) -> None:
        self.feature_group.output_waveform_feature.set_output_waveform_lookup_table_sample_params(params)

    def start_output_waveform(self) -> None:
        self.feature_group.output_waveform_feature.start_output_waveform()

    def stop_output_waveform(self) -> None:
        self.feature_group.output_waveform_feature.stop_output_waveform()

    def get_output_waveform_params(self, max_wait_in_milliseconds: int) -> TLMC_PZ_OutputWaveformParams:
        return self.feature_group.output_waveform_params_getter_feature.get_output_waveform_params(max_wait_in_milliseconds)

    def persist_params(self, parameter_group_id: TLMC_ParameterGroupId) -> None:
        self.feature_group.persist_params_feature.persist_params(parameter_group_id)

    def get_piezo_status_bits(self, max_wait_in_milliseconds: int) -> TLMC_PZ_StatusBit:
        return self.feature_group.piezo_status_bits_feature.get_piezo_status_bits(max_wait_in_milliseconds)

    def get_piezo_status(self, max_wait_in_milliseconds: int) -> TLMC_PZ_Status:
        return self.feature_group.piezo_status_feature.get_piezo_status(max_wait_in_milliseconds)

    def get_position_control_mode(self, max_wait_in_milliseconds: int) -> TLMC_PZ_PositionControlMode:
        return self.feature_group.position_control_mode_feature.get_position_control_mode(max_wait_in_milliseconds)

    def set_position_control_mode(self, control_mode: TLMC_PZ_PositionControlMode, max_wait_in_milliseconds: int) -> None:
        self.feature_group.position_control_mode_feature.set_position_control_mode(control_mode, max_wait_in_milliseconds)

    def get_position(self, max_wait_in_milliseconds: int) -> int:
        return self.feature_group.position_feature.get_position(max_wait_in_milliseconds)

    def set_position(self, position: int) -> None:
        self.feature_group.position_feature.set_position(position)

    def get_position_loop_params(self, max_wait_in_milliseconds: int) -> TLMC_PZ_PositionLoopParams:
        return self.feature_group.position_loop_params_feature.get_position_loop_params(max_wait_in_milliseconds)

    def set_position_loop_params(self, params: TLMC_PZ_PositionLoopParams) -> None:
        return self.feature_group.position_loop_params_feature.set_position_loop_params(params)

    def restore_factory_defaults(self) -> None:
        self.feature_group.restore_factory_defaults_feature.restore_factory_defaults()

    def get_setting(self, settings_name: str, max_wait_in_milliseconds: int) -> TLMC_Setting:
        return self.feature_group.settings_feature.get_setting(settings_name, max_wait_in_milliseconds);

    def get_settings_items(self) -> List[TLMC_Setting]:
        return self.feature_group.settings_feature.get_settings_items()

    def get_settings(self, setting_string_format: TLMC_SettingStringFormat, include_read_only_items: bool) -> str:
        return self.feature_group.settings_feature.get_settings(setting_string_format, include_read_only_items)

    def set_settings(self, settings: str) -> None:
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
        return self.feature_group.set_status_mode_feature.set_status_mode(operating_mode)

    def get_rich_response(self) -> TLMC_RichResponse:
        return self.feature_group.rich_response_feature.get_rich_response()

    def request_status(self, max_wait_in_milliseconds: int) -> None:
        return self.feature_group.status_request_feature.request_status(max_wait_in_milliseconds)

    def convert_from_device_units_to_physical(self, scale_type: TLMC_ScaleType, device_value: int) -> tuple [float, TLMC_Unit]:
        return self.feature_group.unit_converter_feature.convert_from_device_units_to_physical(scale_type, device_value)

    def convert_from_physical_to_device(self, scale_type: TLMC_ScaleType, unit: TLMC_Unit, physical_value: int) -> int:
        return self.feature_group.unit_converter_feature.convert_from_physical_to_device(scale_type, unit, physical_value)

    def get_preferred_physical_unit(self, scale_type: TLMC_ScaleType) -> TLMC_Unit:
        return self.feature_group.unit_converter_feature.get_preferred_physical_unit(scale_type)

    def set_zero(self, max_wait_in_milliseconds: int) -> None:
        self.feature_group.zero_feature.set_zero(max_wait_in_milliseconds)