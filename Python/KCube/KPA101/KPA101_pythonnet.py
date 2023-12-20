"""
KPA101_pythonnet
An example that uses the .NET Kinesis Libraries to connect to a KPA101.
"""
import os
import time
import sys
import clr

# Add References to .NET libraries
clr.AddReference("C:\\Program Files\\Thorlabs\\Kinesis\\Thorlabs.MotionControl.DeviceManagerCLI.dll.")
clr.AddReference("C:\\Program Files\\Thorlabs\\Kinesis\\Thorlabs.MotionControl.KCube.PositionAlignerCLI.dll.")

from Thorlabs.MotionControl.DeviceManagerCLI import *
from Thorlabs.MotionControl.KCube.PositionAlignerCLI import *
from System import Decimal

def main():
    """The main entry point for the application"""
    # Uncomment this line if you are using Simulations
    #SimulationManager.Instance.InitializeSimulations()
    try:

        # Build device list so that the library can find yours
        DeviceManagerCLI.BuildDeviceList()
        # create new device
        serial_no = str("69000001")  # Replace this line with your device's serial number
        kcube = KCubePositionAligner.CreateKCubePositionAligner(serial_no)

        # Connect, begin polling, and enable
        kcube.Connect(serial_no)
        time.sleep(0.25)
        kcube.StartPolling(250)
        time.sleep(0.25)  # wait statements are important to allow settings to be sent to the device

        kcube.EnableDevice()
        time.sleep(0.25)  # Wait for device to enable

        # Get Device information
        device_info = kcube.GetDeviceInfo()
        print(device_info.Description)

        # Wait for Settings to Initialise
        if not kcube.IsSettingsInitialized():
            kcube.WaitForSettingsInitialized(10000)  # 10 second timeout
            assert kcube.IsSettingsInitialized() is True

        #get Device Configuration
        PositionAlignerTrakConfiguration = kcube.GetPositionAlignerConfiguration(serial_no, PositionAlignerConfiguration.DeviceSettingsUseOptionType.UseDeviceSettings)
        #Not used directly in example but illustrates how to obtain device settings
        currentDeviceSettings = kcube.PositionAlignerDeviceSettings

        time.sleep(1)
        
        #Select the detector 
        #PDQ80A = 0x01, PDQ30C = 0x02, PDP90A = 0x03, Other = 0xFF
        flag = True
        while flag:
            a = input("Select the Detector Type: 1.PDQ80A; 2.PDQ300C; 3.PDP90A; 4.Other ")
            if a == "1":
                GUISettings.Detectors = 0x01
                flag = False
            elif a == "2":
                GUISettings.Detectors = 0x02
                flag = False
            elif a == "3":
                GUISettings.Detectors = 0x03
                flag = False
            elif a == "4":
                GUISettings.Detectors = 0xFF
                flag = False
            else:
                print("Invaild input")
        
        #Set the operating mode
        flag = True
        while flag:
            a = input("Set the Operating Mode: 1.Monitor; 2.Open Loop; 3.Close Loop ")
            if a == "1":
                kcube.SetOperatingMode(PositionAlignerStatus.OperatingModes.Monitor, False)
                flag = False
            elif a == "2":
                kcube.SetOperatingMode(PositionAlignerStatus.OperatingModes.OpenLoop, False)
                flag = False
            elif a == "3":
                kcube.SetOperatingMode(PositionAlignerStatus.OperatingModes.CloseLoop, False)
                flag = False
            else:
                print("Invaild input")
        
        time.sleep(1)
        
        #get the type of the detector
        detector = GUISettings.Detectors
        
        #Display the Voltage or Position
        positionDiff = kcube.Status.PositionDifference
        positionSum = kcube.Status.Sum
        if detector == 3: # only PDP series can display the position difference in "mm"
            print("X position: ",positionDiff.X * 5 /positionSum," mm") #5 is half the length of the sensor
            print("Y position: ",positionDiff.Y * 5 /positionSum," mm")
        else:
            print("X Diff: ",positionDiff.X," V") #For PDQ series, the voltage difference CANNOT be converted to real position.
            print("Y Diff: ",positionDiff.Y," V")
        print("Sum: ",positionSum," V")

        # Stop polling and close device
        kcube.StopPolling()
        kcube.Disconnect(True)
    except Exception as e:
        print(e)
        

    # Uncomment this line if you are using Simulations
    #SimulationManager.Instance.UninitializeSimulations()


if __name__ == "__main__":
    main()