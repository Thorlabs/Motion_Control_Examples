"""
XA example for the BSC20x controllers
Date of Creation(YYYY-MM-DD): 2025-08-15
Date of Last Modification on Github: 2025-08-20
Python Version Used: python 3.13.3
XA software version: 1.2.7
"""


import time

from xa_sdk.native_sdks.xa_sdk import XASDK
from xa_sdk.shared.tlmc_type_structures import *
from xa_sdk.shared.xa_error_factory import XADeviceException
from xa_sdk.products.bsc20x import BSC20X
from xa_sdk.products.bsc20x_channel import BSC20XCHANNEL


def main():
    try:
        # Create XASDK object and startup XA system.
        XASDK.try_load_library(__file__)
        XASDK.startup("")

        # Create device object, channel object and enable channel.
        device = BSC20X("70119844", "", TLMC_OperatingModes.Default)
        channel = BSC20XCHANNEL("90119845", "", TLMC_OperatingModes.Default)
        channel.set_enable_state(TLMC_ChannelEnableStates.ChannelEnabled)
        
        # Get Connected controller part number and available methods.
        print("Device part number is:", device.get_hardware_info(TLMC_Wait.TLMC_InfiniteWait).part_number)
        channel.get_method_list()

        # Get list of available stages/actuators and set the apropriate motor profile.
        print(channel.get_connected_products_supported())
        channel.set_connected_product("DRV208")

        # Convert unit methods used to work in real world units.
        new_val = channel.convert_from_physical_to_device(TLMC_ScaleType.TLMC_ScaleType_Distance, TLMC_Unit.TLMC_Unit_Millimetres, 8)
        new_val = channel.convert_from_device_units_to_physical(TLMC_ScaleType.TLMC_ScaleType_Distance, 880000)
        print("New converted value is:", new_val.converted_value, "Unit:", new_val.unit)
        
        # Preform home and moves. 
        channel.home(12000)
        channel.set_move_absolute_params(6553600)
        channel.move_absolute(TLMC_MoveModes.MoveMode_AbsoluteToProgrammedPosition, new_val.converted_value, TLMC_Wait.TLMC_InfiniteWait)
        print("New current position is:", channel.get_position_counter(TLMC_Wait.TLMC_InfiniteWait))

        # Close references, disconnect from controller and shutdown XA system.
        channel.close()
        device.disconnect()
        device.close()
        XASDK.shutdown()

    except XADeviceException as e:
        device.close()
        device.shutdown()
        print(e.error_code)
        XASDK.shutdown()

main()
