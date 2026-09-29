from typing import Protocol, runtime_checkable

@runtime_checkable
class Disconnect(Protocol):

    def disconnect(self) -> None: ...