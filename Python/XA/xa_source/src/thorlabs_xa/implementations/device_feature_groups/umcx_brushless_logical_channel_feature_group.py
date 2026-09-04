import thorlabs_xa.interfaces.device_feature_groups.umcx_brushless_logical_channel_feature_group

from thorlabs_xa.interfaces.device_features.connected_product import ConnectedProduct
from thorlabs_xa.interfaces.device_features.current_loop_params import CurrentLoopParams
from thorlabs_xa.interfaces.device_features.enable_state import EnableState
from thorlabs_xa.interfaces.device_features.end_of_move_messages_mode import EndOfMoveMessagesMode
from thorlabs_xa.interfaces.device_features.firmware_version_info import FirmwareVersionInfo
from thorlabs_xa.interfaces.device_features.general_move_params import GeneralMoveParams
from thorlabs_xa.interfaces.device_features.hardware_info import HardwareInfo
from thorlabs_xa.interfaces.device_features.home import Home
from thorlabs_xa.interfaces.device_features.home_params import HomeParams
from thorlabs_xa.interfaces.device_features.identify import Identify
from thorlabs_xa.interfaces.device_features.io_position_trigger_enable_state import IoPositionTriggerEnableState
from thorlabs_xa.interfaces.device_features.io_trigger_params import IoTriggerParams
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
from thorlabs_xa.interfaces.device_features.umc_status import UmcStatus
from thorlabs_xa.interfaces.device_features.unit_converter import UnitConverter
from thorlabs_xa.interfaces.device_features.universal_status_bits import UniversalStatusBits
from thorlabs_xa.interfaces.device_features.velocity_params import VelocityParams

from thorlabs_xa.implementations.device_features.connected_product_feature import ConnectedProductFeature
from thorlabs_xa.implementations.device_features.current_loop_params_feature import CurrentLoopParamsFeature
from thorlabs_xa.implementations.device_features.enable_state_feature import EnableStateFeature
from thorlabs_xa.implementations.device_features.end_of_move_messages_mode_feature import EndOfMoveMessagesModeFeature
from thorlabs_xa.implementations.device_features.firmware_version_info_feature import FirmwareVersionInfoFeature
from thorlabs_xa.implementations.device_features.general_move_params_feature import GeneralMoveParamsFeature
from thorlabs_xa.implementations.device_features.hardware_info_feature import HardwareInfoFeature
from thorlabs_xa.implementations.device_features.home_feature import HomeFeature
from thorlabs_xa.implementations.device_features.home_params_feature import HomeParamsFeature
from thorlabs_xa.implementations.device_features.identify_feature import IdentifyFeature
from thorlabs_xa.implementations.device_features.io_position_trigger_enable_state_feature import IoPositionTriggerEnableStateFeature
from thorlabs_xa.implementations.device_features.io_trigger_params_feature import IoTriggerParamsFeature
from thorlabs_xa.implementations.device_features.jog_params_feature import JogParamsFeature
from thorlabs_xa.implementations.device_features.joystick_params_feature import JoystickParamsFeature
from thorlabs_xa.implementations.device_features.limit_switch_params_getter_feature import LimitSwitchParamsGetterFeature
from thorlabs_xa.implementations.device_features.load_params_feature import LoadParamsFeature
from thorlabs_xa.implementations.device_features.motor_output_params_feature import MotorOutputParamsFeature
from thorlabs_xa.implementations.device_features.move_feature import MoveFeature
from thorlabs_xa.implementations.device_features.move_absolute_params_feature import MoveAbsoluteParamsFeature
from thorlabs_xa.implementations.device_features.move_relative_params_feature import MoveRelativeParamsFeature
from thorlabs_xa.implementations.device_features.persist_params_feature import PersistParamsFeature
from thorlabs_xa.implementations.device_features.position_counter_feature import PositionCounterFeature
from thorlabs_xa.implementations.device_features.position_loop_params_feature import PositionLoopParamsFeature
from thorlabs_xa.implementations.device_features.profile_mode_params_feature import ProfileModeParamsFeature
from thorlabs_xa.implementations.device_features.restore_factory_defaults_feature import RestoreFactoryDefaultsFeature
from thorlabs_xa.implementations.device_features.rich_response_feature import RichResponseFeature
from thorlabs_xa.implementations.device_features.settings_feature import SettingsFeature
from thorlabs_xa.implementations.device_features.stage_axis_params_feature import StageAxisParamsFeature
from thorlabs_xa.implementations.device_features.status_items_feature import StatusItemsFeature
from thorlabs_xa.implementations.device_features.status_mode_feature import StatusModeFeature
from thorlabs_xa.implementations.device_features.status_request_feature import StatusRequestFeature
from thorlabs_xa.implementations.device_features.stop_feature import StopFeature
from thorlabs_xa.implementations.device_features.track_settle_params_feature import TrackSettleParamsFeature
from thorlabs_xa.implementations.device_features.umc_status_feature import UmcStatusFeature
from thorlabs_xa.implementations.device_features.unit_converter_feature import UnitConverterFeature
from thorlabs_xa.implementations.device_features.universal_status_bits_feature import UniversalStatusBitsFeature
from thorlabs_xa.implementations.device_features.velocity_params_feature import VelocityParamsFeature

from thorlabs_xa.native_sdks.native_functions import NativeFunctions

class UmcxBrushlessLogicalChannelFeatureGroup(thorlabs_xa.interfaces.device_feature_groups.umcx_brushless_logical_channel_feature_group.UmcxBrushlessLogicalChannelFeatureGroup):

    def __init__(self, device_handle: int, native_functions: NativeFunctions) -> None:

        self._connected_product_feature = ConnectedProductFeature(device_handle, native_functions)
        self._current_loop_params_feature = CurrentLoopParamsFeature(device_handle, native_functions)
        self._enable_state_feature = EnableStateFeature(device_handle, native_functions)
        self._end_of_move_messages_mode_feature = EndOfMoveMessagesModeFeature(device_handle, native_functions)
        self._firmware_version_info_feature = FirmwareVersionInfoFeature(device_handle, native_functions)
        self._general_move_params_feature = GeneralMoveParamsFeature(device_handle, native_functions)
        self._hardware_info_feature = HardwareInfoFeature(device_handle, native_functions)
        self._home_feature = HomeFeature(device_handle, native_functions)
        self._home_params_feature = HomeParamsFeature(device_handle, native_functions)
        self._identify_feature = IdentifyFeature(device_handle, native_functions)
        self._io_position_trigger_enable_state_feature = IoPositionTriggerEnableStateFeature(device_handle, native_functions)
        self._io_trigger_params_feature = IoTriggerParamsFeature(device_handle, native_functions)
        self._jog_params_feature = JogParamsFeature(device_handle, native_functions)
        self._joystick_params_feature = JoystickParamsFeature(device_handle, native_functions)
        self._limit_switch_params_getter_feature = LimitSwitchParamsGetterFeature(device_handle, native_functions)
        self._load_params_feature = LoadParamsFeature(device_handle, native_functions)
        self._motor_output_params_feature = MotorOutputParamsFeature(device_handle, native_functions)
        self._move_feature = MoveFeature(device_handle, native_functions)
        self._move_absolute_params_feature = MoveAbsoluteParamsFeature(device_handle, native_functions)
        self._move_relative_params_feature = MoveRelativeParamsFeature(device_handle, native_functions)
        self._persist_params_feature = PersistParamsFeature(device_handle, native_functions)
        self._position_counter_feature = PositionCounterFeature(device_handle, native_functions)
        self._position_loop_params_feature = PositionLoopParamsFeature(device_handle, native_functions)
        self._profile_mode_params_feature = ProfileModeParamsFeature(device_handle, native_functions)
        self._restore_factory_defaults_feature = RestoreFactoryDefaultsFeature(device_handle, native_functions)
        self._rich_response_feature = RichResponseFeature(device_handle, native_functions)
        self._settings_feature = SettingsFeature(device_handle, native_functions)
        self._stage_axis_params_feature = StageAxisParamsFeature(device_handle, native_functions)
        self._status_items_feature = StatusItemsFeature(device_handle, native_functions)
        self._status_mode_feature = StatusModeFeature(device_handle, native_functions)
        self._status_request_feature = StatusRequestFeature(device_handle, native_functions)
        self._stop_feature = StopFeature(device_handle, native_functions)
        self._track_settle_params_feature = TrackSettleParamsFeature(device_handle, native_functions)
        self._umc_status_feature = UmcStatusFeature(device_handle, native_functions)
        self._unit_converter_feature = UnitConverterFeature(device_handle, native_functions)
        self._universal_status_bits_feature = UniversalStatusBitsFeature(device_handle, native_functions)
        self._velocity_params_feature = VelocityParamsFeature(device_handle, native_functions)

    @property
    def connected_product_feature(self) -> ConnectedProduct:
        return self._connected_product_feature

    @property
    def current_loop_params_feature(self) -> CurrentLoopParams:
        return self._current_loop_params_feature

    @property
    def enable_state_feature(self) -> EnableState:
        return self._enable_state_feature

    @property
    def end_of_move_messages_mode_feature(self) -> EndOfMoveMessagesMode:
        return self._end_of_move_messages_mode_feature

    @property
    def firmware_version_info_feature(self) -> FirmwareVersionInfo:
        return self._firmware_version_info_feature

    @property
    def general_move_params_feature(self) -> GeneralMoveParams:
        return self._general_move_params_feature

    @property
    def hardware_info_feature(self) -> HardwareInfo:
        return self._hardware_info_feature

    @property
    def home_feature(self) -> Home:
        return self._home_feature

    @property
    def home_params_feature(self) -> HomeParams:
        return self._home_params_feature

    @property
    def identify_feature(self) -> Identify:
        return self._identify_feature

    @property
    def io_position_trigger_enable_state_feature(self) -> IoPositionTriggerEnableState:
        return self._io_position_trigger_enable_state_feature

    @property
    def io_trigger_params_feature(self) -> IoTriggerParams:
        return self._io_trigger_params_feature

    @property
    def jog_params_feature(self) -> JogParams:
        return self._jog_params_feature

    @property
    def joystick_params_feature(self) -> JoystickParams:
        return self._joystick_params_feature

    @property
    def limit_switch_params_getter_feature(self) -> LimitSwitchParamsGetter:
        return self._limit_switch_params_getter_feature

    @property
    def load_params_feature(self) -> LoadParams:
        return self._load_params_feature

    @property
    def motor_output_params_feature(self) -> MotorOutputParams:
        return self._motor_output_params_feature

    @property
    def move_feature(self) -> Move:
        return self._move_feature

    @property
    def move_absolute_params_feature(self) -> MoveAbsoluteParams:
        return self._move_absolute_params_feature

    @property
    def move_relative_params_feature(self) -> MoveRelativeParams:
        return self._move_relative_params_feature

    @property
    def persist_params_feature(self) -> PersistParams:
        return self._persist_params_feature

    @property
    def position_counter_feature(self) -> PositionCounter:
        return self._position_counter_feature

    @property
    def position_loop_params_feature(self) -> PositionLoopParams:
        return self._position_loop_params_feature

    @property
    def profile_mode_params_feature(self) -> ProfileModeParams:
        return self._profile_mode_params_feature

    @property
    def restore_factory_defaults_feature(self) -> RestoreFactoryDefaults:
        return self._restore_factory_defaults_feature

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
    def track_settle_params_feature(self) -> TrackSettleParams:
        return self._track_settle_params_feature

    @property
    def umc_status_feature(self) -> UmcStatus:
        return self._umc_status_feature

    @property
    def unit_converter_feature(self) -> UnitConverter:
        return self._unit_converter_feature

    @property
    def universal_status_bits_feature(self) -> UniversalStatusBits:
        return self._universal_status_bits_feature

    @property
    def velocity_params_feature(self) -> VelocityParams:
        return self._velocity_params_feature