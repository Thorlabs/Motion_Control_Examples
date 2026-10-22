from typing import Protocol

from thorlabs_xa.interfaces.device_features.disconnect import Disconnect
from thorlabs_xa.interfaces.device_features.firmware_version_info import FirmwareVersionInfo
from thorlabs_xa.interfaces.device_features.hardware_info import HardwareInfo
from thorlabs_xa.interfaces.device_features.identify import Identify
from thorlabs_xa.interfaces.device_features.load_params import LoadParams
from thorlabs_xa.interfaces.device_features.move_sync_array import MoveSyncArray
from thorlabs_xa.interfaces.device_features.move_sync_params import MoveSyncParams
from thorlabs_xa.interfaces.device_features.move_sync_start import MoveSyncStart
from thorlabs_xa.interfaces.device_features.settings import Settings
from thorlabs_xa.interfaces.device_features.status_mode import StatusMode

class Pdxc3FeatureGroup(Protocol):

    @property
    def disconnect_feature(self) -> Disconnect: ...

    @property
    def firmware_version_info_feature(self) -> FirmwareVersionInfo: ...

    @property
    def hardware_info_feature(self) -> HardwareInfo: ...

    @property
    def identify_feature(self) -> Identify: ...

    @property
    def load_params_feature(self) -> LoadParams: ...

    @property
    def move_sync_array_feature(self) -> MoveSyncArray: ...

    @property
    def move_sync_params_feature(self) -> MoveSyncParams: ...

    @property
    def move_sync_start_feature(self) -> MoveSyncStart: ...

    @property
    def settings_feature(self) -> Settings: ...

    @property
    def status_mode_feature(self) -> StatusMode: ...