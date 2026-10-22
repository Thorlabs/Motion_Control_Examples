from typing import Protocol

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

class Kim001FeatureGroup(Protocol):

    @property
    def conversion_factors_feature(self) -> ConversionFactors: ...

    @property
    def dc_pid_params_feature(self) -> DcPidParams: ...

    @property
    def disconnect_feature(self) -> Disconnect: ...

    @property
    def end_of_move_messages_mode_feature(self) -> EndOfMoveMessagesMode: ...

    @property
    def drive_operations_params_feature(self) -> DriveOperationsParams: ...

    @property
    def firmware_version_info_feature(self) -> FirmwareVersionInfo: ...

    @property
    def hardware_info_feature(self) -> HardwareInfo: ...

    @property
    def identify_feature(self) -> Identify: ...

    @property
    def kcube_channel_enable_feature(self) -> KcubeChannelEnable: ...

    @property
    def kcube_feedback_signal_params_feature(self) -> KcubeFeedbackSignalParams: ...

    @property
    def kcube_jog_params_feature(self) -> KcubeJogParams: ...

    @property
    def kcube_mmi_params_feature(self) -> KcubeMmiParams: ...

    @property
    def kcube_io_trigger_params_feature(self) -> KcubeIoTriggerParams: ...

    @property
    def kcube_trigger_params_feature(self) -> KcubeTriggerParams: ...

    @property
    def load_params_feature(self) -> LoadParams: ...

    @property
    def move_feature(self) -> Move: ...

    @property
    def persist_params_feature(self) -> PersistParams: ...

    @property
    def position_counts_feature(self) -> PositionCounts: ...

    @property
    def rich_response_feature(self) -> RichResponse: ...

    @property
    def settings_feature(self) -> Settings: ...

    @property
    def stage_select_params_feature(self) -> StageSelectParams: ...

    @property
    def status_items_feature(self) -> StatusItems: ...

    @property
    def status_mode_feature(self) -> StatusMode: ...

    @property
    def status_request_feature(self) -> StatusRequest: ...

    @property
    def stop_feature(self) -> Stop: ...

    @property
    def unit_converter_feature(self) -> UnitConverter: ...
