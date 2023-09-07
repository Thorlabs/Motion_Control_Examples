import clr
import time

clr.AddReference("C:\\Program Files\\Thorlabs\\Kinesis\\Thorlabs.MotionControl.DeviceManagerCLI.dll")
clr.AddReference("C:\\Program Files\\Thorlabs\\Kinesis\\Thorlabs.MotionControl.GenericMotorCLI.dll")
clr.AddReference("C:\\Program Files\\Thorlabs\\Kinesis\\ThorLabs.MotionControl.FilterFlipperCLI.dll")

from Thorlabs.MotionControl.DeviceManagerCLI import *
from Thorlabs.MotionControl.GenericMotorCLI import *
from Thorlabs.MotionControl.FilterFlipperCLI import *
from System import Decimal, UInt32

def main():
    # Uncomment this line if you are using a simulation
    #SimulationManager.Instance.InitializeSimulations()

    try:
        # Build device list. 
        DeviceManagerCLI.BuildDeviceList()

        # create new device.
        serial_no = "37847808"
        device = FilterFlipper.CreateFilterFlipper(serial_no)

        # Connect to device.
        device.Connect(serial_no)

        # Ensure that the device settings have been initialized.
        if not device.IsSettingsInitialized():
            device.WaitForSettingsInitialized(10000)  # 10 second timeout.
            assert device.IsSettingsInitialized() is True

        # Start polling loop and enable device.
        device.StartPolling(250)  #250ms polling rate.
        time.sleep(5)
        device.EnableDevice()
        time.sleep(5)  # Wait for device to enable.

        # Get Device Information and display description.
        device_info = device.GetDeviceInfo()
        print(device_info.Description)

        # Call device methods.
        print("Homing Device")
        device.Home(60000)  # 60 second timeout.
        print("Done")

        time.sleep(2)

        new_pos = UInt32(2)  # Must be a .NET decimal.
        print(f'Moving to {new_pos}')
        device.SetPosition(new_pos,60000)  # 60 second timeout.
        print("Done")


        # Stop polling loop and disconnect device before program finishes. 
        device.StopPolling()
        device.Disconnect()


    except Exception as e:
        print(e)
        
    #SimulationManager.Instance.UninitializeSimulations()

if __name__ == "__main__":
    main()



 


