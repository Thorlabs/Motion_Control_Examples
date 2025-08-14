"""
Example KSG101_pythonnet.py
Example Date of Creation: 2024-02-13
Example Date of Last Modification on Github: 2024-02-13
Version of Python used for Testing: 3.10.5
==================
Example Description: The example shows how to connect to KSG101 and how to display voltage, position and force
"""

import os
import time
import clr

clr.AddReference("C:\\Program Files\\Thorlabs\\Kinesis\\Thorlabs.MotionControl.DeviceManagerCLI.dll")
clr.AddReference("C:\\Program Files\\Thorlabs\\Kinesis\\Thorlabs.MotionControl.GenericPiezoCLI.dll")
clr.AddReference("C:\\Program Files\\Thorlabs\\Kinesis\\Thorlabs.MotionControl.KCube.StrainGaugeCLI.dll")


from Thorlabs.MotionControl.DeviceManagerCLI import *
from Thorlabs.MotionControl.GenericPiezoCLI import *
from Thorlabs.MotionControl.KCube.StrainGaugeCLI import *
#from System import Decimal


def main():

    # Uncomment this line if you are using simulation
    #SimulationManager.Instance.InitializeSimulations()

    try:
        # Create new device
        serial_no = str("59500025")

        DeviceManagerCLI.BuildDeviceList()
        time.sleep(0.25)

        #print(DeviceManagerCLI.GetDeviceList())

        device = KCubeStrainGauge.CreateKCubeStrainGauge(serial_no)
        
        #Uncomment next line to display available methods
        #print(dir(device))


        # Connect, begin polling, and enable
        device.Connect(serial_no)
        time.sleep(0.25)
        

        # Wait for Settings to Initialise
        if not device.IsSettingsInitialized():
            device.WaitForSettingsInitialized(5000)  # 5 second timeout
            assert device.IsSettingsInitialized() is True

        
        device.StartPolling(250)
        time.sleep(0.25)  # wait statements are important to allow settings to be sent to the device

        device.EnableDevice()
        time.sleep(0.25)  # Wait for device to enable

        # Get Device information
        device_info = device.GetDeviceInfo()
        print(device_info.Description)

        #Get current voltage, position and force
        displaymode=device.GetDisplayMode()

        device.SetDisplayMode(displaymode.Voltage)    
        time.sleep(0.25)
        reading = device.Status.Reading
        print("Voltage {}".format(reading))

        device.SetDisplayMode(displaymode.Position)
        time.sleep(0.25)
        reading = device.Status.Reading
        print("Position {}".format(reading))

        device.SetDisplayMode(displaymode.Force)
        time.sleep(0.25)
        reading = device.Status.Reading
        print("Force {}".format(reading))

                                                
        device.StopPolling()
        device.Disconnect()
    except Exception as e:
        print(e)

    #SimulationManager.Instance.UninitializeSimulations()
    return None


if __name__ == "__main__":
    main()
