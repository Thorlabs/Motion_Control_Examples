"""
BBDXXX Pythonnet Example
Date of Creation(YYYY-MM-DD): 2024-10-02
Date of Last Modification on Github: 2024-10-02
Python Version Used: python3
Kinesis Version Tested: 1.14.49
"""
import os
import time
import sys
import clr

clr.AddReference("C:\\Program Files\\Thorlabs\\Kinesis\\Thorlabs.MotionControl.DeviceManagerCLI.dll")
clr.AddReference("C:\\Program Files\\Thorlabs\\Kinesis\\Thorlabs.MotionControl.GenericMotorCLI.dll")
clr.AddReference("C:\\Program Files\\Thorlabs\\Kinesis\\ThorLabs.MotionControl.Benchtop.BrushlessMotorCLI.dll")

from Thorlabs.MotionControl.DeviceManagerCLI import *
from Thorlabs.MotionControl.GenericMotorCLI import *
from Thorlabs.MotionControl.GenericMotorCLI import Settings, ControlParameters
from Thorlabs.MotionControl.Benchtop.BrushlessMotorCLI import *
from System import Decimal  # necessary for real world units

def main():
    """The main entry point for the application"""

    # Uncomment this line if you are using
    SimulationManager.Instance.InitializeSimulations()

    try:

        DeviceManagerCLI.BuildDeviceList()

        # create new device
        serial_no = "103000001"  # Replace this line with your device's serial number

        # Connect and retrieve a channel1
        device = BenchtopBrushlessMotor.CreateBenchtopBrushlessMotor(serial_no)
        device.Connect(serial_no)

        channel1 = device.GetChannel(1)
        # Ensure that the device settings have been initialized
        if not channel1.IsSettingsInitialized():
            channel1.WaitForSettingsInitialized(10000)  # 10 second timeout
            assert channel1.IsSettingsInitialized() is True

        # Start polling and enable
        channel1.StartPolling(250)  #250ms polling rate
        time.sleep(0.25)
        channel1.EnableDevice()
        time.sleep(0.25)  # Wait for device to enable

        # Get Device Information and display description
        device_info = channel1.GetDeviceInfo()
        print(device_info.Description)

        # Load any configuration settings needed by the controller/stage
        motor_config = channel1.LoadMotorConfiguration(channel1.DeviceID)  # Device ID is the serial no + channel1
        device_settings = channel1.MotorDeviceSettings

        motor_config.UpdateCurrentConfiguration()

        channel1.SetSettings(device_settings, False)

        channel2 = device.GetChannel(2)
        # Ensure that the device settings have been initialized
        if not channel2.IsSettingsInitialized():
            channel2.WaitForSettingsInitialized(10000)  # 10 second timeout
            assert channel2.IsSettingsInitialized() is True

        # Start polling and enable
        channel2.StartPolling(250)  # 250ms polling rate
        time.sleep(0.25)
        channel2.EnableDevice()
        time.sleep(0.25)  # Wait for device to enable

        # Get Device Information and display description
        device_info = channel2.GetDeviceInfo()
        print(device_info.Description)

        # Load any configuration settings needed by the controller/stage
        print(channel2)
        print(serial_no)
        print(channel2.DeviceID)
        motor_config = channel2.LoadMotorConfiguration(channel2.DeviceID)  # Device ID is the serial no + channel1
        device_settings = channel2.MotorDeviceSettings

        motor_config.UpdateCurrentConfiguration()

        channel2.SetSettings(device_settings, False)

        # Get parameters related to homing/zeroing/other
        home_params = channel1.GetHomingParams()
        print(f'Homing Velocity: {home_params.Velocity}\n',
              f'Homing Direction: {home_params.Direction}')

        channel1.SetHomingParams(home_params)  # If changes are made

        # Setting the trigger config parameters for each channel1
        trigger_params_1 = channel1.GetTriggerIOConfigParameters()
        trigger_params_1.TriggerOutMode = Settings.TriggerOutModeType.TrigOutput_AtPositionFwd
        trigger_params_1.TriggerOutPolarity = Settings.PolarityType.High
        trigger_params_1.StartPositionFwd = Decimal(10)
        trigger_params_1.IntervalFwd = Decimal(10)
        trigger_params_1.CycleCount = 1
        trigger_params_1.PulseWidth = 100
        trigger_params_1.PulseCountFwd = 5
        channel1.SetTriggerIOConfigParams(trigger_params_1)

        trigger_params_2 = channel2.GetTriggerIOConfigParameters()
        trigger_params_2.TriggerOutMode = Settings.TriggerOutModeType.TrigOutput_AtPositionFwd
        trigger_params_2.TriggerOutPolarity = Settings.PolarityType.High
        trigger_params_2.StartPositionFwd = Decimal(10)
        trigger_params_2.IntervalFwd = Decimal(10)
        trigger_params_2.CycleCount = 1
        trigger_params_2.PulseWidth = 500
        trigger_params_2.PulseCountFwd = 10
        channel2.SetTriggerIOConfigParams(trigger_params_2)

        # Home or Zero the device (if a motor/piezo)
        print("Homing Channel")
        channel1.Home(60000)  # 60 second timeout
        print("First Channel Homed")
        time.sleep(1.0)

        # Home or Zero the device (if a motor/piezo)
        print("Homing Channel")
        channel2.Home(60000)  # 60 second timeout
        print("Second Channel Homed")

        # Get velocity parameters
        vel_params_1 = channel1.GetVelocityParams()
        print("First Channel:\n")
        print(f'Move Maximum Velocity: {vel_params_1.MaxVelocity}\n',
              f'Move Acceleration: {vel_params_1.Acceleration}\n')

        vel_params_2 = channel2.GetVelocityParams()
        print("Second Channel:\n")
        print(f'Move Maximum Velocity: {vel_params_2.MaxVelocity}\n',
              f'Move Acceleration: {vel_params_2.Acceleration}\n')

        # Enabling trigger state for position steps
        channel1.SetPositionTriggerState(ControlParameters.TriggerState.TrigState_Enabled)
        channel2.SetPositionTriggerState(ControlParameters.TriggerState.TrigState_Enabled)

        time.sleep(1.0)

        # Move the device to a new position
        new_pos = Decimal(75)  # in real units
        print(f'Moving to {new_pos}')
        channel1.MoveTo(new_pos, 60000)  # 60 second timeout

        # Disabling trigger state
        channel1.SetPositionTriggerState(ControlParameters.TriggerState.TrigState_Disabled)
        channel2.SetPositionTriggerState(ControlParameters.TriggerState.TrigState_Disabled)

        # Stop Polling and Disconnect
        channel1.StopPolling()
        channel2.StopPolling()
        device.Disconnect()

    except Exception as e:
        print(e)

    # Uncomment this line if you are using Simulations
    SimulationManager.Instance.UninitializeSimulations()
    ...


if __name__ == "__main__":
    main()
