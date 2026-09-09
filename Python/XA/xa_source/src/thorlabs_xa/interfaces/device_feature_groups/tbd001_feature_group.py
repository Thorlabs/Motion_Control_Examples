from typing import Protocol

from thorlabs_xa.interfaces.device_features.connected_product import ConnectedProduct
from thorlabs_xa.interfaces.device_features.current_loop_params import CurrentLoopParams
from thorlabs_xa.interfaces.device_features.digital_output_states import DigitalOutputStates
from thorlabs_xa.interfaces.device_features.enable_state import EnableState
from thorlabs_xa.interfaces.device_features.firmware_version_info import FirmwareVersionInfo
from thorlabs_xa.interfaces.device_features.general_move_params import GeneralMoveParams
from thorlabs_xa.interfaces.device_features.hardware_info import HardwareInfo
from thorlabs_xa.interfaces.device_features.home import Home
from thorlabs_xa.interfaces.device_features.home_params import HomeParams
from thorlabs_xa.interfaces.device_features.identify import Identify
from thorlabs_xa.interfaces.device_features.jog_params import JogParams
from thorlabs_xa.interfaces.device_features.joystick_params import JoystickParams
from thorlabs_xa.interfaces.device_features.limit_switch_params_getter import LimitSwitchParamsGetter
from thorlabs_xa.interfaces.device_features.load_params import LoadParams
from thorlabs_xa.interfaces.device_features.motor_output_params import MotorOutputParams
from thorlabs_xa.interfaces.device_features.move import Move
from thorlabs_xa.interfaces.device_features.move_absolute_params import MoveAbsoluteParams
from thorlabs_xa.interfaces.device_features.move_relative_params import MoveRelativeParams
from thorlabs_xa.interfaces.device_features.persist_params import PersistParams
from thorlabs_xa.interfaces.device_features.position_counter import PositionCounter
from thorlabs_xa.interfaces.device_features.position_loop_params import PositionLoopParams
from thorlabs_xa.interfaces.device_features.profile_mode_params import ProfileModeParams
from thorlabs_xa.interfaces.device_features.restore_factory_defaults import RestoreFactoryDefaults
from thorlabs_xa.interfaces.device_features.rich_response import RichResponse
from thorlabs_xa.interfaces.device_features.settings import Settings
from thorlabs_xa.interfaces.device_features.stage_axis_params import StageAxisParams
from thorlabs_xa.interfaces.device_features.status_items import StatusItems
from thorlabs_xa.interfaces.device_features.status_mode import StatusMode
from thorlabs_xa.interfaces.device_features.status_request import StatusRequest
from thorlabs_xa.interfaces.device_features.stop import Stop
from thorlabs_xa.interfaces.device_features.track_settle_params import TrackSettleParams
from thorlabs_xa.interfaces.device_features.trigger_params_for_dc_brushless import TriggerParamsForDcBrushless
from thorlabs_xa.interfaces.device_features.unit_converter import UnitConverter
from thorlabs_xa.interfaces.device_features.universal_status import UniversalStatus
from thorlabs_xa.interfaces.device_features.universal_status_bits import UniversalStatusBits
from thorlabs_xa.interfaces.device_features.velocity_params import VelocityParams

class Tbd001FeatureGroup(Protocol):

    @property
    def connected_product_feature(self) -> ConnectedProduct: ...

    @property
    def current_loop_params_feature(self) -> CurrentLoopParams: ...

    @property
    def digital_output_states_feature(self) -> DigitalOutputStates: ...

    @property
    def enable_state_feature(self) -> EnableState: ...

    @property
    def firmware_version_info_feature(self) -> FirmwareVersionInfo: ...

    @property
    def general_move_params_feature(self) -> GeneralMoveParams: ...

    @property
    def hardware_info_feature(self) -> HardwareInfo: ...

    @property
    def home_feature(self) -> Home: ...

    @property
    def home_params_feature(self) -> HomeParams: ...

    @property
    def identify_feature(self) -> Identify: ...

    @property
    def jog_params_feature(self) -> JogParams: ...

    @property
    def joystick_params_feature(self) -> JoystickParams: ...

    @property
    def limit_switch_params_getter_feature(self) -> LimitSwitchParamsGetter: ...

    @property
    def load_params_feature(self) -> LoadParams: ...

    @property
    def motor_output_params_feature(self) -> MotorOutputParams: ...

    @property
    def move_feature(self) -> Move: ...

    @property
    def move_absolute_params_feature(self) -> MoveAbsoluteParams: ...

    @property
    def move_relative_params_feature(self) -> MoveRelativeParams: ...

    @property
    def persist_params_feature(self) -> PersistParams: ...

    @property
    def position_counter_feature(self) -> PositionCounter: ...

    @property
    def position_loop_params_feature(self) -> PositionLoopParams: ...

    @property
    def profile_mode_params_feature(self) -> ProfileModeParams: ...

    @property
    def restore_factory_defaults_feature(self) -> RestoreFactoryDefaults: ...

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
    def track_settle_params_feature(self) -> TrackSettleParams: ...

    @property
    def trigger_params_for_dc_brushless_feature(self) -> TriggerParamsForDcBrushless: ...

    @property
    def unit_converter_feature(self) -> UnitConverter: ...

    @property
    def universal_status_feature(self) -> UniversalStatus: ...

    @property
    def universal_status_bits_feature(self) -> UniversalStatusBits: ...

    @property
    def velocity_params_feature(self) -> VelocityParams: ...