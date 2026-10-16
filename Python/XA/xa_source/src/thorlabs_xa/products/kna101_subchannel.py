from typing import List

from thorlabs_xa.interfaces.device_feature_groups.kna101_subchannel_feature_group import Kna101SubchannelFeatureGroup
from thorlabs_xa.native_sdks.native_functions import NativeFunctions
from thorlabs_xa.shared.enums import TLMC_PZ_PositionControlMode, TLMC_SettingStringFormat
from thorlabs_xa.shared.params import TLMC_PZ_PositionLoopParams, TLMC_Setting
from thorlabs_xa.shared.subchannel import Subchannel


class Kna101Subchannel(Subchannel):

    def __init__(self, subchannel_handle: int, subchannel_number: int, native_functions: NativeFunctions,
                 feature_group: Kna101SubchannelFeatureGroup) -> None:

        super().__init__(subchannel_handle, subchannel_number, native_functions)

        self.feature_group = feature_group

    # LoadParams

    def load_params(self) -> None:
        self.feature_group.load_params_feature.load_params()

    # PositionControlMode

    def get_position_control_mode(self, max_wait_in_milliseconds: int) -> TLMC_PZ_PositionControlMode:
        return self.feature_group.position_control_mode_feature.get_position_control_mode(max_wait_in_milliseconds)

    def set_position_control_mode(self, control_mode: TLMC_PZ_PositionControlMode, max_wait_in_milliseconds: int) -> None:
        self.feature_group.position_control_mode_feature.set_position_control_mode(control_mode, max_wait_in_milliseconds)

    # PositionLoopParams

    def get_position_loop_params(self, max_wait_in_milliseconds: int) -> TLMC_PZ_PositionLoopParams:
        return self.feature_group.position_loop_params_feature.get_position_loop_params(max_wait_in_milliseconds)

    def set_position_loop_params(self, params: TLMC_PZ_PositionLoopParams) -> None:
        self.feature_group.position_loop_params_feature.set_position_loop_params(params)

    # Settings

    def get_setting(self, settings_name: str, max_wait_in_milliseconds: int) -> TLMC_Setting:
        return self.feature_group.settings_feature.get_setting(settings_name, max_wait_in_milliseconds)

    def get_settings_items(self) -> List[TLMC_Setting]:
        return self.feature_group.settings_feature.get_settings_items()

    def get_settings(self, setting_string_format: TLMC_SettingStringFormat, include_read_only_items: bool) -> str:
        return self.feature_group.settings_feature.get_settings(setting_string_format, include_read_only_items)

    def set_settings(self, settings: str) -> None:
        self.feature_group.settings_feature.set_settings(settings)

    def get_setting_discrete_values(self, settings_name: str) -> str:
        return self.feature_group.settings_feature.get_setting_discrete_values(settings_name)
