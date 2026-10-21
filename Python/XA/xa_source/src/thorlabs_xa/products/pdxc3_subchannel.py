from typing import List

from thorlabs_xa.interfaces.device_feature_groups.pdxc3_subchannel_feature_group import Pdxc3SubchannelFeatureGroup

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

from thorlabs_xa.native_sdks.native_functions import NativeFunctions

from thorlabs_xa.shared.enums import TLMC_EnableState, TLMC_MoveMode, TLMC_OperatingMode, TLMC_ParameterGroupId, TLMC_PZ_PositionControlMode, TLMC_ScaleType, TLMC_SettingStringFormat, TLMC_StatusItemId, TLMC_StopMode, TLMC_Unit
from thorlabs_xa.shared.params import TLMC_ConnectedProductInfo, TLMC_RichResponse, TLMC_Setting, TLMC_StageAxisParams, TLMC_StatusItem
from thorlabs_xa.shared.subchannel import Subchannel

class Pdxc3Subchannel(Subchannel,
        ConnectedProduct,
        EnableState,
        Home,
        LoadParams,
        Move,
        PersistParams,
        PositionControlMode,
        RichResponse,
        Settings,
        StageAxisParams,
        StatusItems,
        StatusMode,
        StatusRequest,
        Stop,
        UnitConverter):

    def __init__(self, subchannel_handle: int, subchannel_number: int, feature_group: Pdxc3SubchannelFeatureGroup, native_functions: NativeFunctions) -> None:

        super().__init__(subchannel_handle, subchannel_number, native_functions)

        self.feature_group = feature_group

    def get_connected_product_info(self) -> TLMC_ConnectedProductInfo:

        return self.feature_group.connected_product_feature.get_connected_product_info()

    def get_supported_connected_products(self) -> List[str]:

        return self.feature_group.connected_product_feature.get_supported_connected_products()

    def set_connected_product(self, product_name: str) -> None:

        self.feature_group.connected_product_feature.set_connected_product(product_name)

    def set_connected_product_info(self, product_info: TLMC_ConnectedProductInfo) -> None:

        self.feature_group.connected_product_feature.set_connected_product_info(product_info)

    def get_enable_state(self, max_wait_in_milliseconds: int) -> TLMC_EnableState:

        return self.feature_group.enable_state_feature.get_enable_state(max_wait_in_milliseconds)

    def set_enable_state(self, enable_state: TLMC_EnableState) -> None:

        self.feature_group.enable_state_feature.set_enable_state(enable_state)

    def home(self, max_wait_in_milliseconds: int) -> None:

        self.feature_group.home_feature.home(max_wait_in_milliseconds)

    def load_params(self) -> None:

        self.feature_group.load_params_feature.load_params()

    def move(self, move_mode: TLMC_MoveMode, params: int, max_wait_in_milliseconds: int) -> None:

        self.feature_group.move_feature.move(move_mode, params, max_wait_in_milliseconds)

    def persist_params(self, parameter_group_id: TLMC_ParameterGroupId) -> None:

        self.feature_group.persist_params_feature.persist_params(parameter_group_id)

    def get_position_control_mode(self, max_wait_in_milliseconds: int) -> TLMC_PZ_PositionControlMode:

        return self.feature_group.position_control_mode_feature.get_position_control_mode(max_wait_in_milliseconds)

    def set_position_control_mode(self, control_mode: TLMC_PZ_PositionControlMode, max_wait_in_milliseconds: int) -> None:

        self.feature_group.position_control_mode_feature.set_position_control_mode(control_mode, max_wait_in_milliseconds)

    def get_rich_response(self) -> TLMC_RichResponse:

        return self.feature_group.rich_response_feature.get_rich_response()

    def get_setting(self, settings_name: str, max_wait_in_milliseconds: int) -> TLMC_Setting:

        return self.feature_group.settings_feature.get_setting(settings_name, max_wait_in_milliseconds)

    def get_setting_discrete_values(self, settings_name: str) -> str:

        return self.feature_group.settings_feature.get_setting_discrete_values(settings_name)

    def get_settings(self, setting_string_format: TLMC_SettingStringFormat, include_read_only_items: bool) -> str:

        return self.feature_group.settings_feature.get_settings(setting_string_format, include_read_only_items)

    def get_settings_items(self) -> List[TLMC_Setting]:

        return self.feature_group.settings_feature.get_settings_items()

    def set_settings(self, settings: str) -> None:

        self.feature_group.settings_feature.set_settings(settings)

    def get_stage_axis_params(self, max_wait_in_milliseconds: int) -> TLMC_StageAxisParams:

        return self.feature_group.stage_axis_params_feature.get_stage_axis_params(max_wait_in_milliseconds)

    def set_stage_axis_params(self, params: TLMC_StageAxisParams) -> None:

        self.feature_group.stage_axis_params_feature.set_stage_axis_params(params)

    def get_status_item(self, status_item_id: TLMC_StatusItemId) -> TLMC_StatusItem:

        return self.feature_group.status_items_feature.get_status_item(status_item_id)

    def get_status_item_count(self) -> int:

        return self.feature_group.status_items_feature.get_status_item_count()

    def get_status_items(self, start_index: int, number_of_items: int) -> List[TLMC_StatusItem]:

        return self.feature_group.status_items_feature.get_status_items(start_index, number_of_items)

    def set_status_mode(self, operating_mode: TLMC_OperatingMode) -> None:

        self.feature_group.status_mode_feature.set_status_mode(operating_mode)

    def request_status(self, max_wait_in_milliseconds: int) -> None:

        self.feature_group.status_request_feature.request_status(max_wait_in_milliseconds)

    def stop(self, stop_mode: TLMC_StopMode, max_wait_in_milliseconds: int) -> None:

        self.feature_group.stop_feature.stop(stop_mode, max_wait_in_milliseconds)

    def convert_from_device_units_to_physical(self, scale_type: TLMC_ScaleType, device_value: int) -> tuple[float, TLMC_Unit]:

        return self.feature_group.unit_converter_feature.convert_from_device_units_to_physical(scale_type, device_value)

    def convert_from_physical_to_device(self, scale_type: TLMC_ScaleType, unit: TLMC_Unit, physical_value: int) -> int:

        return self.feature_group.unit_converter_feature.convert_from_physical_to_device(scale_type, unit, physical_value)

    def get_preferred_physical_unit(self, scale_type: TLMC_ScaleType) -> TLMC_Unit:

        return self.feature_group.unit_converter_feature.get_preferred_physical_unit(scale_type)