'''An example that uses the .NET Kinesis Libraries to connect to a KDC.'''
import os
import time
import clr

clr.AddReference("C:\Program Files\Thorlabs\Kinesis\Thorlabs.MotionControl.DeviceManagerCLI.dll")
clr.AddReference("C:\Program Files\Thorlabs\Kinesis\Thorlabs.MotionControl.GenericMotorCLI.dll")
clr.AddReference("C:\Program Files\Thorlabs\Kinesis\ThorLabs.MotionControl.KCube.DCServoCLI.dll")
from System import Decimal
from Thorlabs.MotionControl.DeviceManagerCLI import *
from Thorlabs.MotionControl.GenericMotorCLI import *
from Thorlabs.MotionControl.KCube.DCServoCLI import *

def main():
    '''The main entry point for the application'''
    # SimulationManager.Instance.InitializeSimulations()

    try:
        serial_no = "27500125"

        print(DeviceManagerCLI.BuildDeviceList())

        kcube = KCubeDCServo.CreateKCubeDCServo(serial_no)

        kcube.Connect(serial_no)

        kcube.StartPolling(250)
        time.sleep(0.25)

        kcube.EnableDevice()
        time.sleep(0.25)

        device_info = kcube.GetDeviceInfo();

        device_info = {
            'Description': device_info.Description,
            'Firmware Version': device_info.FirmwareVersion  # returns an object with properties
        }

        print(device_info)
        # print("Homing Actuator")
        # kcube.Home(10000)  # 10s timeout, blocking call
        #
        # print("Device Homed. Moving to position 5.0")
        # kcube.MoveTo(Decimal.Parse(5.0), 10000)  # 10s timeout again
        # time.sleep(1)
        #
        # print(f'Device now at position {kcube.GetPosition()}')
        #
        # time.sleep(1)

        kcube.Disconnect()
    except Exception as e:
        print(e)

    # SimulationManager.Instance.UninitializeSimulations()
    return None


if __name__ == "__main__":
    main()