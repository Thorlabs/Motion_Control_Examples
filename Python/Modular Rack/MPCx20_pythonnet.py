import clr
import time

clr.AddReference("C:\\Program Files\\Thorlabs\\Kinesis\\Thorlabs.MotionControl.DeviceManagerCLI.dll")
clr.AddReference("C:\\Program Files\\Thorlabs\\Kinesis\\Thorlabs.MotionControl.GenericMotorCLI.dll")
clr.AddReference("C:\\Program Files\\Thorlabs\\Kinesis\\ThorLabs.MotionControl.PolarizerCLI.dll")

from Thorlabs.MotionControl.DeviceManagerCLI import *
from Thorlabs.MotionControl.GenericMotorCLI import *
from Thorlabs.MotionControl.PolarizerCLI import *
from System import Decimal

def main():
    # Uncomment this line if you are using a simulation
    #SimulationManager.Instance.InitializeSimulations()

    try:
        # Build device list. 
        DeviceManagerCLI.BuildDeviceList()

        # create new device.
        serial_no = "38000001"
        device = Polarizer.CreatePolarizer(serial_no)

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
        time.sleep(0.25)  # Wait for device to enable.

        # Get Device Information and display description.
        device_info = device.GetDeviceInfo()
        print(device_info.Description)

        # Call device methods.
        print("Homing Device")
        paddle = PolarizerPaddles.Paddle1#choose first paddle
        device.Home(paddle,60000)  # 60 second timeout.
        print("Done")

        time.sleep(2)

        new_pos = Decimal(10.0)  # Must be a .NET decimal.
        print(f'Moving to {new_pos}')
        device.MoveTo(new_pos,paddle, 60000)  # 60 second timeout.
        print("Done")


        # Stop polling loop and disconnect device before program finishes. 
        device.StopPolling()
        device.Disconnect()


    except Exception as e:
        print(e)
        
    #SimulationManager.Instance.UninitializeSimulations()

if __name__ == "__main__":
    main()



 


