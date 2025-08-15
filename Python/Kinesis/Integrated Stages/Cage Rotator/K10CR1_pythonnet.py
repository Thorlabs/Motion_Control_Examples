"""
Example Title: K10CR1_pythonnet.py
Example Date of Creation(YYYY-MM-DD) 2023-02-23
Example Date of Last Modification on Github 2025-04-09
Version of Python: 3.11
Version of the Thorlabs SDK used: 1.14.52
==================
Example Description
Using the .NET Dlls
Example runs the K10CR1 or K10CR2 stage. It shows how to initialize, home and move.
Tested with K10CR2
"""

import clr 
import time 

# Write in file paths of dlls needed. 
clr.AddReference("C:\\Program Files\\Thorlabs\\Kinesis\\Thorlabs.MotionControl.DeviceManagerCLI.dll")
clr.AddReference("C:\\Program Files\\Thorlabs\\Kinesis\\Thorlabs.MotionControl.GenericMotorCLI.dll")
clr.AddReference("C:\\Program Files\\Thorlabs\\Kinesis\\ThorLabs.MotionControl.IntegratedStepperMotorsCLI.dll")

# Import functions from dlls. 
from Thorlabs.MotionControl.DeviceManagerCLI import *
from Thorlabs.MotionControl.GenericMotorCLI import *
from Thorlabs.MotionControl.IntegratedStepperMotorsCLI import *
from System import Decimal 


def main():
    """The main entry point for the application"""

    # Uncomment this line if you are using
    #SimulationManager.Instance.InitializeSimulations()

    try:
        # Build device list.  
        DeviceManagerCLI.BuildDeviceList()

        # create new device.
        serial_no = "55507804"  # Replace this line with your device's serial number.
        device = CageRotator.CreateCageRotator(serial_no)
       
        # Connect to device. 
        device.Connect(serial_no)

        # Ensure that the device settings have been initialized.
        if not device.IsSettingsInitialized():
            device.WaitForSettingsInitialized(10000)  # 10 second timeout.
            assert device.IsSettingsInitialized() is True

        # Start polling loop and enable device.
        device.StartPolling(250)  #250ms polling rate.
        time.sleep(0.25)
        device.EnableDevice()
        time.sleep(0.25)  # Wait for device to enable.

        # Get Device Information and display description.
        device_info = device.GetDeviceInfo()
        print(device_info.Description)

        # Load any configuration settings needed by the controller/stage.
        motor_config=device.LoadMotorConfiguration(serial_no, DeviceConfiguration.DeviceSettingsUseOptionType.UseFileSettings)

        # Call device methods.
        print("Homing Device")
        device.Home(60000)  # 60 second timeout.
        print("Done")

        new_pos = Decimal(150.0)  # Must be a .NET decimal.
        print(f'Moving to {new_pos}')
        device.MoveTo(new_pos, 60000)  # 60 second timeout.
        print("Done")

        # Stop polling loop and disconnect device before program finishes. 
        device.StopPolling()
        device.Disconnect()

    except Exception as e:
        print(e)
        
    # Uncomment this line if you are using Simulations
    #SimulationManager.Instance.UninitializeSimulations()


if __name__ == "__main__":
    main()