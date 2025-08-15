"""
Example KPC101_pythonnet.py
Example Date of Creation: 2024-04-17
Example Date of Last Modification on Github: 2024-04-17
Version of Python used for Testing: 3.9
==================
Example Description: This example controls the KPC101 in open and closed loop
"""
import os
import time
import sys
import clr

clr.AddReference("C:\\Program Files\\Thorlabs\\Kinesis\\Thorlabs.MotionControl.DeviceManagerCLI.dll")
clr.AddReference("C:\\Program Files\\Thorlabs\\Kinesis\\Thorlabs.MotionControl.GenericMotorCLI.dll")
clr.AddReference("C:\\Program Files\\Thorlabs\\Kinesis\\Thorlabs.MotionControl.GenericPiezoCLI.dll")
clr.AddReference("C:\\Program Files\\Thorlabs\\Kinesis\\ThorLabs.MotionControl.KCube.PiezoStrainGaugeCLI.dll")
from Thorlabs.MotionControl.DeviceManagerCLI import *
from Thorlabs.MotionControl.GenericMotorCLI import *
from Thorlabs.MotionControl.GenericPiezoCLI import *
from Thorlabs.MotionControl.KCube.PiezoStrainGaugeCLI import *
from System import Decimal  # necessary for real world units

def main():
    """The main entry point for the application"""

    # Uncomment this line if you are using
    # SimulationManager.Instance.InitializeSimulations()

    try:

        DeviceManagerCLI.BuildDeviceList()

        # create new device
        serial_no = "113250004"  # Replace this line with your device's serial number

        # Connect, begin polling, and enable
        device = KCubePiezoStrainGauge.CreateKCubePiezoStrainGauge(serial_no)

        device.Connect(serial_no)

        # Get Device Information and display description
        device_info = device.GetDeviceInfo()
        print(device_info.Description)

        # Start polling and enable
        device.StartPolling(250)  #250ms polling rate
        time.sleep(0.25)
        device.EnableDevice()
        time.sleep(0.25)  # Wait for device to enable

        if not device.IsSettingsInitialized():
            device.WaitForSettingsInitialized(10000)  # 10 second timeout
            assert device.IsSettingsInitialized() is True

        # Load the device configuration
        device_config = device.GetPiezoConfiguration(serial_no)

        # This shows how to obtain the device settings
        device_settings = device.PiezoDeviceSettings

        # Set the Zero point of the device
        print("Setting Zero Point")
        device.SetZero()
        time.sleep(10)

        # Open loop control
        mode = device.GetPositionControlMode()
        device.SetPositionControlMode(mode.OpenLoop)
        # Get the maximum voltage output of the KPZ
        max_voltage = device.GetMaxOutputVoltage()  # This is stored as a .NET decimal

        # Go to a voltage
        dev_voltage = Decimal(15.0)
        print(f'Going to voltage {dev_voltage}')

        if dev_voltage != Decimal(0) and dev_voltage <= max_voltage:
            device.SetOutputVoltage(dev_voltage)
            time.sleep(5)

            print(f'Moved to Voltage {device.GetOutputVoltage()}')
        else:
            print(f'Voltage must be between 0 and {max_voltage}')

        # Set the Zero point of the device
        print("Setting Zero Point")
        device.SetZero()
        time.sleep(10)

        # Closed loop control
        device.SetPositionControlMode(mode.CloseLoop)
        # Get the maximum voltage output of the KPZ
        max_travel = device.GetMaxTravel()  # This is stored as a .NET decimal

        # Go to a voltage
        dev_travel = Decimal(5.0)
        print(f'Going to {dev_travel}um')

        if dev_travel > Decimal(0) and dev_travel <= max_travel:
            device.SetPosition(dev_travel)
            time.sleep(5)

            print(f'Moved to Position: {device.GetPosition()}um')
        else:
            print(f'Voltage must be between 0 and {max_travel}')

        # Stop Polling and Disconnect
        device.StopPolling()
        device.Disconnect()
    except Exception as e:
        print(e)

    # Uncomment this line if you are using Simulations
    # SimulationManager.Instance.UninitializeSimulations()
    ...


if __name__ == "__main__":
    main()