from abc import ABCMeta

from thorlabs_xa.native_sdks.native_functions import NativeFunctions
from thorlabs_xa.shared.enums import TLMC_DeviceType

class Subchannel(metaclass=ABCMeta):

    def __init__(self, subchannel_handle: int, subchannel_number: int, native_functions: NativeFunctions) -> None:

        self._subchannel_handle = subchannel_handle
        self._subchannel_number = subchannel_number
        self._native_functions = native_functions
        self._parent_device_id: str | None = None
        self._parent_device_type: TLMC_DeviceType | None = None

    def set_parent_device_identity(
        self,
        device_id: str,
        device_type: TLMC_DeviceType,
    ) -> None:
        self._parent_device_id = device_id
        self._parent_device_type = device_type

    @property
    def subchannel_handle(self) -> int:
        return self._subchannel_handle

    @property
    def subchannel_number(self) -> int:
        return self._subchannel_number

    @property
    def device_id(self) -> str:
        if self._parent_device_id is None:
            raise AttributeError(
                "Subchannel parent device identity has not been configured"
            )

        return self._parent_device_id

    @property
    def device_type(self) -> TLMC_DeviceType:
        if self._parent_device_type is None:
            raise AttributeError(
                "Subchannel parent device identity has not been configured"
            )

        return self._parent_device_type