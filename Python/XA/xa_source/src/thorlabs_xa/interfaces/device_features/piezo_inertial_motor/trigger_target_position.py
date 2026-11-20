from typing import Protocol, runtime_checkable

@runtime_checkable
class TriggerTargetPosition(Protocol):

    def get_trigger_target_position(self, max_wait_in_milliseconds: int) -> int: ...
