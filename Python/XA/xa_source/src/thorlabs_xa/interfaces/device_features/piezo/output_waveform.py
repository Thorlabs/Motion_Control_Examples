from typing import Protocol, runtime_checkable

from thorlabs_xa.shared.params import TLMC_PZ_OutputWaveformLoopTableSample, TLMC_PZ_OutputWaveformParams

@runtime_checkable
class OutputWaveform(Protocol):

    def set_output_waveform_lookup_table_sample_params(self, params: TLMC_PZ_OutputWaveformLoopTableSample) -> None: ...

    def set_output_waveform_params(self, params: TLMC_PZ_OutputWaveformParams) -> None: ...
        
    def start_output_waveform(self) -> None: ...

    def stop_output_waveform(self) -> None: ...