from typing import Protocol, runtime_checkable

from thorlabs_xa.shared.enums import TLMC_IoPortNumber
from thorlabs_xa.shared.params import TLMC_IoConfigurationParams

@runtime_checkable
class IoConfigurationParams(Protocol):

    def get_io_configuration_number_of_ports_supported(self) -> int: ...

    def get_io_configuration_params(self, port_number: TLMC_IoPortNumber, max_wait_in_milliseconds: int) -> TLMC_IoConfigurationParams: ...

    def set_io_configuration_params(self, handle: int, port_number: TLMC_IoPortNumber, params: TLMC_IoConfigurationParams) -> None: ...