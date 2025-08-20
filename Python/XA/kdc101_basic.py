"""
XA example for the KDC101 controllers
Date of Creation(YYYY-MM-DD): 2025-08-15
Date of Last Modification on Github: 2025-08-20
Python Version Used: python 3.13.3
XA software version: 1.2.7
"""

import time

from xa_sdk.products.kdc101 import KDC101
from xa_sdk.shared.xa_error_factory import XADeviceException
from xa_sdk.shared.tlmc_type_structures import *
from xa_sdk.native_sdks.xa_sdk import XASDK


def main():
    try:
        # Create XASDK object and startup XA system. 
        XASDK.try_load_library(__file__)
        XASDK.startup("")

        # Create device object and enable channel. 
        device = KDC101("27006239", "", TLMC_OperatingModes.Default)
        device.set_enable_state(TLMC_ChannelEnableStates.ChannelEnabled)
        
        # Get Connected controller part number and available methods.
        print("Device part number is:", device.get_hardware_info(TLMC_Wait.TLMC_InfiniteWait))
        device.get_method_list()
        
        # Get list of available stages/actuators and set the apropriate motor profile.
        print("Compatible products:", device.get_connected_products_supported())
        time.sleep(.5)
        device.set_connected_product('Z912')

        # Convert unit methods used to work in real world units.
        new_val = device.convert_from_physical_to_device(TLMC_ScaleType.TLMC_ScaleType_Velocity, TLMC_Unit.TLMC_Unit_Millimetres, 10)
        new_val = device.convert_from_device_units_to_physical(TLMC_ScaleType.TLMC_ScaleType_Distance, 8689)
        print("New converted value is:", new_val.converted_value, "Unit:", new_val.unit)
        
        # Preform home and moves. 
        device.home(TLMC_Wait.TLMC_InfiniteWait)
        device.move_absolute(TLMC_MoveModes.MoveMode_Absolute, new_val.converted_value, TLMC_Wait.TLMC_InfiniteWait)
        print(device.get_move_absolute_params(TLMC_Wait.TLMC_InfiniteWait).absolute_position)
        print("New current position is:", device.get_position_counter(TLMC_Wait.TLMC_InfiniteWait))

        # close device and shutdown XA system.
        device.disconnect()
        device.close()
        XASDK.shutdown()

    except XADeviceException as e:
        device.close()
        print(e.error_code)
        XASDK.shutdown()

main()
