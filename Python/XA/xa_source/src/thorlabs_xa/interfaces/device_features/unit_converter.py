from typing import Protocol, runtime_checkable

from thorlabs_xa.shared.enums import TLMC_ScaleType, TLMC_Unit

@runtime_checkable
class UnitConverter(Protocol):

    def convert_from_device_units_to_physical(self, scale_type: TLMC_ScaleType, device_value: int) -> tuple [float, TLMC_Unit]: ...

    def convert_from_physical_to_device(self, scale_type: TLMC_ScaleType, unit: TLMC_Unit, physical_value: int) -> int: ...

    def get_preferred_physical_unit(self, scale_type: TLMC_ScaleType) -> TLMC_Unit: ...