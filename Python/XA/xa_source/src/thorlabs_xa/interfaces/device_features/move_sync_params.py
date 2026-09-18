from typing import Protocol, runtime_checkable

from thorlabs_xa.shared.params import TLMC_MoveSyncParams

@runtime_checkable
class MoveSyncParams(Protocol):

    def set_move_sync_params(self, parameters: TLMC_MoveSyncParams) -> None: ...