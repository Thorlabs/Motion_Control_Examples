from typing import Protocol, runtime_checkable

from thorlabs_xa.shared.params import TLMC_MoveSyncArray

@runtime_checkable
class MoveSyncArray(Protocol):

    def set_move_sync_array(self, parameters: TLMC_MoveSyncArray) -> None: ...