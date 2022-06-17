"""An example that uses the .NET Kinesis Libraries to connect to a KDC."""
import os
import time
import sys
import clr

# Add References to .NET libraries
clr.AddReference("C:\\Program Files\\Thorlabs\\Kinesis\\Thorlabs.MotionControl.DeviceManagerCLI.dll")
clr.AddReference("C:\\Program Files\\Thorlabs\\Kinesis\\Thorlabs.MotionControl.GenericMotorCLI.dll")
clr.AddReference("C:\\Program Files\\Thorlabs\\Kinesis\\ThorLabs.MotionControl.KCube.StepperMotorCLI.dll")
from Thorlabs.MotionControl.DeviceManagerCLI import *
from Thorlabs.MotionControl.GenericMotorCLI import *
from Thorlabs.MotionControl.KCube.StepperMotorCLI import *
from System import Decimal  # necessary for real world units

def main():
    """The main entry point for the application"""

    # Uncomment this line if you are using
    SimulationManager.Instance.InitializeSimulations()

    try:

        DeviceManagerCLI.BuildDeviceList()

        # create new device
        serial_no = "26000001"  # Replace this line with your device's serial number
        device = KCubeStepper.CreateKCubeStepper(serial_no)

        # Connect
        device.Connect(serial_no)
        time.sleep(0.25)  # wait statements are important to allow settings to be sent to the device

        # Get Device Information and display description
        device_info = device.GetDeviceInfo()
        print(device_info.Description)

        # Start polling and enable
        device.StartPolling(250)  #250ms polling rate
        time.sleep(25)
        device.EnableDevice()
        time.sleep(0.25)  # Wait for device to enable

        # Configure device
        device_config = device.LoadMotorConfiguration(device.DeviceID)
        # Get homing settings
        home_params = device.GetHomingParams()
        print(f'Homing Velocity: {home_params.Velocity}')

        # Home device
        print("Homing Motor...")
        device.Home(60000)  # 60 seconds
        print("Motor Homed.")

        # Get/Set Velocity Params
        device_vel_params = device.GetVelocityParams()

        print(f'Acceleration: {device_vel_params.Acceleration}',
              f'Velocity: {device_vel_params.MaxVelocity}')

        # Set a position and move it
        new_pos = Decimal(5.0)  # in Real Units
        device.MoveTo(new_pos, 60000)

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