from typing import Protocol

from thorlabs_xa.interfaces.device_features.disconnect import Disconnect
from thorlabs_xa.interfaces.device_features.firmware_version_info import FirmwareVersionInfo
from thorlabs_xa.interfaces.device_features.hardware_info import HardwareInfo
from thorlabs_xa.interfaces.device_features.identify import Identify
from thorlabs_xa.interfaces.device_features.kcube_mmi_lock import KcubeMmiLock
from thorlabs_xa.interfaces.device_features.load_params import LoadParams
from thorlabs_xa.interfaces.device_features.piezo.kna_io_trigger_params import KnaIoTriggerParams
from thorlabs_xa.interfaces.device_features.piezo.kna_mmi_params import KnaMmiParams
from thorlabs_xa.interfaces.device_features.piezo.kna_scan import KnaScan
from thorlabs_xa.interfaces.device_features.piezo.nano_trak_circle_diameter import NanoTrakCircleDiameter
from thorlabs_xa.interfaces.device_features.piezo.nano_trak_circle_diameter_lookup_table import NanoTrakCircleDiameterLookupTable
from thorlabs_xa.interfaces.device_features.piezo.nano_trak_circle_home_position_params import NanoTrakCircleHomePositionParams
from thorlabs_xa.interfaces.device_features.piezo.nano_trak_circle_params import NanoTrakCircleParams
from thorlabs_xa.interfaces.device_features.piezo.nano_trak_circle_to_home_position import NanoTrakCircleToHomePosition
from thorlabs_xa.interfaces.device_features.piezo.nano_trak_eeprom_params import NanoTrakEEPROMParams
from thorlabs_xa.interfaces.device_features.piezo.nano_trak_feedback_source import NanoTrakFeedbackSource
from thorlabs_xa.interfaces.device_features.piezo.nano_trak_gain_params import NanoTrakGainParams
from thorlabs_xa.interfaces.device_features.piezo.nano_trak_mode import NanoTrakMode
from thorlabs_xa.interfaces.device_features.piezo.nano_trak_phase_compensation_params import NanoTrakPhaseCompensationParams
from thorlabs_xa.interfaces.device_features.piezo.nano_trak_status import NanoTrakStatus
from thorlabs_xa.interfaces.device_features.piezo.nano_trak_status_bits_params import NanoTrakStatusBitsParams
from thorlabs_xa.interfaces.device_features.piezo.nano_trak_tia_range_params import NanoTrakTiaRangeParams
from thorlabs_xa.interfaces.device_features.piezo.nano_trak_tna_io_settings import NanoTrakTnaIoSettings
from thorlabs_xa.interfaces.device_features.piezo.nano_trak_track_threshold import NanoTrakTrackThreshold
from thorlabs_xa.interfaces.device_features.settings import Settings
from thorlabs_xa.interfaces.device_features.status_items import StatusItems
from thorlabs_xa.interfaces.device_features.status_mode import StatusMode
from thorlabs_xa.interfaces.device_features.status_request import StatusRequest
from thorlabs_xa.interfaces.device_features.unit_converter import UnitConverter

class Kna101FeatureGroup(Protocol):

    @property
    def firmware_version_info_feature(self) -> FirmwareVersionInfo: ...

    @property
    def hardware_info_feature(self) -> HardwareInfo: ...

    @property
    def identify_feature(self) -> Identify: ...

    @property
    def disconnect_feature(self) -> Disconnect: ...

    @property
    def kcube_mmi_lock_feature(self) -> KcubeMmiLock: ...

    @property
    def kna_io_trigger_params_feature(self) -> KnaIoTriggerParams: ...

    @property
    def kna_mmi_params_feature(self) -> KnaMmiParams: ...

    @property
    def kna_scan_feature(self) -> KnaScan: ...

    @property
    def load_params_feature(self) -> LoadParams: ...

    @property
    def nano_trak_circle_diameter_feature(self) -> NanoTrakCircleDiameter: ...

    @property
    def nano_trak_circle_diameter_lookup_table_feature(self) -> NanoTrakCircleDiameterLookupTable: ...

    @property
    def nano_trak_circle_home_position_params_feature(self) -> NanoTrakCircleHomePositionParams: ...

    @property
    def nano_trak_circle_params_feature(self) -> NanoTrakCircleParams: ...

    @property
    def nano_trak_circle_to_home_position_feature(self) -> NanoTrakCircleToHomePosition: ...

    @property
    def nano_trak_eeprom_params_feature(self) -> NanoTrakEEPROMParams: ...

    @property
    def nano_trak_feedback_source_feature(self) -> NanoTrakFeedbackSource: ...

    @property
    def nano_trak_gain_params_feature(self) -> NanoTrakGainParams: ...

    @property
    def nano_trak_mode_feature(self) -> NanoTrakMode: ...

    @property
    def nano_trak_phase_compensation_params_feature(self) -> NanoTrakPhaseCompensationParams: ...

    @property
    def nano_trak_status_feature(self) -> NanoTrakStatus: ...

    @property
    def nano_trak_status_bits_params_feature(self) -> NanoTrakStatusBitsParams: ...

    @property
    def nano_trak_tia_range_params_feature(self) -> NanoTrakTiaRangeParams: ...

    @property
    def nano_trak_tna_io_settings_feature(self) -> NanoTrakTnaIoSettings: ...

    @property
    def nano_trak_track_threshold_feature(self) -> NanoTrakTrackThreshold: ...

    @property
    def settings_feature(self) -> Settings: ...

    @property
    def status_items_feature(self) -> StatusItems: ...

    @property
    def status_mode_feature(self) -> StatusMode: ...

    @property
    def status_request_feature(self) -> StatusRequest: ...

    @property
    def unit_converter_feature(self) -> UnitConverter: ...