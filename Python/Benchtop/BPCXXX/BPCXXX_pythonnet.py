"""
pythonnet_template
==================

A template useful for the creation of custom software for Thorlabs BPCXXX benchtop controllers.
"""
import os
import time
import sys
import clr

clr.AddReference("C:\\Program Files\\Thorlabs\\Kinesis\\Thorlabs.MotionControl.DeviceManagerCLI.dll")
clr.AddReference("C:\\Program Files\\Thorlabs\\Kinesis\\Thorlabs.MotionControl.GenericPiezoCLI.dll")
clr.AddReference("C:\\Program Files\\Thorlabs\\Kinesis\\ThorLabs.MotionControl.Benchtop.PiezoCLI.dll")
from Thorlabs.MotionControl.DeviceManagerCLI import *
from Thorlabs.MotionControl.GenericPiezoCLI import *
from Thorlabs.MotionControl.Benchtop.PiezoCLI import *
from System import Decimal  # necessary for real world units

def main():
    """The main entry point for the application"""

    # Uncomment this line if you are using
    # SimulationManager.Instance.InitializeSimulations()

    try:

        DeviceManagerCLI.BuildDeviceList()

        # create new device
        serial_no = "71000001"  # Replace this line with your device's serial number

        # Set output voltage. 
        voltage = 0
        # Connect
        device = BenchtopPiezo.CreateBenchtopPiezo(serial_no)
        device.Connect(serial_no)

        # Retrieve channel for the device. Can call multiple times for (X) channels.
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

        # Get Device Information and display description
        device_info = channel.GetDeviceInfo()
        print(device_info.Description)

        # Load any configuration settings needed by the controller/stage
        motor_config = channel.GetPiezoConfiguration(channel.DeviceID)
        time.sleep(0.25)

        currentDeviceSettings = channel.PiezoDeviceSettings
        
        
        maxVolts = channel.GetMaxOutputVoltage()

        if (voltage == 0):
                channel.SetOutputVoltage(Decimal(voltage))
                newVolts = channel.GetOutputVoltage()
                print("Voltage set to Zero")

        elif ((voltage != 0) & (voltage <= maxVolts)):
            
        #Update voltage if required using real world methods
            channel.SetOutputVoltage(Decimal(voltage))

            newVolts = channel.GetOutputVoltage()
            print("Voltage set to {0}", newVolts)
            


        # Stop Polling and Disconnect
        channel.StopPolling()
        device.Disconnect()

    except Exception as e:
        print(e)

    # Uncomment this line if you are using Simulations
    # SimulationManager.Instance.UninitializeSimulations()
    ...


if __name__ == "__main__":
    main()