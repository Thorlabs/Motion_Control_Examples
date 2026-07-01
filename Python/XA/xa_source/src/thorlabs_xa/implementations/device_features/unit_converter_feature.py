from thorlabs_xa.interfaces.device_features.unit_converter import UnitConverter
from thorlabs_xa.native_sdks.native_functions import NativeFunctions
from thorlabs_xa.shared.enums import TLMC_ScaleType, TLMC_Unit

class UnitConverterFeature(UnitConverter):
        
    def __init__(self, device_handle: int, native_functions: NativeFunctions):

        self.device_handle = device_handle
        self.native_functions = native_functions

    def convert_from_device_units_to_physical(self, scale_type: TLMC_ScaleType, device_value: int) -> tuple [float, TLMC_Unit]:

        return self.native_functions.convert_from_device_units_to_physical(self.device_handle, scale_type, device_value)

    def convert_from_physical_to_device(self, scale_type: TLMC_ScaleType, unit: TLMC_Unit, physical_value: int) -> int:

        return self.native_functions.convert_from_physical_to_device(self.device_handle, scale_type, unit, physical_value)

    def get_preferred_physical_unit(self, scale_type: TLMC_ScaleType) -> TLMC_Unit:

        return self.native_functions.get_preferred_physical_unit(self.device_handle, scale_type)