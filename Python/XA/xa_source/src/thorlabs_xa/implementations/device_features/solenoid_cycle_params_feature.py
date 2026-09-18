from thorlabs_xa.interfaces.device_features.solenoid_cycle_params import SolenoidCycleParams
from thorlabs_xa.native_sdks.native_functions import NativeFunctions

from thorlabs_xa.shared.params import TLMC_SolenoidCycleParams

class SolenoidCycleParamsFeature(SolenoidCycleParams):

    def __init__(self, device_handle: int, native_functions: NativeFunctions) -> None:

        self.device_handle = device_handle
        self.native_functions = native_functions

    def get_solenoid_cycle_params(self, max_wait_in_milliseconds: int) -> TLMC_SolenoidCycleParams:
        return self.native_functions.get_solenoid_cycle_params(self.device_handle, max_wait_in_milliseconds)

    def set_solenoid_cycle_params(self, solenoid_cycle_params : TLMC_SolenoidCycleParams) -> None:
        self.native_functions.set_solenoid_cycle_params(self.device_handle, solenoid_cycle_params)