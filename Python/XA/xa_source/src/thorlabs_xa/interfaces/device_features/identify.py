from typing import Protocol, runtime_checkable

@runtime_checkable
class Identify(Protocol):

    def identify(self) -> None: ...