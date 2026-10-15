from thorlabs_xa.interfaces.device_features.piezo.nano_trak_circle_diameter import NanoTrakCircleDiameter
from thorlabs_xa.native_sdks.native_functions import NativeFunctions

class NanoTrakCircleDiameterFeature(NanoTrakCircleDiameter):

    def __init__(self, device_handle: int, native_functions: NativeFunctions) -> None:

        self.device_handle = device_handle
        self.native_functions = native_functions

    def set_nano_trak_circle_diameter(self, circle_diameter: int) -> None:

        self.native_functions.pz_set_nano_trak_circle_diameter(self.device_handle, circle_diameter)