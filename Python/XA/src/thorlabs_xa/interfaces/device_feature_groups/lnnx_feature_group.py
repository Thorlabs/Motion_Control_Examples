
from typing import Protocol

from thorlabs_xa.interfaces.device_features.digital_input_states import DigitalInputStates
from thorlabs_xa.interfaces.device_features.digital_output_states import DigitalOutputStates
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

class LnnxFeatureGroup(Protocol):

    @property
    def digital_input_states_feature(self) -> DigitalInputStates: ...

    @property
    def digital_output_states_feature(self) -> DigitalOutputStates: ...

    @property
    def disconnect_feature(self) -> Disconnect: ...

    @property
    def firmware_version_info_feature(self) -> FirmwareVersionInfo: ...

    @property
    def hardware_info_feature(self) -> HardwareInfo: ...

    @property
    def identify_feature(self) -> Identify: ...

    @property
    def nano_trak_circle_diameter_lookup_table_data_feature(self) -> NanoTrakCircleDiameterLookupTableData: ...

    @property
    def nano_trak_circle_home_position_feature(self) -> NanoTrakCircleHomePosition: ...

    @property
    def nano_trak_circle_params_feature(self) -> NanoTrakCircleParams: ...

    @property
    def nano_trak_eeprom_params_feature(self) -> NanoTrakEEPROMParams: ...

    @property
    def nano_trak_gain_params_feature(self) -> NanoTrakGainParams: ...

    @property
    def nano_trak_mode_feature(self) -> NanoTrakMode: ...

    @property
    def nano_trak_phase_compensation_params_feature(self) -> NanoTrakPhaseCompensationParams: ...

    @property
    def nano_trak_status_feature(self) -> NanoTrakStatus: ...

    @property
    def nano_trak_range_params_feature(self) -> NanoTrakRangeParams: ...

    @property
    def nano_trak_tna_io_settings_feature(self) -> NanoTrakTnaIoSettings: ...

    @property
    def rack_bay_occupied_state_feature(self) -> RackBayOccupiedState: ...

    @property
    def restore_factory_defaults_feature(self) -> RestoreFactoryDefaults: ...

    @property
    def rich_response_feature(self) -> RichResponse: ...

    @property
    def settings_feature(self) -> Settings: ...