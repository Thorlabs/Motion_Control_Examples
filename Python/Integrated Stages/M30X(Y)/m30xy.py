"""
Example Title: M30XY.py
Example Date of Creation(YYYY-MM-DD) 2024-02-01
Example Date of Last Modification on Github 2024-02-01
Version of Python: 3.9
Version of the Thorlabs SDK used: 1.14.44
==================
Example Description
This example use the C DLLs
Example runs the M30XY stage, this uses the Benchtop not integrated stage DLLs
"""

import os
import sys
import time
from ctypes import *
from ctypes import CDLL


def main():

    """Import the correct version of the library"""
    if sys.version_info < (3, 8):
        os.chdir(r"C:\Program Files\Thorlabs\Kinesis")
    else:
        os.add_dll_directory(r"C:\Program Files\Thorlabs\Kinesis")

    lib: CDLL = cdll.LoadLibrary("Thorlabs.MotionControl.Benchtop.DCServo.dll")

    # Uncomment this line if you are using simulations
    #lib.TLI_InitializeSimulations()

    x_chan = c_short(1)
    y_chan = c_short(2)
    serial_num = c_char_p(b"101000004")

    # Open the device
    if lib.TLI_BuildDeviceList() == 0:
        ret = lib.BDC_Open(serial_num)
        # Start polling at a 250ms interval
        lib.BDC_StartPolling(serial_num, x_chan, c_int(250))
        lib.BDC_StartPolling(serial_num, y_chan, c_int(250))

        # Enable Channels
        lib.BDC_EnableChannel(serial_num, x_chan)
        lib.BDC_EnableChannel(serial_num, y_chan)
        time.sleep(0.5)

        # Home the device on channels 1 and 2
        lib.BDC_Home(serial_num, x_chan)
        lib.BDC_Home(serial_num, y_chan)
        time.sleep(30)  # Adjust this value as necessary, but the homing movement can take a while

        # Get the device's current x and y positions in device units
        lib.BDC_RequestPosition(serial_num, x_chan)
        lib.BDC_RequestPosition(serial_num, y_chan)

        x_pos_dev = lib.BDC_GetPosition(serial_num, x_chan)
        y_pos_dev = lib.BDC_GetPosition(serial_num, y_chan)
        print(f'X position: {x_pos_dev} device units')
        print(f'Y position: {y_pos_dev} device units')

        # Set a new absolute move in device units
        x_pos_new = c_int(100000)  # 100000 device units = 10.0mm of movement
        y_pos_new = c_int(100000)  # 100000 device units = 10.0mm of movement

        # BDC_MoveToPosition(serial_number, channel, position)
        lib.BDC_SetMoveAbsolutePosition(serial_num, x_chan, x_pos_new)
        lib.BDC_SetMoveAbsolutePosition(serial_num, y_chan, y_pos_new)
        time.sleep(1)  # 250ms wait time to ensure values are sent to device

        lib.BDC_MoveAbsolute(serial_num, x_chan)
        lib.BDC_MoveAbsolute(serial_num, y_chan)

        time.sleep(5)

        # Print the New Positions:
        lib.BDC_RequestPosition(serial_num, x_chan)
        lib.BDC_RequestPosition(serial_num, y_chan)

        x_pos_dev = lib.BDC_GetPosition(serial_num, x_chan)
        y_pos_dev = lib.BDC_GetPosition(serial_num, y_chan)
        print(f'X position: {x_pos_dev} device units')
        print(f'Y position: {y_pos_dev} device units')


        lib.BDC_Close(serial_num)


    # Uncomment this line if you are using simulations
    #lib.TLI_UninitializeSimulations()


if __name__ == "__main__":
    main()