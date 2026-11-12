"""
Example Title: KST201 simple example
Example Date of Creation(YYYY-MM-DD) 2026-11-11
Example Date of Last Modification on Github 2026-11-11
Version of Python 3.13
Version of the Thorlabs XA 1.13.3
Version of Python wrapper 1.3.0.27658
==================
Example Description: The example shows how to connect to a KST201 device, enable it, home it, and move it to an absolute position. 
The example also shows how to convert between device units and physical units.
"""

import platform

from thorlabs_xa.shared.enums import TLMC_ScaleType, TLMC_EnableState, TLMC_Unit, TLMC_MoveMode, TLMC_OperatingMode,TLMC_ResultCode,TLMC_Wait
from thorlabs_xa.shared.params import TLMC_DeviceInfo, TLMC_Unit
from thorlabs_xa.shared.xa_error_factory import XADeviceException

##########
from thorlabs_xa.products.kst201 import Kst201
from thorlabs_xa.shared.system_manager import SystemManager
from thorlabs_xa.shared.xa_error_factory import XADeviceException
from thorlabs_xa.shared.enums import (
    TLMC_ScaleType,
    TLMC_Unit,
    TLMC_Wait,
    TLMC_ResultCode,
    TLMC_EnableState,
    TLMC_OperatingMode,
    TLMC_MoveMode
)
from thorlabs_xa.shared.params import (
    TLMC_DeviceInfo,
)

KST201_PART_NUMBER = "KST201"
DEFAULT_TIMEOUT = 5000

# Use simulated device to test the example if you do not have a KST201 connected to your system. The simulation will be created with the following configuration:
SIMULATION_CONFIG = {
    "PartNumber": KST201_PART_NUMBER,
    "SerialNumber": "26006127",
    "ActuatorType": "ZFS06",
}

def create_simulation(system_manager: SystemManager) -> TLMC_DeviceInfo:
    system_manager.create_simulation(SIMULATION_CONFIG)

    device_info = TLMC_DeviceInfo()
    device_info.device_type_description = SIMULATION_CONFIG["PartNumber"]
    device_info.device = SIMULATION_CONFIG["SerialNumber"]
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
            if listed_device_info.part_number == KST201_PART_NUMBER:
                device_info = listed_device_info
                print("KST201 found.")

        if not device_info:
            print("No KST201 devices found, check that your device is powered and is visible to your system. Continuing with simulation!")
            device_info = create_simulation(system_manager)

    try:
        # Open device
        device = system_manager.open_device_as(
            device_info.device,
            device_info.transport,
            TLMC_OperatingMode.TLMC_OperatingMode_Default,
            Kst201
        )

    
        print("Enabling KST201...")
        device.set_enable_state(TLMC_EnableState.TLMC_Enabled)

        enable_state = device.get_enable_state(DEFAULT_TIMEOUT)

        if enable_state == TLMC_EnableState.TLMC_Enabled:
            print("KST201 enabled.")
        else:
            print("KST201 not enabled as expected.")
            return
        
        # --- HOME ---
        print("Homing...")
        device.home(TLMC_Wait.TLMC_InfiniteWait)    

        # --- ABSOLUTE MOVE ---
        #convert 2mm to device units
        newposition_deviceunits = device.convert_from_physical_to_device(TLMC_ScaleType.TLMC_ScaleType_Distance, TLMC_Unit.TLMC_Unit_Millimetres, 2)

        print("Move absolute to 2mm... ")
        device.move(TLMC_MoveMode.TLMC_MoveMode_Absolute, newposition_deviceunits, TLMC_Wait.TLMC_InfiniteWait)

        # Get position after home
        moved_position_deviceunits = device.get_position_counter(TLMC_Wait.TLMC_InfiniteWait)
        print(f"Position after home in device units: {moved_position_deviceunits}")
        # Converting position to physical units
        moved_position_physical, physical_unit = device.convert_from_device_units_to_physical(TLMC_ScaleType.TLMC_ScaleType_Distance, moved_position_deviceunits)
        print(f"Position after home: {moved_position_physical} {physical_unit.name}")

    except XADeviceException as e:

        print("Encountered error, code: ", e.error_code, TLMC_ResultCode(e.error_code).name)


    finally:

        if device is not None:
            print("Shutting down KST201...")
            device.disconnect()
            device.close()

        print("Shutting down system...")
        system_manager.shutdown()

    print("Completed.")

if __name__ == "__main__":
    main()

