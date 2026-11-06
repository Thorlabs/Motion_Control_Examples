from typing import Protocol

from thorlabs_xa.interfaces.device_features.digital_output_states import DigitalOutputStates
from thorlabs_xa.interfaces.device_features.disconnect import Disconnect
from thorlabs_xa.interfaces.device_features.firmware_version_info import FirmwareVersionInfo
from thorlabs_xa.interfaces.device_features.hardware_info import HardwareInfo
from thorlabs_xa.interfaces.device_features.rack_identify import RackIdentify
from thorlabs_xa.interfaces.device_features.load_params import LoadParams
from thorlabs_xa.interfaces.device_features.rack_bay_occupied_state import RackBayOccupiedState
from thorlabs_xa.interfaces.device_features.settings import Settings

class Bpc30xFeatureGroup(Protocol):

    @property
    def digital_output_states_feature(self) -> DigitalOutputStates: ...

    @property
    def disconnect_feature(self) -> Disconnect: ...

    @property
    def firmware_version_info_feature(self) -> FirmwareVersionInfo: ...

    @property
    def hardware_info_feature(self) -> HardwareInfo: ...

    @property
    def load_params_feature(self) -> LoadParams: ...
    
    @property
    def rack_identify_feature(self) -> RackIdentify: ...

    @property
    def rack_bay_occupied_state_feature(self) -> RackBayOccupiedState: ...

    @property
    def settings_feature(self) -> Settings: ...