from typing import Protocol

from thorlabs_xa.interfaces.device_features.aux_io_configuration_params import AuxIoConfigurationParams
from thorlabs_xa.interfaces.device_features.disconnect import Disconnect
from thorlabs_xa.interfaces.device_features.firmware_version_info import FirmwareVersionInfo
from thorlabs_xa.interfaces.device_features.hardware_info import HardwareInfo
from thorlabs_xa.interfaces.device_features.io_configuration_params import IoConfigurationParams
from thorlabs_xa.interfaces.device_features.load_params import LoadParams
from thorlabs_xa.interfaces.device_features.move_sync_array import MoveSyncArray
from thorlabs_xa.interfaces.device_features.move_sync_params import MoveSyncParams
from thorlabs_xa.interfaces.device_features.move_sync_start import MoveSyncStart
from thorlabs_xa.interfaces.device_features.rack_bay_occupied_state import RackBayOccupiedState
from thorlabs_xa.interfaces.device_features.settings import Settings

class UmcxFeatureGroup(Protocol):

    @property
    def aux_io_configuration_params_feature(self) -> AuxIoConfigurationParams: ...

    @property
    def disconnect_feature(self) -> Disconnect: ...

    @property
    def firmware_version_info_feature(self) -> FirmwareVersionInfo: ...

    @property
    def hardware_info_feature(self) -> HardwareInfo: ...

    @property
    def io_configuration_params_feature(self) -> IoConfigurationParams: ...

    @property
    def load_params_feature(self) -> LoadParams: ...

    @property
    def move_sync_array_feature(self) -> MoveSyncArray: ...

    @property
    def move_sync_params_feature(self) -> MoveSyncParams: ...

    @property
    def move_sync_start_feature(self) -> MoveSyncStart: ...

    @property
    def rack_bay_occupied_state_feature(self) -> RackBayOccupiedState: ...

    @property
    def settings_feature(self) -> Settings: ...