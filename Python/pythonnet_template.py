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
clr.AddReference("C:\\Program Files\\Thorlabs\\Kinesis\\ThorLabs.MotionControl.<>.dll")
from Thorlabs.MotionControl.DeviceManagerCLI import *
from Thorlabs.MotionControl.GenericMotorCLI import *
# from Thorlabs.MotionControl.<> import *
from System import Decimal  # necessary for real world units

def main():
    """The main entry point for the application"""

    # Uncomment this line if you are using
    # SimulationManager.Instance.InitializeSimulations()

    try:

        DeviceManagerCLI.BuildDeviceList()

        # create new device
        serial_no = "26000001"  # Replace this line with your device's serial number

        # Connect, begin polling, and enable
        device = None

        # Ensure that the device settings have been initialized
        if not device.IsSettingsInitialized():
            device.WaitForSettingsInitialized(10000)  # 10 second timeout
            assert device.IsSettingsInitialized() is True

        # Start polling and enable
        device.StartPolling(250)  #250ms polling rate
        time.sleep(25)
        device.Enable()
        time.sleep(0.25)  # Wait for device to enable

        # Get Device Information and display description
        device_info = device.GetDeviceInfo()
        print(device_info.Description)

        # Load any configuration settings needed by the controller/stage

        # Get parameters related to homing/zeroing/other

        # Home or Zero the device (if a motor/piezo)

        # Move the device to a new position

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
