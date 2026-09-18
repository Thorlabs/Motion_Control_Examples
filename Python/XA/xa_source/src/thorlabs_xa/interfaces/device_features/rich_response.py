from typing import Protocol, runtime_checkable

from thorlabs_xa.shared.params import TLMC_RichResponse

@runtime_checkable
class RichResponse(Protocol):

    def get_rich_response(self) -> TLMC_RichResponse: ...