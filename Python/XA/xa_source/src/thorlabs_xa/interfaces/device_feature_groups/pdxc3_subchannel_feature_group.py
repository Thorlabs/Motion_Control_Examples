from typing import Protocol

from thorlabs_xa.interfaces.device_features.connected_product import ConnectedProduct
from thorlabs_xa.interfaces.device_features.enable_state import EnableState
from thorlabs_xa.interfaces.device_features.home import Home
from thorlabs_xa.interfaces.device_features.load_params import LoadParams
from thorlabs_xa.interfaces.device_features.move import Move
from thorlabs_xa.interfaces.device_features.persist_params import PersistParams
from thorlabs_xa.interfaces.device_features.piezo.position_control_mode import PositionControlMode
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
    def connected_product_feature(self) -> ConnectedProduct: ...

    @property
    def enable_state_feature(self) -> EnableState: ...

    @property
    def home_feature(self) -> Home: ...

    @property
    def load_params_feature(self) -> LoadParams: ...

    @property
    def move_feature(self) -> Move: ...

    @property
    def persist_params_feature(self) -> PersistParams: ...

    @property
    def position_control_mode_feature(self) -> PositionControlMode: ...

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