"""
K10CR1_RotationMethods_pythonnet
==================

An example of using the K10CR1 integrated rotation stages with python via pythonnet. Demonstrates MoveContinuous methods to rotate stage until user stops execution. 
"""

import clr 
import os 
import time 
import sys

# Write in file paths of dlls needed. 
clr.AddReference("C:\\Program Files\\Thorlabs\\Kinesis\\Thorlabs.MotionControl.DeviceManagerCLI.dll")
clr.AddReference("C:\\Program Files\\Thorlabs\\Kinesis\\Thorlabs.MotionControl.GenericMotorCLI.dll")
clr.AddReference("C:\\Program Files\\Thorlabs\\Kinesis\\ThorLabs.MotionControl.IntegratedStepperMotorsCLI.dll")

# Import functions from dlls. 
from Thorlabs.MotionControl.DeviceManagerCLI import *
from Thorlabs.MotionControl.GenericMotorCLI import *
from Thorlabs.MotionControl.GenericMotorCLI import MotorDirection
from Thorlabs.MotionControl.IntegratedStepperMotorsCLI import *
from System import Decimal 


def main():
    """The main entry point for the application"""

    # Uncomment this line if you are using
    # SimulationManager.Instance.InitializeSimulations()

    try:
        # Build device list.  
        DeviceManagerCLI.BuildDeviceList()

        # create new device.
        serial_no = "55000114"  # Replace this line with your device's serial number.
        device = CageRotator.CreateCageRotator(serial_no)
        
       
        # Connect to device. 
        device.Connect(serial_no)

        # Ensure that the device settings have been initialized.
        if not device.IsSettingsInitialized():
            device.WaitForSettingsInitialized(10000)  # 10 second timeout.
            assert device.IsSettingsInitialized() is True

        # Start polling loop and enable device.
        device.StartPolling(250)  #250ms polling rate.
        time.sleep(25)
        device.EnableDevice()
        time.sleep(25)  # Wait for device to enable.

        # Get Device Information and display description.
        device_info = device.GetDeviceInfo()
        print(device_info.Description)

        # Load any configuration settings needed by the controller/stage.
        device.LoadMotorConfiguration(serial_no, DeviceConfiguration.DeviceSettingsUseOptionType.UseDeviceSettings)
        motor_config = device.LoadMotorConfiguration(serial_no)

        # Call device methods.
        print("Homing Device")
        device.Home(60000)  # 60 second timeout.
        print("Done")

        new_direction_forward = MotorDirection.Forward 
        new_direction_backward = MotorDirection.Backward
        # new_velocity = 10 Only if using .MoveContinuousAtVelocity
        
        
        input("Press enter to initialize move")
        print("Press ctrl+c to stop movement")

        
        try:
            device.MoveContinuous(MotorDirection.Forward) # Set direction of Move
            # device.MoveContinuousAtVelocity('Forward', new_velocity) 
            while True:
                time.sleep(.1)
             
            


        except KeyboardInterrupt:
            print("Move Cancelled by User")
            device.StopImmediate()# Stop device, polling loop and disconnect device before program finishes. 
            device.StopPolling()
            device.Disconnect()

    except Exception as e:
        print(e)
        
    # Uncomment this line if you are using Simulations
    # SimulationManager.Instance.UninitializeSimulations()


if __name__ == "__main__":
    main()
