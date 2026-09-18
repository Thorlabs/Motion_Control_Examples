import thorlabs_xa.interfaces.device_feature_groups.kim001_feature_group

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

from thorlabs_xa.implementations.device_features.piezo_inertial_motor.conversion_factors_feature import ConversionFactorsFeature
from thorlabs_xa.implementations.device_features.dc_pid_params_feature import DcPidParamsFeature
from thorlabs_xa.implementations.device_features.disconnect_feature import DisconnectFeature
from thorlabs_xa.implementations.device_features.piezo_inertial_motor.drive_operations_params_feature import DriveOperationsParamsFeature
from thorlabs_xa.implementations.device_features.end_of_move_messages_mode_feature import EndOfMoveMessagesModeFeature
from thorlabs_xa.implementations.device_features.firmware_version_info_feature import FirmwareVersionInfoFeature
from thorlabs_xa.implementations.device_features.hardware_info_feature import HardwareInfoFeature
from thorlabs_xa.implementations.device_features.identify_feature import IdentifyFeature
from thorlabs_xa.implementations.device_features.piezo_inertial_motor.kcube_channel_enable_feature import KcubeChannelEnableFeature
from thorlabs_xa.implementations.device_features.piezo_inertial_motor.kcube_feedback_signal_params_feature import KcubeFeedbackSignalParamsFeature
from thorlabs_xa.implementations.device_features.piezo_inertial_motor.kcube_io_trigger_params_feature import KcubeIoTriggerParamsFeature
from thorlabs_xa.implementations.device_features.piezo_inertial_motor.kcube_jog_params_feature import KcubeJogParamsFeature
from thorlabs_xa.implementations.device_features.piezo_inertial_motor.kcube_mmi_params_feature import KcubeMmiParamsFeature
from thorlabs_xa.implementations.device_features.piezo_inertial_motor.kcube_trigger_params_feature import KcubeTriggerParamsFeature
from thorlabs_xa.implementations.device_features.load_params_feature import LoadParamsFeature
from thorlabs_xa.implementations.device_features.move_feature import MoveFeature
from thorlabs_xa.implementations.device_features.persist_params_feature import PersistParamsFeature
from thorlabs_xa.implementations.device_features.piezo_inertial_motor.position_counts_feature import PositionCountsFeature
from thorlabs_xa.implementations.device_features.rich_response_feature import RichResponseFeature
from thorlabs_xa.implementations.device_features.settings_feature import SettingsFeature
from thorlabs_xa.implementations.device_features.piezo_inertial_motor.stage_select_params_feature import StageSelectParamsFeature
from thorlabs_xa.implementations.device_features.status_items_feature import StatusItemsFeature
from thorlabs_xa.implementations.device_features.status_mode_feature import StatusModeFeature
from thorlabs_xa.implementations.device_features.status_request_feature import StatusRequestFeature
from thorlabs_xa.implementations.device_features.stop_feature import StopFeature
from thorlabs_xa.implementations.device_features.unit_converter_feature import UnitConverterFeature

from thorlabs_xa.native_sdks.native_functions import NativeFunctions

class Kim001FeatureGroup(thorlabs_xa.interfaces.device_feature_groups.kim001_feature_group.Kim001FeatureGroup):

    def __init__(self, device_handle: int, native_functions: NativeFunctions) -> None:

        self._conversion_factors_feature = ConversionFactorsFeature(device_handle, native_functions)
        self._dc_pid_params_feature = DcPidParamsFeature(device_handle, native_functions)
        self._disconnect_feature = DisconnectFeature(device_handle, native_functions)
        self._drive_operations_params_feature = DriveOperationsParamsFeature(device_handle, native_functions)
        self._end_of_move_messages_mode_feature = EndOfMoveMessagesModeFeature(device_handle, native_functions)
        self._firmware_version_info_feature = FirmwareVersionInfoFeature(device_handle, native_functions)
        self._hardware_info_feature = HardwareInfoFeature(device_handle, native_functions)
        self._identify_feature = IdentifyFeature(device_handle, native_functions)
        self._kcube_channel_enable_feature = KcubeChannelEnableFeature(device_handle, native_functions)
        self._kcube_feedback_signal_params_feature = KcubeFeedbackSignalParamsFeature(device_handle, native_functions)
        self._kcube_io_trigger_params_feature = KcubeIoTriggerParamsFeature(device_handle, native_functions)
        self._kcube_jog_params_feature = KcubeJogParamsFeature(device_handle, native_functions)
        self._kcube_mmi_params_feature = KcubeMmiParamsFeature(device_handle, native_functions)
        self._kcube_trigger_params_feature = KcubeTriggerParamsFeature(device_handle, native_functions)
        self._load_params_feature = LoadParamsFeature(device_handle, native_functions)
        self._move_feature = MoveFeature(device_handle, native_functions)
        self._persist_params_feature = PersistParamsFeature(device_handle, native_functions)
        self._position_counts_feature = PositionCountsFeature(device_handle, native_functions)
        self._rich_response_feature = RichResponseFeature(device_handle, native_functions)
        self._settings_feature = SettingsFeature(device_handle, native_functions)
        self._stage_select_params_feature = StageSelectParamsFeature(device_handle, native_functions)
        self._status_items_feature = StatusItemsFeature(device_handle, native_functions)
        self._status_mode_feature = StatusModeFeature(device_handle, native_functions)
        self._status_request_feature = StatusRequestFeature(device_handle, native_functions)
        self._stop_feature = StopFeature(device_handle, native_functions)
        self._unit_converter_feature = UnitConverterFeature(device_handle, native_functions)


    @property
    def conversion_factors_feature(self) -> ConversionFactors:
        return self._conversion_factors_feature

    @property
    def dc_pid_params_feature(self) -> DcPidParams:
        return self._dc_pid_params_feature

    @property
    def disconnect_feature(self) -> Disconnect:
        return self._disconnect_feature

    @property
    def drive_operations_params_feature(self) -> DriveOperationsParams:
        return self._drive_operations_params_feature

    @property
    def end_of_move_messages_mode_feature(self) -> EndOfMoveMessagesMode:
        return self._end_of_move_messages_mode_feature

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
    def kcube_channel_enable_feature(self) -> KcubeChannelEnable:
        return self._kcube_channel_enable_feature

    @property
    def kcube_feedback_signal_params_feature(self) -> KcubeFeedbackSignalParams:
        return self._kcube_feedback_signal_params_feature

    @property
    def kcube_io_trigger_params_feature(self) -> KcubeIoTriggerParams:
        return self._kcube_io_trigger_params_feature

    @property
    def kcube_jog_params_feature(self) -> KcubeJogParams:
        return self._kcube_jog_params_feature

    @property
    def kcube_mmi_params_feature(self) -> KcubeMmiParams:
        return self._kcube_mmi_params_feature

    @property
    def kcube_trigger_params_feature(self) -> KcubeTriggerParams:
        return self._kcube_trigger_params_feature

    @property
    def load_params_feature(self) -> LoadParams:
        return self._load_params_feature

    @property
    def move_feature(self) -> Move:
        return self._move_feature

    @property
    def persist_params_feature(self) -> PersistParams:
        return self._persist_params_feature

    @property
    def position_counts_feature(self) -> PositionCounts:
        return self._position_counts_feature

    @property
    def rich_response_feature(self) -> RichResponse:
        return self._rich_response_feature

    @property
    def settings_feature(self) -> Settings:
        return self._settings_feature

    @property
    def stage_select_params_feature(self) -> StageSelectParams:
        return self._stage_select_params_feature

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
    def stop_feature(self) -> Stop:
        return self._stop_feature

    @property
    def unit_converter_feature(self) -> UnitConverter:
        return self._unit_converter_feature
