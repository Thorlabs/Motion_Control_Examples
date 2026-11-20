from thorlabs_xa.interfaces.device_features.piezo_inertial_motor.move_jog import MoveJog
from thorlabs_xa.native_sdks.native_functions import NativeFunctions
from thorlabs_xa.shared.enums import TLMC_MoveDirection

class MoveJogFeature(MoveJog):

    def __init__(self, device_handle: int, native_functions: NativeFunctions) -> None:

        self.device_handle = device_handle
        self.native_functions = native_functions

    def move_jog(self, direction: TLMC_MoveDirection, max_wait_in_milliseconds: int) -> None:
        self.native_functions.move_jog(self.device_handle, direction, max_wait_in_milliseconds)
