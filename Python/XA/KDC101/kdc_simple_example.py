"""
Example Title: KDC101 simple example
Example Date of Creation(YYYY-MM-DD) 2026-07-26
Example Date of Last Modification on Github 2026-07-26
Version of Python 3.13
Version of the Thorlabs XA 1.7.14
Version of Python wrapper 1.2.1.27471
==================
Example Description: The example shows how to connect to a KDC101 device, enable it, home it, and move it to an absolute position. 
The example also shows how to convert between device units and physical units.
"""

import platform

from thorlabs_xa.products.kdc101 import Kdc101
from thorlabs_xa.shared.system_manager import SystemManager
from thorlabs_xa.shared.enums import TLMC_ScaleType, TLMC_EnableState, TLMC_Unit, TLMC_MoveMode, TLMC_OperatingMode,TLMC_ResultCode,TLMC_Wait
from thorlabs_xa.shared.params import TLMC_DeviceInfo, TLMC_Unit
from thorlabs_xa.shared.xa_error_factory import XADeviceException

KDC101_PART_NUMBER = "KDC101"
DEFAULT_TIMEOUT = 500

# Use simulated device to test the example if you do not have a KDC101 connected to your system. The simulation will be created with the following configuration:
SIMULATION_CONFIG_STRING = { "PartNumber" : KDC101_PART_NUMBER, "SerialNumber" : "27001234", "ActuatorType" : "MTS25-Z8" }

def create_simulation(system_manager: SystemManager) -> TLMC_DeviceInfo:

    system_manager.create_simulation(SIMULATION_CONFIG_STRING)

    device_info = TLMC_DeviceInfo()

    device_info.device_type_description = SIMULATION_CONFIG_STRING["PartNumber"]
    device_info.device = SIMULATION_CONFIG_STRING["SerialNumber"]
    device_info.transport = ""

    return device_info

def main():

    # Create system manager for device discovery and management. 
    system_manager = SystemManager.instance()

    if platform.system() == "Linux":
        # If using Linux, we are required to state the port explicitly. Replace if you require an alternative port.
        system_manager.startup("deviceDiscovery.connections=/dev/ttyUSB0")
    else:
        # If using Windows, we can use the default settings.
        system_manager.startup()

    # Find devices
    devices = system_manager.get_device_list()
    device_info: TLMC_DeviceInfo | None = None
    if not devices:
        print("No devices found, check that your device is powered and is visible to your system. Continuing with simulation!")
        device_info = create_simulation(system_manager)
    else:
        print("Devices found:")
        for listed_device_info in devices:            
            if listed_device_info.part_number == KDC101_PART_NUMBER:
                device_info = listed_device_info
                print("KDC101 found.")

        if not device_info:
            print("No KDC101 devices found, check that your device is powered and is visible to your system. Continuing with simulation!")
            device_info = create_simulation(system_manager)


    try:
        # Create device object and enable device.
        device = system_manager.open_device_as(device_info.device, device_info.transport, TLMC_OperatingMode.TLMC_OperatingMode_Default, Kdc101)

        print("Enabling KDC101...")
        device.set_enable_state(TLMC_EnableState.TLMC_Enabled)

        enable_state = device.get_enable_state(DEFAULT_TIMEOUT)

        if enable_state == TLMC_EnableState.TLMC_Enabled:
            print("KDC101 enabled.")
        else:
            print("KDC101 not enabled as expected.")
            return
        
        # --- HOME ---
        print("Homing...")
        device.home(TLMC_Wait.TLMC_InfiniteWait)    

        # Get position after home
        home_position_deviceunits = device.get_position_counter(TLMC_Wait.TLMC_InfiniteWait)
        print(f"Position after home in device units: {home_position_deviceunits}")
        # Converting position to physical units
        home_position_physical, physical_unit = device.convert_from_device_units_to_physical(TLMC_ScaleType.TLMC_ScaleType_Distance, home_position_deviceunits)
        print(f"Position after home: {home_position_physical} {physical_unit.name}")

        # --- ABSOLUTE MOVE ---
        #convert 2mm to device units
        newposition_deviceunits = device.convert_from_physical_to_device(TLMC_ScaleType.TLMC_ScaleType_Distance, TLMC_Unit.TLMC_Unit_Millimetres, 2)

        print("Move absolute to 2mm... ")
        device.move(TLMC_MoveMode.TLMC_MoveMode_Absolute, newposition_deviceunits, TLMC_Wait.TLMC_InfiniteWait)
    
    except XADeviceException as e:

        print("Encountered error, code: ", e.error_code, TLMC_ResultCode(e.error_code).name)


    finally:

        if device is not None:
            print("Shutting down KDC101...")
            device.disconnect()
            device.close()

        print("Shutting down system...")
        system_manager.shutdown()

    print("Completed.")



main()