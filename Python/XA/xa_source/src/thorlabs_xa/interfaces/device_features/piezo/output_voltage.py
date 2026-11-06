from typing import Protocol, runtime_checkable

@runtime_checkable
class OutputVoltage(Protocol):

    def get_output_voltage(self, max_wait_in_milliseconds: int) -> int: ...

    def set_output_voltage(self, output_voltage: int) -> None: ...