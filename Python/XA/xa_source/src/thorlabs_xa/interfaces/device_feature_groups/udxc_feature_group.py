from typing import Protocol

from thorlabs_xa.interfaces.device_features.connected_product import ConnectedProduct
from thorlabs_xa.interfaces.device_features.disconnect import Disconnect
from thorlabs_xa.interfaces.device_features.enable_state import EnableState
from thorlabs_xa.interfaces.device_features.hardware_info import HardwareInfo
from thorlabs_xa.interfaces.device_features.home import Home
from thorlabs_xa.interfaces.device_features.identify import Identify
from thorlabs_xa.interfaces.device_features.load_params import LoadParams
from thorlabs_xa.interfaces.device_features.persist_params import PersistParams
from thorlabs_xa.interfaces.device_features.piezo.position_control_mode import PositionControlMode
from thorlabs_xa.interfaces.device_features.piezo_inertial_motor.abnormal_move_detection_params import AbnormalMoveDetectionParams
from thorlabs_xa.interfaces.device_features.piezo_inertial_motor.amplifier_output_params import AmplifierOutputParams
from thorlabs_xa.interfaces.device_features.piezo_inertial_motor.closed_loop_move_params import ClosedLoopMoveParams
from thorlabs_xa.interfaces.device_features.piezo_inertial_motor.closed_loop_params import ClosedLoopParams
from thorlabs_xa.interfaces.device_features.piezo_inertial_motor.current_position import CurrentPosition
from thorlabs_xa.interfaces.device_features.piezo_inertial_motor.ethernet_params import EthernetParams
from thorlabs_xa.interfaces.device_features.piezo_inertial_motor.external_trigger_config import ExternalTriggerConfig
from thorlabs_xa.interfaces.device_features.piezo_inertial_motor.external_trigger_params import ExternalTriggerParams
from thorlabs_xa.interfaces.device_features.piezo_inertial_motor.jog_params import JogParams
from thorlabs_xa.interfaces.device_features.piezo_inertial_motor.move_absolute_to_programmed_position import MoveAbsoluteToProgrammedPosition
from thorlabs_xa.interfaces.device_features.piezo_inertial_motor.move_jog import MoveJog
from thorlabs_xa.interfaces.device_features.piezo_inertial_motor.move_stop import MoveStop
from thorlabs_xa.interfaces.device_features.piezo_inertial_motor.open_loop_move_params import OpenLoopMoveParams
from thorlabs_xa.interfaces.device_features.piezo_inertial_motor.piezo_inertial_motor_status import PiezoInertialMotorStatus
from thorlabs_xa.interfaces.device_features.piezo_inertial_motor.pulse_para_acquire import PulseParaAcquire
from thorlabs_xa.interfaces.device_features.piezo_inertial_motor.trigger_target_position import TriggerTargetPosition
from thorlabs_xa.interfaces.device_features.rich_response import RichResponse
from thorlabs_xa.interfaces.device_features.settings import Settings
from thorlabs_xa.interfaces.device_features.stage_axis_params import StageAxisParams
from thorlabs_xa.interfaces.device_features.status_items import StatusItems
from thorlabs_xa.interfaces.device_features.status_mode import StatusMode
from thorlabs_xa.interfaces.device_features.status_request import StatusRequest
from thorlabs_xa.interfaces.device_features.unit_converter import UnitConverter

class UdxcFeatureGroup(Protocol):

    @property
    def connected_product_feature(self) -> ConnectedProduct: ...

    @property
    def disconnect_feature(self) -> Disconnect: ...

    @property
    def enable_state_feature(self) -> EnableState: ...

    @property
    def hardware_info_feature(self) -> HardwareInfo: ...

    @property
    def home_feature(self) -> Home: ...

    @property
    def identify_feature(self) -> Identify: ...

    @property
    def load_params_feature(self) -> LoadParams: ...

    @property
    def move_absolute_to_programmed_position_feature(self) -> MoveAbsoluteToProgrammedPosition: ...

    @property
    def move_jog_feature(self) -> MoveJog: ...

    @property
    def move_stop_feature(self) -> MoveStop: ...

    @property
    def persist_params_feature(self) -> PersistParams: ...

    @property
    def position_control_mode_feature(self) -> PositionControlMode: ...

    @property
    def abnormal_move_detection_params_feature(self) -> AbnormalMoveDetectionParams: ...

    @property
    def amplifier_output_params_feature(self) -> AmplifierOutputParams: ...

    @property
    def closed_loop_move_params_feature(self) -> ClosedLoopMoveParams: ...

    @property
    def closed_loop_params_feature(self) -> ClosedLoopParams: ...

    @property
    def current_position_feature(self) -> CurrentPosition: ...

    @property
    def ethernet_params_feature(self) -> EthernetParams: ...

    @property
    def external_trigger_config_feature(self) -> ExternalTriggerConfig: ...

    @property
    def external_trigger_params_feature(self) -> ExternalTriggerParams: ...

    @property
    def jog_params_feature(self) -> JogParams: ...

    @property
    def open_loop_move_params_feature(self) -> OpenLoopMoveParams: ...

    @property
    def piezo_inertial_motor_status_feature(self) -> PiezoInertialMotorStatus: ...

    @property
    def pulse_para_acquire_feature(self) -> PulseParaAcquire: ...

    @property
    def trigger_target_position_feature(self) -> TriggerTargetPosition: ...

    @property
    def rich_response_feature(self) -> RichResponse: ...

    @property
    def settings_feature(self) -> Settings: ...

    @property
    def stage_axis_params_feature(self) -> StageAxisParams: ...

    @property
    def status_items_feature(self) -> StatusItems: ...

    @property
    def set_status_mode_feature(self) -> StatusMode: ...

    @property
    def status_request_feature(self) -> StatusRequest: ...

    @property
    def unit_converter_feature(self) -> UnitConverter: ...
