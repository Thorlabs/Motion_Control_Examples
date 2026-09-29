from thorlabs_xa.interfaces.device_features.end_of_move_message_mode import EndOfMoveMessageMode

from thorlabs_xa.native_sdks.native_functions import NativeFunctions
from thorlabs_xa.shared.enums import TLMC_EndOfMoveMessageMode

class EndOfMoveMessageModeFeature(EndOfMoveMessageMode):

    def __init__(self, device_handle: int, native_functions: NativeFunctions) -> None:

        self.device_handle = device_handle
        self.native_functions = native_functions

    def set_end_of_move_message_mode(self, message_mode: TLMC_EndOfMoveMessageMode) -> None:

        self.native_functions.set_end_of_move_message_mode(self.device_handle, message_mode)