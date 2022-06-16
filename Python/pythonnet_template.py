"""An example that uses the .NET Kinesis Libraries to connect to a KDC."""
import os
import time
import sys
import clr

# Add References to .NET libraries
clr.AddReference("C:\\Program Files\\Thorlabs\\Kinesis\\Thorlabs.MotionControl.<Binary>.dll.")
clr.AddReference("C:\\Program Files\\Thorlabs\\Kinesis\\Thorlabs.MotionControl.<Binary>.dll.")
clr.AddReference("C:\\Program Files\\Thorlabs\\Kinesis\\Thorlabs.MotionControl.<Binary>.dll.")

'''
from <Binary> import *
from <Binary> import *
from <Binary> import *
'''


def main():
    """The main entry point for the application"""

    # Uncomment this line if you are using
    # SimulationManager.Instance.InitializeSimulations()

    try:

        # create new device
        serial_no = ""  # Replace this line with your device's serial number

        # Connect, begin polling, and enable

        time.sleep(0.25)  # wait statements are important to allow settings to be sent to the device

        time.sleep(0.25)  # Wait for device to enable
    except Exception as e:
        print(e)

    # Uncomment this line if you are using Simulations
    # SimulationManager.Instance.UnitializeSimulations()
    ...
