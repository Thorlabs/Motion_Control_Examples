from thorlabs_xa.interfaces.device_features.piezo.nano_trak_tia_self_calibrate import NanoTrakTiaSelfCalibrate
from thorlabs_xa.native_sdks.native_functions import NativeFunctions

class NanoTrakTiaSelfCalibrateFeature(NanoTrakTiaSelfCalibrate):

    def __init__(self, device_handle: int, native_functions: NativeFunctions) -> None:

        self.device_handle = device_handle
        self.native_functions = native_functions

    def nano_trak_tia_self_calibrate(self) -> None:

        return self.native_functions.pz_nano_trak_tia_self_calibrate(self.device_handle)