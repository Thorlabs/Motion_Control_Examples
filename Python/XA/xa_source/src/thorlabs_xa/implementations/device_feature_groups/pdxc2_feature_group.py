import thorlabs_xa.interfaces.device_feature_groups.pdxc2_feature_group

from thorlabs_xa.interfaces.device_features.piezo_inertial_motor.abnormal_move_detection_params import AbnormalMoveDetectionParams
from thorlabs_xa.interfaces.device_features.piezo_inertial_motor.amplifier_output_params import AmplifierOutputParams
from thorlabs_xa.interfaces.device_features.piezo_inertial_motor.closed_loop_move_params import ClosedLoopMoveParams
from thorlabs_xa.interfaces.device_features.piezo_inertial_motor.closed_loop_params import ClosedLoopParams
from thorlabs_xa.interfaces.device_features.connected_product import ConnectedProduct
from thorlabs_xa.interfaces.device_features.disconnect import Disconnect
from thorlabs_xa.interfaces.device_features.enable_state import EnableState
from thorlabs_xa.interfaces.device_features.piezo_inertial_motor.ethernet_params import EthernetParams
from thorlabs_xa.interfaces.device_features.piezo_inertial_motor.external_trigger_config import ExternalTriggerConfig
from thorlabs_xa.interfaces.device_features.piezo_inertial_motor.external_trigger_params import ExternalTriggerParams
from thorlabs_xa.interfaces.device_features.firmware_version_info import FirmwareVersionInfo
from thorlabs_xa.interfaces.device_features.hardware_info import HardwareInfo
from thorlabs_xa.interfaces.device_features.home import Home
from thorlabs_xa.interfaces.device_features.identify import Identify
from thorlabs_xa.interfaces.device_features.piezo_inertial_motor.jog_params import JogParams
from thorlabs_xa.interfaces.device_features.load_params import LoadParams
from thorlabs_xa.interfaces.device_features.move import Move
from thorlabs_xa.interfaces.device_features.piezo_inertial_motor.open_loop_move_params import OpenLoopMoveParams
from thorlabs_xa.interfaces.device_features.persist_params import PersistParams
from thorlabs_xa.interfaces.device_features.piezo.position_control_mode import PositionControlMode
from thorlabs_xa.interfaces.device_features.piezo_inertial_motor.piezo_inertial_motor_status import PiezoInertialMotorStatus
from thorlabs_xa.interfaces.device_features.rich_response import RichResponse
from thorlabs_xa.interfaces.device_features.settings import Settings
from thorlabs_xa.interfaces.device_features.stage_axis_params import StageAxisParams
from thorlabs_xa.interfaces.device_features.status_items import StatusItems
from thorlabs_xa.interfaces.device_features.status_mode import StatusMode
from thorlabs_xa.interfaces.device_features.status_request import StatusRequest
from thorlabs_xa.interfaces.device_features.stop import Stop
from thorlabs_xa.interfaces.device_features.unit_converter import UnitConverter

from thorlabs_xa.implementations.device_features.piezo_inertial_motor.abnormal_move_detection_params_feature import AbnormalMoveDetectionParamsFeature
from thorlabs_xa.implementations.device_features.piezo_inertial_motor.amplifier_output_params_feature import AmplifierOutputParamsFeature
from thorlabs_xa.implementations.device_features.piezo_inertial_motor.closed_loop_move_params_feature import ClosedLoopMoveParamsFeature
from thorlabs_xa.implementations.device_features.piezo_inertial_motor.closed_loop_params_feature import ClosedLoopParamsFeature
from thorlabs_xa.implementations.device_features.connected_product_feature import ConnectedProductFeature
from thorlabs_xa.implementations.device_features.disconnect_feature import DisconnectFeature
from thorlabs_xa.implementations.device_features.enable_state_feature import EnableStateFeature
from thorlabs_xa.implementations.device_features.piezo_inertial_motor.ethernet_params_feature import EthernetParamsFeature
from thorlabs_xa.implementations.device_features.piezo_inertial_motor.external_trigger_config_feature import ExternalTriggerConfigFeature
from thorlabs_xa.implementations.device_features.piezo_inertial_motor.external_trigger_params_feature import ExternalTriggerParamsFeature
from thorlabs_xa.implementations.device_features.firmware_version_info_feature import FirmwareVersionInfoFeature
from thorlabs_xa.implementations.device_features.hardware_info_feature import HardwareInfoFeature
from thorlabs_xa.implementations.device_features.home_feature import HomeFeature
from thorlabs_xa.implementations.device_features.identify_feature import IdentifyFeature
from thorlabs_xa.implementations.device_features.piezo_inertial_motor.jog_params_feature import JogParamsFeature
from thorlabs_xa.implementations.device_features.load_params_feature import LoadParamsFeature
from thorlabs_xa.implementations.device_features.move_feature import MoveFeature
from thorlabs_xa.implementations.device_features.piezo_inertial_motor.open_loop_move_params_feature import OpenLoopMoveParamsFeature
from thorlabs_xa.implementations.device_features.persist_params_feature import PersistParamsFeature
from thorlabs_xa.implementations.device_features.piezo.position_control_mode_feature import PositionControlModeFeature
from thorlabs_xa.implementations.device_features.piezo_inertial_motor.piezo_inertial_motor_status_feature import PiezoInertialMotorStatusFeature
from thorlabs_xa.implementations.device_features.rich_response_feature import RichResponseFeature
from thorlabs_xa.implementations.device_features.settings_feature import SettingsFeature
from thorlabs_xa.implementations.device_features.stage_axis_params_feature import StageAxisParamsFeature
from thorlabs_xa.implementations.device_features.status_items_feature import StatusItemsFeature
from thorlabs_xa.implementations.device_features.status_mode_feature import StatusModeFeature
from thorlabs_xa.implementations.device_features.status_request_feature import StatusRequestFeature
from thorlabs_xa.implementations.device_features.stop_feature import StopFeature
from thorlabs_xa.implementations.device_features.unit_converter_feature import UnitConverterFeature
from thorlabs_xa.implementations.device_features.piezo_inertial_motor.jog_params_feature import JogParamsFeature
from thorlabs_xa.implementations.device_features.piezo_inertial_motor.open_loop_move_params_feature import OpenLoopMoveParamsFeature

from thorlabs_xa.native_sdks.native_functions import NativeFunctions

class Pdxc2FeatureGroup(thorlabs_xa.interfaces.device_feature_groups.pdxc2_feature_group.Pdxc2FeatureGroup):

    def __init__(self, device_handle: int, native_functions: NativeFunctions) -> None:

        self._abnormal_move_detection_params_feature = AbnormalMoveDetectionParamsFeature(device_handle, native_functions)
        self._amplifier_output_params_feature = AmplifierOutputParamsFeature(device_handle, native_functions)
        self._closed_loop_move_params_feature = ClosedLoopMoveParamsFeature(device_handle, native_functions)
        self._closed_loop_params_feature = ClosedLoopParamsFeature(device_handle, native_functions)
        self._connected_product_feature = ConnectedProductFeature(device_handle, native_functions)
        self._disconnect_feature = DisconnectFeature(device_handle, native_functions)
        self._enable_state_feature = EnableStateFeature(device_handle, native_functions)
        self._ethernet_params_feature = EthernetParamsFeature(device_handle, native_functions)
        self._external_trigger_config_feature = ExternalTriggerConfigFeature(device_handle, native_functions)
        self._external_trigger_params_feature = ExternalTriggerParamsFeature(device_handle, native_functions)
        self._firmware_version_info_feature = FirmwareVersionInfoFeature(device_handle, native_functions)
        self._hardware_info_feature = HardwareInfoFeature(device_handle, native_functions)
        self._home_feature = HomeFeature(device_handle, native_functions)
        self._identify_feature = IdentifyFeature(device_handle, native_functions)
        self._jog_params_feature = JogParamsFeature(device_handle, native_functions)
        self._load_params_feature = LoadParamsFeature(device_handle, native_functions)
        self._move_feature = MoveFeature(device_handle, native_functions)
        self._open_loop_move_params_feature = OpenLoopMoveParamsFeature(device_handle, native_functions)
        self._persist_params_feature = PersistParamsFeature(device_handle, native_functions)
        self._position_control_mode_feature = PositionControlModeFeature(device_handle, native_functions)
        self._piezo_inertial_motor_status_feature = PiezoInertialMotorStatusFeature(device_handle, native_functions)
        self._rich_response_feature = RichResponseFeature(device_handle, native_functions)
        self._settings_feature = SettingsFeature(device_handle, native_functions)
        self._stage_axis_params_feature = StageAxisParamsFeature(device_handle, native_functions)
        self._status_items_feature = StatusItemsFeature(device_handle, native_functions)
        self._status_mode_feature = StatusModeFeature(device_handle, native_functions)
        self._status_request_feature = StatusRequestFeature(device_handle, native_functions)
        self._stop_feature = StopFeature(device_handle, native_functions)
        self._unit_converter_feature = UnitConverterFeature(device_handle, native_functions)

    @property
    def abnormal_move_detection_params_feature(self) -> AbnormalMoveDetectionParams:
        return self._abnormal_move_detection_params_feature

    @property
    def amplifier_output_params_feature(self) -> AmplifierOutputParams:
        return self._amplifier_output_params_feature

    @property
    def closed_loop_move_params_feature(self) -> ClosedLoopMoveParams:
        return self._closed_loop_move_params_feature

    @property
    def closed_loop_params_feature(self) -> ClosedLoopParams:
        return self._closed_loop_params_feature

    @property
    def jog_params_feature(self) -> JogParams:
        return self._jog_params_feature

    @property
    def open_loop_move_params_feature(self) -> OpenLoopMoveParams:
        return self._open_loop_move_params_feature

    @property
    def connected_product_feature(self) -> ConnectedProduct:
        return self._connected_product_feature

    @property
    def disconnect_feature(self) -> Disconnect:
        return self._disconnect_feature

    @property
    def enable_state_feature(self) -> EnableState:
        return self._enable_state_feature

    @property
    def ethernet_params_feature(self) -> EthernetParams:
        return self._ethernet_params_feature

    @property
    def external_trigger_config_feature(self) -> ExternalTriggerConfig:
        return self._external_trigger_config_feature

    @property
    def external_trigger_params_feature(self) -> ExternalTriggerParams:
        return self._external_trigger_params_feature

    @property
    def firmware_version_info_feature(self) -> FirmwareVersionInfo:
        return self._firmware_version_info_feature

    @property
    def hardware_info_feature(self) -> HardwareInfo:
        return self._hardware_info_feature

    @property
    def home_feature(self) -> Home:
        return self._home_feature

    @property
    def identify_feature(self) -> Identify:
        return self._identify_feature

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
    def position_control_mode_feature(self) -> PositionControlMode:
        return self._position_control_mode_feature

    @property
    def piezo_inertial_motor_status_feature(self) -> PiezoInertialMotorStatus:
        return self._piezo_inertial_motor_status_feature

    @property
    def rich_response_feature(self) -> RichResponse:
        return self._rich_response_feature

    @property
    def settings_feature(self) -> Settings:
        return self._settings_feature

    @property
    def stage_axis_params_feature(self) -> StageAxisParams:
        return self._stage_axis_params_feature

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