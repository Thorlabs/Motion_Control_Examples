from thorlabs_xa.interfaces.device_features.persist_params import PersistParams
from thorlabs_xa.native_sdks.native_functions import NativeFunctions
from thorlabs_xa.shared.enums import TLMC_ParameterGroupId

class PersistParamsFeature(PersistParams):
    
    def __init__(self, device_handle: int, native_functions: NativeFunctions) -> None:

        self.device_handle = device_handle
        self.native_functions = native_functions

    def persist_params(self, parameter_group_id: TLMC_ParameterGroupId) -> None:

        self.native_functions.persist_params(self.device_handle, parameter_group_id)