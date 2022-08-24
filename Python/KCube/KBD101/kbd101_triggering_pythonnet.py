"""An example that uses the .NET Kinesis Libraries to connect to a KBC."""
import os
import time
import sys
import clr

# Add References to .NET libraries
clr.AddReference("C:\\Program Files\\Thorlabs\\Kinesis\\Thorlabs.MotionControl.DeviceManagerCLI.dll.")
clr.AddReference("C:\\Program Files\\Thorlabs\\Kinesis\\Thorlabs.MotionControl.GenericMotorCLI.dll.")
clr.AddReference("C:\\Program Files\\Thorlabs\\Kinesis\\Thorlabs.MotionControl.KCube.BrushlessMotorCLI.dll.")


from Thorlabs.MotionControl.DeviceManagerCLI import *
from Thorlabs.MotionControl.GenericMotorCLI import *
from Thorlabs.MotionControl.GenericMotorCLI.Settings import KCubeTriggerConfigSettings
from Thorlabs.MotionControl.KCube.BrushlessMotorCLI import *
from System import Decimal

def main():
    """The main entry point for the application"""

    # Uncomment this line if you are using
    # SimulationManager.Instance.InitializeSimulations()

    try:

        # Build device list so that the library can find yours
        DeviceManagerCLI.BuildDeviceList()
        # create new device
        serial_no = str("28251022")  # Replace this line with your device's serial number
        kcube = KCubeBrushlessMotor.CreateKCubeBrushlessMotor(serial_no)

        # Connect, begin polling, and enable
        kcube.Connect(serial_no)
        time.sleep(0.5)
        kcube.StartPolling(250)
        time.sleep(0.5)  # wait statements are important to allow settings to be sent to the device

        kcube.EnableDevice()
        time.sleep(0.5)  # Wait for device to enable

        # Get Device information
        device_info = kcube.GetDeviceInfo()
        print(device_info.Description)

        # Wait for Settings to Initialise
        if not kcube.IsSettingsInitialized():
            kcube.WaitForSettingsInitialized(10000)  # 10 second timeout
            assert kcube.IsSettingsInitialized() is True

        # Before homing or moving device, ensure the motors configuration is loaded
        m_config = kcube.LoadMotorConfiguration(serial_no,
                                                DeviceConfiguration.DeviceSettingsUseOptionType.UseDeviceSettings)
        kcube.SetSettings(kcube.MotorDeviceSettings, True)
        time.sleep(1)

        # Home stage
        print("Homing Device...")
        kcube.Home(60000)  # 60 second timeout
        print("Device Homed")

        #get settings to modify
        trigger_config_params = kcube.GetTriggerConfigParams()

        #trigger 1 will instruct a move and 2 will output when in motion
        trigger_config_params.Trigger1Mode = KCubeTriggerConfigSettings.TriggerPortMode.TrigIN_RelativeMove 
        trigger_config_params.Trigger2Mode = KCubeTriggerConfigSettings.TriggerPortMode.TrigOUT_InMotion
        trigger_config_params.Trigger1Polarity = KCubeTriggerConfigSettings.TriggerPolarity.TriggerHigh
        trigger_config_params.Trigger2Polarity = KCubeTriggerConfigSettings.TriggerPolarity.TriggerHigh

        #set modified settings
        kcube.SetTriggerConfigParams(trigger_config_params)

        kcube.SetVelocityParams(Decimal(10), Decimal(10))
        kcube.SetMoveRelativeDistance(Decimal(10))

        print("Accepting Triggers for 10s")
        time.sleep(10)

        # Stop polling and close device
        kcube.StopPolling()
        kcube.Disconnect(True)
        print("Device Closed")
    except Exception as e:
        print(e)

    # Uncomment this line if you are using Simulations
    # SimulationManager.Instance.UnitializeSimulations()
    ...


if __name__ == "__main__":
    main()
