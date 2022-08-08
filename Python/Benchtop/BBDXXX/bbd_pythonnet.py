"""
pythonnet_template
==================

A template useful for the creation of custom software for MotionControl Products.
Originally written in a python 3.10.5 environment with a pre-release version of pythonnet (June 22)
"""
import os
import time
import sys
import clr

clr.AddReference("C:\\Program Files\\Thorlabs\\Kinesis\\Thorlabs.MotionControl.DeviceManagerCLI.dll")
clr.AddReference("C:\\Program Files\\Thorlabs\\Kinesis\\Thorlabs.MotionControl.GenericMotorCLI.dll")
clr.AddReference("C:\\Program Files\\Thorlabs\\Kinesis\\ThorLabs.MotionControl.Benchtop.BrushlessMotorCLI.dll")
from Thorlabs.MotionControl.DeviceManagerCLI import *
from Thorlabs.MotionControl.GenericMotorCLI import *
from Thorlabs.MotionControl.Benchtop.BrushlessMotorCLI import *
from System import Decimal  # necessary for real world units

def main():
    """The main entry point for the application"""

    # Uncomment this line if you are using
    SimulationManager.Instance.InitializeSimulations()

    try:

        DeviceManagerCLI.BuildDeviceList()

        # create new device
        serial_no = "103000001"  # Replace this line with your device's serial number

        # Connect and retrieve a channel
        device = BenchtopBrushlessMotor.CreateBenchtopBrushlessMotor(serial_no)
        device.Connect(serial_no)

        channel = device.GetChannel(1)
        # Ensure that the device settings have been initialized
        if not channel.IsSettingsInitialized():
            channel.WaitForSettingsInitialized(10000)  # 10 second timeout
            assert channel.IsSettingsInitialized() is True

        # Start polling and enable
        channel.StartPolling(250)  #250ms polling rate
        time.sleep(25)
        channel.EnableDevice()
        time.sleep(0.25)  # Wait for device to enable

        # Get Device Information and display description
        device_info = channel.GetDeviceInfo()
        print(device_info.Description)

        # Load any configuration settings needed by the controller/stage
        print(channel)
        motor_config = channel.LoadMotorConfiguration(serial_no)
        device_settings = channel.MotorDeviceSettings

        channel.UpdateConfiguration()

        channel.SetSettings(device_settings)

        # Get parameters related to homing/zeroing/other
        home_params = channel.GetHomingParams()
        print(f'Homing Velocity: {home_params.Velocity}\n',
              f'Homing Direction: {home_params.Direction}')

        channel.SetHomingParams(home_params)  # If changes are made

        # Home or Zero the device (if a motor/piezo)
        print("Homing Channel")
        channel.Home(60000)  # 60 second timeout
        print("Channel Homed")

        # Get velocity parameters
        vel_params = channel.GetVelocityParams()
        print(f'Move Maximum Velocity: {vel_params.MaxVelocity}\n',
              f'Move Acceleration: {vel_params.Acceleration}')

        # Move the device to a new position
        new_pos = Decimal(10.0)  # in real units
        print(f'Moving to {new_pos}')
        channel.MoveTo(new_pos, 60000)  # 60 second timeout

        # Stop Polling and Disconnect
        channel.StopPolling()
        device.Disconnect()

    except Exception as e:
        print(e)

    # Uncomment this line if you are using Simulations
    SimulationManager.Instance.UninitializeSimulations()
    ...


if __name__ == "__main__":
    main()
