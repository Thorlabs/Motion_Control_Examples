"""
Example Title: KVC101.py
Example Date of Creation(YYYY-MM-DD) 2024-08-28
Example Date of Last Modification on Github
Version of Python: 3.9
Version of the Thorlabs SDK used: 1.14.49
==================
Example Description
Using the .NET Dlls
Example runs the CTV12(/M) stage using the KVC101 controller, this uses the Brushless motor DLLs
"""

import sys, os, time, clr
from System import Decimal

clr.AddReference("C:\\Program Files\\Thorlabs\\Kinesis\\Thorlabs.MotionControl.DeviceManagerCLI.dll")
clr.AddReference("C:\\Program Files\\Thorlabs\\Kinesis\\Thorlabs.MotionControl.GenericMotorCLI.dll")
clr.AddReference("C:\\Program Files\\Thorlabs\\Kinesis\\Thorlabs.MotionControl.KCube.BrushlessMotorCLI.dll.")

from Thorlabs.MotionControl.DeviceManagerCLI import *
from Thorlabs.MotionControl.GenericMotorCLI import *
from Thorlabs.MotionControl.KCube.BrushlessMotorCLI import *

def main():
    """The main entry point for the application"""
    DeviceManagerCLI.BuildDeviceList()

    serial_no = str("109000003")
    device = KCubeVoiceCoil.CreateKCubeVoiceCoil(serial_no)
    device.Connect(serial_no)
    time.sleep(0.25)
    device.StartPolling(250)
    time.sleep(0.25)
    device.EnableDevice()
    time.sleep(0.25)


    device_info = device.GetDeviceInfo()
    print(device_info.Description)
    m_config = device.LoadMotorConfiguration(serial_no,DeviceConfiguration.DeviceSettingsUseOptionType.UseDeviceSettings)

    device.Home(10000)

    scanParams = device.GetScanMoveParams()
    scanParams.Amplitude = Decimal(6)
    scanParams.AngularAcceleration = Decimal(1.5)
    scanParams.Frequency = Decimal(1.5)
    scanParams.NumberOfCycles = 20
    scanParams.StartPosition = Decimal(6)

    device.SetScanMoveParams(scanParams)

    device.StartScanMove()

    time.sleep(10)
    device.StopPolling()
    device.Disconnect()

if __name__ == "__main__":
    main()
