from typing import Protocol, runtime_checkable

from thorlabs_xa.shared.enums import TLMC_RackBayNumber, TLMC_RackBayOccupiedState

@runtime_checkable
class RackBayOccupiedState(Protocol):

    def get_rack_bay_occupied_state(self, bay_number: TLMC_RackBayNumber, max_wait_in_milliseconds: int) -> TLMC_RackBayOccupiedState: ...