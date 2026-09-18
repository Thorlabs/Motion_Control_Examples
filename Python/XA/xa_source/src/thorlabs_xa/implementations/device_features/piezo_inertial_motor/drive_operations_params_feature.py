from thorlabs_xa.interfaces.device_features.piezo_inertial_motor.drive_operations_params import DriveOperationsParams
from thorlabs_xa.native_sdks.native_functions import NativeFunctions
from thorlabs_xa.shared.params import TLMC_PZIM_DriveOperationsParams

class DriveOperationsParamsFeature(DriveOperationsParams):

    def __init__(self, device_handle: int, native_functions: NativeFunctions) -> None:

        self.device_handle = device_handle
        self.native_functions = native_functions

    def get_drive_operations_params(self, max_wait_in_milliseconds: int) -> TLMC_PZIM_DriveOperationsParams:

        return self.native_functions.pzim_get_drive_operations_params(self.device_handle, max_wait_in_milliseconds)

    def set_drive_operations_params(self, params: TLMC_PZIM_DriveOperationsParams) -> None:

        self.native_functions.pzim_set_drive_operations_params(self.device_handle, params)