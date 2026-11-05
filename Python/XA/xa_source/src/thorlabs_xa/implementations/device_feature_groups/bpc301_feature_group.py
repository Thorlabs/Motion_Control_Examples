import thorlabs_xa.interfaces.device_feature_groups.bpc301_feature_group

from thorlabs_xa.interfaces.device_features.digital_output_states import DigitalOutputStates
from thorlabs_xa.interfaces.device_features.disconnect import Disconnect
from thorlabs_xa.interfaces.device_features.enable_state import EnableState
from thorlabs_xa.interfaces.device_features.firmware_version_info import FirmwareVersionInfo
from thorlabs_xa.interfaces.device_features.hardware_info import HardwareInfo
from thorlabs_xa.interfaces.device_features.identify import Identify
from thorlabs_xa.interfaces.device_features.load_params import LoadParams
from thorlabs_xa.interfaces.device_features.piezo.max_output_voltage_params import MaxOutputVoltageParams
from thorlabs_xa.interfaces.device_features.piezo.max_travel import MaxTravel
from thorlabs_xa.interfaces.device_features.piezo.output_voltage import OutputVoltage
from thorlabs_xa.interfaces.device_features.piezo.output_voltage_control_source_params import OutputVoltageControlSourceParams
from thorlabs_xa.interfaces.device_features.piezo.output_waveform import OutputWaveform
from thorlabs_xa.interfaces.device_features.piezo.piezo_status import PiezoStatus
from thorlabs_xa.interfaces.device_features.piezo.piezo_status_bits import PiezoStatusBits
from thorlabs_xa.interfaces.device_features.piezo.position import Position
from thorlabs_xa.interfaces.device_features.piezo.position_control_mode import PositionControlMode
from thorlabs_xa.interfaces.device_features.piezo.position_loop_params import PositionLoopParams
from thorlabs_xa.interfaces.device_features.restore_factory_defaults import RestoreFactoryDefaults
from thorlabs_xa.interfaces.device_features.settings import Settings
from thorlabs_xa.interfaces.device_features.piezo.slew_rate_params import SlewRateParams
from thorlabs_xa.interfaces.device_features.status_items import StatusItems
from thorlabs_xa.interfaces.device_features.status_mode import StatusMode
from thorlabs_xa.interfaces.device_features.unit_converter import UnitConverter
from thorlabs_xa.interfaces.device_features.piezo.zero import Zero

from thorlabs_xa.implementations.device_features.digital_output_states_feature import DigitalOutputStatesFeature
from thorlabs_xa.implementations.device_features.disconnect_feature import DisconnectFeature
from thorlabs_xa.implementations.device_features.enable_state_feature import EnableStateFeature
from thorlabs_xa.implementations.device_features.firmware_version_info_feature import FirmwareVersionInfoFeature
from thorlabs_xa.implementations.device_features.hardware_info_feature import HardwareInfoFeature
from thorlabs_xa.implementations.device_features.identify_feature import IdentifyFeature
from thorlabs_xa.implementations.device_features.load_params_feature import LoadParamsFeature
from thorlabs_xa.implementations.device_features.piezo.max_output_voltage_params_feature import MaxOutputVoltageParamsFeature
from thorlabs_xa.implementations.device_features.piezo.max_travel_feature import MaxTravelFeature
from thorlabs_xa.implementations.device_features.piezo.output_voltage_feature import OutputVoltageFeature
from thorlabs_xa.implementations.device_features.piezo.output_voltage_control_source_params_feature import OutputVoltageControlSourceParamsFeature
from thorlabs_xa.implementations.device_features.piezo.output_waveform_feature import OutputWaveformFeature
from thorlabs_xa.implementations.device_features.piezo.piezo_status_feature import PiezoStatusFeature
from thorlabs_xa.implementations.device_features.piezo.piezo_status_bits_feature import PiezoStatusBitsFeature
from thorlabs_xa.implementations.device_features.piezo.position_feature import PositionFeature
from thorlabs_xa.implementations.device_features.piezo.position_control_mode_feature import PositionControlModeFeature
from thorlabs_xa.implementations.device_features.piezo.position_loop_params_feature import PositionLoopParamsFeature
from thorlabs_xa.implementations.device_features.restore_factory_defaults_feature import RestoreFactoryDefaultsFeature
from thorlabs_xa.implementations.device_features.settings_feature import SettingsFeature
from thorlabs_xa.implementations.device_features.piezo.slew_rate_params_feature import SlewRateParamsFeature
from thorlabs_xa.implementations.device_features.status_items_feature import StatusItemsFeature
from thorlabs_xa.implementations.device_features.status_mode_feature import StatusModeFeature
from thorlabs_xa.implementations.device_features.unit_converter_feature import UnitConverterFeature
from thorlabs_xa.implementations.device_features.piezo.zero_feature import ZeroFeature

from thorlabs_xa.native_sdks.native_functions import NativeFunctions

class Bpc301FeatureGroup(thorlabs_xa.interfaces.device_feature_groups.bpc301_feature_group.Bpc301FeatureGroup):

    def __init__(self, device_handle: int, native_functions: NativeFunctions) -> None:

        self._digital_output_states_feature = DigitalOutputStatesFeature(device_handle, native_functions)
        self._disconnect_feature = DisconnectFeature(device_handle, native_functions)
        self._enable_state_feature = EnableStateFeature(device_handle, native_functions)
        self._firmware_version_info_feature = FirmwareVersionInfoFeature(device_handle, native_functions)
        self._hardware_info_feature = HardwareInfoFeature(device_handle, native_functions)
        self._identify_feature = IdentifyFeature(device_handle, native_functions)
        self._load_params_feature = LoadParamsFeature(device_handle, native_functions)
        self._max_output_voltage_params_feature = MaxOutputVoltageParamsFeature(device_handle, native_functions)
        self._max_travel_feature = MaxTravelFeature(device_handle, native_functions)
        self._output_voltage_feature = OutputVoltageFeature(device_handle, native_functions)
        self._output_voltage_control_source_params_feature = OutputVoltageControlSourceParamsFeature(device_handle, native_functions)
        self._output_waveform_feature = OutputWaveformFeature(device_handle, native_functions)
        self._piezo_status_feature = PiezoStatusFeature(device_handle, native_functions)
        self._piezo_status_bits_feature = PiezoStatusBitsFeature(device_handle, native_functions)
        self._position_feature = PositionFeature(device_handle, native_functions)
        self._position_control_mode_feature = PositionControlModeFeature(device_handle, native_functions)
        self._position_loop_params_feature = PositionLoopParamsFeature(device_handle, native_functions)
        self._restore_factory_defaults_feature = RestoreFactoryDefaultsFeature(device_handle, native_functions)
        self._settings_feature = SettingsFeature(device_handle, native_functions)
        self._slew_rate_params_feature = SlewRateParamsFeature(device_handle, native_functions)
        self._status_items_feature = StatusItemsFeature(device_handle, native_functions)
        self._status_mode_feature = StatusModeFeature(device_handle, native_functions)
        self._unit_converter_feature = UnitConverterFeature(device_handle, native_functions)
        self._zero_feature = ZeroFeature(device_handle, native_functions)

    @property
    def digital_output_states_feature(self) -> DigitalOutputStates:
        return self._digital_output_states_feature

    @property
    def disconnect_feature(self) -> Disconnect:
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
    def load_params_feature(self) -> LoadParams:
        return self._load_params_feature

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
    def output_waveform_feature(self) -> OutputWaveform:
        return self._output_waveform_feature

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
    def slew_rate_params_feature(self) -> SlewRateParams:
        return self._slew_rate_params_feature

    @property
    def status_items_feature(self) -> StatusItems:
        return self._status_items_feature

    @property
    def status_mode_feature(self) -> StatusMode:
        return self._status_mode_feature

    @property
    def unit_converter_feature(self) -> UnitConverter:
        return self._unit_converter_feature

    @property
    def zero_feature(self) -> Zero:
        return self._zero_feature