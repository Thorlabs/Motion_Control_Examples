import time

from xa_sdk.native_sdks.xa_sdk import XASDK
from xa_sdk.shared.tlmc_type_structures import *
from xa_sdk.shared.xa_error_factory import XADeviceException
from xa_sdk.products.kst201 import KST201

 
def main():
    try:
        # Create XASDK object and startup XA system.
        XASDK.try_load_library(__file__)
        XASDK.startup("")

        # Create device object and enable channel. 
        device = KST201("26250194", "", TLMC_OperatingModes.Default)
        device.set_enable_state(TLMC_ChannelEnableStates.ChannelEnabled)

        # Get Connected controller part number and available methods.
        print("Device part number is:", device.get_hardware_info(TLMC_Wait.TLMC_InfiniteWait).part_number)
        device.get_method_list()
        
        # Get list of available stages/actuators and set the apropriate motor profile. 
        print("Compatible products:\n", device.get_connected_products_supported())
        device.set_connected_product("ZFS13")
        
        # Convert unit methods used to work in real world units. 
        new_val = device.convert_from_physical_to_device(TLMC_ScaleType.TLMC_ScaleType_Distance, TLMC_Unit.TLMC_Unit_Millimetres, 13)
        new_val = device.convert_from_device_units_to_physical(TLMC_ScaleType.TLMC_ScaleType_Distance, 54613333)
        print("New converted value is:", new_val.converted_value, "Unit:", new_val.unit)

        device.home(TLMC_Wait.TLMC_InfiniteWait)
        time.sleep(1)
        device.set_move_relative_params(new_val)
        device.move_relative(TLMC_MoveModes.MoveMode_RelativeByProgrammedDistance, TLMC_Wait.TLMC_Unused ,TLMC_Wait.TLMC_InfiniteWait)
        print("New current position is", device.get_position_counter(TLMC_Wait.TLMC_InfiniteWait))

        # Close device and shutdown XA system. 
        device.disconnect()
        device.close()
        XASDK.shutdown()

    except XADeviceException as e:
        device.close()
        print(e.error_code)
        XASDK.shutdown()

main()
