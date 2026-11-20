from thorlabs_xa.interfaces.device_features.piezo_inertial_motor.move_absolute_to_programmed_position import MoveAbsoluteToProgrammedPosition
from thorlabs_xa.native_sdks.native_functions import NativeFunctions
from thorlabs_xa.shared.enums import TLMC_MoveMode, TLMC_Wait

class MoveAbsoluteToProgrammedPositionFeature(MoveAbsoluteToProgrammedPosition):

    def __init__(self, device_handle: int, native_functions: NativeFunctions) -> None:

        self.device_handle = device_handle
        self.native_functions = native_functions

    def move_absolute_to_programmed_position(self, max_wait_in_milliseconds: int) -> None:
        self.native_functions.move(
            self.device_handle,
            TLMC_MoveMode.TLMC_MoveMode_AbsoluteToProgrammedPosition,
            TLMC_Wait.TLMC_Unused,
            max_wait_in_milliseconds,
        )
