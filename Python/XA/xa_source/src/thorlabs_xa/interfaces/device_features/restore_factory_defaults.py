from typing import Protocol, runtime_checkable

@runtime_checkable
class RestoreFactoryDefaults(Protocol):

    def restore_factory_defaults(self) -> None: ...