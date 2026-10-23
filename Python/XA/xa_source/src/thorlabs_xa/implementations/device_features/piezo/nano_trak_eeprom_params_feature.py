from thorlabs_xa.interfaces.device_features.piezo.nano_trak_eeprom_params import NanoTrakEEPROMParams
from thorlabs_xa.native_sdks.native_functions import NativeFunctions
from thorlabs_xa.shared.params import TLMC_PZ_NanoTrakEEPROMParams

class NanoTrakEEPROMParamsFeature(NanoTrakEEPROMParams):

    def __init__(self, device_handle: int, native_functions: NativeFunctions) -> None:

        self.device_handle = device_handle
        self.native_functions = native_functions

    def set_nano_trak_eeprom_params(self, params: TLMC_PZ_NanoTrakEEPROMParams) -> None:

        self.native_functions.pz_set_nano_trak_eeprom_params(self.device_handle, params)