from typing import Protocol

from thorlabs_xa.interfaces.device_features.analog_monitor_configuration_params import AnalogMonitorConfigurationParams
from thorlabs_xa.interfaces.device_features.aux_io_configuration_params import AuxIoConfigurationParams
from thorlabs_xa.interfaces.device_features.digital_input_states import DigitalInputStates
from thorlabs_xa.interfaces.device_features.digital_output_states import DigitalOutputStates
from thorlabs_xa.interfaces.device_features.disconnect import Disconnect
from thorlabs_xa.interfaces.device_features.firmware_version_info import FirmwareVersionInfo
from thorlabs_xa.interfaces.device_features.hardware_info import HardwareInfo
from thorlabs_xa.interfaces.device_features.io_configuration_params import IoConfigurationParams
from thorlabs_xa.interfaces.device_features.lcd_display_params import LcdDisplayParams
from thorlabs_xa.interfaces.device_features.load_params import LoadParams
from thorlabs_xa.interfaces.device_features.move_sync_array import MoveSyncArray
from thorlabs_xa.interfaces.device_features.move_sync_params import MoveSyncParams
from thorlabs_xa.interfaces.device_features.move_sync_start import MoveSyncStart
from thorlabs_xa.interfaces.device_features.persist_params import PersistParams
from thorlabs_xa.interfaces.device_features.rack_identify import RackIdentify
from thorlabs_xa.interfaces.device_features.rack_bay_occupied_state import RackBayOccupiedState
from thorlabs_xa.interfaces.device_features.rack_identify import RackIdentify
from thorlabs_xa.interfaces.device_features.settings import Settings

class Bbd30xFeatureGroup(Protocol):

    @property
    def analog_monitor_configuration_params_feature(self) -> AnalogMonitorConfigurationParams: ...

    @property
    def aux_io_configuration_params_feature(self) -> AuxIoConfigurationParams: ...

    @property
    def digital_input_states_feature(self) -> DigitalInputStates: ...

    @property
    def digital_output_states_feature(self) -> DigitalOutputStates: ...

    @property
    def disconnect_feature(self) -> Disconnect: ...

    @property
    def firmware_version_info_feature(self) -> FirmwareVersionInfo: ...

    @property
    def hardware_info_feature(self) -> HardwareInfo: ...

    @property
    def io_configuration_params_feature(self) -> IoConfigurationParams: ...

    @property
    def lcd_display_params_feature(self) -> LcdDisplayParams: ...

    @property
    def load_params_feature(self) -> LoadParams: ...

    @property
    def move_sync_array_feature(self) -> MoveSyncArray: ...

    @property
    def move_sync_params_feature(self) -> MoveSyncParams: ...

    @property
    def move_sync_start_feature(self) -> MoveSyncStart: ...

    @property
    def persist_params_feature(self) -> PersistParams: ...

    @property
    def rack_bay_occupied_state_feature(self) -> RackBayOccupiedState: ...

    @property
    def rack_identify_feature(self) -> RackIdentify: ...

    @property
    def settings_feature(self) -> Settings: ...