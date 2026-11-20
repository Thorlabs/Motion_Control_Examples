from typing import Protocol, runtime_checkable

from thorlabs_xa.shared.params import TLMC_PZIM_EthernetParams

@runtime_checkable
class EthernetParams(Protocol):

    def get_ethernet_params(self, max_wait_in_milliseconds: int) -> TLMC_PZIM_EthernetParams:...

    def set_ethernet_params(self, params: TLMC_PZIM_EthernetParams) -> None:...
