"""
Pythonnet example for Thorlabs PPC001 piezo controllers and PFM450E objective scanners
2023-10-02
2023-10-02
Python 3.10.5 and .NET 1.4.6
Kinesis version 1.14.41
=======================
This example goes over connecting to the device, setting the output voltage and disconnecting from the Console
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
    # SimulationManager.Instance.InitializeSimulations()

    try:

        DeviceManagerCLI.BuildDeviceList()

        # create new device
        serial_no = "44000001"  # Replace this line with your device's serial number

        # set voltage here 
        voltage = Decimal(4)
        
        DeviceManagerCLI.BuildDeviceList()

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
        channel.StartPolling(250)  #250ms polling rate
        time.sleep(25)
        channel.EnableDevice()
        time.sleep(0.25)  # Wait for device to enable

        # Set to open or closed loop

        channel.SetPositionControlMode(Piezo.PiezoControlModeTypes.CloseLoop)
        time.sleep(.25)
        # Get Device Information and display description
        device_info = channel.GetDeviceInfo()
        print(device_info.Description)

        # Load any configuration settings needed by the controller/stage
        piezoConfiguration = channel.GetPiezoConfiguration(serial_no)
       

        # Get max output volts
        maxVolts = channel.GetMaxOutputVoltage()
        print(maxVolts)

        # Move the device to a new position
        if (voltage != Decimal(0)):
            
                # Update velocity if required using real world methods
                channel.SetOutputVoltage(voltage)
                time.sleep(.25)
                newVolts = channel.GetOutputVoltage()
                time.sleep(.25)
                print(f'Voltage set to {newVolts}')
            



        # Stop Polling and Disconnect
        channel.StopPolling()
        channel.Disconnect()

    except Exception as e:
        # this can be bad practice: It sometimes obscures the error source
        print(e)

    # Uncomment this line if you are using Simulations
    # SimulationManager.Instance.UninitializeSimulations()
    ...


if __name__ == "__main__":
    main()