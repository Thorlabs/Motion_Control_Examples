from typing import Protocol, runtime_checkable

@runtime_checkable
class LoadParams(Protocol):

    def load_params(self) -> None: ...