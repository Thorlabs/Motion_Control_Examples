from typing import List, Protocol, runtime_checkable

from thorlabs_xa.shared.params import TLMC_StatusItem, TLMC_StatusItemId

@runtime_checkable
class StatusItems(Protocol):

    def get_status_item(self, status_item_id: TLMC_StatusItemId) -> TLMC_StatusItem: ...

    def get_status_item_count(self) -> int: ...

    def get_status_items(self, start_index: int, number_of_items: int) -> List[TLMC_StatusItem]: ...