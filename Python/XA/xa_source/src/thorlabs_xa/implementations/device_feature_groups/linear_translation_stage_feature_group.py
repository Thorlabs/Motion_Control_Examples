import thorlabs_xa.interfaces.device_feature_groups.linear_translation_stage_feature_group

from thorlabs_xa.implementations.device_features.button_params_feature import ButtonParamsFeature
from thorlabs_xa.implementations.device_features.calibration_feature import CalibrationFeature
from thorlabs_xa.implementations.device_features.connected_product_feature import ConnectedProductFeature
from thorlabs_xa.implementations.device_features.disconnect_feature import DisconnectFeature
from thorlabs_xa.implementations.device_features.enable_state_feature import EnableStateFeature
from thorlabs_xa.implementations.device_features.firmware_version_info_feature import FirmwareVersionInfoFeature
from thorlabs_xa.implementations.device_features.general_move_params_feature import GeneralMoveParamsFeature
from thorlabs_xa.implementations.device_features.hardware_info_feature import HardwareInfoFeature
from thorlabs_xa.implementations.device_features.home_feature import HomeFeature
from thorlabs_xa.implementations.device_features.home_params_feature import HomeParamsFeature
from thorlabs_xa.implementations.device_features.identify_feature import IdentifyFeature
from thorlabs_xa.implementations.device_features.jog_params_feature import JogParamsFeature
from thorlabs_xa.implementations.device_features.limit_switch_params_getter_feature import LimitSwitchParamsGetterFeature
from thorlabs_xa.implementations.device_features.load_params_feature import LoadParamsFeature
from thorlabs_xa.implementations.device_features.move_feature import MoveFeature
from thorlabs_xa.implementations.device_features.move_absolute_params_feature import MoveAbsoluteParamsFeature
from thorlabs_xa.implementations.device_features.move_relative_params_feature import MoveRelativeParamsFeature
from thorlabs_xa.implementations.device_features.persist_params_feature import PersistParamsFeature
from thorlabs_xa.implementations.device_features.position_counter_feature import PositionCounterFeature
from thorlabs_xa.implementations.device_features.potentiometer_params_feature import PotentiometerParamsFeature
from thorlabs_xa.implementations.device_features.status_mode_feature import StatusModeFeature
from thorlabs_xa.implementations.device_features.settings_feature import SettingsFeature
from thorlabs_xa.implementations.device_features.status_items_feature import StatusItemsFeature
from thorlabs_xa.implementations.device_features.status_request_feature import StatusRequestFeature
from thorlabs_xa.implementations.device_features.stepper_status_feature import StepperStatusFeature
from thorlabs_xa.implementations.device_features.stop_feature import StopFeature
from thorlabs_xa.implementations.device_features.unit_converter_feature import UnitConverterFeature
from thorlabs_xa.implementations.device_features.universal_status_feature import UniversalStatusFeature
from thorlabs_xa.implementations.device_features.velocity_params_feature import VelocityParamsFeature

from thorlabs_xa.interfaces.device_features.button_params import ButtonParams
from thorlabs_xa.interfaces.device_features.calibration import Calibration
from thorlabs_xa.interfaces.device_features.connected_product import ConnectedProduct
from thorlabs_xa.interfaces.device_features.disconnect import Disconnect
from thorlabs_xa.interfaces.device_features.enable_state import EnableState
from thorlabs_xa.interfaces.device_features.firmware_version_info import FirmwareVersionInfo
from thorlabs_xa.interfaces.device_features.general_move_params import GeneralMoveParams
from thorlabs_xa.interfaces.device_features.hardware_info import HardwareInfo
from thorlabs_xa.interfaces.device_features.home import Home
from thorlabs_xa.interfaces.device_features.home_params import HomeParams
from thorlabs_xa.interfaces.device_features.identify import Identify
from thorlabs_xa.interfaces.device_features.jog_params import JogParams
from thorlabs_xa.interfaces.device_features.limit_switch_params_getter import LimitSwitchParamsGetter
from thorlabs_xa.interfaces.device_features.load_params import LoadParams
from thorlabs_xa.interfaces.device_features.move import Move
from thorlabs_xa.interfaces.device_features.move_absolute_params import MoveAbsoluteParams
from thorlabs_xa.interfaces.device_features.move_relative_params import MoveRelativeParams
from thorlabs_xa.interfaces.device_features.persist_params import PersistParams
from thorlabs_xa.interfaces.device_features.potentiometer_params import PotentiometerParams
from thorlabs_xa.interfaces.device_features.position_counter import PositionCounter
from thorlabs_xa.interfaces.device_features.status_mode import StatusMode
from thorlabs_xa.interfaces.device_features.settings import Settings
from thorlabs_xa.interfaces.device_features.status_items import StatusItems
from thorlabs_xa.interfaces.device_features.status_request import StatusRequest
from thorlabs_xa.interfaces.device_features.stepper_status import StepperStatus
from thorlabs_xa.interfaces.device_features.stop import Stop
from thorlabs_xa.interfaces.device_features.unit_converter import UnitConverter
from thorlabs_xa.interfaces.device_features.universal_status import UniversalStatus
from thorlabs_xa.interfaces.device_features.velocity_params import VelocityParams

from thorlabs_xa.native_sdks.native_functions import NativeFunctions

class LinearTranslationStageFeatureGroup(thorlabs_xa.interfaces.device_feature_groups.linear_translation_stage_feature_group.LinearTranslationStageFeatureGroup):

    def __init__(self, device_handle: int, native_functions: NativeFunctions) -> None:
        self._button_params_feature = ButtonParamsFeature(device_handle, native_functions)
        self._calibration_feature = CalibrationFeature(device_handle, native_functions)
        self._connected_product_feature = ConnectedProductFeature(device_handle, native_functions)
        self._disconnect_feature = DisconnectFeature(device_handle, native_functions)
        self._enable_state_feature = EnableStateFeature(device_handle, native_functions)
        self._firmware_version_info_feature = FirmwareVersionInfoFeature(device_handle, native_functions)
        self._general_move_params = GeneralMoveParamsFeature(device_handle, native_functions)
        self._hardware_info_feature = HardwareInfoFeature(device_handle, native_functions)
        self._home_feature = HomeFeature(device_handle, native_functions)
        self._home_params_feature = HomeParamsFeature(device_handle, native_functions)
        self._identify_feature = IdentifyFeature(device_handle, native_functions)
        self._jog_params_feature = JogParamsFeature(device_handle, native_functions)
        self._limit_switch_params_getter_feature = LimitSwitchParamsGetterFeature(device_handle, native_functions)
        self._load_params_feature = LoadParamsFeature(device_handle, native_functions)
        self._move_feature = MoveFeature(device_handle, native_functions)
        self._move_absolute_params_feature = MoveAbsoluteParamsFeature(device_handle, native_functions)
        self._move_relative_params_feature = MoveRelativeParamsFeature(device_handle, native_functions)
        self._persist_params_feature = PersistParamsFeature(device_handle, native_functions)
        self._potentiometer_params_feature = PotentiometerParamsFeature(device_handle, native_functions)
        self._position_counter_feature = PositionCounterFeature(device_handle, native_functions)
        self._set_status_mode_feature = StatusModeFeature(device_handle, native_functions)
        self._settings_feature = SettingsFeature(device_handle, native_functions)
        self._status_items_feature = StatusItemsFeature(device_handle, native_functions)
        self._status_request_feature = StatusRequestFeature(device_handle, native_functions)
        self._stepper_status_feature = StepperStatusFeature(device_handle, native_functions)
        self._stop_feature = StopFeature(device_handle, native_functions)
        self._unit_converter_feature = UnitConverterFeature(device_handle, native_functions)
        self._universal_status_feature = UniversalStatusFeature(device_handle, native_functions)
        self._velocity_params_feature = VelocityParamsFeature(device_handle, native_functions)

    @property
    def button_params_feature(self) -> ButtonParams:
        return self._button_params_feature
    
    @property
    def calibration_feature(self) -> Calibration:
        return self._calibration_feature

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
    def firmware_version_info_feature(self) -> FirmwareVersionInfo:
        return self.firmware_version_info_feature
    
    @property
    def general_move_params_feature(self) -> GeneralMoveParams:
        return self._general_move_params
    
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
    def persist_params_feature(self) -> PersistParams:
        return self._persist_params_feature
    
    @property 
    def potentiometer_params_feature(self) -> PotentiometerParams:
        return self._potentiometer_params_feature
    
    @property
    def position_counter_feature(self) -> PositionCounter:
        return self._position_counter_feature
    
    @property
    def settings_feature(self) -> Settings:
        return self._settings_feature
    
    @property
    def status_items_feature(self) -> StatusItems:
        return self._status_items_feature
    
    @property
    def set_status_mode_feature(self) -> StatusMode:
        return self._set_status_mode_feature
    
    @property
    def status_request_feature(self) -> StatusRequest:
        return self._status_request_feature
    
    @property
    def stepper_status_feature(self) -> StepperStatus:
        return self._stepper_status_feature
    
    @property 
    def stop_feature(self) -> Stop:
        return self._stop_feature
    
    @property
    def unit_converter_feature(self) -> UnitConverter:
        return self._unit_converter_feature
    
    @property
    def universal_status_feature(self) -> UniversalStatus:
        return self._universal_status_feature
    
    @property
    def velocity_params_feature(self) -> VelocityParams:
        return self._velocity_params_feature

