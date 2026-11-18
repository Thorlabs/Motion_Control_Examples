"""
Example Title: KST201 KST101 XA Kinesis example
Example Date of Creation(YYYY-MM-DD) 2026-11-16
Example Date of Last Modification on Github 2026-11-16
Version of Python 3.13
Version of the Thorlabs XA 1.13.3
Version of Python wrapper 1.9.2
==================
This example shows that it is possible to simultaneously control one device with XA SDK and another device with Kinesis SDK. 
A KST201 is homed and moved to an absolute position using the Thorlabs XA SDK with the Python wrapper, 
while a KST101 is homed and moved to an absolute position using the Thorlabs Kinesis .NET dlls.
"""

#general import
import time

# XA imports
from thorlabs_xa.shared.system_manager import SystemManager
from thorlabs_xa.shared.enums import TLMC_ScaleType, TLMC_EnableState, TLMC_Unit, TLMC_MoveMode, TLMC_OperatingMode,TLMC_Wait
from thorlabs_xa.shared.params import TLMC_Unit
from thorlabs_xa.products.kst201 import Kst201

# Add References to Kinesis .NET libraries
import clr
from System import Decimal  # necessary for real world units
clr.AddReference("C:\\Program Files\\Thorlabs\\Kinesis\\Thorlabs.MotionControl.DeviceManagerCLI.dll")
clr.AddReference("C:\\Program Files\\Thorlabs\\Kinesis\\Thorlabs.MotionControl.GenericMotorCLI.dll")
clr.AddReference("C:\\Program Files\\Thorlabs\\Kinesis\\ThorLabs.MotionControl.KCube.StepperMotorCLI.dll")
from Thorlabs.MotionControl.DeviceManagerCLI import *
from Thorlabs.MotionControl.GenericMotorCLI import *
from Thorlabs.MotionControl.KCube.StepperMotorCLI import *

def main():

    try:

        #connect to Kinesis device, enable.

        DeviceManagerCLI.BuildDeviceList()

        # create new Kinesis device
        Kserial_no = "26003851"  # KST101 serial number
        Kdevice = KCubeStepper.CreateKCubeStepper(Kserial_no)

        # Connect
        Kdevice.Connect(Kserial_no)
        time.sleep(0.25)  # wait statements are important to allow settings to be sent to the device

        # Start polling and enable
        Kdevice.StartPolling(250)  #250ms polling rate
        time.sleep(0.25)
        print("Enabling KST101...")
        Kdevice.EnableDevice()
        time.sleep(0.25)  # Wait for device to enable
        # Configure Kinesis device
        use_file_settings = DeviceConfiguration.DeviceSettingsUseOptionType.UseFileSettings
        device_config = Kdevice.LoadMotorConfiguration(Kdevice.DeviceID, use_file_settings)


        #connect to XA device, enable.
        # Create system manager for device discovery and management. 
        system_manager = SystemManager.instance()
        system_manager.startup()
        XAserial_no = "26006127"  # KST201 serial number
             
        XAdevice = system_manager.open_device_as(XAserial_no, "", TLMC_OperatingMode.TLMC_OperatingMode_Default, Kst201)
            
        print("Enabling KST201...")
        XAdevice.set_enable_state(TLMC_EnableState.TLMC_Enabled)

        #Home
        print("Homing KST101...")
        Kdevice.Home(60000)  # 60 seconds
        print("Homing KST201...")
        XAdevice.home(TLMC_Wait.TLMC_InfiniteWait)

        #Move to a position  
        #move Kinesis device
        new_pos = Decimal(2.0)  # in Real Units
        print("Move KST101 absolute to 2mm... ")
        Kdevice.MoveTo(new_pos, 60000)

        #move XA device        
        newposition_deviceunits = XAdevice.convert_from_physical_to_device(TLMC_ScaleType.TLMC_ScaleType_Distance, TLMC_Unit.TLMC_Unit_Millimetres, 2)
        print("Move KST201 absolute to 2mm... ")
        XAdevice.move(TLMC_MoveMode.TLMC_MoveMode_Absolute, newposition_deviceunits, TLMC_Wait.TLMC_InfiniteWait)


    except Exception as e:
        print(e)

    finally:

        #For XA device:
        if XAdevice is not None:
            print("Shutting down KST201...")
            XAdevice.disconnect()
            XAdevice.close()

        print("Shutting down system...")
        system_manager.shutdown()

        #For Kinesis device:  Stop Polling and Disconnect
        print("Shutting down KST101...")
        Kdevice.StopPolling()
        Kdevice.Disconnect()


if __name__ == "__main__":
    main()