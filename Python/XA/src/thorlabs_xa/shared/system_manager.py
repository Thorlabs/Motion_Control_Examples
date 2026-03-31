from __future__ import annotations

import threading
from typing import Any, List, Optional, Type, TypeVar

from thorlabs_xa.native_sdks.c_native_functions import CNativeFunctions
from thorlabs_xa.shared.device import Device
from thorlabs_xa.shared.device_factory import DeviceFactory
from thorlabs_xa.shared.enums import TLMC_OperatingMode
from thorlabs_xa.shared.params import TLMC_ApiVersion, TLMC_DeviceInfo

TDev = TypeVar("TDev", bound=Device)

class SystemManager:
    
    _instance: SystemManager | None = None
    _lock = threading.Lock()
    _initialized: bool

    def __new__(cls, *args: Any, **kwargs: Any) -> SystemManager:
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    inst = super().__new__(cls)
                    inst._initialized = False
                    cls._instance = inst
        return cls._instance

    def __init__(self) -> None:
        if self._initialized:
            return

        self.native_functions = CNativeFunctions()
        self.device_factory = DeviceFactory(self.native_functions)

        self._initialized = True

    @classmethod
    def instance(cls) -> SystemManager:
        return cls()

    def startup(self, settings_file_name: Optional[str] = None) -> None:
        self.native_functions.startup(settings_file_name)

    def shutdown(self) -> None:
        self.native_functions.shutdown()

    def get_api_version(self) -> TLMC_ApiVersion:
        return self.native_functions.get_api_version()

    def get_device_list(self) -> List[TLMC_DeviceInfo]:
        device_count = self.native_functions.get_device_list_item_count()
        return self.native_functions.get_device_list_items(0, device_count)

    def open_device(self, device_id: str, transport: str, operating_mode: TLMC_OperatingMode) -> Device:
        device_handle = self.native_functions.open(device_id, transport, operating_mode)
        device_info = self.native_functions.get_device_info(device_handle)
        return self.device_factory.create(device_handle, device_info)

    def open_device_as(self, device_id: str, transport: str, operating_mode: TLMC_OperatingMode, expected_type: Type[TDev]) -> TDev:
        device = self.open_device(device_id, transport, operating_mode)

        if not isinstance(device, expected_type):
            raise TypeError(
                f"Factory produced {type(device).__name__}; "
                f"expected {expected_type.__name__}"
            )
        return device

    def create_simulation(self, description: dict[str, str]) -> None:
        self.native_functions.create_simulation(description)

    def remove_simulation(self, description: str) -> None:
        self.native_functions.remove_simulation(description)