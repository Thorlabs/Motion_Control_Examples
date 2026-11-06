from typing import Protocol

from thorlabs_xa.interfaces.device_features.piezo_inertial_motor.abnormal_move_detection_params import AbnormalMoveDetectionParams
from thorlabs_xa.interfaces.device_features.piezo_inertial_motor.amplifier_output_params import AmplifierOutputParams
from thorlabs_xa.interfaces.device_features.piezo_inertial_motor.closed_loop_move_params import ClosedLoopMoveParams
from thorlabs_xa.interfaces.device_features.piezo_inertial_motor.closed_loop_params import ClosedLoopParams
from thorlabs_xa.interfaces.device_features.connected_product import ConnectedProduct
from thorlabs_xa.interfaces.device_features.enable_state import EnableState
from thorlabs_xa.interfaces.device_features.piezo_inertial_motor.external_trigger_config import ExternalTriggerConfig
from thorlabs_xa.interfaces.device_features.piezo_inertial_motor.external_trigger_params import ExternalTriggerParams
from thorlabs_xa.interfaces.device_features.home import Home
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

class Pdxc3SubchannelFeatureGroup(Protocol):

    @property
    def abnormal_move_detection_params_feature(self) -> AbnormalMoveDetectionParams: ...

    @property
    def amplifier_output_params_feature(self) -> AmplifierOutputParams: ...

    @property
    def closed_loop_move_params_feature(self) -> ClosedLoopMoveParams: ...

    @property
    def closed_loop_params_feature(self) -> ClosedLoopParams: ...

    @property
    def connected_product_feature(self) -> ConnectedProduct: ...

    @property
    def enable_state_feature(self) -> EnableState: ...

    @property
    def external_trigger_config_feature(self) -> ExternalTriggerConfig: ...

    @property
    def external_trigger_params_feature(self) -> ExternalTriggerParams: ...

    @property
    def home_feature(self) -> Home: ...

    @property
    def jog_params_feature(self) -> JogParams: ...

    @property
    def load_params_feature(self) -> LoadParams: ...

    @property
    def move_feature(self) -> Move: ...

    @property
    def open_loop_move_params_feature(self) -> OpenLoopMoveParams: ...

    @property
    def persist_params_feature(self) -> PersistParams: ...

    @property
    def position_control_mode_feature(self) -> PositionControlMode: ...

    @property
    def piezo_inertial_motor_status_feature(self) -> PiezoInertialMotorStatus: ...

    @property
    def rich_response_feature(self) -> RichResponse: ...

    @property
    def settings_feature(self) -> Settings: ...

    @property
    def stage_axis_params_feature(self) -> StageAxisParams: ...

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