import thorlabs_xa.interfaces.device_feature_groups.kna101_feature_group

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

from thorlabs_xa.implementations.device_features.disconnect_feature import DisconnectFeature
from thorlabs_xa.implementations.device_features.firmware_version_info_feature import FirmwareVersionInfoFeature
from thorlabs_xa.implementations.device_features.hardware_info_feature import HardwareInfoFeature
from thorlabs_xa.implementations.device_features.identify_feature import IdentifyFeature
from thorlabs_xa.implementations.device_features.kcube_mmi_lock_feature import KcubeMmiLockFeature
from thorlabs_xa.implementations.device_features.load_params_feature import LoadParamsFeature
from thorlabs_xa.implementations.device_features.piezo.kna_io_trigger_params_feature import KnaIoTriggerParamsFeature
from thorlabs_xa.implementations.device_features.piezo.kna_mmi_params_feature import KnaMmiParamsFeature
from thorlabs_xa.implementations.device_features.piezo.kna_scan_feature import KnaScanFeature
from thorlabs_xa.implementations.device_features.piezo.nano_trak_circle_diameter_feature import NanoTrakCircleDiameterFeature
from thorlabs_xa.implementations.device_features.piezo.nano_trak_circle_diameter_lookup_table_feature import NanoTrakCircleDiameterLookupTableFeature
from thorlabs_xa.implementations.device_features.piezo.nano_trak_circle_home_position_params_feature import NanoTrakCircleHomePositionParamsFeature
from thorlabs_xa.implementations.device_features.piezo.nano_trak_circle_params_feature import NanoTrakCircleParamsFeature
from thorlabs_xa.implementations.device_features.piezo.nano_trak_circle_to_home_position_feature import NanoTrakCircleToHomePositionFeature
from thorlabs_xa.implementations.device_features.piezo.nano_trak_eeprom_params_feature import NanoTrakEEPROMParamsFeature
from thorlabs_xa.implementations.device_features.piezo.nano_trak_feedback_source_feature import NanoTrakFeedbackSourceFeature
from thorlabs_xa.implementations.device_features.piezo.nano_trak_gain_params_feature import NanoTrakGainParamsFeature
from thorlabs_xa.implementations.device_features.piezo.nano_trak_mode_feature import NanoTrakModeFeature
from thorlabs_xa.implementations.device_features.piezo.nano_trak_phase_compensation_params_feature import NanoTrakPhaseCompensationParamsFeature
from thorlabs_xa.implementations.device_features.piezo.nano_trak_status_feature import NanoTrakStatusFeature
from thorlabs_xa.implementations.device_features.piezo.nano_trak_status_bits_params_feature import NanoTrakStatusBitsParamsFeature
from thorlabs_xa.implementations.device_features.piezo.nano_trak_tia_range_params_feature import NanoTrakTiaRangeParamsFeature
from thorlabs_xa.implementations.device_features.piezo.nano_trak_tna_io_settings_feature import NanoTrakTnaIoSettingsFeature
from thorlabs_xa.implementations.device_features.piezo.nano_trak_track_threshold_feature import NanoTrakTrackThresholdFeature
from thorlabs_xa.implementations.device_features.settings_feature import SettingsFeature
from thorlabs_xa.implementations.device_features.status_items_feature import StatusItemsFeature
from thorlabs_xa.implementations.device_features.status_mode_feature import StatusModeFeature
from thorlabs_xa.implementations.device_features.status_request_feature import StatusRequestFeature
from thorlabs_xa.implementations.device_features.unit_converter_feature import UnitConverterFeature

from thorlabs_xa.native_sdks.native_functions import NativeFunctions

class Kna101FeatureGroup(thorlabs_xa.interfaces.device_feature_groups.kna101_feature_group.Kna101FeatureGroup):

    def __init__(self, device_handle: int, native_functions: NativeFunctions) -> None:

        self._disconnect_feature = DisconnectFeature(device_handle, native_functions)
        self._firmware_version_info_feature = FirmwareVersionInfoFeature(device_handle, native_functions)
        self._hardware_info_feature = HardwareInfoFeature(device_handle, native_functions)
        self._identify_feature = IdentifyFeature(device_handle, native_functions)
        self._kcube_mmi_lock_feature = KcubeMmiLockFeature(device_handle, native_functions)
        self._kna_io_trigger_params_feature = KnaIoTriggerParamsFeature(device_handle, native_functions)
        self._kna_mmi_params_feature = KnaMmiParamsFeature(device_handle, native_functions)
        self._kna_scan_feature = KnaScanFeature(device_handle, native_functions)
        self._load_params_feature = LoadParamsFeature(device_handle, native_functions)
        self._nano_trak_circle_diameter_feature = NanoTrakCircleDiameterFeature(device_handle, native_functions)
        self._nano_trak_circle_diameter_lookup_table_feature = NanoTrakCircleDiameterLookupTableFeature(device_handle, native_functions)
        self._nano_trak_circle_home_position_params_feature = NanoTrakCircleHomePositionParamsFeature(device_handle, native_functions)
        self._nano_trak_circle_params_feature = NanoTrakCircleParamsFeature(device_handle, native_functions)
        self._nano_trak_circle_to_home_position_feature = NanoTrakCircleToHomePositionFeature(device_handle, native_functions)
        self._nano_trak_eeprom_params_feature = NanoTrakEEPROMParamsFeature(device_handle, native_functions)
        self._nano_trak_feedback_source_feature = NanoTrakFeedbackSourceFeature(device_handle, native_functions)
        self._nano_trak_gain_params_feature = NanoTrakGainParamsFeature(device_handle, native_functions)
        self._nano_trak_mode_feature = NanoTrakModeFeature(device_handle, native_functions)
        self._nano_trak_phase_compensation_params_feature = NanoTrakPhaseCompensationParamsFeature(device_handle, native_functions)
        self._nano_trak_status_feature = NanoTrakStatusFeature(device_handle, native_functions)
        self._nano_trak_status_bits_params_feature = NanoTrakStatusBitsParamsFeature(device_handle, native_functions)
        self._nano_trak_tia_range_params_feature = NanoTrakTiaRangeParamsFeature(device_handle, native_functions)
        self._nano_trak_tna_io_settings_feature = NanoTrakTnaIoSettingsFeature(device_handle, native_functions)
        self._nano_trak_track_threshold_feature = NanoTrakTrackThresholdFeature(device_handle, native_functions)
        self._settings_feature = SettingsFeature(device_handle, native_functions)
        self._status_items_feature = StatusItemsFeature(device_handle, native_functions)
        self._status_mode_feature = StatusModeFeature(device_handle, native_functions)
        self._status_request_feature = StatusRequestFeature(device_handle, native_functions)
        self._unit_converter_feature = UnitConverterFeature(device_handle, native_functions)

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
    def disconnect_feature(self) -> Disconnect:
        return self._disconnect_feature

    @property
    def kcube_mmi_lock_feature(self) -> KcubeMmiLock:
        return self._kcube_mmi_lock_feature

    @property
    def kna_io_trigger_params_feature(self) -> KnaIoTriggerParams:
        return self._kna_io_trigger_params_feature

    @property
    def kna_mmi_params_feature(self) -> KnaMmiParams:
        return self._kna_mmi_params_feature

    @property
    def kna_scan_feature(self) -> KnaScan:
        return self._kna_scan_feature

    @property
    def load_params_feature(self) -> LoadParams:
        return self._load_params_feature

    @property
    def nano_trak_circle_diameter_feature(self) -> NanoTrakCircleDiameter:
        return self._nano_trak_circle_diameter_feature

    @property
    def nano_trak_circle_diameter_lookup_table_feature(self) -> NanoTrakCircleDiameterLookupTable:
        return self._nano_trak_circle_diameter_lookup_table_feature

    @property
    def nano_trak_circle_home_position_params_feature(self) -> NanoTrakCircleHomePositionParams:
        return self._nano_trak_circle_home_position_params_feature

    @property
    def nano_trak_circle_params_feature(self) -> NanoTrakCircleParams:
        return self._nano_trak_circle_params_feature

    @property
    def nano_trak_circle_to_home_position_feature(self) -> NanoTrakCircleToHomePosition:
        return self._nano_trak_circle_to_home_position_feature

    @property
    def nano_trak_eeprom_params_feature(self) -> NanoTrakEEPROMParams:
        return self._nano_trak_eeprom_params_feature

    @property
    def nano_trak_feedback_source_feature(self) -> NanoTrakFeedbackSource:
        return self._nano_trak_feedback_source_feature

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
    def nano_trak_status_feature(self) -> NanoTrakStatus:
        return self._nano_trak_status_feature

    @property
    def nano_trak_status_bits_params_feature(self) -> NanoTrakStatusBitsParams:
        return self._nano_trak_status_bits_params_feature

    @property
    def nano_trak_tia_range_params_feature(self) -> NanoTrakTiaRangeParams:
        return self._nano_trak_tia_range_params_feature

    @property
    def nano_trak_tna_io_settings_feature(self) -> NanoTrakTnaIoSettings:
        return self._nano_trak_tna_io_settings_feature

    @property
    def nano_trak_track_threshold_feature(self) -> NanoTrakTrackThreshold:
        return self._nano_trak_track_threshold_feature

    @property
    def settings_feature(self) -> Settings:
        return self._settings_feature

    @property
    def status_items_feature(self) -> StatusItems:
        return self._status_items_feature

    @property
    def status_mode_feature(self) -> StatusMode:
        return self._status_mode_feature

    @property
    def status_request_feature(self) -> StatusRequest:
        return self._status_request_feature

    @property
    def unit_converter_feature(self) -> UnitConverter:
        return self._unit_converter_feature