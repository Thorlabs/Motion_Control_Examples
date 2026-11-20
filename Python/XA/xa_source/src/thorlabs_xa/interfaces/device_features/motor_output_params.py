from typing import Protocol, runtime_checkable

from thorlabs_xa.shared.params import TLMC_MotorOutputParams

@runtime_checkable
class MotorOutputParams(Protocol):

    def get_motor_output_params(self, max_wait_in_milliseconds: int) -> TLMC_MotorOutputParams: ...

    def set_motor_output_params(self, params: TLMC_MotorOutputParams) -> None: ...