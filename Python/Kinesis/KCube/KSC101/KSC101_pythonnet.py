import os
import time
import sys
import clr

clr.AddReference("C:\\Program Files\\Thorlabs\\Kinesis\\Thorlabs.MotionControl.DeviceManagerCLI.dll")
clr.AddReference("C:\\Program Files\\Thorlabs\\Kinesis\\Thorlabs.MotionControl.GenericMotorCLI.dll")
clr.AddReference("C:\\Program Files\\Thorlabs\\Kinesis\\ThorLabs.MotionControl.KCube.SolenoidCLI.dll")
from Thorlabs.MotionControl.DeviceManagerCLI import *
from Thorlabs.MotionControl.GenericMotorCLI import *
from Thorlabs.MotionControl.KCube.SolenoidCLI import *
from System import Decimal  # necessary for real world units

def main():
    """The main entry point for the application"""

    # Uncomment this line if you are using simulation
    # SimulationManager.Instance.InitializeSimulations()

    try:

        DeviceManagerCLI.BuildDeviceList()

        # create new device
        serial_no = "68800377"  # Replace this line with your device's serial number

        # Connect
        device = KCubeSolenoid.CreateKCubeSolenoid(serial_no)
        device.Connect(serial_no)

        # Ensure that the device settings have been initialized
        if not device.IsSettingsInitialized():
            device.WaitForSettingsInitialized(10000)  # 10 second timeout
            assert device.IsSettingsInitialized() is True

        # Start polling and enable
        device.StartPolling(250)  #250ms polling rate
        time.sleep(0.25)
        device.EnableDevice()
        time.sleep(0.5)  # Wait for device to enable


        # Get Device Information and display description
        device_info = device.GetDeviceInfo()
        print(device_info.Description)

        device.SetOperatingMode(SolenoidStatus.OperatingModes.Manual)

        device.SetOperatingState(SolenoidStatus.OperatingStates.Active)
        time.sleep(5)
        device.SetOperatingState(SolenoidStatus.OperatingStates.Inactive)
        time.sleep(5)

        # Stop Polling and Disconnect
        device.StopPolling()
        device.Disconnect()

    except Exception as e:
        # this can be bad practice: It sometimes obscures the error source
        print(e)

    # Uncomment this line if you are using Simulations
    # SimulationManager.Instance.UninitializeSimulations()



if __name__ == "__main__":
    main()
