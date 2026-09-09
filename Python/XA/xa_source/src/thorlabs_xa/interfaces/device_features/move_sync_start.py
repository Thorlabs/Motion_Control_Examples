from typing import Protocol, runtime_checkable

from thorlabs_xa.shared.params import TLMC_MoveSyncStartParams

@runtime_checkable
class MoveSyncStart(Protocol):

    def move_sync_start(self, parameters: TLMC_MoveSyncStartParams) -> None: ...