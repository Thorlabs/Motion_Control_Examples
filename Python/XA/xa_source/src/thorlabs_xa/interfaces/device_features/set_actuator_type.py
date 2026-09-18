from typing import Protocol, runtime_checkable

@runtime_checkable
class SetActuatorType(Protocol):

    def set_actuator_type(self, actuator_type: int) -> None: ...
