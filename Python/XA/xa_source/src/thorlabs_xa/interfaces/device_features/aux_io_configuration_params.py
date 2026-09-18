from typing import Protocol, runtime_checkable

from thorlabs_xa.shared.enums import TLMC_AuxIoPortMode, TLMC_AuxIoPortNumber

@runtime_checkable
class AuxIoConfigurationParams(Protocol):

    def get_aux_io_port_mode(self, port_number: TLMC_AuxIoPortNumber, max_wait_in_milliseconds: int) -> TLMC_AuxIoPortMode: ...

    def set_aux_io_port_mode(self, port_number: TLMC_AuxIoPortNumber, port_mode: TLMC_AuxIoPortMode): ...

    def get_aux_io_software_states(self, max_wait_in_milliseconds: int) -> int: ...

    def set_aux_io_software_states(self, software_states: int): ...