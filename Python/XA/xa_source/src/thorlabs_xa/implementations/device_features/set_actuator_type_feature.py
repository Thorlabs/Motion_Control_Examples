from thorlabs_xa.interfaces.device_features.set_actuator_type import SetActuatorType
from thorlabs_xa.native_sdks.native_functions import NativeFunctions

class SetActuatorTypeFeature(SetActuatorType):

    def __init__(self, device_handle: int, native_functions: NativeFunctions):

        self.device_handle = device_handle
        self.native_functions = native_functions

    def set_actuator_type(self, actuator_type: int):
        
        self.native_functions.set_actuator_type(self.device_handle, actuator_type)
