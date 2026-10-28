import thorlabs_xa.interfaces.device_feature_groups.pdxc3_feature_group

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

from thorlabs_xa.implementations.device_features.disconnect_feature import DisconnectFeature
from thorlabs_xa.implementations.device_features.firmware_version_info_feature import FirmwareVersionInfoFeature
from thorlabs_xa.implementations.device_features.hardware_info_feature import HardwareInfoFeature
from thorlabs_xa.implementations.device_features.identify_feature import IdentifyFeature
from thorlabs_xa.implementations.device_features.load_params_feature import LoadParamsFeature
from thorlabs_xa.implementations.device_features.move_sync_array_feature import MoveSyncArrayFeature
from thorlabs_xa.implementations.device_features.move_sync_params_feature import MoveSyncParamsFeature
from thorlabs_xa.implementations.device_features.move_sync_start_feature import MoveSyncStartFeature
from thorlabs_xa.implementations.device_features.settings_feature import SettingsFeature
from thorlabs_xa.implementations.device_features.status_mode_feature import StatusModeFeature

from thorlabs_xa.native_sdks.native_functions import NativeFunctions

class Pdxc3FeatureGroup(thorlabs_xa.interfaces.device_feature_groups.pdxc3_feature_group.Pdxc3FeatureGroup):

    def __init__(self, device_handle: int, native_functions: NativeFunctions) -> None:

        self._disconnect_feature = DisconnectFeature(device_handle, native_functions)
        self._firmware_version_info_feature = FirmwareVersionInfoFeature(device_handle, native_functions)
        self._hardware_info_feature = HardwareInfoFeature(device_handle, native_functions)
        self._identify_feature = IdentifyFeature(device_handle, native_functions)
        self._load_params_feature = LoadParamsFeature(device_handle, native_functions)
        self._move_sync_array_feature = MoveSyncArrayFeature(device_handle, native_functions)
        self._move_sync_params_feature = MoveSyncParamsFeature(device_handle, native_functions)
        self._move_sync_start_feature = MoveSyncStartFeature(device_handle, native_functions)
        self._settings_feature = SettingsFeature(device_handle, native_functions)
        self._status_mode_feature = StatusModeFeature(device_handle, native_functions)

    @property
    def disconnect_feature(self) -> Disconnect:
        return self._disconnect_feature

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
    def move_sync_array_feature(self) -> MoveSyncArray:
        return self._move_sync_array_feature

    @property
    def move_sync_params_feature(self) -> MoveSyncParams:
        return self._move_sync_params_feature

    @property
    def move_sync_start_feature(self) -> MoveSyncStart:
        return self._move_sync_start_feature

    @property
    def settings_feature(self) -> Settings:
        return self._settings_feature

    @property
    def status_mode_feature(self) -> StatusMode:
        return self._status_mode_feature