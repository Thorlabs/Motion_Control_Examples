from typing import Protocol

from thorlabs_xa.interfaces.device_features.av_modes import AvModes
from thorlabs_xa.interfaces.device_features.disconnect import Disconnect
from thorlabs_xa.interfaces.device_features.enable_state import EnableState
from thorlabs_xa.interfaces.device_features.firmware_version_info import FirmwareVersionInfo
from thorlabs_xa.interfaces.device_features.hardware_info import HardwareInfo
from thorlabs_xa.interfaces.device_features.identify import Identify
from thorlabs_xa.interfaces.device_features.kcube_io_trigger_params import KcubeIoTriggerParams
from thorlabs_xa.interfaces.device_features.kcube_mmi_params import KcubeMmiParams
from thorlabs_xa.interfaces.device_features.load_params import LoadParams
from thorlabs_xa.interfaces.device_features.persist_params import PersistParams
from thorlabs_xa.interfaces.device_features.rich_response import RichResponse
from thorlabs_xa.interfaces.device_features.settings import Settings
from thorlabs_xa.interfaces.device_features.solenoid_cycle_params import SolenoidCycleParams
from thorlabs_xa.interfaces.device_features.solenoid_interlock_mode import SolenoidInterlockMode
from thorlabs_xa.interfaces.device_features.solenoid_operating_mode import SolenoidOperatingMode
from thorlabs_xa.interfaces.device_features.solenoid_state import SolenoidState
from thorlabs_xa.interfaces.device_features.solenoid_status import SolenoidStatus
from thorlabs_xa.interfaces.device_features.solenoid_status_bits import SolenoidStatusBits
from thorlabs_xa.interfaces.device_features.status_items import StatusItems
from thorlabs_xa.interfaces.device_features.status_mode import StatusMode
from thorlabs_xa.interfaces.device_features.status_request import StatusRequest

class Ksc101FeatureGroup(Protocol):

    @property
    def av_modes_feature(self) -> AvModes: ...

    @property
    def disconnect_feature(self) -> Disconnect: ...

    @property
    def enable_state_feature(self) -> EnableState: ...

    @property
    def firmware_version_info_feature(self) -> FirmwareVersionInfo: ...

    @property
    def hardware_info_feature(self) -> HardwareInfo: ...

    @property
    def identify_feature(self) -> Identify: ...

    @property
    def kcube_io_trigger_params_feature(self) -> KcubeIoTriggerParams: ...

    @property
    def kcube_mmi_params_feature(self) -> KcubeMmiParams: ...

    @property
    def load_params_feature(self) -> LoadParams: ...

    @property
    def persist_params_feature(self) -> PersistParams: ...

    @property
    def rich_response_feature(self) -> RichResponse: ...

    @property
    def settings_feature(self) -> Settings: ...

    @property
    def solenoid_cycle_params_feature(self) -> SolenoidCycleParams: ...

    @property
    def solenoid_interlock_mode_feature(self) -> SolenoidInterlockMode: ...

    @property
    def solenoid_operating_mode_feature(self) -> SolenoidOperatingMode: ...

    @property
    def solenoid_state_feature(self) -> SolenoidState: ...

    @property
    def solenoid_status_feature(self) -> SolenoidStatus: ...

    @property
    def solenoid_status_bits_feature(self) -> SolenoidStatusBits: ...

    @property
    def status_items_feature(self) -> StatusItems: ...

    @property
    def status_mode_feature(self) -> StatusMode: ...

    @property
    def status_request_feature(self) -> StatusRequest: ...