import thorlabs_xa.interfaces.device_feature_groups.bsc201_feature_group

from thorlabs_xa.interfaces.device_features.adc_inputs import AdcInputs
from thorlabs_xa.interfaces.device_features.bow_index import BowIndex
from thorlabs_xa.interfaces.device_features.connected_product import ConnectedProduct
from thorlabs_xa.interfaces.device_features.digital_output_states import DigitalOutputStates
from thorlabs_xa.interfaces.device_features.disconnect import Disconnect
from thorlabs_xa.interfaces.device_features.enable_state import EnableState
from thorlabs_xa.interfaces.device_features.encoder_counter import EncoderCounter
from thorlabs_xa.interfaces.device_features.firmware_version_info import FirmwareVersionInfo
from thorlabs_xa.interfaces.device_features.general_move_params import GeneralMoveParams
from thorlabs_xa.interfaces.device_features.hardware_info import HardwareInfo
from thorlabs_xa.interfaces.device_features.home import Home
from thorlabs_xa.interfaces.device_features.home_params import HomeParams
from thorlabs_xa.interfaces.device_features.identify import Identify
from thorlabs_xa.interfaces.device_features.jog_params import JogParams
from thorlabs_xa.interfaces.device_features.limit_switch_params_getter import LimitSwitchParamsGetter
from thorlabs_xa.interfaces.device_features.limit_switch_params_setter import LimitSwitchParamsSetter
from thorlabs_xa.interfaces.device_features.load_params import LoadParams
from thorlabs_xa.interfaces.device_features.move import Move
from thorlabs_xa.interfaces.device_features.move_absolute_params import MoveAbsoluteParams
from thorlabs_xa.interfaces.device_features.move_relative_params import MoveRelativeParams
from thorlabs_xa.interfaces.device_features.no_flash_programming import NoFlashProgramming
from thorlabs_xa.interfaces.device_features.persist_params import PersistParams
from thorlabs_xa.interfaces.device_features.position_counter import PositionCounter
from thorlabs_xa.interfaces.device_features.power_params import PowerParams
from thorlabs_xa.interfaces.device_features.profile_mode_params import ProfileModeParams
from thorlabs_xa.interfaces.device_features.rich_response import RichResponse
from thorlabs_xa.interfaces.device_features.settings import Settings
from thorlabs_xa.interfaces.device_features.status_items import StatusItems
from thorlabs_xa.interfaces.device_features.status_mode import StatusMode
from thorlabs_xa.interfaces.device_features.status_request import StatusRequest
from thorlabs_xa.interfaces.device_features.stepper_loop_params import StepperLoopParams
from thorlabs_xa.interfaces.device_features.stepper_status import StepperStatus
from thorlabs_xa.interfaces.device_features.stop import Stop
from thorlabs_xa.interfaces.device_features.trigger_params_for_stepper import TriggerParamsForStepper
from thorlabs_xa.interfaces.device_features.unit_converter import UnitConverter
from thorlabs_xa.interfaces.device_features.universal_status_bits import UniversalStatusBits
from thorlabs_xa.interfaces.device_features.velocity_params import VelocityParams
from thorlabs_xa.interfaces.device_features.yes_flash_programming import YesFlashProgramming

from thorlabs_xa.implementations.device_features.adc_inputs_feature import AdcInputsFeature
from thorlabs_xa.implementations.device_features.bow_index_feature import BowIndexFeature
from thorlabs_xa.implementations.device_features.connected_product_feature import ConnectedProductFeature
from thorlabs_xa.implementations.device_features.digital_output_states_feature import DigitalOutputStatesFeature
from thorlabs_xa.implementations.device_features.disconnect_feature import DisconnectFeature
from thorlabs_xa.implementations.device_features.enable_state_feature import EnableStateFeature
from thorlabs_xa.implementations.device_features.encoder_counter_feature import EncoderCounterFeature
from thorlabs_xa.implementations.device_features.firmware_version_info_feature import FirmwareVersionInfoFeature
from thorlabs_xa.implementations.device_features.general_move_params_feature import GeneralMoveParamsFeature
from thorlabs_xa.implementations.device_features.hardware_info_feature import HardwareInfoFeature
from thorlabs_xa.implementations.device_features.home_feature import HomeFeature
from thorlabs_xa.implementations.device_features.home_params_feature import HomeParamsFeature
from thorlabs_xa.implementations.device_features.identify_feature import IdentifyFeature
from thorlabs_xa.implementations.device_features.jog_params_feature import JogParamsFeature
from thorlabs_xa.implementations.device_features.limit_switch_params_getter_feature import LimitSwitchParamsGetterFeature
from thorlabs_xa.implementations.device_features.limit_switch_params_setter_feature import LimitSwitchParamsSetterFeature
from thorlabs_xa.implementations.device_features.load_params_feature import LoadParamsFeature
from thorlabs_xa.implementations.device_features.move_feature import MoveFeature
from thorlabs_xa.implementations.device_features.move_absolute_params_feature import MoveAbsoluteParamsFeature
from thorlabs_xa.implementations.device_features.move_relative_params_feature import MoveRelativeParamsFeature
from thorlabs_xa.implementations.device_features.no_flash_programming_feature import NoFlashProgrammingFeature
from thorlabs_xa.implementations.device_features.persist_params_feature import PersistParamsFeature
from thorlabs_xa.implementations.device_features.position_counter_feature import PositionCounterFeature
from thorlabs_xa.implementations.device_features.power_params_feature import PowerParamsFeature
from thorlabs_xa.implementations.device_features.profile_mode_params_feature import ProfileModeParamsFeature
from thorlabs_xa.implementations.device_features.rich_response_feature import RichResponseFeature
from thorlabs_xa.implementations.device_features.settings_feature import SettingsFeature
from thorlabs_xa.implementations.device_features.status_items_feature import StatusItemsFeature
from thorlabs_xa.implementations.device_features.status_mode_feature import StatusModeFeature
from thorlabs_xa.implementations.device_features.status_request_feature import StatusRequestFeature
from thorlabs_xa.implementations.device_features.stepper_loop_params_feature import StepperLoopParamsFeature
from thorlabs_xa.implementations.device_features.stepper_status_feature import StepperStatusFeature
from thorlabs_xa.implementations.device_features.stop_feature import StopFeature
from thorlabs_xa.implementations.device_features.trigger_params_for_stepper_feature import TriggerParamsForStepperFeature
from thorlabs_xa.implementations.device_features.unit_converter_feature import UnitConverterFeature
from thorlabs_xa.implementations.device_features.universal_status_bits_feature import UniversalStatusBitsFeature
from thorlabs_xa.implementations.device_features.velocity_params_feature import VelocityParamsFeature
from thorlabs_xa.implementations.device_features.yes_flash_programming_feature import YesFlashProgrammingFeature

from thorlabs_xa.native_sdks.native_functions import NativeFunctions

class Bsc201FeatureGroup(thorlabs_xa.interfaces.device_feature_groups.bsc201_feature_group.Bsc201FeatureGroup):

    def __init__(self, device_handle: int, native_functions: NativeFunctions) -> None:

        self._adc_inputs_feature = AdcInputsFeature(device_handle, native_functions)
        self._bow_index_feature = BowIndexFeature(device_handle, native_functions)
        self._connected_product_feature = ConnectedProductFeature(device_handle, native_functions)
        self._digital_output_states_feature = DigitalOutputStatesFeature(device_handle, native_functions)
        self._disconnect_feature = DisconnectFeature(device_handle, native_functions)
        self._enable_state_feature = EnableStateFeature(device_handle, native_functions)
        self._encoder_counter_feature = EncoderCounterFeature(device_handle, native_functions)
        self._firmware_version_info_feature = FirmwareVersionInfoFeature(device_handle, native_functions)
        self._general_move_params_feature = GeneralMoveParamsFeature(device_handle, native_functions)
        self._hardware_info_feature = HardwareInfoFeature(device_handle, native_functions)
        self._home_feature = HomeFeature(device_handle, native_functions)
        self._home_params_feature = HomeParamsFeature(device_handle, native_functions)
        self._identify_feature = IdentifyFeature(device_handle, native_functions)
        self._jog_params_feature = JogParamsFeature(device_handle, native_functions)
        self._limit_switch_params_getter_feature = LimitSwitchParamsGetterFeature(device_handle, native_functions)
        self._limit_switch_params_setter_feature = LimitSwitchParamsSetterFeature(device_handle, native_functions)
        self._load_params_feature = LoadParamsFeature(device_handle, native_functions)
        self._move_feature = MoveFeature(device_handle, native_functions)
        self._move_absolute_params_feature = MoveAbsoluteParamsFeature(device_handle, native_functions)
        self._move_relative_params_feature = MoveRelativeParamsFeature(device_handle, native_functions)
        self._no_flash_programming_feature = NoFlashProgrammingFeature(device_handle, native_functions)
        self._persist_params_feature = PersistParamsFeature(device_handle, native_functions)
        self._position_counter_feature = PositionCounterFeature(device_handle, native_functions)
        self._power_params_feature = PowerParamsFeature(device_handle, native_functions)
        self._profile_mode_params_feature = ProfileModeParamsFeature(device_handle, native_functions)
        self._rich_response_feature = RichResponseFeature(device_handle, native_functions)
        self._settings_feature = SettingsFeature(device_handle, native_functions)
        self._status_items_feature = StatusItemsFeature(device_handle, native_functions)
        self._status_mode_feature = StatusModeFeature(device_handle, native_functions)
        self._status_request_feature = StatusRequestFeature(device_handle, native_functions)
        self._stepper_loop_params_feature = StepperLoopParamsFeature(device_handle, native_functions)
        self._stepper_status_feature = StepperStatusFeature(device_handle, native_functions)
        self._stop_feature = StopFeature(device_handle, native_functions)
        self._trigger_params_for_stepper_feature = TriggerParamsForStepperFeature(device_handle, native_functions)
        self._unit_converter_feature = UnitConverterFeature(device_handle, native_functions)
        self._universal_status_bits_feature = UniversalStatusBitsFeature(device_handle, native_functions)
        self._velocity_params_feature = VelocityParamsFeature(device_handle, native_functions)
        self._yes_flash_programming_feature = YesFlashProgrammingFeature(device_handle, native_functions)

    @property
    def adc_inputs_feature(self) -> AdcInputs:
        return self._adc_inputs_feature

    @property
    def bow_index_feature(self) -> BowIndex:
        return self._bow_index_feature

    @property
    def connected_product_feature(self) -> ConnectedProduct:
        return self._connected_product_feature

    @property
    def digital_output_states_feature(self) -> DigitalOutputStates:
        return self._digital_output_states_feature

    @property
    def disconnect_feature(self) -> Disconnect:
        return self._disconnect_feature

    @property
    def enable_state_feature(self) -> EnableState:
        return self._enable_state_feature

    @property
    def encoder_counter_feature(self) -> EncoderCounter:
        return self._encoder_counter_feature

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
    def jog_params_feature(self) -> JogParams:
        return self._jog_params_feature

    @property
    def limit_switch_params_getter_feature(self) -> LimitSwitchParamsGetter:
        return self._limit_switch_params_getter_feature

    @property
    def limit_switch_params_setter_feature(self) -> LimitSwitchParamsSetter:
        return self._limit_switch_params_setter_feature

    @property
    def load_params_feature(self) -> LoadParams:
        return self._load_params_feature

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
    def no_flash_programming_feature(self) -> NoFlashProgramming:
        return self._no_flash_programming_feature

    @property
    def persist_params_feature(self) -> PersistParams:
        return self._persist_params_feature

    @property
    def position_counter_feature(self) -> PositionCounter:
        return self._position_counter_feature

    @property
    def power_params_feature(self) -> PowerParams:
        return self._power_params_feature

    @property
    def profile_mode_params_feature(self) -> ProfileModeParams:
        return self._profile_mode_params_feature

    @property
    def rich_response_feature(self) -> RichResponse:
        return self._rich_response_feature

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
    def stepper_loop_params_feature(self) -> StepperLoopParams:
        return self._stepper_loop_params_feature

    @property
    def stepper_status_feature(self) -> StepperStatus:
        return self._stepper_status_feature

    @property
    def stop_feature(self) -> Stop:
        return self._stop_feature

    @property
    def trigger_params_for_stepper_feature(self) -> TriggerParamsForStepper:
        return self._trigger_params_for_stepper_feature

    @property
    def unit_converter_feature(self) -> UnitConverter:
        return self._unit_converter_feature

    @property
    def universal_status_bits_feature(self) -> UniversalStatusBits:
        return self._universal_status_bits_feature

    @property
    def velocity_params_feature(self) -> VelocityParams:
        return self._velocity_params_feature

    @property
    def yes_flash_programming_feature(self) -> YesFlashProgramming:
        return self._yes_flash_programming_feature