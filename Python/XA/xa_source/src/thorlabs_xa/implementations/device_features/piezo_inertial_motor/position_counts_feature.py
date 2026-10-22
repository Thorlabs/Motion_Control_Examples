from thorlabs_xa.interfaces.device_features.piezo_inertial_motor.position_counts import PositionCounts
from thorlabs_xa.native_sdks.native_functions import NativeFunctions

from thorlabs_xa.shared.params import TLMC_PZIM_PositionCounts

class PositionCountsFeature(PositionCounts):

    def __init__(self, device_handle: int, native_functions: NativeFunctions) -> None:

        self.device_handle = device_handle
        self.native_functions = native_functions

    def get_position_counts(self, max_wait_in_milliseconds: int) -> TLMC_PZIM_PositionCounts:

        return self.native_functions.pzim_get_position_counts(self.device_handle, max_wait_in_milliseconds)

    def set_position_counts(self, params: TLMC_PZIM_PositionCounts) -> None:

        self.native_functions.pzim_set_position_counts(self.device_handle, params)