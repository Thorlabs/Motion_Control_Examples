from thorlabs_xa.interfaces.device_features.rack_bay_occupied_state import RackBayOccupiedState
from thorlabs_xa.native_sdks.native_functions import NativeFunctions
from thorlabs_xa.shared.enums import TLMC_RackBayNumber, TLMC_RackBayOccupiedState

class RackBayOccupiedStateFeature(RackBayOccupiedState):

    def __init__(self, device_handle: int, native_functions: NativeFunctions):

        self.device_handle = device_handle
        self.native_functions = native_functions

    def get_rack_bay_occupied_state(self, bay_number: TLMC_RackBayNumber, max_wait_in_milliseconds: int) -> TLMC_RackBayOccupiedState:

        return self.native_functions.get_rack_bay_occupied_state(self.device_handle, bay_number, max_wait_in_milliseconds)