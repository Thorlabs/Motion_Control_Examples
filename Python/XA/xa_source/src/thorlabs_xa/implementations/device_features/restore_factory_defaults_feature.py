from thorlabs_xa.interfaces.device_features.restore_factory_defaults import RestoreFactoryDefaults
from thorlabs_xa.native_sdks.native_functions import NativeFunctions

class RestoreFactoryDefaultsFeature(RestoreFactoryDefaults):

    def __init__(self, device_handle: int, native_functions: NativeFunctions):

        self.device_handle = device_handle
        self.native_functions = native_functions

    def restore_factory_defaults(self):

        self.native_functions.restore_factory_defaults(self.device_handle)