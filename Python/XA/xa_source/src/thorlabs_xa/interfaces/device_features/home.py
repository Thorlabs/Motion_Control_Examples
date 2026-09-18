from typing import Protocol, runtime_checkable

@runtime_checkable
class Home(Protocol):

    def home(self, max_wait_in_milliseconds: int) -> None: ...
