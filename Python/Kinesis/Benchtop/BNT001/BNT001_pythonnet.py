"""
BNT001 Pythonnet Example
Date of Creation(YYYY-MM-DD): 2024-07-10
Date of Last Modification on Github(YYYY-MM-DD): 2024-07-10
Python Version Used: 3.10.11
Kinesis Version Tested: 1.14.49
"""
import os
import time
import sys
import clr

# Add References to .NET libraries
clr.AddReference("C:\\Program Files\\Thorlabs\\Kinesis\\Thorlabs.MotionControl.DeviceManagerCLI.dll.")
clr.AddReference("C:\\Program Files\\Thorlabs\\Kinesis\\Thorlabs.MotionControl.GenericNanoTrakCLI.dll")
clr.AddReference("C:\\Program Files\\Thorlabs\\Kinesis\\Thorlabs.MotionControl.Benchtop.NanoTrakCLI.dll")

from Thorlabs.MotionControl.DeviceManagerCLI import *
from Thorlabs.MotionControl.GenericNanoTrakCLI import *
from Thorlabs.MotionControl.Benchtop.NanoTrakCLI import *
from Thorlabs.MotionControl.GenericNanoTrakCLI.Settings import *

def main():
    """The main entry point for the application"""
    # Uncomment this line if you are using Simulations
    #SimulationManager.Instance.InitializeSimulations()
    
    serial_no = "22000001"  # Replace this line with your device's serial number
    #Set the home position
    xPos = 5
    yPos = 5
    
    try:

        # Build device list so that the library can find yours
        DeviceManagerCLI.BuildDeviceList()
        # create new device
        device = BenchtopNanoTrak.CreateBenchtopNanoTrak(serial_no)

        # Connect, begin polling, and enable
        device.Connect(serial_no)
        time.sleep(0.25)
        device.StartPolling(250)
        time.sleep(0.25)  # wait statements are important to allow settings to be sent to the device

        # Wait for Settings to Initialise
        if not device.IsSettingsInitialized():
            device.WaitForSettingsInitialized(10000)  # 10 second timeout
            assert device.IsSettingsInitialized() is True
        
        # Enable the channel otherwise any move is ignored
        device.EnableDevice()
        time.sleep(0.25)  # Wait for device to enable

        # Get Device Configuration
        nanoTrakConfoguration = device.GetNanoTrakConfiguration(serial_no)
        # Not used directly in example but illustrates how to obtain device settings
        currentDeviceSettings = device.NanoTrakDeviceSettings
        device.SetSettings(currentDeviceSettings,True) # write current settings to hardware

        time.sleep(1)
        
        # Get Device information
        device_info = device.GetDeviceInfo()
        print(device_info.Description)
        
        
        # Set the NanoTrak to Tracking mode
        device.SetMode(NanoTrakStatus.OperatingModes.Tracking)
        if (xPos > 0 or yPos > 0):
            # Retrieve and edit home position
            homePosition = device.GetCircleHomePosition()
            homePosition.HPosition = xPos
            homePosition.VPosition = yPos
            device.SetCircleHomePosition(homePosition)
            device.HomeCircle()
        
        #Set TIA range mode
        device.SetTIARangeMode(TIARangeModes.AutoRangeAtSelected, TIAOddOrEven.All)
        
        #Display Circle Position and TIA Reading
        for i in range(10):
            pos = device.GetCirclePosition()
            tiaReading = device.GetReading()
            print("Circle Position: X = {:.3f}, Y = {:.3f};  TIA Reading: {} A".format(pos.HPosition,  pos.VPosition, tiaReading.AbsoluteReading))
            time.sleep(0.25)


        # Stop polling and close device
        device.StopPolling()
        device.DisableDevice()
        device.Disconnect(True)
    except Exception as e:
        print(e)
        

    # Uncomment this line if you are using Simulations
    #SimulationManager.Instance.UninitializeSimulations()


if __name__ == "__main__":
    main()