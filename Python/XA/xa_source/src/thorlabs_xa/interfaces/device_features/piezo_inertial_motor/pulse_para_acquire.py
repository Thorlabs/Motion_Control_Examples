from typing import Protocol, runtime_checkable

@runtime_checkable
class PulseParaAcquire(Protocol):

    def pulse_para_acquire(self, max_wait_in_milliseconds: int) -> None: ...
