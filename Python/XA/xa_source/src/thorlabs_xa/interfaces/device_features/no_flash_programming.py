from typing import Protocol, runtime_checkable

@runtime_checkable
class NoFlashProgramming(Protocol):

    def send_no_flash_programming(self) -> None: ...
