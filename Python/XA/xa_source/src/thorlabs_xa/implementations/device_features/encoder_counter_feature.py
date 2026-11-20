from thorlabs_xa.interfaces.device_features.encoder_counter import EncoderCounter
from thorlabs_xa.native_sdks.native_functions import NativeFunctions

class EncoderCounterFeature(EncoderCounter):

    def __init__(self, device_handle: int, native_functions: NativeFunctions) -> None:

        self.device_handle = device_handle
        self.native_functions = native_functions

    def get_encoder_counter(self, max_wait_in_milliseconds: int) -> int:
        return self.native_functions.get_encoder_counter(self.device_handle, max_wait_in_milliseconds)

    def set_encoder_counter(self, new_encoder_counter: int) -> None:
        self.native_functions.set_encoder_counter(self.device_handle, new_encoder_counter)
