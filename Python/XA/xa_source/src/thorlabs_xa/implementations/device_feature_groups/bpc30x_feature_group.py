import thorlabs_xa.interfaces.device_feature_groups.bpc30x_feature_group

from thorlabs_xa.interfaces.device_features.digital_output_states import DigitalOutputStates
from thorlabs_xa.interfaces.device_features.disconnect import Disconnect
from thorlabs_xa.interfaces.device_features.firmware_version_info import FirmwareVersionInfo
from thorlabs_xa.interfaces.device_features.hardware_info import HardwareInfo
from thorlabs_xa.interfaces.device_features.load_params import LoadParams
from thorlabs_xa.interfaces.device_features.rack_bay_occupied_state import RackBayOccupiedState
from thorlabs_xa.interfaces.device_features.rack_identify import RackIdentify
from thorlabs_xa.interfaces.device_features.settings import Settings

from thorlabs_xa.implementations.device_features.digital_output_states_feature import DigitalOutputStatesFeature
from thorlabs_xa.implementations.device_features.disconnect_feature import DisconnectFeature
from thorlabs_xa.implementations.device_features.firmware_version_info_feature import FirmwareVersionInfoFeature
from thorlabs_xa.implementations.device_features.hardware_info_feature import HardwareInfoFeature
from thorlabs_xa.implementations.device_features.load_params_feature import LoadParamsFeature
from thorlabs_xa.implementations.device_features.rack_bay_occupied_state_feature import RackBayOccupiedStateFeature
from thorlabs_xa.implementations.device_features.rack_identify_feature import RackIdentifyFeature
from thorlabs_xa.implementations.device_features.settings_feature import SettingsFeature

from thorlabs_xa.native_sdks.native_functions import NativeFunctions

class Bpc30xFeatureGroup(thorlabs_xa.interfaces.device_feature_groups.bpc30x_feature_group.Bpc30xFeatureGroup):

    def __init__(self, device_handle: int, native_functions: NativeFunctions) -> None:

        self._digital_output_states_feature = DigitalOutputStatesFeature(device_handle, native_functions)
        self._disconnect_feature = DisconnectFeature(device_handle, native_functions)
        self._firmware_version_info_feature = FirmwareVersionInfoFeature(device_handle, native_functions)
        self._hardware_info_feature = HardwareInfoFeature(device_handle, native_functions)
        self._load_params_feature = LoadParamsFeature(device_handle, native_functions)
        self._rack_bay_occupied_state_feature = RackBayOccupiedStateFeature(device_handle, native_functions)
        self._rack_identify_feature = RackIdentifyFeature(device_handle, native_functions)
        self._settings_feature = SettingsFeature(device_handle, native_functions)

    @property
    def digital_output_states_feature(self) -> DigitalOutputStates:
        return self._digital_output_states_feature

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
    def load_params_feature(self) -> LoadParams:
        return self._load_params_feature

    @property
    def rack_bay_occupied_state_feature(self) -> RackBayOccupiedState:
        return self._rack_bay_occupied_state_feature

    @property
    def rack_identify_feature(self) -> RackIdentify:
        return self._rack_identify_feature
    
    @property
    def settings_feature(self) -> Settings:
        return self._settings_feature