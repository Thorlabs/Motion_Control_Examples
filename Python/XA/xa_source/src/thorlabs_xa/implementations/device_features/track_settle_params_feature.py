from thorlabs_xa.interfaces.device_features.track_settle_params import TrackSettleParams
from thorlabs_xa.native_sdks.native_functions import NativeFunctions
from thorlabs_xa.shared.params import TLMC_TrackSettleParams

class TrackSettleParamsFeature(TrackSettleParams):

    def __init__(self, device_handle: int, native_functions: NativeFunctions):
        
        self.device_handle = device_handle
        self.native_functions = native_functions

    def get_track_settle_params(self, max_wait_in_milliseconds: int):

        return self.native_functions.get_track_settle_params(self.device_handle, max_wait_in_milliseconds)

    def set_track_settle_params(self, params: TLMC_TrackSettleParams):

        self.native_functions.set_track_settle_params(self.device_handle, params)
