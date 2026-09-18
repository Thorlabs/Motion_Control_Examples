from typing import Protocol, runtime_checkable

from thorlabs_xa.shared.params import TLMC_FirmwareVersion

@runtime_checkable
class FirmwareVersionInfo(Protocol):

    def get_firmware_version_info(self, max_wait_in_milliseconds: int) -> tuple [TLMC_FirmwareVersion, TLMC_FirmwareVersion]: ...