from typing import List

from thorlabs_xa.interfaces.device_feature_groups.linear_translation_stage_feature_group import LinearTranslationStageFeatureGroup
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
from thorlabs_xa.shared.device import Device
from thorlabs_xa.shared.enums import TLMC_CalibrationState, TLMC_EnableState, TLMC_MoveMode, TLMC_OperatingMode, TLMC_ParameterGroupId, TLMC_ScaleType, TLMC_SettingStringFormat, TLMC_StatusItemId, TLMC_StopMode, TLMC_Unit 
from thorlabs_xa.shared.params import TLMC_ButtonParams, TLMC_ConnectedProductInfo, TLMC_DeviceInfo, TLMC_FirmwareVersion, TLMC_GeneralMoveParams, TLMC_HardwareInfo, TLMC_HomeParams,TLMC_JogParams,TLMC_LimitSwitchParams,TLMC_MoveAbsoluteParams, TLMC_MoveRelativeParams, TLMC_PotentiometerParams,TLMC_StepperStatus, TLMC_Setting, TLMC_StatusItem, TLMC_UniversalStatus, TLMC_VelocityParams

class LinearTranslationStage(Device,
                          ButtonParams,
                          Calibration,
                          ConnectedProduct,
                          Disconnect,
                          EnableState,
                          FirmwareVersionInfo,
                          GeneralMoveParams,
                          HardwareInfo,
                          Home,
                          HomeParams,
                          Identify,
                          JogParams,
                          LimitSwitchParamsGetter,
                          LoadParams,
                          Move,
                          MoveAbsoluteParams,
                          MoveRelativeParams,
                          PersistParams,
                          PotentiometerParams,
                          PositionCounter,
                          StatusMode,
                          Settings,
                          StatusItems,
                          StatusRequest,
                          StepperStatus,
                          Stop,
                          UnitConverter,
                          UniversalStatus,
                          VelocityParams):
    """
    Thorlabs Long travel stage control.
    """
    def __init__(self, device_handle: int, device_info: TLMC_DeviceInfo, feature_group: LinearTranslationStageFeatureGroup, native_functions: NativeFunctions) -> None:
        
        super().__init__(device_handle, device_info, native_functions)

        self.feature_group = feature_group
    
    def get_button_params(self, max_wait_in_milliseconds: int) -> TLMC_ButtonParams:
        return self.feature_group.button_params_feature.get_button_params(max_wait_in_milliseconds)
    
    def set_button_params(self, params: TLMC_ButtonParams) -> None:
        self.feature_group.button_params_feature.set_button_params(params)
    
    def get_calibration_state(self, max_wait_in_milliseconds: int) -> TLMC_CalibrationState:
        return self.feature_group.calibration_feature.get_calibration_state(max_wait_in_milliseconds)
    
    def activate(self) -> None:
        self.feature_group.calibration_feature.activate()
    
    def deactivate(self):
        self.feature_group.calibration_feature.deactivate()

    def get_connected_product_info(self) -> TLMC_ConnectedProductInfo:
        return self.feature_group.connected_product_feature.get_connected_product_info()
    
    def get_supported_connected_products(self) -> List[str]:
        return self.feature_group.connected_product_feature.get_supported_connected_products()
    
    def set_connected_product(self, product_name: str) -> None:
        self.feature_group.connected_product_feature.set_connected_product(product_name)
    
    def set_connected_product_info(self, product_info: TLMC_ConnectedProductInfo) -> None:
        self.feature_group.connected_product_feature.set_connected_product_info(product_info)

    def disconnect(self) -> None:
        self.feature_group.disconnect_feature.disconnect()

    def get_enable_state(self, max_wait_in_milliseconds: int) -> TLMC_EnableState:
        return self.feature_group.enable_state_feature.get_enable_state(max_wait_in_milliseconds)
    
    def set_enable_state(self, enable_state: TLMC_EnableState) -> None:
        self.feature_group.enable_state_feature.set_enable_state(enable_state)

    def get_firmware_version_info(self, max_wait_in_milliseconds: int) -> tuple [TLMC_FirmwareVersion, TLMC_FirmwareVersion]:
        return self.feature_group.firmware_version_info_feature.get_firmware_version_info(max_wait_in_milliseconds)
    
    def get_general_move_params(self, max_wait_in_milliseconds: int) -> TLMC_GeneralMoveParams:
        return self.feature_group.general_move_params_feature.get_general_move_params(max_wait_in_milliseconds)
    
    def set_general_move_params(self, params: TLMC_GeneralMoveParams):
        self.feature_group.general_move_params_feature.set_general_move_params(params)

    def get_hardware_info(self, max_wait_in_milliseconds: int) -> TLMC_HardwareInfo:
        return self.feature_group.hardware_info_feature.get_hardware_info(max_wait_in_milliseconds)
    
    def home(self, max_wait_in_milliseconds: int) -> None:
        self.feature_group.home_feature.home(max_wait_in_milliseconds)

    def get_home_params(self, max_wait_in_milliseconds: int) -> TLMC_HomeParams:
        return self.feature_group.home_params_feature.get_home_params(max_wait_in_milliseconds)
    
    def set_home_params(self, params: TLMC_HomeParams) -> None:
        self.feature_group.home_params_feature.set_home_params(params)

    def identify(self) -> None:
        self.feature_group.identify_feature.identify()
    
    def get_jog_params(self, max_wait_in_milliseconds: int) -> TLMC_JogParams:
        return self.feature_group.jog_params_feature.get_jog_params(max_wait_in_milliseconds)
    
    def set_jog_params(self, params: TLMC_JogParams) -> None:
        self.feature_group.jog_params_feature.set_jog_params(params)

    def get_limit_switch_params(self, max_wait_in_milliseconds: int) -> TLMC_LimitSwitchParams:
        return self.feature_group.limit_switch_params_getter_feature.get_limit_switch_params(max_wait_in_milliseconds)
        
    def load_params(self) -> None:
        self.feature_group.load_params_feature.load_params()

    def move(self, move_mode: TLMC_MoveMode, params: int, max_wait_in_milliseconds: int):
        self.feature_group.move_feature.move(move_mode, params, max_wait_in_milliseconds)

    def get_move_absolute_params(self, max_wait_in_milliseconds: int) -> TLMC_MoveAbsoluteParams:
        return self.feature_group.move_absolute_params_feature.get_move_absolute_params(max_wait_in_milliseconds)
    
    def set_move_absolute_params(self, params: TLMC_MoveAbsoluteParams) -> None:
        self.feature_group.move_absolute_params_feature.set_move_absolute_params(params)
    
    def get_move_relative_params(self, max_wait_in_milliseconds: int) -> TLMC_MoveRelativeParams:
        return self.feature_group.move_relative_params_feature.get_move_relative_params(max_wait_in_milliseconds)
    
    def set_move_relative_params(self, params: TLMC_MoveRelativeParams) -> None:
        self.feature_group.move_relative_params_feature.set_move_relative_params(params)
    
    def persist_params(self, parameter_group_id: TLMC_ParameterGroupId) -> None:
        self.feature_group.persist_params_feature.persist_params(parameter_group_id)
    
    def get_potentiometer_params(self, max_wait_in_milliseconds: int) -> TLMC_PotentiometerParams:
        return self.feature_group.potentiometer_params_feature.get_potentiometer_params(max_wait_in_milliseconds)
    
    def set_potentiometer_params(self, params: TLMC_PotentiometerParams):
        self.feature_group.potentiometer_params_feature.set_potentiometer_params(params)
    
    def get_position_counter(self, max_wait_in_milliseconds: int) -> int:
        return self.feature_group.position_counter_feature.get_position_counter(max_wait_in_milliseconds)

    def set_position_counter(self, new_position_counter: int) -> None:
        self.feature_group.position_counter_feature.set_position_counter(new_position_counter)
    
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

    def get_status_item(self, status_item_id: TLMC_StatusItemId) -> TLMC_StatusItem:
        return self.feature_group.status_items_feature.get_status_item(status_item_id)
    
    def get_status_item_count(self) -> int:
        return self.feature_group.status_items_feature.get_status_item_count()
    
    def get_status_items(self, start_index: int, number_of_items: int) -> List[TLMC_StatusItem]:
        return self.feature_group.status_items_feature.get_status_items(start_index, number_of_items)
    
    def set_status_mode(self, operating_mode: TLMC_OperatingMode) -> None:
        return self.feature_group.set_status_mode_feature.set_status_mode(operating_mode)
    
    def get_stepper_status(self, max_wait_in_milliseconds: int) -> TLMC_StepperStatus:
        return self.feature_group.stepper_status_feature.get_stepper_status(max_wait_in_milliseconds)
    
    def stop(self, stop_mode: TLMC_StopMode, max_wait_in_milliseconds : int) -> None:
        return self.feature_group.stop_feature.stop(stop_mode, max_wait_in_milliseconds)
    
    def request_status(self, max_wait_in_milliseconds: int) -> None:
        return self.feature_group.status_request_feature.request_status(max_wait_in_milliseconds)
    
    def convert_from_device_units_to_physical(self, scale_type: TLMC_ScaleType, device_value: int) -> tuple [float, TLMC_Unit]:
        return self.feature_group.unit_converter_feature.convert_from_device_units_to_physical(scale_type, device_value)
    
    def convert_from_physical_to_device(self, scale_type: TLMC_ScaleType, unit: TLMC_Unit, physical_value: int) -> int:
        return self.feature_group.unit_converter_feature.convert_from_physical_to_device(scale_type, unit, physical_value)

    def get_preferred_physical_unit(self, scale_type: TLMC_ScaleType) -> TLMC_Unit:
        return self.feature_group.unit_converter_feature.get_preferred_physical_unit(scale_type)
    
    def get_universal_status(self, max_wait_in_milliseconds: int) -> TLMC_UniversalStatus:
        return self.feature_group.universal_status_feature.get_universal_status(max_wait_in_milliseconds)
    
    def get_velocity_params(self, max_wait_in_milliseconds: int) -> TLMC_VelocityParams:
        return self.feature_group.velocity_params_feature.get_velocity_params(max_wait_in_milliseconds)
    
    def set_velocity_params(self, params: TLMC_VelocityParams) -> None:
        return self.feature_group.velocity_params_feature.set_velocity_params(params)