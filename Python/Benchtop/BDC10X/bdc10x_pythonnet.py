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
clr.AddReference("C:\\Program Files\\Thorlabs\\Kinesis\\ThorLabs.MotionControl.Benchtop.DCServoCLI.dll")
from Thorlabs.MotionControl.DeviceManagerCLI import *
from Thorlabs.MotionControl.GenericMotorCLI import *
from Thorlabs.MotionControl.Benchtop.DCServoCLI import *
from System import Decimal  # necessary for real world units

def main():
    """The main entry point for the application"""

    # Uncomment this line if you are using
    SimulationManager.Instance.InitializeSimulations()

    try:

        DeviceManagerCLI.BuildDeviceList()

        # create new device
        serial_no = "43000001"  # Replace this line with your device's serial number

        # Connect
        device = BenchtopDCServo.CreateBenchtopDCServo(serial_no)
        device.Connect(serial_no)

        # Retrieve channel for the device
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
        motor_config = channel.LoadMotorConfiguration(channel.DeviceID)
        time.sleep(0.25)

        # Get parameters related to homing/zeroing/other
        # These include Offset Distance, Velocity, Direction, and Limit Switch
        homing_params = channel.GetHomingParams()
        homing_params.Velocity = Decimal(5.0)  # real world units

        channel.SetHomingParams(homing_params)

        # Home or Zero the device (if a motor/piezo)
        print("Homing channel")
        channel.Home(60000)  # 60 second timeout
        print("Channel Homed.")

        # Retrieve and edit velocity params
        vel_params = channel.GetVelocityParams()
        vel_params.MaxVelocity = Decimal(5.0)  # This is distinct from homing
        vel_params.Acceleration = Decimal(1000.0)

        channel.SetVelocityParams(vel_params)

        # Move the device to a new position
        print("Moving to new position")
        new_pos = Decimal(5.0)  # real units
        channel.MoveTo(new_pos, 60000)  # 60 second timeout
        print("Channel Moved.")

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
