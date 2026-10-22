from thorlabs_xa.interfaces.device_features.piezo.kna_scan import KnaScan
from thorlabs_xa.native_sdks.native_functions import NativeFunctions
from thorlabs_xa.shared.params import TLMC_PZ_KnaScanData

class KnaScanFeature(KnaScan):

    def __init__(self, device_handle: int, native_functions: NativeFunctions) -> None:

        self.device_handle = device_handle
        self.native_functions = native_functions

    def start_kna_scan(self) -> None:

        self.native_functions.pz_start_kna_scan(self.device_handle)

    def stop_kna_scan(self) -> None:

        self.native_functions.pz_stop_kna_scan(self.device_handle)

    def get_kna_scan_data(self, max_wait_in_milliseconds: int) -> TLMC_PZ_KnaScanData:

        return self.native_functions.pz_get_kna_scan_data(self.device_handle, max_wait_in_milliseconds)
