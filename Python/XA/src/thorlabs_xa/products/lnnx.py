from typing import List

from thorlabs_xa.native_sdks.native_functions import NativeFunctions
from thorlabs_xa.shared.device import Device

from thorlabs_xa.interfaces.device_feature_groups.lnnx_feature_group import LnnxFeatureGroup

from thorlabs_xa.shared.enums import TLMC_DigitalInput, TLMC_DigitalOutput, TLMC_PZ_SetNanoTrakModeType, TLMC_RackBayNumber, TLMC_RackBayOccupiedState, TLMC_SettingStringFormat
from thorlabs_xa.shared.params import TLMC_DeviceInfo, TLMC_FirmwareVersion, TLMC_HardwareInfo, TLMC_PZ_NanoTrakCircleDiameterLookupTableData, TLMC_PZ_NanoTrakCircleHomePositionParams, TLMC_PZ_NanoTrakCircleParams, TLMC_PZ_NanoTrakEEPROMParams, TLMC_PZ_NanoTrakGainParams, TLMC_PZ_NanoTrakMode, TLMC_PZ_NanoTrakPhaseCompensationParams, TLMC_PZ_NanoTrakRangeParams, TLMC_PZ_NanoTrakStatus, TLMC_PZ_NanoTrakTnaIoSettings, TLMC_RichResponse, TLMC_Setting

from thorlabs_xa.interfaces.device_features.disconnect import Disconnect
from thorlabs_xa.interfaces.device_features.digital_input_states import DigitalInputStates
from thorlabs_xa.interfaces.device_features.digital_output_states import DigitalOutputStates
from thorlabs_xa.interfaces.device_features.firmware_version_info import FirmwareVersionInfo
from thorlabs_xa.interfaces.device_features.hardware_info import HardwareInfo
from thorlabs_xa.interfaces.device_features.identify import Identify
from thorlabs_xa.interfaces.device_features.piezo.nano_trak_circle_diameter_lookup_table_data import NanoTrakCircleDiameterLookupTableData
from thorlabs_xa.interfaces.device_features.piezo.nano_trak_circle_home_position import NanoTrakCircleHomePosition
from thorlabs_xa.interfaces.device_features.piezo.nano_trak_circle_params import NanoTrakCircleParams
from thorlabs_xa.interfaces.device_features.piezo.nano_trak_eeprom_params import NanoTrakEEPROMParams
from thorlabs_xa.interfaces.device_features.piezo.nano_trak_gain_params import NanoTrakGainParams
from thorlabs_xa.interfaces.device_features.piezo.nano_trak_mode import NanoTrakMode
from thorlabs_xa.interfaces.device_features.piezo.nano_trak_phase_compensation_params import NanoTrakPhaseCompensationParams
from thorlabs_xa.interfaces.device_features.piezo.nano_trak_range_params import NanoTrakRangeParams
from thorlabs_xa.interfaces.device_features.piezo.nano_trak_status import NanoTrakStatus
from thorlabs_xa.interfaces.device_features.piezo.nano_trak_tna_io_settings import NanoTrakTnaIoSettings
from thorlabs_xa.interfaces.device_features.rack_bay_occupied_state import RackBayOccupiedState
from thorlabs_xa.interfaces.device_features.restore_factory_defaults import RestoreFactoryDefaults
from thorlabs_xa.interfaces.device_features.rich_response import RichResponse
from thorlabs_xa.interfaces.device_features.settings import Settings

class Lnnx(Device,
    DigitalInputStates,
    DigitalOutputStates,
    Disconnect,
    FirmwareVersionInfo,
    HardwareInfo,
    Identify,
    NanoTrakCircleDiameterLookupTableData,
    NanoTrakCircleHomePosition,
    NanoTrakCircleParams,
    NanoTrakEEPROMParams,
    NanoTrakGainParams,
    NanoTrakMode,
    NanoTrakPhaseCompensationParams,
    NanoTrakRangeParams,
    NanoTrakStatus,
    NanoTrakTnaIoSettings,
    RackBayOccupiedState,
    RestoreFactoryDefaults,
    RichResponse,
    Settings):
    """
    Thorlabs Low Noise NanoTrak Piezo Controller.
    """
    def __init__(self, device_handle: int, device_info: TLMC_DeviceInfo, feature_group: LnnxFeatureGroup, native_functions: NativeFunctions):

        super().__init__(device_handle, device_info, native_functions)

        self.feature_group = feature_group

    def get_digital_input_states(self, max_wait_in_milliseconds: int) -> TLMC_DigitalInput:
        return self.feature_group.digital_input_states_feature.get_digital_input_states(max_wait_in_milliseconds)

    def get_digital_output_states(self, max_wait_in_milliseconds: int) -> TLMC_DigitalOutput:
        return self.feature_group.digital_output_states_feature.get_digital_output_states(max_wait_in_milliseconds)

    def set_digital_output_states(self, params: TLMC_DigitalOutput) -> None:
        self.feature_group.digital_output_states_feature.set_digital_output_states(params)

    def disconnect(self) -> None:
        self.feature_group.disconnect_feature.disconnect()
        
    def get_firmware_version_info(self, max_wait_in_milliseconds: int) -> tuple [TLMC_FirmwareVersion, TLMC_FirmwareVersion]:
        return self.feature_group.firmware_version_info_feature.get_firmware_version_info(max_wait_in_milliseconds)

    def get_hardware_info(self, max_wait_in_milliseconds: int) -> TLMC_HardwareInfo:
        return self.feature_group.hardware_info_feature.get_hardware_info(max_wait_in_milliseconds)
    
    def identify(self) -> None:
        self.feature_group.identify_feature.identify()

    def get_nano_trak_circle_diameter_lookup_table_data(self, max_wait_in_milliseconds: int) -> TLMC_PZ_NanoTrakCircleDiameterLookupTableData:
        return self.feature_group.nano_trak_circle_diameter_lookup_table_data_feature.get_nano_trak_circle_diameter_lookup_table_data(max_wait_in_milliseconds)

    def set_nano_trak_circle_diameter_lookup_table_data(self, params: TLMC_PZ_NanoTrakCircleDiameterLookupTableData) -> None:
        self.feature_group.nano_trak_circle_diameter_lookup_table_data_feature.set_nano_trak_circle_diameter_lookup_table_data(params)

    def get_nano_trak_circle_home_position(self, max_wait_in_milliseconds: int) -> TLMC_PZ_NanoTrakCircleHomePositionParams:
        return self.feature_group.nano_trak_circle_home_position_feature.get_nano_trak_circle_home_position(max_wait_in_milliseconds)

    def set_nano_trak_circle_home_position(self, params: TLMC_PZ_NanoTrakCircleHomePositionParams) -> None:
        self.feature_group.nano_trak_circle_home_position_feature.set_nano_trak_circle_home_position(params)

    def get_nano_trak_circle_params(self, max_wait_in_milliseconds: int) -> TLMC_PZ_NanoTrakCircleParams:
        return self.feature_group.nano_trak_circle_params_feature.get_nano_trak_circle_params(max_wait_in_milliseconds)

    def set_nano_trak_circle_params(self, params: TLMC_PZ_NanoTrakCircleParams) -> None:
        self.feature_group.nano_trak_circle_params_feature.set_nano_trak_circle_params(params)

    def set_nano_trak_eeprom_params(self, params: TLMC_PZ_NanoTrakEEPROMParams) -> None:
        self.feature_group.nano_trak_eeprom_params_feature.set_nano_trak_eeprom_params(params)

    def get_nano_trak_gain_params(self, max_wait_in_milliseconds: int) -> TLMC_PZ_NanoTrakGainParams:
        return self.feature_group.nano_trak_gain_params_feature.get_nano_trak_gain_params(max_wait_in_milliseconds)

    def set_nano_trak_gain_params(self, params: TLMC_PZ_NanoTrakGainParams) -> None:
        self.feature_group.nano_trak_gain_params_feature.set_nano_trak_gain_params(params)

    def get_nano_trak_mode(self, max_wait_in_milliseconds: int) -> TLMC_PZ_NanoTrakMode:
        return self.feature_group.nano_trak_mode_feature.get_nano_trak_mode(max_wait_in_milliseconds)

    def set_nano_trak_mode(self, set_mode: TLMC_PZ_SetNanoTrakModeType) -> None:
        self.feature_group.nano_trak_mode_feature.set_nano_trak_mode(set_mode)

    def get_nano_trak_phase_compensation_params(self, max_wait_in_milliseconds: int) -> TLMC_PZ_NanoTrakPhaseCompensationParams:
        return self.feature_group.nano_trak_phase_compensation_params_feature.get_nano_trak_phase_compensation_params(max_wait_in_milliseconds)

    def set_nano_trak_phase_compensation_params(self, params: TLMC_PZ_NanoTrakPhaseCompensationParams) -> None:
        self.feature_group.nano_trak_phase_compensation_params_feature.set_nano_trak_phase_compensation_params(params)

    def get_nano_trak_range_params(self, max_wait_in_milliseconds: int) -> TLMC_PZ_NanoTrakRangeParams:
        return self.feature_group.nano_trak_range_params_feature.get_nano_trak_range_params(max_wait_in_milliseconds)

    def set_nano_trak_range_params(self, params: TLMC_PZ_NanoTrakRangeParams) -> None:
        self.feature_group.nano_trak_range_params_feature.set_nano_trak_range_params(params)

    def get_nano_trak_status(self, max_wait_in_milliseconds: int) -> TLMC_PZ_NanoTrakStatus:
        return self.feature_group.nano_trak_status_feature.get_nano_trak_status(max_wait_in_milliseconds)

    def get_nano_trak_tna_io_settings(self, max_wait_in_milliseconds: int) -> TLMC_PZ_NanoTrakTnaIoSettings:
        return self.feature_group.nano_trak_tna_io_settings_feature.get_nano_trak_tna_io_settings(max_wait_in_milliseconds)

    def set_nano_trak_tna_io_settings(self, params: TLMC_PZ_NanoTrakTnaIoSettings) -> None:
        self.feature_group.nano_trak_tna_io_settings_feature.set_nano_trak_tna_io_settings(params)

    def get_rack_bay_occupied_state(self, bay_number: TLMC_RackBayNumber, max_wait_in_milliseconds: int) -> TLMC_RackBayOccupiedState:
        return self.feature_group.rack_bay_occupied_state_feature.get_rack_bay_occupied_state(bay_number, max_wait_in_milliseconds)

    def restore_factory_defaults(self) -> None:
        self.feature_group.restore_factory_defaults_feature.restore_factory_defaults()

    def get_rich_response(self) -> TLMC_RichResponse:
        return self.feature_group.rich_response_feature.get_rich_response()

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