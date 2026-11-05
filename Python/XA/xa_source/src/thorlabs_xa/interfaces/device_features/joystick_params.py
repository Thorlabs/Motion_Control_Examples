from typing import Protocol, runtime_checkable

from thorlabs_xa.shared.params import TLMC_JoystickParams

@runtime_checkable
class JoystickParams(Protocol):

    def get_joystick_params(self, max_wait_in_milliseconds: int) -> TLMC_JoystickParams: ...

    def set_joystick_params(self, params: TLMC_JoystickParams) -> None: ...