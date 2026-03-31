from typing import Protocol, runtime_checkable

from thorlabs_xa.shared.params import TLMC_ConnectedProductInfo

@runtime_checkable
class ConnectedProduct(Protocol):

    def get_connected_product_info(self) -> TLMC_ConnectedProductInfo: ...

    def set_connected_product_info(self, product_info: TLMC_ConnectedProductInfo) -> None: ...

    def set_connected_product(self, product_name: str) -> None: ...

    def get_connected_products_supported(self, max_length: int) -> tuple [str, int]: ...