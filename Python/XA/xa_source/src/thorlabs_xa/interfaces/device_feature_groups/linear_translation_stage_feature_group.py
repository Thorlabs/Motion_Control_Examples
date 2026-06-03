from typing import Protocol

from thorlabs_xa.interfaces.device_features.button_params import ButtonParams
from thorlabs_xa.interfaces.device_features.calibration import Calibration
from thorlabs_xa.interfaces.device_features.connected_product import ConnectedProduct
from thorlabs_xa.interfaces.device_features.disconnect import Disconnect
from thorlabs_xa.interfaces.device_features.enable_state import EnableState
from thorlabs_xa.interfaces.device_features.firmware_version_info import FirmwareVersionInfo
from thorlabs_xa.interfaces.device_features.hardware_info import HardwareInfo
from thorlabs_xa.interfaces.device_features.general_move_params import GeneralMoveParams
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
from thorlabs_xa.interfaces.device_features.stop import Stop
from thorlabs_xa.interfaces.device_features.unit_converter import UnitConverter
from thorlabs_xa.interfaces.device_features.stepper_status import StepperStatus
from thorlabs_xa.interfaces.device_features.universal_status import UniversalStatus
from thorlabs_xa.interfaces.device_features.velocity_params import VelocityParams

class LinearTranslationStageFeatureGroup(Protocol):

    @property
    def button_params_feature(self) -> ButtonParams: ...

    @property
    def calibration_feature(self) -> Calibration: ...

    @property
    def connected_product_feature(self) -> ConnectedProduct: ...

    @property
    def disconnect_feature(self) -> Disconnect: ...

    @property
    def enable_state_feature(self) -> EnableState: ...

    @property
    def firmware_version_info_feature(self) -> FirmwareVersionInfo: ...

    @property
    def hardware_info_feature(self) -> HardwareInfo: ...

    @property
    def general_move_params_feature(self) -> GeneralMoveParams: ...

    @property
    def home_feature(self) -> Home: ...

    @property
    def home_params_feature(self) -> HomeParams: ...

    @property
    def identify_feature(self) -> Identify: ...

    @property
    def jog_params_feature(self) -> JogParams: ...

    @property
    def limit_switch_params_getter_feature(self) -> LimitSwitchParamsGetter: ...

    @property
    def load_params_feature(self) -> LoadParams: ...

    @property
    def move_feature(self) -> Move: ...

    @property
    def move_absolute_params_feature(self) -> MoveAbsoluteParams: ...

    @property
    def move_relative_params_feature(self) -> MoveRelativeParams: ...

    @property
    def persist_params_feature(self) -> PersistParams: ...

    @property
    def potentiometer_params_feature(self) -> PotentiometerParams: ...

    @property
    def position_counter_feature(self) -> PositionCounter: ...

    @property
    def settings_feature(self) -> Settings: ...

    @property
    def status_items_feature(self) -> StatusItems: ...

    @property
    def set_status_mode_feature(self) -> StatusMode: ...

    @property
    def status_request_feature(self) -> StatusRequest: ...

    @property
    def stop_feature(self) -> Stop: ...

    @property
    def unit_converter_feature(self) -> UnitConverter: ...

    @property
    def stepper_status_feature(self) -> StepperStatus: ...

    @property
    def universal_status_feature(self) -> UniversalStatus: ...

    @property
    def velocity_params_feature(self) -> VelocityParams: ...

