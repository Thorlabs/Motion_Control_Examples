from thorlabs_xa.interfaces.device_features.power_options import PowerOptions
from thorlabs_xa.native_sdks.native_functions import NativeFunctions

from thorlabs_xa.shared.enums import TLMC_PowerOptions

class PowerOptionsFeature(PowerOptions):

    def __init__(self, device_handle: int, native_functions: NativeFunctions) -> None:

        self.device_handle = device_handle
        self.native_functions = native_functions

    def get_power_options(self, max_wait_in_milliseconds: int) -> TLMC_PowerOptions:
        return self.native_functions.get_power_options(self.device_handle, max_wait_in_milliseconds)

    def set_power_options(self, power_options: TLMC_PowerOptions) -> None:
        self.native_functions.set_power_options(self.device_handle, power_options)