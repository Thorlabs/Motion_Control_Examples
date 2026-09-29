import thorlabs_xa.interfaces.device_feature_groups.kpc101_feature_group

from thorlabs_xa.implementations.device_features.connected_product_feature import ConnectedProductFeature
from thorlabs_xa.implementations.device_features.digital_output_states_feature import DigitalOutputStatesFeature
from thorlabs_xa.implementations.device_features.disconnect_feature import DisconnectFeature
from thorlabs_xa.implementations.device_features.enable_state_feature import EnableStateFeature
from thorlabs_xa.implementations.device_features.firmware_version_info_feature import FirmwareVersionInfoFeature
from thorlabs_xa.implementations.device_features.hardware_info_feature import HardwareInfoFeature
from thorlabs_xa.implementations.device_features.identify_feature import IdentifyFeature
from thorlabs_xa.implementations.device_features.kcube_mmi_lock_feature import KcubeMmiLockFeature
from thorlabs_xa.implementations.device_features.piezo.kpc_io_settings_params_feature import KpcIoSettingsParamsFeature
from thorlabs_xa.implementations.device_features.piezo.kpc_io_trigger_params_feature import KpcIoTriggerParamsFeature
from thorlabs_xa.implementations.device_features.load_params_feature import LoadParamsFeature
from thorlabs_xa.implementations.device_features.persist_params_feature import PersistParamsFeature
from thorlabs_xa.implementations.device_features.piezo.kpc_mmi_params_feature import KpcMmiParamsFeature
from thorlabs_xa.implementations.device_features.piezo.max_travel_feature import MaxTravelFeature
from thorlabs_xa.implementations.device_features.piezo.output_voltage_control_source_params_feature import OutputVoltageControlSourceParamsFeature
from thorlabs_xa.implementations.device_features.piezo.output_voltage_feature import OutputVoltageFeature
from thorlabs_xa.implementations.device_features.piezo.output_waveform_feature import OutputWaveformFeature
from thorlabs_xa.implementations.device_features.piezo.output_waveform_params_getter_feature import OutputWaveformParamsGetterFeature
from thorlabs_xa.implementations.device_features.piezo.piezo_status_bits_feature import PiezoStatusBitsFeature
from thorlabs_xa.implementations.device_features.piezo.piezo_status_feature import PiezoStatusFeature
from thorlabs_xa.implementations.device_features.piezo.position_control_mode_feature import PositionControlModeFeature
from thorlabs_xa.implementations.device_features.piezo.position_feature import PositionFeature
from thorlabs_xa.implementations.device_features.piezo.position_loop_params_feature import PositionLoopParamsFeature
from thorlabs_xa.implementations.device_features.restore_factory_defaults_feature import RestoreFactoryDefaultsFeature
from thorlabs_xa.implementations.device_features.rich_response_feature import RichResponseFeature
from thorlabs_xa.implementations.device_features.settings_feature import SettingsFeature
from thorlabs_xa.implementations.device_features.status_items_feature import StatusItemsFeature
from thorlabs_xa.implementations.device_features.status_mode_feature import StatusModeFeature
from thorlabs_xa.implementations.device_features.status_request_feature import StatusRequestFeature
from thorlabs_xa.implementations.device_features.unit_converter_feature import UnitConverterFeature
from thorlabs_xa.implementations.device_features.piezo.zero_feature import ZeroFeature

from thorlabs_xa.interfaces.device_features.connected_product import ConnectedProduct
from thorlabs_xa.interfaces.device_features.digital_output_states import DigitalOutputStates
from thorlabs_xa.interfaces.device_features.disconnect import Disconnect
from thorlabs_xa.interfaces.device_features.enable_state import EnableState
from thorlabs_xa.interfaces.device_features.firmware_version_info import FirmwareVersionInfo
from thorlabs_xa.interfaces.device_features.hardware_info import HardwareInfo
from thorlabs_xa.interfaces.device_features.identify import Identify
from thorlabs_xa.interfaces.device_features.kcube_mmi_lock import KcubeMmiLock
from thorlabs_xa.interfaces.device_features.load_params import LoadParams
from thorlabs_xa.interfaces.device_features.persist_params import PersistParams
from thorlabs_xa.interfaces.device_features.piezo.kpc_io_settings_params import KpcIoSettingsParams
from thorlabs_xa.interfaces.device_features.piezo.kpc_io_trigger_params import KpcIoTriggerParams
from thorlabs_xa.interfaces.device_features.piezo.kpc_mmi_params import KpcMmiParams
from thorlabs_xa.interfaces.device_features.piezo.max_travel import MaxTravel
from thorlabs_xa.interfaces.device_features.piezo.output_voltage import OutputVoltage
from thorlabs_xa.interfaces.device_features.piezo.output_voltage_control_source_params import OutputVoltageControlSourceParams
from thorlabs_xa.interfaces.device_features.piezo.output_waveform import OutputWaveform
from thorlabs_xa.interfaces.device_features.piezo.output_waveform_params_getter import OutputWaveformParamsGetter
from thorlabs_xa.interfaces.device_features.piezo.piezo_status import PiezoStatus
from thorlabs_xa.interfaces.device_features.piezo.piezo_status_bits import PiezoStatusBits
from thorlabs_xa.interfaces.device_features.piezo.position import Position
from thorlabs_xa.interfaces.device_features.piezo.position_control_mode import PositionControlMode
from thorlabs_xa.interfaces.device_features.piezo.position_loop_params import PositionLoopParams
from thorlabs_xa.interfaces.device_features.piezo.zero import Zero
from thorlabs_xa.interfaces.device_features.restore_factory_defaults import RestoreFactoryDefaults
from thorlabs_xa.interfaces.device_features.rich_response import RichResponse
from thorlabs_xa.interfaces.device_features.settings import Settings
from thorlabs_xa.interfaces.device_features.status_items import StatusItems
from thorlabs_xa.interfaces.device_features.status_mode import StatusMode
from thorlabs_xa.interfaces.device_features.status_request import StatusRequest
from thorlabs_xa.interfaces.device_features.unit_converter import UnitConverter

from thorlabs_xa.native_sdks.native_functions import NativeFunctions

class Kpc101FeatureGroup(thorlabs_xa.interfaces.device_feature_groups.kpc101_feature_group.Kpc101FeatureGroup):

    def __init__(self, device_handle: int, native_functions: NativeFunctions) -> None:

        self._connected_product_feature = ConnectedProductFeature(device_handle, native_functions)
        self._digital_output_states_feature = DigitalOutputStatesFeature(device_handle, native_functions)
        self._disconnect_feature = DisconnectFeature(device_handle, native_functions)
        self._enable_state_feature = EnableStateFeature(device_handle, native_functions)
        self._firmware_version_info_feature = FirmwareVersionInfoFeature(device_handle, native_functions)
        self._hardware_info_feature = HardwareInfoFeature(device_handle, native_functions)
        self._identify_feature = IdentifyFeature(device_handle, native_functions)
        self._kcube_mmi_lock_feature = KcubeMmiLockFeature(device_handle, native_functions)
        self._kpc_io_settings_params_feature = KpcIoSettingsParamsFeature(device_handle, native_functions)
        self._kpc_io_trigger_params_feature = KpcIoTriggerParamsFeature(device_handle, native_functions)
        self._kpc_mmi_params_feature = KpcMmiParamsFeature(device_handle, native_functions)
        self._load_params_feature = LoadParamsFeature(device_handle, native_functions)
        self._max_travel_feature = MaxTravelFeature(device_handle, native_functions)
        self._output_voltage_feature = OutputVoltageFeature(device_handle, native_functions)
        self._output_voltage_control_source_params_feature = OutputVoltageControlSourceParamsFeature(device_handle, native_functions)
        self._output_waveform_feature = OutputWaveformFeature(device_handle, native_functions)
        self._output_waveform_params_getter_feature = OutputWaveformParamsGetterFeature(device_handle, native_functions)
        self._persist_params_feature = PersistParamsFeature(device_handle, native_functions)
        self._piezo_status_feature = PiezoStatusFeature(device_handle, native_functions)
        self._piezo_status_bits_feature = PiezoStatusBitsFeature(device_handle, native_functions)
        self._position_loop_params_feature = PositionLoopParamsFeature(device_handle, native_functions)
        self._position_feature = PositionFeature(device_handle, native_functions)
        self._position_control_mode_feature = PositionControlModeFeature(device_handle, native_functions)
        self._restore_factory_defaults_feature = RestoreFactoryDefaultsFeature(device_handle, native_functions)
        self._rich_response_feature = RichResponseFeature(device_handle, native_functions)
        self._settings_feature = SettingsFeature(device_handle, native_functions)
        self._status_items_feature = StatusItemsFeature(device_handle, native_functions)
        self._status_request_feature = StatusRequestFeature(device_handle, native_functions)
        self._set_status_mode_feature = StatusModeFeature(device_handle, native_functions)
        self._unit_converter_feature = UnitConverterFeature(device_handle, native_functions)
        self._zero_feature = ZeroFeature(device_handle, native_functions)

    @property
    def connected_product_feature(self) -> ConnectedProduct:
        return self._connected_product_feature

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
    def hardware_version_info_feature(self) -> HardwareInfo:
        return self._hardware_info_feature

    @property
    def identify_feature(self) -> Identify:
        return self._identify_feature

    @property
    def kcube_mmi_lock_feature(self) -> KcubeMmiLock:
        return self._kcube_mmi_lock_feature

    @property
    def kpc_io_settings_params_feature(self) -> KpcIoSettingsParams:
        return self._kpc_io_settings_params_feature

    @property
    def kpc_io_trigger_params_feature(self) -> KpcIoTriggerParams:
        return self._kpc_io_trigger_params_feature

    @property
    def kpc_mmi_params_feature(self) -> KpcMmiParams:
        return self._kpc_mmi_params_feature

    @property
    def load_params_feature(self) -> LoadParams:
        return self._load_params_feature

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
    def output_waveform_params_getter_feature(self) -> OutputWaveformParamsGetter:
        return self._output_waveform_params_getter_feature

    @property
    def persist_params_feature(self) -> PersistParams:
        return self._persist_params_feature

    @property
    def piezo_status_feature(self) -> PiezoStatus:
        return self._piezo_status_feature

    @property
    def piezo_status_bits_feature(self) -> PiezoStatusBits:
        return self._piezo_status_bits_feature

    @property
    def position_loop_params_feature(self) -> PositionLoopParams:
        return self._position_loop_params_feature

    @property
    def position_feature(self) -> Position:
        return self._position_feature

    @property
    def position_control_mode_feature(self) -> PositionControlMode:
        return self._position_control_mode_feature

    @property
    def restore_factory_defaults_feature(self) -> RestoreFactoryDefaults:
        return self._restore_factory_defaults_feature

    @property
    def rich_response_feature(self) -> RichResponse:
        return self._rich_response_feature
    
    @property
    def settings_feature(self) -> Settings:
        return self._settings_feature

    @property
    def status_items_feature(self) -> StatusItems:
        return self._status_items_feature

    @property
    def set_status_mode_feature(self) -> StatusMode:
        return self._set_status_mode_feature

    @property
    def status_request_feature(self) -> StatusRequest:
        return self._status_request_feature

    @property
    def unit_converter_feature(self) -> UnitConverter:
        return self._unit_converter_feature

    @property
    def zero_feature(self) -> Zero:
        return self._zero_feature