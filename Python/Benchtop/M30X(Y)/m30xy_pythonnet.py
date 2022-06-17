"""An example that uses the .NET Kinesis Libraries to connect to a KDC."""
import os
import time
import sys
import clr
import numpy as np

# Add References to .NET libraries
clr.AddReference("C:\\Program Files\\Thorlabs\\Kinesis\\Thorlabs.MotionControl.DeviceManagerCLI.dll")
clr.AddReference("C:\\Program Files\\Thorlabs\\Kinesis\\Thorlabs.MotionControl.GenericMotorCLI.dll")
clr.AddReference("C:\\Program Files\\Thorlabs\\Kinesis\\Thorlabs.MotionControl.Benchtop.DCServoCLI.dll.")


from Thorlabs.MotionControl.DeviceManagerCLI import *
from Thorlabs.MotionControl.GenericMotorCLI import *
from Thorlabs.MotionControl.Benchtop.DCServoCLI import *
from System import Decimal


def main():
    """The main entry point for the application"""

    # Uncomment this line if you are using
    # SimulationManager.Instance.InitializeSimulations()

    try:

        DeviceManagerCLI.BuildDeviceList()
        # create new device
        serial_no = "101272674"  # Replace this line with your device's serial number

        device = BenchtopDCServo.CreateBenchtopDCServo(serial_no)

        # Connect, begin polling, and enable
        device.Connect(serial_no)
        time.sleep(0.25)  # wait statements are important to allow settings to be sent to the device

        # Get Device Information and display description
        device_info = device.GetDeviceInfo()
        print(device_info.Description)

        # Get the channel for the device
        x_channel = device.GetChannel(1)  # Returns a benchtop channel object
        y_channel = device.GetChannel(2)

        # Start Polling and enable channel
        x_channel.StartPolling(250)
        y_channel.StartPolling(250)
        time.sleep(0.25)
        x_channel.EnableDevice()
        y_channel.EnableDevice()
        time.sleep(0.25)

        # Check that the settings are initialised, else error.
        if not x_channel.IsSettingsInitialized() or not y_channel.IsSettingsInitialized():
            x_channel.WaitForSettingsInitialized(10000)  # 10 second timeout
            y_channel.WaitForSettingsInitialized(10000)
            assert device.IsSettingsInitialized() is True

        # Load the motor configuration on the channel
        x_config = x_channel.LoadMotorConfiguration(x_channel.DeviceID)
        y_config = y_channel.LoadMotorConfiguration(y_channel.DeviceID)

        # Read in the device settings
        dev_settings = x_channel.MotorDeviceSettings

        # Get the Homing Params
        x_home_params = x_channel.GetHomingParams()
        y_home_params = y_channel.GetHomingParams()

        x_home_params.Velocity = Decimal(2.0)
        y_home_params.Velocity = Decimal(2.0)

        # Home the device
        print("Homing X Channel")
        x_channel.Home(60000)  # 60 second timeout
        print("Homing Y Channel")
        y_channel.Home(60000)

        # Create circle coordinates
        angles = np.arange(0, 2 * np.pi, 0.025)
        radius = 10.0  # mm
        xs = radius * np.cos(angles)
        ys = radius * np.sin(angles)

        x_vel_params = x_channel.GetVelocityParams()
        y_vel_params = y_channel.GetVelocityParams()

        x_vel_params.Acceleration = Decimal(5.0)
        x_vel_params.MaxVelocity = Decimal(2.4)
        y_vel_params.Acceleration = Decimal(5.0)
        y_vel_params.MaxVelocity = Decimal(2.4)

        x_channel.SetVelocityParams(x_vel_params)
        y_channel.SetVelocityParams(y_vel_params)

        # Go to a new position
        for i in range(len(angles)):
            x_channel.MoveTo(Decimal(float(xs[i])), 20000)
            y_channel.MoveTo(Decimal(float(ys[i])), 20000)

        # Return to Home
        x_channel.Home(60000)
        y_channel.Home(60000)

        # Stop polling and exit
        x_channel.StopPolling()
        device.Disconnect()
    except Exception as e:
        print(e)

    # Uncomment this line if you are using Simulations
    # SimulationManager.Instance.UninitializeSimulations()
    ...


if __name__ == "__main__":
    main()
