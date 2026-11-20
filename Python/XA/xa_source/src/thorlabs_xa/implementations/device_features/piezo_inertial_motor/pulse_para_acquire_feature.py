from thorlabs_xa.interfaces.device_features.piezo_inertial_motor.pulse_para_acquire import PulseParaAcquire
from thorlabs_xa.native_sdks.native_functions import NativeFunctions

class PulseParaAcquireFeature(PulseParaAcquire):

    def __init__(self, device_handle: int, native_functions: NativeFunctions) -> None:

        self.device_handle = device_handle
        self.native_functions = native_functions

    def pulse_para_acquire(self, max_wait_in_milliseconds: int) -> None:
        self.native_functions.pzim_pulse_para_acquire(self.device_handle, max_wait_in_milliseconds)
