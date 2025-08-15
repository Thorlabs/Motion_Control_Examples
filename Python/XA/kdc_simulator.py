import time

from xa_sdk.products.kdc101 import KDC101
from xa_sdk.products.kbd101 import KBD101
from xa_sdk.products.kst201 import KST201
from xa_sdk.products.bbd30x_channel import BBD30XCHANNEL
from xa_sdk.products.bbd30x import BBD30X
from xa_sdk.products.bsc20x import BSC20X
from xa_sdk.products.bsc20x_channel import BSC20XCHANNEL
from xa_sdk.native_sdks.xa_sdk import XASDK
from xa_sdk.shared.tlmc_type_structures import *
from xa_sdk.shared.xa_error_factory import XADeviceException

def main():        
    try:
        # Create instance of SDK object to start up XA system.
        XASDK.try_load_library(__file__)
        XASDK.startup("")

        # Create simulation string and device object. 
        kdc_simulation = {"PartNumber":"KDC101","SerialNumber":"27265111","ActuatorType":"Z825"} 
        XASDK.create_simulation(kdc_simulation)
        device = KDC101("27265111", "", TLMC_OperatingModes.Default)
        
        # Enable the channel and get list of available methods.
        device.set_enable_state(TLMC_ChannelEnableStates.ChannelEnabled)
        print("Device part number is:", device.get_hardware_info(12000).part_number)
        device.get_method_list()

        # Convert methods to work in real world units. 
        new_val = device.convert_from_physical_to_device(TLMC_ScaleType.TLMC_ScaleType_Distance, TLMC_Unit.TLMC_Unit_Millimetres, 880000)
        new_val = device.convert_from_device_units_to_physical(TLMC_ScaleType.TLMC_ScaleType_Acceleration, 880000)
        print("New converted value is:", new_val.converted_value, "Unit:", new_val.unit)

        # Preform home and move methods. 
        device.home(0)
        device.set_move_absolute_params(new_val.converted_value)
        time.sleep(1)
        device.move_absolute(TLMC_MoveModes.MoveMode_Absolute, 9000, TLMC_Wait.TLMC_InfiniteWait)
        print("New current position is:", device.get_position_counter(12000))

        # Remove references and shutdown the XA system. 
        device.disconnect()
        device.close()
        XASDK.remove_simulation(kdc_simulation)
        XASDK.shutdown()
        
    except XADeviceException as e:
        device.close()
        print(e.error_code)
        XASDK.shutdown()


main()