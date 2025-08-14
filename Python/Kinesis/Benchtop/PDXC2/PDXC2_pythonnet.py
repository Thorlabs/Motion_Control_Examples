"""
PDXC2 Pythonnet Example
Date of Creation(YYYY-MM-DD): 2024-08-02
Date of Last Modification on Github: 2024-08-02
Python Version Used: python3
Kinesis Version Tested: 1.14.49
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
from Thorlabs.MotionControl.Benchtop.PiezoCLI.PDXC2 import *
from Thorlabs.MotionControl.GenericPiezoCLI.Piezo import *


def main():
    """The main entry point for the application"""
    # Uncomment this line if you are using Simulations
    # SimulationManager.Instance.InitializeSimulations()
    try:

        # Build device list so that the library can find yours
        DeviceManagerCLI.BuildDeviceList()
        # create new device
        serial_no = str("112000001")  # Replace this line with your device's serial number
        device = InertiaStageController.CreateInertiaStageController(serial_no)

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

        #Get Device Configuration
        pdxc2Configuration = device.GetPDXC2Configuration(serial_no, DeviceConfiguration.DeviceSettingsUseOptionType.UseDeviceSettings)
        #Not used directly in example but illustrates how to obtain device settings
        currentDeviceSettings = PDXC2Settings.GetSettings(pdxc2Configuration)

        time.sleep(1)
        
        #Optionally set the deivce to Open Loop Mode and move the stage to target position (position is set in "steps")
        openLoopPosition = 0
        if (openLoopPosition > 0):
            #Set the open loop move paramaters for the PDXC2
            device.SetPositionControlMode(PiezoControlModeTypes.OpenLoop)
            openLoopParams = OpenLoopMoveParams()
            openLoopParams.StepSize = openLoopPosition
            device.SetOpenLoopMoveParameters(openLoopParams)

            #Move the stage
            device.MoveStart()
            print("Moving the device to ",openLoopPosition)

            #check if the stage stops
            pos = device.GetCurrentPosition()
            time.sleep(0.5)
            while (pos != device.GetCurrentPosition()):
                pos = device.GetCurrentPosition()
                time.sleep(0.5)

            #Display current position
            print("Device Moved to ", pos)
                
        #Optionally set the deivce to Close Loop Mode and move the stage to target position (position is set in "nm")
        #close loop mode is only valid for PDX series stages with encoder
        closeLoopPosition = 0
        if (closeLoopPosition > 0):
            #Set the control mode to close loop mode
            device.SetPositionControlMode(PiezoControlModeTypes.CloseLoop)
            
            #Performance Optimize
            device.PulseParamsAcquireStart()
            time.sleep(0.5)
            print("Optimizing performance, please wait...")
            #when IsPulseParamsAcquired is 1, it indicates the optimization has finished
            while (not device.Status.IsPulseParamsAcquired):
                time.sleep(0.5)
            
            #home the device and set the target position
            device.Home(60000) #60 second timeout
            device.SetClosedLoopTarget(closeLoopPosition)

            #Move the stage
            device.MoveStart()
            print("Moving the device to ",closeLoopPosition," nm")

            #check if the stage stops
            pos = device.GetCurrentPosition()
            time.sleep(0.5)
            while (pos != device.GetCurrentPosition()):
                pos = device.GetCurrentPosition()
                time.sleep(0.5)

            #Display current position
            print("Device Moved to ", pos," nm")
        
        # Stop polling and close device
        device.StopPolling()
        device.Disconnect(True)
    except Exception as e:
        print(e)

    # Uncomment this line if you are using Simulations
    # SimulationManager.Instance.UninitializeSimulations()


if __name__ == "__main__":
    main()