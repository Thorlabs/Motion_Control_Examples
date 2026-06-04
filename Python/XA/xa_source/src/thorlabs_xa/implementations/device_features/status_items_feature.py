from typing import List
from thorlabs_xa.interfaces.device_features.status_items import StatusItems
from thorlabs_xa.native_sdks.native_functions import NativeFunctions
from thorlabs_xa.shared.enums import TLMC_StatusItemId
from thorlabs_xa.shared.params import TLMC_StatusItem

class StatusItemsFeature(StatusItems):

    def __init__(self, device_handle: int, native_functions: NativeFunctions):

        self.device_handle = device_handle
        self.native_functions = native_functions

    def get_status_item(self, status_item_id: TLMC_StatusItemId) -> TLMC_StatusItem:

        return self.native_functions.get_status_item(self.device_handle, status_item_id)

    def get_status_item_count(self):

        return self.native_functions.get_status_item_count(self.device_handle)

    def get_status_items(self, start_index: int, number_of_items: int) -> List[TLMC_StatusItem]:

        return self.native_functions.get_status_items(self.device_handle, start_index, number_of_items)