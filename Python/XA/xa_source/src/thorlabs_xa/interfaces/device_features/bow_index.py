from typing import Protocol, runtime_checkable

from thorlabs_xa.shared.enums import TLMC_BowIndex

@runtime_checkable
class BowIndex(Protocol):

    def get_bow_index(self, max_wait_in_milliseconds: int) -> TLMC_BowIndex: ...

    def set_bow_index(self, bow_index: TLMC_BowIndex): ...