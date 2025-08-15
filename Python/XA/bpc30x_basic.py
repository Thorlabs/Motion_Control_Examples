import time


from xa_sdk.native_sdks.xa_sdk import XASDK
from xa_sdk.shared.tlmc_type_structures import *
from xa_sdk.shared.xa_error_factory import XADeviceException
from xa_sdk.products.bpc30x import BPC30X
from xa_sdk.products.bpc30x_channel import BPC30XCHANNEL


def main():
    try:
        # Create XASDK object and startup XA system.
        XASDK.try_load_library(__file__)
        XASDK.startup("")

        # Create device object, channel object and enable channel.
        device = BPC30X("71897133", "", TLMC_OperatingModes.Default)
        channel = BPC30XCHANNEL("91897134", "", TLMC_OperatingModes.Default)
        channel.set_enable_state(TLMC_ChannelEnableStates.ChannelEnabled)
        
        # Get Connected controller part number and available methods.
        print("Device part number is:", device.get_hardware_info(TLMC_Wait.TLMC_InfiniteWait))
        channel.get_method_list()

        # Convert unit methods used to work in real world units.
        new_val = channel.convert_from_physical_to_device(TLMC_ScaleType.TLMC_ScaleType_Voltage, TLMC_Unit.TLMC_Unit_Volts, 25)
        new_val = channel.convert_from_device_units_to_physical(TLMC_ScaleType.TLMC_ScaleType_Voltage, 880000)
        print("New converted value is:", new_val.converted_value, "Unit:", new_val.unit)

        # Zero channel and preform moves
        channel.set_zero(TLMC_Wait.TLMC_InfiniteWait)
        channel.set_max_output_voltage(new_val.converted_value)
        channel.set_output_voltage(new_val.converted_value)
        time.sleep(1)
        print("New output voltage is:", channel.get_output_voltage(TLMC_Wait.TLMC_InfiniteWait))
        print("New max output voltage is:", channel.get_max_output_voltage_params(TLMC_Wait.TLMC_InfiniteWait))

        # Close references, disconnect from controller and shutdown XA system.
        channel.close()
        device.disconnect()
        device.close()
        XASDK.shutdown()

    except XADeviceException as e:
        device.close()
        device.shutdown
        print(e.error_code)
        XASDK.shutdown()

main()