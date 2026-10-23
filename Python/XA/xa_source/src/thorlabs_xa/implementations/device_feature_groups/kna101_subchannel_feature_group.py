import thorlabs_xa.interfaces.device_feature_groups.kna101_subchannel_feature_group

from thorlabs_xa.implementations.device_features.load_params_feature import LoadParamsFeature
from thorlabs_xa.implementations.device_features.piezo.position_control_mode_feature import PositionControlModeFeature
from thorlabs_xa.implementations.device_features.piezo.position_loop_params_feature import PositionLoopParamsFeature
from thorlabs_xa.implementations.device_features.settings_feature import SettingsFeature
from thorlabs_xa.interfaces.device_features.load_params import LoadParams
from thorlabs_xa.interfaces.device_features.piezo.position_control_mode import PositionControlMode
from thorlabs_xa.interfaces.device_features.piezo.position_loop_params import PositionLoopParams
from thorlabs_xa.interfaces.device_features.settings import Settings
from thorlabs_xa.native_sdks.native_functions import NativeFunctions


class Kna101SubchannelFeatureGroup(thorlabs_xa.interfaces.device_feature_groups.kna101_subchannel_feature_group.Kna101SubchannelFeatureGroup):

    def __init__(self, subchannel_handle: int, native_functions: NativeFunctions) -> None:

        self._load_params_feature = LoadParamsFeature(subchannel_handle, native_functions)
        self._position_control_mode_feature = PositionControlModeFeature(subchannel_handle, native_functions)
        self._position_loop_params_feature = PositionLoopParamsFeature(subchannel_handle, native_functions)
        self._settings_feature = SettingsFeature(subchannel_handle, native_functions)

    @property
    def load_params_feature(self) -> LoadParams:
        return self._load_params_feature

    @property
    def position_control_mode_feature(self) -> PositionControlMode:
        return self._position_control_mode_feature

    @property
    def position_loop_params_feature(self) -> PositionLoopParams:
        return self._position_loop_params_feature

    @property
    def settings_feature(self) -> Settings:
        return self._settings_feature
