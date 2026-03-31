from thorlabs_xa.interfaces.device_features.connected_product import ConnectedProduct

from thorlabs_xa.native_sdks.native_functions import NativeFunctions

from thorlabs_xa.shared.params import TLMC_ConnectedProductInfo

class ConnectedProductFeature(ConnectedProduct):

    def __init__(self, device_handle: int, native_functions: NativeFunctions) -> None:
        self.device_handle = device_handle
        self.native_functions = native_functions

    def get_connected_product_info(self) -> TLMC_ConnectedProductInfo:
        return self.native_functions.get_connected_product_info(self.device_handle)

    def set_connected_product_info(self, product_info: TLMC_ConnectedProductInfo) -> None:
        self.native_functions.set_connected_product_info(self.device_handle, product_info)

    def set_connected_product(self, product_name: str) -> None:
        self.native_functions.set_connected_product(self.device_handle, product_name)

    def get_connected_products_supported(self, max_length: int) -> tuple [str, int]:
        return self.native_functions.get_connected_products_supported(self.device_handle, max_length)
