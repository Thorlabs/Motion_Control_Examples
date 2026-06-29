from typing import List

from thorlabs_xa.interfaces.device_features.settings import Settings
from thorlabs_xa.native_sdks.native_functions import NativeFunctions
from thorlabs_xa.shared.enums import TLMC_SettingStringFormat
from thorlabs_xa.shared.params import TLMC_Setting

class SettingsFeature(Settings):

    def __init__(self, device_handle: int, native_functions: NativeFunctions) -> None:

        self.device_handle = device_handle
        self.native_functions = native_functions

    def get_setting(self, settings_name: str, max_wait_in_milliseconds: int) -> TLMC_Setting:
        return self.native_functions.get_setting(self.device_handle, settings_name, max_wait_in_milliseconds)

    def get_settings_items(self) -> List[TLMC_Setting]:
        
        number_of_settings = self.native_functions.get_setting_count(self.device_handle)
        return self.native_functions.get_settings(self.device_handle, 0, number_of_settings)

    def get_settings(self, setting_string_format: TLMC_SettingStringFormat, include_read_only_items: bool) -> str:
        return self.native_functions.get_settings_as_string(self.device_handle, setting_string_format, include_read_only_items)
    
    def set_settings(self, settings: str) -> None:
        
        self.native_functions.set_settings_from_string(self.device_handle, settings)

    def get_setting_discrete_values(self, settings_name: str) -> str:
        return self.native_functions.get_setting_discrete_values(self.device_handle, settings_name)