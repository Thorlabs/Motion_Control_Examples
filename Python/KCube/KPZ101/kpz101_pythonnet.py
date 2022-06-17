"""
kpz101_pythonnet
==================

An example of using the .NET API with the pythonnet package for controlling a KPZ101
"""
import os
import time
import sys
import clr

clr.AddReference("C:\\Program Files\\Thorlabs\\Kinesis\\Thorlabs.MotionControl.DeviceManagerCLI.dll")
clr.AddReference("C:\\Program Files\\Thorlabs\\Kinesis\\Thorlabs.MotionControl.GenericMotorCLI.dll")
clr.AddReference("C:\\Program Files\\Thorlabs\\Kinesis\\ThorLabs.MotionControl.KCube.PiezoCLI.dll")
from Thorlabs.MotionControl.DeviceManagerCLI import *
from Thorlabs.MotionControl.GenericMotorCLI import *
from Thorlabs.MotionControl.KCube.PiezoCLI import *
from System import Decimal  # necessary for real world units

def main():
    """The main entry point for the application"""

    # Uncomment this line if you are using
    # SimulationManager.Instance.InitializeSimulations()

    try:

        DeviceManagerCLI.BuildDeviceList()

        # create new device
        serial_no = "26000001"  # Replace this line with your device's serial number

        # Connect, begin polling, and enable
        device = KCubePiezo.CreateKCubePiezo(serial_no)

        # Get Device Information and display description
        device_info = device.GetDeviceInfo()
        print(device_info.Description)

        # Start polling and enable
        device.StartPolling(250)  #250ms polling rate
        time.sleep(25)
        device.Enable()
        time.sleep(0.25)  # Wait for device to enable

        if not device.IsSettingsInitialized() or not device.IsSettingsInitialized():
            device.WaitForSettingsInitialized(10000)  # 10 second timeout
            assert device.IsSettingsInitialized() is True

        # Load the device configuration
        device_config = device.GetPiezoConfiguration(serial_no)

        # This shows how to obtain the device settings
        device_settings = device.PiezoDeviceSettings

        # Set the Zero point of the device
        print("Setting Zero Point")
        device.SetZero()

        # Get the maximum voltage output of the KPZ
        max_voltage = device.GetMaxOutputVoltage()  # This is stored as a .NET decimal

        # Go to a voltage
        dev_voltage = Decimal(15.0)
        print(f'Going to voltage {dev_voltage}')

        if dev_voltage != 0 and dev_voltage <= max_voltage:
            device.SetOutputVoltage(dev_voltage)
            time.Sleep(1)

            print(f'Moved to Voltage {device.GetOutputVoltage()}')
        else:
            print(f'Voltage must be between 0 and {max_voltage}')

        # Stop Polling and Disconnect
        device.StopPolling()
        device.Disconnect()
    except Exception as e:
        print(e)

    # Uncomment this line if you are using Simulations
    # SimulationManager.Instance.UnitializeSimulations()
    ...


if __name__ == "__main__":
    main()