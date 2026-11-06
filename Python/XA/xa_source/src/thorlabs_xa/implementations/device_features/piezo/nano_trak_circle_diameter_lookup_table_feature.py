from thorlabs_xa.interfaces.device_features.piezo.nano_trak_circle_diameter_lookup_table import NanoTrakCircleDiameterLookupTable
from thorlabs_xa.native_sdks.native_functions import NativeFunctions
from thorlabs_xa.shared.params import TLMC_PZ_NanoTrakCircleDiameterLookupTable

class NanoTrakCircleDiameterLookupTableFeature(NanoTrakCircleDiameterLookupTable):

    def __init__(self, device_handle: int, native_functions: NativeFunctions) -> None:

        self.device_handle = device_handle
        self.native_functions = native_functions

    def get_nano_trak_circle_diameter_lookup_table(self, max_wait_in_milliseconds: int) -> TLMC_PZ_NanoTrakCircleDiameterLookupTable:

        return self.native_functions.pz_get_nano_trak_circle_diameter_lookup_table(self.device_handle, max_wait_in_milliseconds)

    def set_nano_trak_circle_diameter_lookup_table(self, params: TLMC_PZ_NanoTrakCircleDiameterLookupTable) -> None:

        self.native_functions.pz_set_nano_trak_circle_diameter_lookup_table(self.device_handle, params)
