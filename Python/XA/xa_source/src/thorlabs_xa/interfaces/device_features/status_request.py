from typing import Protocol, runtime_checkable

@runtime_checkable
class StatusRequest(Protocol):

    def request_status(self, max_wait_in_milliseconds: int) -> None: ...