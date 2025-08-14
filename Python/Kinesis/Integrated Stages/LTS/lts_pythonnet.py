"""
lts_pythonnet
==================

An example of using the LTS integrated stages with python via pythonnet
"""
import os
import time
import sys
import clr

clr.AddReference("C:\\Program Files\\Thorlabs\\Kinesis\\Thorlabs.MotionControl.DeviceManagerCLI.dll")
clr.AddReference("C:\\Program Files\\Thorlabs\\Kinesis\\Thorlabs.MotionControl.GenericMotorCLI.dll")
clr.AddReference("C:\\Program Files\\Thorlabs\\Kinesis\\ThorLabs.MotionControl.IntegratedStepperMotorsCLI.dll")
from Thorlabs.MotionControl.DeviceManagerCLI import *
from Thorlabs.MotionControl.GenericMotorCLI import *
from Thorlabs.MotionControl.IntegratedStepperMotorsCLI import *
from System import Decimal  # necessary for real world units

def main():
    """The main entry point for the application"""

    # Uncomment this line if you are using
    # SimulationManager.Instance.InitializeSimulations()

    try:

        DeviceManagerCLI.BuildDeviceList()

        # create new device
        serial_no = "45877001"  # Replace this line with your device's serial number

        # Connect, begin polling, and enable
        device = LongTravelStage.CreateLongTravelStage(serial_no)
        device.Connect(serial_no)

        # Ensure that the device settings have been initialized
        if not device.IsSettingsInitialized():
            device.WaitForSettingsInitialized(10000)  # 10 second timeout
            assert device.IsSettingsInitialized() is True

        # Start polling and enable
        device.StartPolling(250)  #250ms polling rate
        time.sleep(0.25)
        device.EnableDevice()
        time.sleep(0.25)  # Wait for device to enable

        # Get Device Information and display description
        device_info = device.GetDeviceInfo()
        print(device_info.Description)

        # Load any configuration settings needed by the controller/stage
        motor_config = device.LoadMotorConfiguration(serial_no)

        # Get parameters related to homing/zeroing/other
        home_params = device.GetHomingParams()
        print(f'Homing velocity: {home_params.Velocity}\n,'
              f'Homing Direction: {home_params.Direction}')
        home_params.Velocity = Decimal(10.0)  # real units, mm/s
        # Set homing params (if changed)
        device.SetHomingParams(home_params)

        # Home or Zero the device (if a motor/piezo)
        print("Homing Device")
        device.Home(60000)  # 60 second timeout
        print("Done")

        # Get Velocity Params
        vel_params = device.GetVelocityParams()
        vel_params.MaxVelocity = Decimal(50.0)  # This is a bad idea
        device.SetVelocityParams(vel_params)
        # Move the device to a new position
        new_pos = Decimal(150.0)  # Must be a .NET decimal
        print(f'Moving to {new_pos}')
        device.MoveTo(new_pos, 60000)  # 60 second timeout
        print("Done")

        # Stop Polling and Disconnect
        device.StopPolling()
        device.Disconnect()

    except Exception as e:
        print(e)

    # Uncomment this line if you are using Simulations
    # SimulationManager.Instance.UninitializeSimulations()
    ...


if __name__ == "__main__":
    main()
