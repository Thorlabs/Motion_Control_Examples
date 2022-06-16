"""An example that uses the .NET Kinesis Libraries to connect to a KDC."""
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
        serial_no = str("28251092")  # Replace this line with your device's serial number
        kcube = KCubeBrushlessMotor.CreateKCubeBrushlessMotor(serial_no)

        # Connect, begin polling, and enable
        kcube.Connect(serial_no)
        time.sleep(0.25)
        kcube.StartPolling(250)
        time.sleep(0.25)  # wait statements are important to allow settings to be sent to the device

        kcube.EnableDevice()
        time.sleep(0.25)  # Wait for device to enable

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

        time.sleep(1)

        # Home stage
        print("Homing Device...")
        kcube.Home(60000)  # 60 second timeout
        print("Device Homed")

        # Move Device to a new position:
        pos = Decimal(50.0)  # Position must be a .NET decimal
        kcube.MoveTo(pos, 60000)  # 60 second timeout

        # Stop polling and close device
        kcube.StopPolling()
        kcube.Disconnect(True)
    except Exception as e:
        print(e)

    # Uncomment this line if you are using Simulations
    # SimulationManager.Instance.UnitializeSimulations()
    ...


if __name__ == "__main__":
    main()
