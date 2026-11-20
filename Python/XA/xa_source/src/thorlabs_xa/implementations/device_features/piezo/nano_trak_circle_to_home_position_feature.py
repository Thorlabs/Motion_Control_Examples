from thorlabs_xa.interfaces.device_features.piezo.nano_trak_circle_to_home_position import NanoTrakCircleToHomePosition
from thorlabs_xa.native_sdks.native_functions import NativeFunctions

class NanoTrakCircleToHomePositionFeature(NanoTrakCircleToHomePosition):

    def __init__(self, device_handle: int, native_functions: NativeFunctions) -> None:

        self.device_handle = device_handle
        self.native_functions = native_functions

    def nano_trak_circle_to_home_position(self) -> None:

        self.native_functions.pz_nano_trak_circle_to_home_position(self.device_handle)