from typing import Protocol

from thorlabs_xa.interfaces.device_features.load_params import LoadParams
from thorlabs_xa.interfaces.device_features.piezo.position_control_mode import PositionControlMode
from thorlabs_xa.interfaces.device_features.piezo.position_loop_params import PositionLoopParams
from thorlabs_xa.interfaces.device_features.settings import Settings


class Kna101SubchannelFeatureGroup(Protocol):

    @property
    def load_params_feature(self) -> LoadParams: ...

    @property
    def position_control_mode_feature(self) -> PositionControlMode: ...

    @property
    def position_loop_params_feature(self) -> PositionLoopParams: ...

    @property
    def settings_feature(self) -> Settings: ...
