"""
UDXC Pythonnet Example
Date of Creation(YYYY-MM-DD): 2025-11-3
Date of Last Modification on Github: 2025-11-3
Python Version Used: python3.12
Kinesis Version Tested: 1.14.56
"""

import os
import time
import sys
import clr

# Add References to .NET libraries
clr.AddReference("C:\\Program Files\\Thorlabs\\Kinesis\\Thorlabs.MotionControl.Benchtop.PiezoCLI.dll")
clr.AddReference("C:\\Program Files\\Thorlabs\\Kinesis\\Thorlabs.MotionControl.DeviceManagerCLI.dll.")
clr.AddReference("C:\\Program Files\\Thorlabs\\Kinesis\\Thorlabs.MotionControl.GenericPiezoCLI.dll")

from Thorlabs.MotionControl.DeviceManagerCLI import *
from Thorlabs.MotionControl.Benchtop.PiezoCLI import *
from Thorlabs.MotionControl.Benchtop.PiezoCLI.UDXC import *
from Thorlabs.MotionControl.GenericPiezoCLI.Piezo import *


def main():
    """The main entry point for the application"""
    # Uncomment this line if you are using Simulations
    # SimulationManager.Instance.InitializeSimulations()
    try:

        # Build device list so that the library can find your devices
        DeviceManagerCLI.BuildDeviceList()
        # create new device
        serial_no = str("122000001")  # Replace this line with your device's serial number
        device = InertialStageController.CreateInertialStageController(serial_no)

        # Connect, begin polling, and enable
        device.Connect(serial_no)
        time.sleep(0.25)
        device.StartPolling(250) #250ms polling rate
        time.sleep(0.25)  # wait statements are important to allow settings to be sent to the device
        device.EnableDevice()
        time.sleep(0.25)  # Wait for device to enable

        # Get Device information
        deviceInfo = device.GetDeviceInfo()
        print(deviceInfo.Description)

        # Wait for Settings to Initialise
        if not device.IsSettingsInitialized():
            device.WaitForSettingsInitialized(10000)  # 10 second timeout
            assert device.IsSettingsInitialized() is True

        # Get Device Configuration
        udxcConfiguration = device.GetUDXCConfiguration(serial_no, DeviceConfiguration.DeviceSettingsUseOptionType.UseDeviceSettings)
        # Not used directly in example but illustrates how to obtain device settings
        currentDeviceSettings = UDXCSettings.GetSettings(udxcConfiguration)
        device.SetSettings(currentDeviceSettings,True,True)

        time.sleep(1)

        # Performance Optimize
        device.PulseParamsAcquireStart()
        time.sleep(0.5)
        print("Optimizing performance, please wait...")
        # When IsPulseParamsAcquired is 1, it indicates the optimization has finished
        while (not device.Status.IsPulseParamsAcquired):
            time.sleep(0.5)
            
        # Home the device
        print("Homing device...")
        device.Home(60000) #60 second timeout
        print("Device homed")
        
        # Optionally move the stage to target position (position is set in "nm")
        closeLoopPosition = 100000
        if (closeLoopPosition != 0):
            
            # Set the target position
            device.SetClosedLoopTarget(closeLoopPosition)

            # Get and Set the velocity and acceleration
            closedLoopParams = device.GetClosedLoopParameters()
            closedLoopParams.RefSpeed = 10000000 # velocity is set in nm/s
            closedLoopParams.Acceleration = 10000000 # acceleration is set in nm/s^2
            device.SetClosedLoopParameters(closedLoopParams)

            # Move the stage
            device.MoveStart()
            print("Moving the device to ",closeLoopPosition," nm")

            # Monitor the position
            posCheckCnt = 0
            for i in range(200):
                newPos = device.GetCurrentPosition()
                if abs(closeLoopPosition - newPos) < 6000:
                    if (posCheckCnt > 3):
                        break
                    else:
                        time.sleep(0.25)
                        posCheckCnt = posCheckCnt + 1
                else:
                    time.sleep(0.25)

            # Print the current position
            print("Device moved to ", newPos," nm")

        # Stop polling and close device
        device.StopPolling()
        device.Disconnect(True)
    except Exception as e:
        print(e)

    # Uncomment this line if you are using Simulations
    # SimulationManager.Instance.UninitializeSimulations()


if __name__ == "__main__":
    main()