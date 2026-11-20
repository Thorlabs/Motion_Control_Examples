from typing import Protocol, runtime_checkable

from thorlabs_xa.shared.params import TLMC_PZIM_AmplifierOutputParams

@runtime_checkable
class AmplifierOutputParams(Protocol):

    def get_amplifier_output_params(self, max_wait_in_milliseconds: int) -> TLMC_PZIM_AmplifierOutputParams:...

    def set_amplifier_output_params(self, params: TLMC_PZIM_AmplifierOutputParams) -> None:...
