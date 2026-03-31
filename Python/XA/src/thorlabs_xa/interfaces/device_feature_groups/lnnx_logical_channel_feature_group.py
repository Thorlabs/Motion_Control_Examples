from typing import Protocol

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
from thorlabs_xa.interfaces.device_features.restore_factory_defaults import RestoreFactoryDefaults
from thorlabs_xa.interfaces.device_features.settings import Settings
from thorlabs_xa.interfaces.device_features.status_items import StatusItems
from thorlabs_xa.interfaces.device_features.status_mode import StatusMode
from thorlabs_xa.interfaces.device_features.unit_converter import UnitConverter
from thorlabs_xa.interfaces.device_features.piezo.zero import Zero

class LnnxLogicalChannelFeatureGroup(Protocol):
    
    @property
    def enable_state_feature(self) -> EnableState: ...

    @property
    def firmware_version_info_feature(self) -> FirmwareVersionInfo: ...

    @property
    def hardware_info_feature(self) -> HardwareInfo: ...
    
    @property
    def identify_feature(self) -> Identify: ...

    @property
    def max_output_voltage_params_feature(self) -> MaxOutputVoltageParams: ...

    @property
    def max_travel_feature(self) -> MaxTravel: ...

    @property
    def output_voltage_feature(self) -> OutputVoltage: ...

    @property
    def output_voltage_control_source_params_feature(self) -> OutputVoltageControlSourceParams: ...

    @property
    def piezo_status_feature(self) -> PiezoStatus: ...

    @property
    def piezo_status_bits_feature(self) -> PiezoStatusBits: ...

    @property
    def position_feature(self) -> Position: ...

    @property
    def position_control_mode_feature(self) -> PositionControlMode: ...

    @property
    def restore_factory_defaults_feature(self) -> RestoreFactoryDefaults: ...

    @property
    def settings_feature(self) -> Settings: ...

    @property
    def status_items_feature(self) -> StatusItems: ...

    @property
    def status_mode_feature(self) -> StatusMode: ...

    @property
    def unit_converter_feature(self) -> UnitConverter: ...

    @property
    def zero_feature(self) -> Zero: ...