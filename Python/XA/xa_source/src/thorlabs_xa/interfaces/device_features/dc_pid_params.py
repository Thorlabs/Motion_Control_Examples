from typing import Protocol, runtime_checkable

from thorlabs_xa.shared.params import TLMC_DcPidParams

@runtime_checkable
class DcPidParams(Protocol):

    def get_dc_pid_params(self, max_wait_in_milliseconds: int) -> TLMC_DcPidParams: ...

    def set_dc_pid_params(self, parameters: TLMC_DcPidParams): ...
