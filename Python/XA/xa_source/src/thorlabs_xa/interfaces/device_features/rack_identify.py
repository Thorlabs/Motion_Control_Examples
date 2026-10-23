from typing import Protocol, runtime_checkable

@runtime_checkable
class RackIdentify(Protocol):

    def rack_identify(self, channel: int) -> None: ...