"""
Pythonnet example for Thorlabs PPC001 piezo controllers and PFM450E objective scanners
Date of Creation(YYYY-MM-DD): 2023-10-02
Date of Last Modification on Github: 2024-11-07
Python Version Used: 3.9
Kinesis Version Tested: 1.14.50
=======================
This example goes over connecting to the device, setting the output voltage in open loop, then new postion in closed loop.
"""

import os
import time
import sys
import clr

clr.AddReference("C:\\Program Files\\Thorlabs\\Kinesis\\Thorlabs.MotionControl.DeviceManagerCLI.dll")
clr.AddReference("C:\\Program Files\\Thorlabs\\Kinesis\\Thorlabs.MotionControl.GenericPiezoCLI.dll")
clr.AddReference("C:\\Program Files\\Thorlabs\\Kinesis\\ThorLabs.MotionControl.Benchtop.PrecisionPiezoCLI.dll")
from Thorlabs.MotionControl.DeviceManagerCLI import *
from Thorlabs.MotionControl.GenericPiezoCLI import *
from Thorlabs.MotionControl.GenericPiezoCLI import Piezo
from Thorlabs.MotionControl.Benchtop.PrecisionPiezoCLI import *
from System import Decimal  # necessary for real world units


def main():
    """The main entry point for the application"""

    # Uncomment this line if you are using
    SimulationManager.Instance.InitializeSimulations()

    try:
        DeviceManagerCLI.BuildDeviceList()

        # create new device
        serial_no = "44000001"  # Replace this line with your device's serial number

        # set voltage here
        voltage = Decimal(75)
        position = Decimal(150)


        # Connect, begin polling, and enable
        device = BenchtopPrecisionPiezo.CreateBenchtopPiezo(serial_no)

        device.Connect(serial_no)

        # Because this is a benchtop controller we need a channel object
        channel = device.GetChannel(1)

        # Ensure that the device settings have been initialized
        if not channel.IsSettingsInitialized():
            channel.WaitForSettingsInitialized(10000)  # 10 second timeout
            assert channel.IsSettingsInitialized() is True

        # Start polling and enable
        channel.StartPolling(250)  # 250ms polling rate
        time.sleep(0.25)
        channel.EnableDevice()
        time.sleep(0.25)  # Wait for device to enable

        # Get Device Information and display description
        device_info = channel.GetDeviceInfo()
        print(device_info.Description)

        # Load any configuration settings needed by the controller/stage
        piezoConfiguration = channel.GetPiezoConfiguration(serial_no)

        # Open loop example
        channel.SetPositionControlMode(Piezo.PiezoControlModeTypes.OpenLoop)
        time.sleep(.25)

        # Get max output volts
        maxVolts = channel.GetMaxOutputVoltage()
        print(f'Max voltage = {maxVolts}V')

        # Set the new Voltage
        if (voltage != Decimal(0)):
            if (voltage <= maxVolts):
                # Update velocity if required using real world methods
                channel.SetOutputVoltage(voltage)
                time.sleep(5)
                newVolts = channel.GetOutputVoltage()
                time.sleep(.25)
                print(f'Voltage set to {newVolts}')
            else:
                print("Set voltage must be less than max voltage")

        # Closed loop example
        channel.SetPositionControlMode(Piezo.PiezoControlModeTypes.CloseLoop)
        time.sleep(.25)

        # Get max output volts
        maxPos = channel.GetMaxTravel()
        print(f'Max position = {maxPos}µm')

        # Move the device to a new position
        if (position != Decimal(0)):
            if (position <= maxPos):
                # Update velocity if required using real world methods
                channel.SetPosition(position)
                time.sleep(5)
                newPos = channel.GetPosition()
                time.sleep(.25)
                print(f'Position set to {newPos}')
            else:
                print("Set position must be less than max position")

        # Stop Polling and Disconnect
        channel.StopPolling()
        channel.Disconnect()

    except Exception as e:
        # this can be bad practice: It sometimes obscures the error source
        print(e)

    # Uncomment this line if you are using Simulations
    SimulationManager.Instance.UninitializeSimulations()
    ...


if __name__ == "__main__":
    main()
