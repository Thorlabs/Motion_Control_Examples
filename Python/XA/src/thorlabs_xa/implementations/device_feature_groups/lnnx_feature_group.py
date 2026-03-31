from thorlabs_xa.native_sdks.native_functions import NativeFunctions

from thorlabs_xa.interfaces.device_features.digital_output_states import DigitalOutputStates
from thorlabs_xa.interfaces.device_features.digital_input_states import DigitalInputStates
from thorlabs_xa.interfaces.device_features.disconnect import Disconnect
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

from thorlabs_xa.implementations.device_features.digital_input_states_feature import DigitalInputStatesFeature
from thorlabs_xa.implementations.device_features.digital_output_states_feature import DigitalOutputStatesFeature
from thorlabs_xa.implementations.device_features.disconnect_feature import DisconnectFeature
from thorlabs_xa.implementations.device_features.firmware_version_info_feature import FirmwareVersionInfoFeature
from thorlabs_xa.implementations.device_features.hardware_info_feature import HardwareInfoFeature
from thorlabs_xa.implementations.device_features.identify_feature import IdentifyFeature
from thorlabs_xa.implementations.device_features.piezo.nano_trak_circle_diameter_lookup_table_data_feature import NanoTrakCircleDiameterLookupTableDataFeature
from thorlabs_xa.implementations.device_features.piezo.nano_trak_circle_home_position_feature import NanoTrakCircleHomePositionFeature
from thorlabs_xa.implementations.device_features.piezo.nano_trak_circle_params_feature import NanoTrakCircleParamsFeature
from thorlabs_xa.implementations.device_features.piezo.nano_trak_eeprom_params_feature import NanoTrakEEPROMParamsFeature
from thorlabs_xa.implementations.device_features.piezo.nano_trak_gain_params_feature import NanoTrakGainParamsFeature
from thorlabs_xa.implementations.device_features.piezo.nano_trak_mode_feature import NanoTrakModeFeature
from thorlabs_xa.implementations.device_features.piezo.nano_trak_phase_compensation_params_feature import NanoTrakPhaseCompensationParamsFeature
from thorlabs_xa.implementations.device_features.piezo.nano_trak_range_params_feature import NanoTrakRangeParamsFeature
from thorlabs_xa.implementations.device_features.piezo.nano_trak_status_feature import NanoTrakStatusFeature
from thorlabs_xa.implementations.device_features.piezo.nano_trak_tna_io_settings_feature import NanoTrakTnaIoSettingsFeature
from thorlabs_xa.implementations.device_features.rack_bay_occupied_state_feature import RackBayOccupiedStateFeature
from thorlabs_xa.implementations.device_features.restore_factory_defaults_feature import RestoreFactoryDefaultsFeature
from thorlabs_xa.implementations.device_features.rich_response_feature import RichResponseFeature
from thorlabs_xa.implementations.device_features.settings_feature import SettingsFeature

import thorlabs_xa.interfaces.device_feature_groups.lnnx_feature_group

class LnnxFeatureGroup(thorlabs_xa.interfaces.device_feature_groups.lnnx_feature_group.LnnxFeatureGroup):

    def __init__(self, device_handle: int, native_functions: NativeFunctions):

        self._digital_input_states_feature = DigitalInputStatesFeature(device_handle, native_functions)
        self._digital_output_states_feature = DigitalOutputStatesFeature(device_handle, native_functions)
        self._disconnect_feature = DisconnectFeature(device_handle, native_functions)
        self._firmware_version_info_feature = FirmwareVersionInfoFeature(device_handle, native_functions)
        self._hardware_info_feature = HardwareInfoFeature(device_handle, native_functions)
        self._identify_feature = IdentifyFeature(device_handle, native_functions)
        self._nano_trak_circle_diameter_lookup_table_data_feature = NanoTrakCircleDiameterLookupTableDataFeature(device_handle, native_functions)
        self._nano_trak_circle_home_position_feature = NanoTrakCircleHomePositionFeature(device_handle, native_functions)
        self._nano_trak_circle_params_feature = NanoTrakCircleParamsFeature(device_handle, native_functions)
        self._nano_trak_eeprom_params_feature = NanoTrakEEPROMParamsFeature(device_handle, native_functions)
        self._nano_trak_gain_params_feature = NanoTrakGainParamsFeature(device_handle, native_functions)
        self._nano_trak_mode_feature = NanoTrakModeFeature(device_handle, native_functions)
        self._nano_trak_phase_compensation_params_feature = NanoTrakPhaseCompensationParamsFeature(device_handle, native_functions)
        self._nano_trak_range_params_feature = NanoTrakRangeParamsFeature(device_handle, native_functions)
        self._nano_trak_status_feature = NanoTrakStatusFeature(device_handle, native_functions)
        self._nano_trak_tna_io_settings_feature = NanoTrakTnaIoSettingsFeature(device_handle, native_functions)
        self._rack_bay_occupied_state_feature = RackBayOccupiedStateFeature(device_handle, native_functions)
        self._restore_factory_defaults_feature = RestoreFactoryDefaultsFeature(device_handle, native_functions)
        self._rich_response_feature = RichResponseFeature(device_handle, native_functions)
        self._settings_feature = SettingsFeature(device_handle, native_functions)

    @property
    def digital_input_states_feature(self) -> DigitalInputStates:

        return self._digital_input_states_feature

    @property
    def digital_output_states_feature(self) -> DigitalOutputStates:

        return self._digital_output_states_feature

    @property
    def disconnect_feature(self) -> Disconnect:

        return self._disconnect_feature

    @property
    def firmware_version_info_feature(self) -> FirmwareVersionInfo:

        return self._firmware_version_info_feature

    @property
    def hardware_info_feature(self) -> HardwareInfo:

        return self._hardware_info_feature

    @property
    def identify_feature(self) -> Identify:

        return self._identify_feature

    @property
    def nano_trak_circle_diameter_lookup_table_data_feature(self) -> NanoTrakCircleDiameterLookupTableData:

        return self._nano_trak_circle_diameter_lookup_table_data_feature

    @property
    def nano_trak_circle_home_position_feature(self) -> NanoTrakCircleHomePosition:

        return self._nano_trak_circle_home_position_feature

    @property
    def nano_trak_circle_params_feature(self) -> NanoTrakCircleParams:

        return self._nano_trak_circle_params_feature

    @property
    def nano_trak_eeprom_params_feature(self) -> NanoTrakEEPROMParams:

        return self._nano_trak_eeprom_params_feature

    @property
    def nano_trak_gain_params_feature(self) -> NanoTrakGainParams:

        return self._nano_trak_gain_params_feature

    @property
    def nano_trak_mode_feature(self) -> NanoTrakMode:

        return self._nano_trak_mode_feature

    @property
    def nano_trak_phase_compensation_params_feature(self) -> NanoTrakPhaseCompensationParams:

        return self._nano_trak_phase_compensation_params_feature

    @property
    def nano_trak_range_params_feature(self) -> NanoTrakRangeParams:

        return self._nano_trak_range_params_feature

    @property
    def nano_trak_status_feature(self) -> NanoTrakStatus:

        return self._nano_trak_status_feature

    @property
    def nano_trak_tna_io_settings_feature(self) -> NanoTrakTnaIoSettings:

        return self._nano_trak_tna_io_settings_feature

    @property
    def rack_bay_occupied_state_feature(self) -> RackBayOccupiedState:

        return self._rack_bay_occupied_state_feature

    @property
    def restore_factory_defaults_feature(self) -> RestoreFactoryDefaults:

        return self._restore_factory_defaults_feature

    @property
    def rich_response_feature(self) -> RichResponse:

        return self._rich_response_feature

    @property
    def settings_feature(self) -> Settings:

        return self._settings_feature