from typing import List

from thorlabs_xa.interfaces.device_feature_groups.kim001_feature_group import Kim001FeatureGroup

from thorlabs_xa.interfaces.device_features.piezo_inertial_motor.conversion_factors import ConversionFactors
from thorlabs_xa.interfaces.device_features.dc_pid_params import DcPidParams
from thorlabs_xa.interfaces.device_features.disconnect import Disconnect
from thorlabs_xa.interfaces.device_features.piezo_inertial_motor.drive_operations_params import DriveOperationsParams
from thorlabs_xa.interfaces.device_features.end_of_move_messages_mode import EndOfMoveMessagesMode
from thorlabs_xa.interfaces.device_features.firmware_version_info import FirmwareVersionInfo
from thorlabs_xa.interfaces.device_features.hardware_info import HardwareInfo
from thorlabs_xa.interfaces.device_features.identify import Identify
from thorlabs_xa.interfaces.device_features.piezo_inertial_motor.kcube_channel_enable import KcubeChannelEnable
from thorlabs_xa.interfaces.device_features.piezo_inertial_motor.kcube_feedback_signal_params import KcubeFeedbackSignalParams
from thorlabs_xa.interfaces.device_features.piezo_inertial_motor.kcube_io_trigger_params import KcubeIoTriggerParams
from thorlabs_xa.interfaces.device_features.piezo_inertial_motor.kcube_jog_params import KcubeJogParams
from thorlabs_xa.interfaces.device_features.piezo_inertial_motor.kcube_mmi_params import KcubeMmiParams
from thorlabs_xa.interfaces.device_features.piezo_inertial_motor.kcube_trigger_params import KcubeTriggerParams
from thorlabs_xa.interfaces.device_features.load_params import LoadParams
from thorlabs_xa.interfaces.device_features.move import Move
from thorlabs_xa.interfaces.device_features.persist_params import PersistParams
from thorlabs_xa.interfaces.device_features.piezo_inertial_motor.position_counts import PositionCounts
from thorlabs_xa.interfaces.device_features.rich_response import RichResponse
from thorlabs_xa.interfaces.device_features.settings import Settings
from thorlabs_xa.interfaces.device_features.piezo_inertial_motor.stage_select_params import StageSelectParams
from thorlabs_xa.interfaces.device_features.status_items import StatusItems
from thorlabs_xa.interfaces.device_features.status_mode import StatusMode
from thorlabs_xa.interfaces.device_features.status_request import StatusRequest
from thorlabs_xa.interfaces.device_features.stop import Stop
from thorlabs_xa.interfaces.device_features.unit_converter import UnitConverter

from thorlabs_xa.native_sdks.native_functions import NativeFunctions
from thorlabs_xa.shared.params import TLMC_DeviceInfo

from thorlabs_xa.shared.enums import TLMC_EndOfMoveMessagesMode, TLMC_PZIM_KcubeChannelEnableMode, TLMC_MoveMode, TLMC_OperatingMode, TLMC_ParameterGroupId, TLMC_ScaleType, TLMC_SettingStringFormat, TLMC_StatusItemId, TLMC_StopMode, TLMC_Unit
from thorlabs_xa.shared.params import TLMC_DcPidParams, TLMC_PZIM_DriveOperationsParams, TLMC_FirmwareVersion, TLMC_HardwareInfo, TLMC_PZIM_KcubeFeedbackSignalParams, TLMC_PZIM_KcubeIoTriggerParams, TLMC_PZIM_KcubeJogParams, TLMC_PZIM_KcubeMmiParams, TLMC_PZIM_KcubeTriggerParams, TLMC_PZIM_PositionCounts, TLMC_RichResponse, TLMC_Setting, TLMC_PZIM_StageSelectParams, TLMC_StatusItem
from thorlabs_xa.shared.device import Device

class Kim001(Device,
        ConversionFactors,
        DcPidParams,
        Disconnect,
        DriveOperationsParams,
        EndOfMoveMessagesMode,
        FirmwareVersionInfo,
        HardwareInfo,
        Identify,
        KcubeChannelEnable,
        KcubeFeedbackSignalParams,
        KcubeIoTriggerParams,
        KcubeJogParams,
        KcubeMmiParams,
        KcubeTriggerParams,
        LoadParams,
        Move,
        PersistParams,
        PositionCounts,
        RichResponse,
        Settings,
        StageSelectParams,
        StatusItems,
        StatusMode,
        StatusRequest,
        Stop,
        UnitConverter):

    def __init__(self, device_handle: int, device_info: TLMC_DeviceInfo, feature_group: Kim001FeatureGroup, native_functions: NativeFunctions) -> None:

        super().__init__(device_handle, device_info, native_functions)

        self.feature_group = feature_group


    def get_conversion_factors(self, max_wait_in_milliseconds: int) -> int:

        return self.feature_group.conversion_factors_feature.get_conversion_factors(max_wait_in_milliseconds)

    def get_dc_pid_params(self, max_wait_in_milliseconds: int) -> TLMC_DcPidParams:

        return self.feature_group.dc_pid_params_feature.get_dc_pid_params(max_wait_in_milliseconds)

    def set_dc_pid_params(self, parameters: TLMC_DcPidParams) -> None:

        self.feature_group.dc_pid_params_feature.set_dc_pid_params(parameters)

    def disconnect(self) -> None:

        self.feature_group.disconnect_feature.disconnect()

    def get_drive_operations_params(self, max_wait_in_milliseconds: int) -> TLMC_PZIM_DriveOperationsParams:

        return self.feature_group.drive_operations_params_feature.get_drive_operations_params(max_wait_in_milliseconds)

    def set_drive_operations_params(self, params: TLMC_PZIM_DriveOperationsParams) -> None:

        self.feature_group.drive_operations_params_feature.set_drive_operations_params(params)

    def set_end_of_move_messages_mode(self, messages_mode: TLMC_EndOfMoveMessagesMode) -> None:

        self.feature_group.end_of_move_messages_mode_feature.set_end_of_move_messages_mode(messages_mode)

    def get_firmware_version_info(self, max_wait_in_milliseconds: int) -> tuple[TLMC_FirmwareVersion, TLMC_FirmwareVersion]:

        return self.feature_group.firmware_version_info_feature.get_firmware_version_info(max_wait_in_milliseconds)

    def get_hardware_info(self, max_wait_in_milliseconds: int) -> TLMC_HardwareInfo:

        return self.feature_group.hardware_info_feature.get_hardware_info(max_wait_in_milliseconds)

    def identify(self) -> None:

        self.feature_group.identify_feature.identify()

    def get_kcube_channel_enable(self, max_wait_in_milliseconds: int) -> TLMC_PZIM_KcubeChannelEnableMode:

        return self.feature_group.kcube_channel_enable_feature.get_kcube_channel_enable(max_wait_in_milliseconds)

    def set_kcube_channel_enable(self, channelMode: TLMC_PZIM_KcubeChannelEnableMode) -> None:

        self.feature_group.kcube_channel_enable_feature.set_kcube_channel_enable(channelMode)

    def get_kcube_feedback_signal_params(self, max_wait_in_milliseconds: int) -> TLMC_PZIM_KcubeFeedbackSignalParams:

        return self.feature_group.kcube_feedback_signal_params_feature.get_kcube_feedback_signal_params(max_wait_in_milliseconds)

    def set_kcube_feedback_signal_params(self, params: TLMC_PZIM_KcubeFeedbackSignalParams) -> None:

        self.feature_group.kcube_feedback_signal_params_feature.set_kcube_feedback_signal_params(params)

    def get_kcube_io_trigger_params(self, max_wait_in_milliseconds: int) -> TLMC_PZIM_KcubeIoTriggerParams:

        return self.feature_group.kcube_io_trigger_params_feature.get_kcube_io_trigger_params(max_wait_in_milliseconds)

    def set_kcube_io_trigger_params(self, params: TLMC_PZIM_KcubeIoTriggerParams) -> None:

        self.feature_group.kcube_io_trigger_params_feature.set_kcube_io_trigger_params(params)

    def get_kcube_jog_params(self, max_wait_in_milliseconds: int) -> TLMC_PZIM_KcubeJogParams:

        return self.feature_group.kcube_jog_params_feature.get_kcube_jog_params(max_wait_in_milliseconds)

    def set_kcube_jog_params(self, params: TLMC_PZIM_KcubeJogParams) -> None:

        self.feature_group.kcube_jog_params_feature.set_kcube_jog_params(params)

    def get_kcube_mmi_params(self, max_wait_in_milliseconds: int) -> TLMC_PZIM_KcubeMmiParams:

        return self.feature_group.kcube_mmi_params_feature.get_kcube_mmi_params(max_wait_in_milliseconds)

    def set_kcube_mmi_params(self, params: TLMC_PZIM_KcubeMmiParams) -> None:

        self.feature_group.kcube_mmi_params_feature.set_kcube_mmi_params(params)

    def get_kcube_trigger_params(self, max_wait_in_milliseconds: int) -> TLMC_PZIM_KcubeTriggerParams:

        return self.feature_group.kcube_trigger_params_feature.get_kcube_trigger_params(max_wait_in_milliseconds)

    def set_kcube_trigger_params(self, params: TLMC_PZIM_KcubeTriggerParams) -> None:

        self.feature_group.kcube_trigger_params_feature.set_kcube_trigger_params(params)

    def load_params(self) -> None:

        self.feature_group.load_params_feature.load_params()

    def move(self, move_mode: TLMC_MoveMode, params: int, max_wait_in_milliseconds: int) -> None:

        self.feature_group.move_feature.move(move_mode, params, max_wait_in_milliseconds)

    def persist_params(self, parameter_group_id: TLMC_ParameterGroupId) -> None:

        self.feature_group.persist_params_feature.persist_params(parameter_group_id)

    def get_position_counts(self, max_wait_in_milliseconds: int) -> TLMC_PZIM_PositionCounts:

        return self.feature_group.position_counts_feature.get_position_counts(max_wait_in_milliseconds)

    def set_position_counts(self, params: TLMC_PZIM_PositionCounts) -> None:

        self.feature_group.position_counts_feature.set_position_counts(params)

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

    def set_stage_select_params(self, params: TLMC_PZIM_StageSelectParams) -> None:

        self.feature_group.stage_select_params_feature.set_stage_select_params(params)

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

    def stop(self, stop_mode: TLMC_StopMode, max_wait_in_milliseconds: int) -> None:

        self.feature_group.stop_feature.stop(stop_mode, max_wait_in_milliseconds)

    def convert_from_device_units_to_physical(self, scale_type: TLMC_ScaleType, device_value: int) -> tuple[float, TLMC_Unit]:

        return self.feature_group.unit_converter_feature.convert_from_device_units_to_physical(scale_type, device_value)

    def convert_from_physical_to_device(self, scale_type: TLMC_ScaleType, unit: TLMC_Unit, physical_value: int) -> int:

        return self.feature_group.unit_converter_feature.convert_from_physical_to_device(scale_type, unit, physical_value)

    def get_preferred_physical_unit(self, scale_type: TLMC_ScaleType) -> TLMC_Unit:

        return self.feature_group.unit_converter_feature.get_preferred_physical_unit(scale_type)