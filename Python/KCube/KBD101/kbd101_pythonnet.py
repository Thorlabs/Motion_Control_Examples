"""An example that uses the .NET Kinesis Libraries to connect to a KDC."""
import os
import time
import sys
import clr

# Add References to .NET libraries
clr.AddReference("C:\\Program Files\\Thorlabs\\Kinesis\\Thorlabs.MotionControl.DeviceManagerCLI.dll.")
clr.AddReference("C:\\Program Files\\Thorlabs\\Kinesis\\Thorlabs.MotionControl.GenericMotorCLI.dll.")
clr.AddReference("C:\\Program Files\\Thorlabs\\Kinesis\\Thorlabs.MotionControl.KCube.BrushlessMotorCLI.dll.")


from Thorlabs.MotionControl.DeviceManagerCLI import *
from Thorlabs.MotionControl.GenericMotorCLI import *
from Thorlabs.MotionControl.KCube.BrushlessMotorCLI import *


def main():
    """The main entry point for the application"""

    # Uncomment this line if you are using
    # SimulationManager.Instance.InitializeSimulations()

    try:

        # create new device
        serial_no = "28251092"  # Replace this line with your device's serial number
        kcube = KCubeBrushlessMotor.CreateKCubeBrushlessMotor(serial_no)

        # Connect, begin polling, and enable
        kcube.Connect(serial_no)
        time.Sleep(0.25)
        kcube.StartPolling(250)
        time.sleep(0.25)  # wait statements are important to allow settings to be sent to the device

        kcube.EnableDevice()
        time.sleep(0.25)  # Wait for device to enable


        # Stop polling and close device
        kcube.StopPolling()
        kcube.Disconnect()
    except Exception as e:
        print(e)

    # Uncomment this line if you are using Simulations
    # SimulationManager.Instance.UnitializeSimulations()
    ...
