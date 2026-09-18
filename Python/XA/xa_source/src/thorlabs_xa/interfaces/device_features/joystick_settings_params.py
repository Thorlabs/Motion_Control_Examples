from typing import Protocol, runtime_checkable

from thorlabs_xa.shared.params import TLMC_JoystickSettingsParams

@runtime_checkable
class JoystickSettingsParams(Protocol):

    def get_joystick_settings_params(self, max_wait_in_milliseconds: int) -> TLMC_JoystickSettingsParams:...

    def set_joystick_settings_params(self, params: TLMC_JoystickSettingsParams) -> None:...