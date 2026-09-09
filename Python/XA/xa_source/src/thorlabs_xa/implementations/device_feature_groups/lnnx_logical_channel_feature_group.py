from thorlabs_xa.native_sdks.native_functions import NativeFunctions

from thorlabs_xa.implementations.device_features.connected_product_feature import ConnectedProductFeature
from thorlabs_xa.implementations.device_features.disconnect_feature import DisconnectFeature
from thorlabs_xa.implementations.device_features.enable_state_feature import EnableStateFeature
from thorlabs_xa.implementations.device_features.firmware_version_info_feature import FirmwareVersionInfoFeature
from thorlabs_xa.implementations.device_features.hardware_info_feature import HardwareInfoFeature
from thorlabs_xa.implementations.device_features.identify_feature import IdentifyFeature
from thorlabs_xa.implementations.device_features.piezo.max_output_voltage_params_feature import MaxOutputVoltageParamsFeature
from thorlabs_xa.implementations.device_features.piezo.max_travel_feature import MaxTravelFeature
from thorlabs_xa.implementations.device_features.piezo.output_voltage_feature import OutputVoltageFeature
from thorlabs_xa.implementations.device_features.piezo.output_voltage_control_source_params_feature import OutputVoltageControlSourceParamsFeature
from thorlabs_xa.implementations.device_features.piezo.piezo_status_feature import PiezoStatusFeature
from thorlabs_xa.implementations.device_features.piezo.piezo_status_bits_feature import PiezoStatusBitsFeature
from thorlabs_xa.implementations.device_features.piezo.position_feature import PositionFeature
from thorlabs_xa.implementations.device_features.piezo.position_control_mode_feature import PositionControlModeFeature
from thorlabs_xa.implementations.device_features.piezo.position_loop_params_feature import PositionLoopParamsFeature
from thorlabs_xa.implementations.device_features.restore_factory_defaults_feature import RestoreFactoryDefaultsFeature
from thorlabs_xa.implementations.device_features.settings_feature import SettingsFeature
from thorlabs_xa.implementations.device_features.piezo.stage_info_params_feature import StageInfoParamsFeature
from thorlabs_xa.implementations.device_features.status_items_feature import StatusItemsFeature
from thorlabs_xa.implementations.device_features.status_mode_feature import StatusModeFeature
from thorlabs_xa.implementations.device_features.unit_converter_feature import UnitConverterFeature
from thorlabs_xa.implementations.device_features.piezo.zero_feature import ZeroFeature

from thorlabs_xa.interfaces.device_features.connected_product import ConnectedProduct
from thorlabs_xa.interfaces.device_features.disconnect import Disconnect
from thorlabs_xa.interfaces.device_features.enable_state import EnableState
from thorlabs_xa.interfaces.device_features.firmware_version_info import FirmwareVersionInfo
from thorlabs_xa.interfaces.device_features.hardware_info import HardwareInfo
from thorlabs_xa.interfaces.device_features.identify import Identify
from thorlabs_xa.interfaces.device_features.piezo.max_output_voltage_params import MaxOutputVoltageParams
from thorlabs_xa.interfaces.device_features.piezo.max_travel import MaxTravel
from thorlabs_xa.interfaces.device_features.piezo.output_voltage import OutputVoltage
from thorlabs_xa.interfaces.device_features.piezo.output_voltage_control_source_params import OutputVoltageControlSourceParams
from thorlabs_xa.interfaces.device_features.piezo.piezo_status import PiezoStatus
from thorlabs_xa.interfaces.device_features.piezo.piezo_status_bits import PiezoStatusBits
from thorlabs_xa.interfaces.device_features.piezo.position import Position
from thorlabs_xa.interfaces.device_features.piezo.position_control_mode import PositionControlMode
from thorlabs_xa.interfaces.device_features.piezo.position_loop_params import PositionLoopParams
from thorlabs_xa.interfaces.device_features.restore_factory_defaults import RestoreFactoryDefaults
from thorlabs_xa.interfaces.device_features.settings import Settings
from thorlabs_xa.interfaces.device_features.piezo.stage_info_params import StageInfoParams
from thorlabs_xa.interfaces.device_features.status_items import StatusItems
from thorlabs_xa.interfaces.device_features.status_mode import StatusMode
from thorlabs_xa.interfaces.device_features.unit_converter import UnitConverter
from thorlabs_xa.interfaces.device_features.piezo.zero import Zero

import thorlabs_xa.interfaces.device_feature_groups.lnnx_logical_channel_feature_group

class LnnxLogicalChannelFeatureGroup(thorlabs_xa.interfaces.device_feature_groups.lnnx_logical_channel_feature_group.LnnxLogicalChannelFeatureGroup):

    def __init__(self, device_handle: int, native_functions: NativeFunctions) -> None:

        self._connected_product_feature : ConnectedProduct = ConnectedProductFeature(device_handle, native_functions)
        self._disconnect_feature : Disconnect = DisconnectFeature(device_handle, native_functions)
        self._enable_state_feature : EnableState = EnableStateFeature(device_handle, native_functions)
        self._firmware_version_info_feature : FirmwareVersionInfo = FirmwareVersionInfoFeature(device_handle, native_functions)
        self._hardware_info_feature : HardwareInfo = HardwareInfoFeature(device_handle, native_functions)
        self._identify_feature : Identify = IdentifyFeature(device_handle, native_functions)
        self._max_output_voltage_params_feature : MaxOutputVoltageParams = MaxOutputVoltageParamsFeature(device_handle, native_functions)
        self._max_travel_feature : MaxTravel = MaxTravelFeature(device_handle, native_functions)
        self._output_voltage_feature : OutputVoltage = OutputVoltageFeature(device_handle, native_functions)
        self._output_voltage_control_source_params_feature : OutputVoltageControlSourceParams = OutputVoltageControlSourceParamsFeature(device_handle, native_functions)
        self._piezo_status_feature : PiezoStatus = PiezoStatusFeature(device_handle, native_functions)
        self._piezo_status_bits_feature : PiezoStatusBits = PiezoStatusBitsFeature(device_handle, native_functions)
        self._position_feature : Position = PositionFeature(device_handle, native_functions)
        self._position_control_mode_feature : PositionControlMode = PositionControlModeFeature(device_handle, native_functions)
        self._position_loop_params_feature : PositionLoopParams = PositionLoopParamsFeature(device_handle, native_functions)
        self._restore_factory_defaults_feature : RestoreFactoryDefaults = RestoreFactoryDefaultsFeature(device_handle, native_functions)
        self._settings_feature : Settings = SettingsFeature(device_handle, native_functions)
        self._stage_info_params_feature : StageInfoParamsFeature = StageInfoParamsFeature(device_handle, native_functions)
        self._status_items_feature : StatusItems = StatusItemsFeature(device_handle, native_functions)
        self._set_status_mode_feature : StatusMode = StatusModeFeature(device_handle, native_functions)
        self._unit_converter_feature : UnitConverter = UnitConverterFeature(device_handle, native_functions)
        self._zero_feature : Zero = ZeroFeature(device_handle, native_functions)

    @property
    def connected_product_feature(self) -> ConnectedProduct:

        return self._connected_product_feature

    @property
    def disconnect_product_feature(self) -> Disconnect:

        return self._disconnect_feature

    @property
    def enable_state_feature(self) -> EnableState:

        return self._enable_state_feature

    @property
    def firmware_version_info_feature(self) -> FirmwareVersionInfo:

        return self._firmware_version_info_feature

    @property
    def hardware_info_feature(self) -> HardwareInfo:

        return self._hardware_info_feature

    @property
    def identify_feature(self) -> Identify:

        return self._identify_feature

    @property
    def max_output_voltage_params_feature(self) -> MaxOutputVoltageParams:

        return self._max_output_voltage_params_feature

    @property
    def max_travel_feature(self) -> MaxTravel:

        return self._max_travel_feature

    @property
    def output_voltage_feature(self) -> OutputVoltage:

        return self._output_voltage_feature

    @property
    def output_voltage_control_source_params_feature(self) -> OutputVoltageControlSourceParams:

        return self._output_voltage_control_source_params_feature

    @property
    def piezo_status_feature(self) -> PiezoStatus:

        return self._piezo_status_feature

    @property
    def piezo_status_bits_feature(self) -> PiezoStatusBits:

        return self._piezo_status_bits_feature

    @property
    def position_feature(self) -> Position:

        return self._position_feature

    @property
    def position_control_mode_feature(self) -> PositionControlMode:

        return self._position_control_mode_feature
    
    @property
    def position_loop_params_feature(self) -> PositionLoopParams:

        return self._position_loop_params_feature

    @property
    def restore_factory_defaults_feature(self) -> RestoreFactoryDefaults:

        return self._restore_factory_defaults_feature
    
    @property
    def settings_feature(self) -> Settings:

        return self._settings_feature
    
    @property
    def stage_info_params_feature(self) -> StageInfoParams:
        
        return self._stage_info_params_feature

    @property
    def status_items_feature(self) -> StatusItems:

        return self._status_items_feature

    @property
    def set_status_mode_feature(self) -> StatusMode:

        return self._set_status_mode_feature

    @property
    def unit_converter_feature(self) -> UnitConverter:

        return self._unit_converter_feature

    @property
    def zero_feature(self) -> Zero:

        return self._zero_feature