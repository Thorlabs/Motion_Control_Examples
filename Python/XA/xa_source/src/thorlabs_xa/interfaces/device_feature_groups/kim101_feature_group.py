from typing import Protocol

from thorlabs_xa.interfaces.device_features.disconnect import Disconnect
from thorlabs_xa.interfaces.device_features.firmware_version_info import FirmwareVersionInfo
from thorlabs_xa.interfaces.device_features.hardware_info import HardwareInfo
from thorlabs_xa.interfaces.device_features.piezo_inertial_motor.kcube_channel_enable import KcubeChannelEnable
from thorlabs_xa.interfaces.device_features.piezo_inertial_motor.stage_select_params import StageSelectParams
from thorlabs_xa.interfaces.device_features.load_params import LoadParams
from thorlabs_xa.interfaces.device_features.settings import Settings
from thorlabs_xa.interfaces.device_features.status_mode import StatusMode

class Kim101FeatureGroup(Protocol):

    @property
    def disconnect_feature(self) -> Disconnect: ...

    @property
    def firmware_version_info_feature(self) -> FirmwareVersionInfo: ...

    @property
    def hardware_info_feature(self) -> HardwareInfo: ...

    @property
    def kcube_channel_enable_feature(self) -> KcubeChannelEnable: ...

    @property
    def load_params_feature(self) -> LoadParams: ...

    @property
    def settings_feature(self) -> Settings: ...

    @property
    def stage_select_params_feature(self) -> StageSelectParams: ...

    @property
    def status_mode_feature(self) -> StatusMode: ...