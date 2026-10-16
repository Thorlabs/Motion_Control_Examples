from typing import Protocol

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

class Kpc101FeatureGroup(Protocol):

    @property
    def connected_product_feature(self) -> ConnectedProduct: ...

    @property
    def digital_output_states_feature(self) -> DigitalOutputStates: ...

    @property
    def disconnect_feature(self) -> Disconnect: ...

    @property
    def enable_state_feature(self) -> EnableState: ...

    @property
    def firmware_version_info_feature(self) -> FirmwareVersionInfo: ...

    @property
    def hardware_version_info_feature(self) -> HardwareInfo: ...

    @property
    def identify_feature(self) -> Identify: ...

    @property
    def kcube_mmi_lock_feature(self) -> KcubeMmiLock: ...

    @property
    def kpc_io_settings_params_feature(self) -> KpcIoSettingsParams: ...

    @property
    def kpc_io_trigger_params_feature(self) -> KpcIoTriggerParams: ...

    @property
    def kpc_mmi_params_feature(self) -> KpcMmiParams: ...

    @property
    def load_params_feature(self) -> LoadParams: ...

    @property
    def max_travel_feature(self) -> MaxTravel: ...

    @property
    def output_voltage_feature(self) -> OutputVoltage: ...

    @property
    def output_voltage_control_source_params_feature(self) -> OutputVoltageControlSourceParams: ...

    @property
    def output_waveform_feature(self) -> OutputWaveform: ...

    @property
    def output_waveform_params_getter_feature(self) -> OutputWaveformParamsGetter: ...

    @property
    def persist_params_feature(self) -> PersistParams: ...

    @property
    def piezo_status_feature(self) -> PiezoStatus: ...

    @property
    def piezo_status_bits_feature(self) -> PiezoStatusBits: ...

    @property
    def position_loop_params_feature(self) -> PositionLoopParams: ...

    @property
    def position_feature(self) -> Position: ...

    @property
    def position_control_mode_feature(self) -> PositionControlMode: ...

    @property
    def restore_factory_defaults_feature(self) -> RestoreFactoryDefaults: ...

    @property
    def rich_response_feature(self) -> RichResponse: ...

    @property
    def settings_feature(self) -> Settings: ...

    @property
    def status_items_feature(self) -> StatusItems: ...

    @property
    def status_request_feature(self) -> StatusRequest: ...

    @property
    def status_mode_feature(self) -> StatusMode: ...

    @property
    def unit_converter_feature(self) -> UnitConverter: ...

    @property
    def zero_feature(self) -> Zero: ...
