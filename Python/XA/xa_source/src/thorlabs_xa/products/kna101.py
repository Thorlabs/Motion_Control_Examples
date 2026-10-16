from typing import List

from thorlabs_xa.implementations.device_feature_groups.kna101_subchannel_feature_group import Kna101SubchannelFeatureGroup
from thorlabs_xa.interfaces.device_feature_groups.kna101_feature_group import Kna101FeatureGroup

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

from thorlabs_xa.native_sdks.native_functions import NativeFunctions
from thorlabs_xa.products.kna101_subchannel import Kna101Subchannel
from thorlabs_xa.shared.params import TLMC_DeviceInfo, TLMC_PZ_NanoTrakStatusBitsParams

from thorlabs_xa.shared.enums import TLMC_KcubeMmiLockState, TLMC_PZ_NanoTrakFeedbackSource, TLMC_OperatingMode, TLMC_ScaleType, TLMC_PZ_SetNanoTrakModeType, TLMC_SettingStringFormat, TLMC_StatusItemId, TLMC_Unit
from thorlabs_xa.shared.params import TLMC_FirmwareVersion, TLMC_HardwareInfo, TLMC_PZ_KnaIoTriggerParams, TLMC_PZ_KnaMmiParams, TLMC_PZ_KnaScanData, TLMC_PZ_NanoTrakCircleDiameterLookupTable, TLMC_PZ_NanoTrakCircleHomePositionParams, TLMC_PZ_NanoTrakCircleParams, TLMC_PZ_NanoTrakEEPROMParams, TLMC_PZ_NanoTrakGainParams, TLMC_PZ_NanoTrakMode, TLMC_PZ_NanoTrakPhaseCompensationParams, TLMC_PZ_NanoTrakStatus, TLMC_PZ_NanoTrakTiaRangeParams, TLMC_PZ_NanoTrakTnaIoSettings, TLMC_PZ_NanoTrakTrackThresholdParams, TLMC_Setting, TLMC_StatusItem
from thorlabs_xa.shared.device import Device

class Kna101(Device,
        Disconnect,
        FirmwareVersionInfo,
        HardwareInfo,
        Identify,
        KcubeMmiLock,
        KnaIoTriggerParams,
        KnaMmiParams,
        KnaScan,
        LoadParams,
        NanoTrakCircleDiameter,
        NanoTrakCircleDiameterLookupTable,
        NanoTrakCircleHomePositionParams,
        NanoTrakCircleParams,
        NanoTrakCircleToHomePosition,
        NanoTrakEEPROMParams,
        NanoTrakFeedbackSource,
        NanoTrakGainParams,
        NanoTrakMode,
        NanoTrakPhaseCompensationParams,
        NanoTrakStatus,
        NanoTrakStatusBitsParams,
        NanoTrakTiaRangeParams,
        NanoTrakTnaIoSettings,
        NanoTrakTrackThreshold,
        Settings,
        StatusItems,
        StatusMode,
        StatusRequest,
        UnitConverter):

    _SUBCHANNEL_COUNT = 2

    def __init__(self, device_handle: int, device_info: TLMC_DeviceInfo, feature_group: Kna101FeatureGroup, native_functions: NativeFunctions) -> None:

        super().__init__(device_handle, device_info, native_functions)

        self.feature_group = feature_group
        self._subchannels: dict[int, Kna101Subchannel] = {}
        self._init_subchannels(native_functions)

    def _init_subchannels(self, native_functions: NativeFunctions) -> None:
        for channel_number in range(1, self._SUBCHANNEL_COUNT + 1):
            subchannel_handle = native_functions.get_channel(self._device_handle, channel_number)
            feature_group = Kna101SubchannelFeatureGroup(subchannel_handle, native_functions)
            subchannel = Kna101Subchannel(
                subchannel_handle, channel_number, native_functions,
                feature_group
            )
            self._subchannels[channel_number] = subchannel

    def get_subchannel(self, subchannel_number: int) -> Kna101Subchannel:
        subchannel = self._subchannels.get(subchannel_number)
        if subchannel is None:
            raise ValueError(f"Subchannel number {subchannel_number} is not available on this device.")
        return subchannel

    def get_all_subchannels(self) -> List[Kna101Subchannel]:
        return list(self._subchannels.values())

    def disconnect(self) -> None:

        self.feature_group.disconnect_feature.disconnect()

    def get_firmware_version_info(self, max_wait_in_milliseconds: int) -> tuple[TLMC_FirmwareVersion, TLMC_FirmwareVersion]:

        return self.feature_group.firmware_version_info_feature.get_firmware_version_info(max_wait_in_milliseconds)

    def get_hardware_info(self, max_wait_in_milliseconds: int) -> TLMC_HardwareInfo:

        return self.feature_group.hardware_info_feature.get_hardware_info(max_wait_in_milliseconds)

    def identify(self) -> None:

        self.feature_group.identify_feature.identify()

    def get_kcube_mmi_lock_state(self, max_wait_in_milliseconds: int) -> TLMC_KcubeMmiLockState:

        return self.feature_group.kcube_mmi_lock_feature.get_kcube_mmi_lock_state(max_wait_in_milliseconds)

    def set_kcube_mmi_lock_state(self, lock_state: TLMC_KcubeMmiLockState) -> None:

        self.feature_group.kcube_mmi_lock_feature.set_kcube_mmi_lock_state(lock_state)

    def get_kna_io_trigger_params(self, max_wait_in_milliseconds: int) -> TLMC_PZ_KnaIoTriggerParams:

        return self.feature_group.kna_io_trigger_params_feature.get_kna_io_trigger_params(max_wait_in_milliseconds)

    def set_kna_io_trigger_params(self, params: TLMC_PZ_KnaIoTriggerParams) -> None:

        self.feature_group.kna_io_trigger_params_feature.set_kna_io_trigger_params(params)

    def get_kna_mmi_params(self, max_wait_in_milliseconds: int) -> TLMC_PZ_KnaMmiParams:

        return self.feature_group.kna_mmi_params_feature.get_kna_mmi_params(max_wait_in_milliseconds)

    def set_kna_mmi_params(self, params: TLMC_PZ_KnaMmiParams) -> None:

        self.feature_group.kna_mmi_params_feature.set_kna_mmi_params(params)

    def start_kna_scan(self) -> None:

        self.feature_group.kna_scan_feature.start_kna_scan()

    def stop_kna_scan(self) -> None:

        self.feature_group.kna_scan_feature.stop_kna_scan()

    def get_kna_scan_data(self, max_wait_in_milliseconds: int) -> TLMC_PZ_KnaScanData:

        return self.feature_group.kna_scan_feature.get_kna_scan_data(max_wait_in_milliseconds)

    def load_params(self) -> None:

        self.feature_group.load_params_feature.load_params()

    def set_nano_trak_circle_diameter(self, circle_diameter: int) -> None:

        self.feature_group.nano_trak_circle_diameter_feature.set_nano_trak_circle_diameter(circle_diameter)

    def get_nano_trak_circle_diameter_lookup_table(self, max_wait_in_milliseconds: int) -> TLMC_PZ_NanoTrakCircleDiameterLookupTable:

        return self.feature_group.nano_trak_circle_diameter_lookup_table_feature.get_nano_trak_circle_diameter_lookup_table(max_wait_in_milliseconds)

    def set_nano_trak_circle_diameter_lookup_table(self, params: TLMC_PZ_NanoTrakCircleDiameterLookupTable) -> None:

        self.feature_group.nano_trak_circle_diameter_lookup_table_feature.set_nano_trak_circle_diameter_lookup_table(params)

    def get_nano_trak_circle_home_position_params(self, max_wait_in_milliseconds: int) -> TLMC_PZ_NanoTrakCircleHomePositionParams:

        return self.feature_group.nano_trak_circle_home_position_params_feature.get_nano_trak_circle_home_position_params(max_wait_in_milliseconds)

    def set_nano_trak_circle_home_position_params(self, params: TLMC_PZ_NanoTrakCircleHomePositionParams) -> None:

        self.feature_group.nano_trak_circle_home_position_params_feature.set_nano_trak_circle_home_position_params(params)

    def get_nano_trak_circle_params(self, max_wait_in_milliseconds: int) -> TLMC_PZ_NanoTrakCircleParams:

        return self.feature_group.nano_trak_circle_params_feature.get_nano_trak_circle_params(max_wait_in_milliseconds)

    def set_nano_trak_circle_params(self, params: TLMC_PZ_NanoTrakCircleParams) -> None:

        self.feature_group.nano_trak_circle_params_feature.set_nano_trak_circle_params(params)

    def nano_trak_circle_to_home_position(self) -> None:

        self.feature_group.nano_trak_circle_to_home_position_feature.nano_trak_circle_to_home_position()

    def set_nano_trak_eeprom_params(self, params: TLMC_PZ_NanoTrakEEPROMParams) -> None:

        self.feature_group.nano_trak_eeprom_params_feature.set_nano_trak_eeprom_params(params)

    def get_nano_trak_feedback_source(self, max_wait_in_milliseconds: int) -> TLMC_PZ_NanoTrakFeedbackSource:

        return self.feature_group.nano_trak_feedback_source_feature.get_nano_trak_feedback_source(max_wait_in_milliseconds)

    def set_nano_trak_feedback_source(self, params: TLMC_PZ_NanoTrakFeedbackSource) -> None:

        self.feature_group.nano_trak_feedback_source_feature.set_nano_trak_feedback_source(params)

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

    def get_nano_trak_status(self, max_wait_in_milliseconds: int) -> TLMC_PZ_NanoTrakStatus:

        return self.feature_group.nano_trak_status_feature.get_nano_trak_status(max_wait_in_milliseconds)

    def get_nano_trak_status_bits_params(self, max_wait_in_milliseconds: int) -> TLMC_PZ_NanoTrakStatusBitsParams:

        return self.feature_group.nano_trak_status_bits_params_feature.get_nano_trak_status_bits_params(max_wait_in_milliseconds)

    def get_nano_trak_tia_range_params(self, max_wait_in_milliseconds: int) -> TLMC_PZ_NanoTrakTiaRangeParams:

        return self.feature_group.nano_trak_tia_range_params_feature.get_nano_trak_tia_range_params(max_wait_in_milliseconds)

    def set_nano_trak_tia_range_params(self, params: TLMC_PZ_NanoTrakTiaRangeParams) -> None:

        self.feature_group.nano_trak_tia_range_params_feature.set_nano_trak_tia_range_params(params)

    def get_nano_trak_tna_io_settings(self, max_wait_in_milliseconds: int) -> TLMC_PZ_NanoTrakTnaIoSettings:

        return self.feature_group.nano_trak_tna_io_settings_feature.get_nano_trak_tna_io_settings(max_wait_in_milliseconds)

    def set_nano_trak_tna_io_settings(self, params: TLMC_PZ_NanoTrakTnaIoSettings) -> None:

        self.feature_group.nano_trak_tna_io_settings_feature.set_nano_trak_tna_io_settings(params)

    def get_nano_trak_track_threshold(self, max_wait_in_milliseconds: int) -> TLMC_PZ_NanoTrakTrackThresholdParams:

        return self.feature_group.nano_trak_track_threshold_feature.get_nano_trak_track_threshold(max_wait_in_milliseconds)

    def set_nano_trak_track_threshold(self, params: TLMC_PZ_NanoTrakTrackThresholdParams) -> None:

        self.feature_group.nano_trak_track_threshold_feature.set_nano_trak_track_threshold(params)

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

    def convert_from_device_units_to_physical(self, scale_type: TLMC_ScaleType, device_value: int) -> tuple[float, TLMC_Unit]:

        return self.feature_group.unit_converter_feature.convert_from_device_units_to_physical(scale_type, device_value)

    def convert_from_physical_to_device(self, scale_type: TLMC_ScaleType, unit: TLMC_Unit, physical_value: int) -> int:

        return self.feature_group.unit_converter_feature.convert_from_physical_to_device(scale_type, unit, physical_value)

    def get_preferred_physical_unit(self, scale_type: TLMC_ScaleType) -> TLMC_Unit:

        return self.feature_group.unit_converter_feature.get_preferred_physical_unit(scale_type)