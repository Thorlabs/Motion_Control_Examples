import thorlabs_xa.interfaces.device_feature_groups.kim101_feature_group

from thorlabs_xa.interfaces.device_features.disconnect import Disconnect
from thorlabs_xa.interfaces.device_features.firmware_version_info import FirmwareVersionInfo
from thorlabs_xa.interfaces.device_features.hardware_info import HardwareInfo
from thorlabs_xa.interfaces.device_features.piezo_inertial_motor.kcube_channel_enable import KcubeChannelEnable
from thorlabs_xa.interfaces.device_features.piezo_inertial_motor.stage_select_params import StageSelectParams
from thorlabs_xa.interfaces.device_features.load_params import LoadParams
from thorlabs_xa.interfaces.device_features.settings import Settings
from thorlabs_xa.interfaces.device_features.status_mode import StatusMode

from thorlabs_xa.implementations.device_features.disconnect_feature import DisconnectFeature
from thorlabs_xa.implementations.device_features.firmware_version_info_feature import FirmwareVersionInfoFeature
from thorlabs_xa.implementations.device_features.hardware_info_feature import HardwareInfoFeature
from thorlabs_xa.implementations.device_features.piezo_inertial_motor.kcube_channel_enable_feature import KcubeChannelEnableFeature
from thorlabs_xa.implementations.device_features.piezo_inertial_motor.stage_select_params_feature import StageSelectParamsFeature
from thorlabs_xa.implementations.device_features.load_params_feature import LoadParamsFeature
from thorlabs_xa.implementations.device_features.settings_feature import SettingsFeature
from thorlabs_xa.implementations.device_features.status_mode_feature import StatusModeFeature

from thorlabs_xa.native_sdks.native_functions import NativeFunctions

class Kim101FeatureGroup(thorlabs_xa.interfaces.device_feature_groups.kim101_feature_group.Kim101FeatureGroup):

    def __init__(self, device_handle: int, native_functions: NativeFunctions) -> None:

        self._disconnect_feature = DisconnectFeature(device_handle, native_functions)
        self._firmware_version_info_feature = FirmwareVersionInfoFeature(device_handle, native_functions)
        self._hardware_info_feature = HardwareInfoFeature(device_handle, native_functions)
        self._kcube_channel_enable_feature = KcubeChannelEnableFeature(device_handle, native_functions)
        self._load_params_feature = LoadParamsFeature(device_handle, native_functions)
        self._settings_feature = SettingsFeature(device_handle, native_functions)
        self._stage_select_params_feature = StageSelectParamsFeature(device_handle, native_functions)
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
    def kcube_channel_enable_feature(self) -> KcubeChannelEnable:
        return self._kcube_channel_enable_feature

    @property
    def load_params_feature(self) -> LoadParams:
        return self._load_params_feature

    @property
    def settings_feature(self) -> Settings:
        return self._settings_feature

    @property
    def stage_select_params_feature(self) -> StageSelectParams:
        return self._stage_select_params_feature

    @property
    def status_mode_feature(self) -> StatusMode:
        return self._status_mode_feature