"""
BSC101 Pythonnet Example
Date of Creation(YYYY-MM-DD): 2023-05-19
Date of Last Modification on Github: 2023-05-24
Python Version Used: python 3.10.5
Kinesis Version Tested: 1.14.40

"""
import os
import time
import sys
import clr

clr.AddReference("C:\\Program Files\\Thorlabs\\Kinesis\\Thorlabs.MotionControl.DeviceManagerCLI.dll")
clr.AddReference("C:\\Program Files\\Thorlabs\\Kinesis\\Thorlabs.MotionControl.GenericMotorCLI.dll")
clr.AddReference("C:\\Program Files\\Thorlabs\\Kinesis\\Thorlabs.MotionControl.Benchtop.StepperMotorCLI.dll")
from Thorlabs.MotionControl.DeviceManagerCLI import *
from Thorlabs.MotionControl.GenericMotorCLI import *
from Thorlabs.MotionControl.Benchtop.StepperMotorCLI import *
from System import Decimal  # necessary for real world units

def main():
    """The main entry point for the application"""

    # Uncomment this line if you are using
    # SimulationManager.Instance.InitializeSimulations()

    try:

        DeviceManagerCLI.BuildDeviceList()

        # create new device
        serial_no = "40000001"  # Replace this line with your device's serial number

        # Connect, begin polling, and enable
        device = BenchtopStepperMotor.CreateBenchtopStepperMotor(serial_no)
        device.Connect(serial_no)
        time.sleep(0.25)  # wait statements are important to allow settings to be sent to the device

        # For benchtop devices, get the channel
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
        channel_config = channel.LoadMotorConfiguration(serial_no) # If using BSC203, change serial_no to channel.DeviceID. 
        chan_settings = channel.MotorDeviceSettings

        channel.GetSettings(chan_settings)

        channel_config.DeviceSettingsName = 'HS NRT150 Enc Stage 150mm'

        channel_config.UpdateCurrentConfiguration()

        channel.SetSettings(chan_settings, True, False)

        # Get parameters related to homing/zeroing/other

        # Home or Zero the device (if a motor/piezo)
        print("Homing Motor")
        channel.Home(60000)
        print("Done")
        # Move the device to a new position
        channel.SetMoveRelativeDistance(Decimal(5.0))

        print("Moving 10 times")
        for i in range(10):
            channel.MoveRelative(10000)
            time.sleep(5)
        print("Done")

        # Stop Polling and Disconnect
        channel.StopPolling()
        device.Disconnect()

    except Exception as e:
        # this can be bad practice: It sometimes obscures the error source
        print(e)

    # Uncomment this line if you are using Simulations
    # SimulationManager.Instance.UninitializeSimulations()
    ...


if __name__ == "__main__":
    main()
