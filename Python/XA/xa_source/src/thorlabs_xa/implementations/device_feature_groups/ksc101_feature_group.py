import thorlabs_xa.interfaces.device_feature_groups.ksc101_feature_group

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

from thorlabs_xa.implementations.device_features.av_modes_feature import AvModesFeature
from thorlabs_xa.implementations.device_features.disconnect_feature import DisconnectFeature
from thorlabs_xa.implementations.device_features.enable_state_feature import EnableStateFeature
from thorlabs_xa.implementations.device_features.firmware_version_info_feature import FirmwareVersionInfoFeature
from thorlabs_xa.implementations.device_features.hardware_info_feature import HardwareInfoFeature
from thorlabs_xa.implementations.device_features.identify_feature import IdentifyFeature
from thorlabs_xa.implementations.device_features.kcube_io_trigger_params_feature import KcubeIoTriggerParamsFeature
from thorlabs_xa.implementations.device_features.kcube_mmi_params_feature import KcubeMmiParamsFeature
from thorlabs_xa.implementations.device_features.load_params_feature import LoadParamsFeature
from thorlabs_xa.implementations.device_features.persist_params_feature import PersistParamsFeature
from thorlabs_xa.implementations.device_features.rich_response_feature import RichResponseFeature
from thorlabs_xa.implementations.device_features.settings_feature import SettingsFeature
from thorlabs_xa.implementations.device_features.solenoid_cycle_params_feature import SolenoidCycleParamsFeature
from thorlabs_xa.implementations.device_features.solenoid_interlock_mode_feature import SolenoidInterlockModeFeature
from thorlabs_xa.implementations.device_features.solenoid_operating_mode_feature import SolenoidOperatingModeFeature
from thorlabs_xa.implementations.device_features.solenoid_state_feature import SolenoidStateFeature
from thorlabs_xa.implementations.device_features.solenoid_status_feature import SolenoidStatusFeature
from thorlabs_xa.implementations.device_features.solenoid_status_bits_feature import SolenoidStatusBitsFeature
from thorlabs_xa.implementations.device_features.status_items_feature import StatusItemsFeature
from thorlabs_xa.implementations.device_features.status_mode_feature import StatusModeFeature
from thorlabs_xa.implementations.device_features.status_request_feature import StatusRequestFeature

from thorlabs_xa.native_sdks.native_functions import NativeFunctions

class Ksc101FeatureGroup(thorlabs_xa.interfaces.device_feature_groups.ksc101_feature_group.Ksc101FeatureGroup):

    def __init__(self, device_handle: int, native_functions: NativeFunctions) -> None:

        self._av_modes_feature = AvModesFeature(device_handle, native_functions)
        self._disconnect_feature = DisconnectFeature(device_handle, native_functions)
        self._enable_state_feature = EnableStateFeature(device_handle, native_functions)
        self._firmware_version_info_feature = FirmwareVersionInfoFeature(device_handle, native_functions)
        self._hardware_info_feature = HardwareInfoFeature(device_handle, native_functions)
        self._identify_feature = IdentifyFeature(device_handle, native_functions)
        self._kcube_io_trigger_params_feature = KcubeIoTriggerParamsFeature(device_handle, native_functions)
        self._kcube_mmi_params_feature = KcubeMmiParamsFeature(device_handle, native_functions)
        self._load_params_feature = LoadParamsFeature(device_handle, native_functions)
        self._persist_params_feature = PersistParamsFeature(device_handle, native_functions)
        self._rich_response_feature = RichResponseFeature(device_handle, native_functions)
        self._settings_feature = SettingsFeature(device_handle, native_functions)
        self._solenoid_cycle_params_feature = SolenoidCycleParamsFeature(device_handle, native_functions)
        self._solenoid_interlock_mode_feature = SolenoidInterlockModeFeature(device_handle, native_functions)
        self._solenoid_operating_mode_feature = SolenoidOperatingModeFeature(device_handle, native_functions)
        self._solenoid_state_feature = SolenoidStateFeature(device_handle, native_functions)
        self._solenoid_status_feature = SolenoidStatusFeature(device_handle, native_functions)
        self._solenoid_status_bits_feature = SolenoidStatusBitsFeature(device_handle, native_functions)
        self._status_items_feature = StatusItemsFeature(device_handle, native_functions)
        self._status_mode_feature = StatusModeFeature(device_handle, native_functions)
        self._status_request_feature = StatusRequestFeature(device_handle, native_functions)

    @property
    def av_modes_feature(self) -> AvModes:
        return self._av_modes_feature

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
    def kcube_io_trigger_params_feature(self) -> KcubeIoTriggerParams:
        return self._kcube_io_trigger_params_feature

    @property
    def kcube_mmi_params_feature(self) -> KcubeMmiParams:
        return self._kcube_mmi_params_feature

    @property
    def load_params_feature(self) -> LoadParams:
        return self._load_params_feature

    @property
    def persist_params_feature(self) -> PersistParams:
        return self._persist_params_feature

    @property
    def rich_response_feature(self) -> RichResponse:
        return self._rich_response_feature

    @property
    def settings_feature(self) -> Settings:
        return self._settings_feature

    @property
    def solenoid_cycle_params_feature(self) -> SolenoidCycleParams:
        return self._solenoid_cycle_params_feature

    @property
    def solenoid_interlock_mode_feature(self) -> SolenoidInterlockMode:
        return self._solenoid_interlock_mode_feature

    @property
    def solenoid_operating_mode_feature(self) -> SolenoidOperatingMode:
        return self._solenoid_operating_mode_feature

    @property
    def solenoid_state_feature(self) -> SolenoidState:
        return self._solenoid_state_feature

    @property
    def solenoid_status_feature(self) -> SolenoidStatus:
        return self._solenoid_status_feature

    @property
    def solenoid_status_bits_feature(self) -> SolenoidStatusBits:
        return self._solenoid_status_bits_feature

    @property
    def status_items_feature(self) -> StatusItems:
        return self._status_items_feature

    @property
    def status_mode_feature(self) -> StatusMode:
        return self._status_mode_feature

    @property
    def status_request_feature(self) -> StatusRequest:
        return self._status_request_feature