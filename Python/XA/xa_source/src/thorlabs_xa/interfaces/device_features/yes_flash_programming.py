from typing import Protocol, runtime_checkable

@runtime_checkable
class YesFlashProgramming(Protocol):

    def send_yes_flash_programming(self): ...