from abc import ABCMeta

from thorlabs_xa.native_sdks.native_functions import NativeFunctions
from thorlabs_xa.shared.enums import TLMC_DeviceFamily, TLMC_DeviceType
from thorlabs_xa.shared.params import TLMC_DeviceInfo

class Device(metaclass=ABCMeta):

    def __init__(self, device_handle: int, device_info: TLMC_DeviceInfo, native_functions: NativeFunctions):

        self._device_handle = device_handle
        self._device_id = device_info.device
        self._device_family = device_info.device_family
        self._parent_device_id = device_info.parent_device
        self._part_number = device_info.part_number
        self._transport = device_info.transport
        self._device_type = device_info.device_type
        self._device_type_description = device_info.device_type_description
        self._native_functions = native_functions

    def close(self):

        self._native_functions.close(self._device_handle)

    @property
    def device_id(self) -> str:
        return self._device_id
    
    @property
    def device_family(self) -> TLMC_DeviceFamily:
        return self._device_family
    
    @property
    def parent_device_id(self) -> str:
        return self._device_id
    
    @property
    def part_number(self) -> str:
        return self._part_number
    
    @property
    def transport(self) -> str:
        return self._transport
    
    @property
    def device_type(self) -> TLMC_DeviceType:
        return self._device_type
    
    @property
    def device_type_description(self) -> str:
        return self._device_type_description