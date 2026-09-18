from typing import List, Protocol, runtime_checkable

from thorlabs_xa.shared.enums import TLMC_SettingStringFormat
from thorlabs_xa.shared.params import TLMC_Setting

@runtime_checkable
class Settings(Protocol):

    def get_setting(self, settings_name: str, max_wait_in_milliseconds: int) -> TLMC_Setting: ...

    def get_settings_items(self) -> List[TLMC_Setting]: ...

    def get_settings(self, setting_string_format: TLMC_SettingStringFormat, include_read_only_items: bool) -> str: ...

    def set_settings(self, settings: str) -> None: ...

    def get_setting_discrete_values(self, settings_name: str) -> str: ...