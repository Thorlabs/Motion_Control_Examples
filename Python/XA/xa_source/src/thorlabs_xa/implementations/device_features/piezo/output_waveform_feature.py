from thorlabs_xa.interfaces.device_features.piezo.output_waveform import OutputWaveform
from thorlabs_xa.native_sdks.native_functions import NativeFunctions
from thorlabs_xa.shared.params import TLMC_PZ_OutputWaveformLoopTableSample, TLMC_PZ_OutputWaveformParams

class OutputWaveformFeature(OutputWaveform):

    def __init__(self, device_handle: int, native_functions: NativeFunctions) -> None:

        self.device_handle = device_handle
        self.native_functions = native_functions

    def set_output_waveform_lookup_table_sample_params(self, params: TLMC_PZ_OutputWaveformLoopTableSample) -> None:

        self.native_functions.pz_set_output_waveform_loop_table_sample(self.device_handle, params)

    def set_output_waveform_params(self, params: TLMC_PZ_OutputWaveformParams) -> None:
        
        return self.native_functions.pz_set_output_waveform_params(self.device_handle, params)
    
    def start_output_waveform(self) -> None:
        
        self.native_functions.pz_start_output_waveform(self.device_handle)

    def stop_output_waveform(self) -> None:
        
        self.native_functions.pz_stop_output_waveform(self.device_handle)