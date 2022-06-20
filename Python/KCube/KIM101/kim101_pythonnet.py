"""
KIM101
==================

An example showing the usage of the Thorlabs Kinesis .NET API in controlling the KCube Intertial Motor Controller.
Uses the clr module from pythonnet package
Written and tested in python 3.10.5
"""
import os
import time
import sys
import clr

clr.AddReference("C:\\Program Files\\Thorlabs\\Kinesis\\Thorlabs.MotionControl.DeviceManagerCLI.dll")
clr.AddReference("C:\\Program Files\\Thorlabs\\Kinesis\\Thorlabs.MotionControl.GenericMotorCLI.dll")
clr.AddReference("C:\\Program Files\\Thorlabs\\Kinesis\\ThorLabs.MotionControl.KCube.InertialMotorCLI.dll")
from Thorlabs.MotionControl.DeviceManagerCLI import *
from Thorlabs.MotionControl.GenericMotorCLI import *
from Thorlabs.MotionControl.KCube.InertialMotorCLI import *
from System import Decimal  # necessary for real world units

def main():
    """The main entry point for the application"""

    # Uncomment this line if you are using
    SimulationManager.Instance.InitializeSimulations()

    try:

        DeviceManagerCLI.BuildDeviceList()

        # create new device
        serial_no = "74000001"  # Replace this line with your device's serial number

        device = KCubeInertialMotor.CreateKCubeInertialMotor(serial_no)

        # Connect
        device.Connect(serial_no)
        time.sleep(0.25)


        # Ensure that the device settings have been initialized
        if not device.IsSettingsInitialized():
            device.WaitForSettingsInitialized(10000)  # 10 second timeout
            assert device.IsSettingsInitialized() is True

        # Get Device Information and display description
        device_info = device.GetDeviceInfo()
        print(device_info.Description)
        # Start polling and enable channel
        device.StartPolling(250)  #250ms polling rate
        time.sleep(25)
        device.EnableDevice()
        time.sleep(0.25)  # Wait for device to enable

        # Load any configuration settings needed by the controller/stage
        inertial_motor_config = device.GetInertialMotorConfiguration(serial_no)

        # Get parameters related to homing/zeroing/moving
        device_settings = ThorlabsInertialMotorSettings.GetSettings(inertial_motor_config)

        # Step parameters for an intertial motor channel
        chan1 = InertialMotorStatus.MotorChannels.Channel1  # enum chan ident
        device_settings.Drive.Channel(chan1).StepRate = 500
        device_settings.Drive.Channel(chan1).StepAcceleration = 100000

        # Send settings to the device
        device.SetSettings(device_settings, True, True)

        # Home or Zero the device (if a motor/piezo)
        print("Zeroing device")
        device.SetPositionAs(chan1, 0)

        # Move the device to a new position
        new_pos = Decimal(5.0)
        print(f'Moving to position {new_pos}')
        device.MoveTo(chan1, new_pos, 60000)  # 60 second timeout
        print("Move Complete")

        # Stop Polling and Disconnect
        device.StopPolling()
        device.Disconnect()

    except Exception as e:
        print(e)

    # Uncomment this line if you are using Simulations
    SimulationManager.Instance.UninitializeSimulations()
    ...


if __name__ == "__main__":
    main()
