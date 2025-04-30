"""
TTC_pythonnet Example
Date of Creation(YYYY-MM-DD): 2025-04-28
Date of Last Modification on Github: 2025-04-28
Python Version Used: python 3.11
Kinesis Version Tested: 1.14.52

"""
import time
import clr

# Add References to .NET libraries
clr.AddReference("C:\\Program Files\\Thorlabs\\Kinesis\\Thorlabs.MotionControl.DeviceManagerCLI.dll")
clr.AddReference("C:\\Program Files\\Thorlabs\\Kinesis\\Thorlabs.MotionControl.TCube.TECCLI.dll")
from Thorlabs.MotionControl.DeviceManagerCLI import *
from Thorlabs.MotionControl.TCube.TECCLI import *

from System import Decimal  # necessary for real world units

def main():
    """The main entry point for the application"""

    # Uncomment this line if you are using a aimulated device
    #SimulationManager.Instance.InitializeSimulations()

    try:

        DeviceManagerCLI.BuildDeviceList()

        # create new device
        serial_no = "87000001"  # Replace this line with your device's serial number
        device = TCubeTEC.CreateTCubeTEC(serial_no)

        # Connect
        device.Connect(serial_no)
        time.sleep(0.25)  # wait statements are important to allow settings to be sent to the device

        # Get Device Information and display description
        device_info = device.GetDeviceInfo()
        print(device_info.Description)

        # Start polling and enable
        device.StartPolling(250)  #250ms polling rate
        time.sleep(0.25)
        device.EnableDevice()
        time.sleep(0.25)  # Wait for device to enable

        # Configure device#
        device_config = device.GetTECConfiguration(device.DeviceID)

        temperature=Decimal(10)
        device.SetTemperature(temperature)

        for i in range (10):
            print(device.GetValueReading())
            time.sleep(1)



        # Stop Polling and Disconnect
        device.StopPolling()
        device.Disconnect()
    except Exception as e:
        print(e)

    # Uncomment this line if you are using Simulations
    #SimulationManager.Instance.UninitializeSimulations()
    ...


if __name__ == "__main__":
    main()