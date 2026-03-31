from typing import Protocol, runtime_checkable

from thorlabs_xa.shared.params import TLMC_PZ_OutputWaveformParams

@runtime_checkable
class OutputWaveformParamsGetter(Protocol):

    def get_output_waveform_params(self, max_wait_in_milliseconds: int) -> TLMC_PZ_OutputWaveformParams: ...