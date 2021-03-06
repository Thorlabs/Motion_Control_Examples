"""An example that uses the .NET Kinesis Libraries to connect to a KDC."""
import os
import time
import clr

clr.AddReference("C:\\Program Files\\Thorlabs\\Kinesis\\Thorlabs.MotionControl.DeviceManagerCLI.dll")
clr.AddReference("C:\\Program Files\\Thorlabs\\Kinesis\\Thorlabs.MotionControl.GenericMotorCLI.dll")
clr.AddReference("C:\\Program Files\\Thorlabs\\Kinesis\\ThorLabs.MotionControl.KCube.DCServoCLI.dll")
from Thorlabs.MotionControl.DeviceManagerCLI import *
from Thorlabs.MotionControl.GenericMotorCLI import *
from Thorlabs.MotionControl.KCube.DCServoCLI import *
from System import Decimal


def main():
    """The main entry point for the application"""

    # Uncomment this line if you are using
    # SimulationManager.Instance.InitializeSimulations()

    try:

        # Create new device
        serial_no = str("27500125")

        DeviceManagerCLI.BuildDeviceList()

        kcube = KCubeDCServo.CreateKCubeDCServo(serial_no)

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

        # Before homing or moving device, ensure the motor's configuration is loaded
        m_config = kcube.LoadMotorConfiguration(serial_no,
                                                DeviceConfiguration.DeviceSettingsUseOptionType.UseDeviceSettings)

        print("Homing Actuator")
        kcube.Home(60000)  # 10s timeout, blocking call

        print("Device Homed. Moving to position 5.0")
        f = 5.0
        d = Decimal(f)
        kcube.MoveTo(d, 10000)  # 10s timeout again
        time.sleep(1)

        print(f'Device now at position {kcube.Position}')
        time.sleep(1)

        kcube.Disconnect()
    except Exception as e:
        print(e)

    # SimulationManager.Instance.UninitializeSimulations()
    return None


if __name__ == "__main__":
    main()
