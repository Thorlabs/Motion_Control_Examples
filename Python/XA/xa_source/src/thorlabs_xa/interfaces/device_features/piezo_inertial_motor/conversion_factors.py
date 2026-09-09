from typing import Protocol, runtime_checkable

@runtime_checkable
class ConversionFactors(Protocol):

    def get_conversion_factors(self, max_wait_in_milliseconds: int) -> int:...
