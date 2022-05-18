'''
m30xy.py
========

An example showing the usage of a Thorlabs M30XY stage.

The stage is based off of Brushed DC motors, and so uses the BDC101 C API
controls. This example will import these functions using ctypes, connect
to the device, and then make moves.2
'''
import os
import sys
import time
from ctypes import *  # This is generally bad practice, but done here for brevity

'''Import the correct version of the library'''
if sys.version_info < (3, 8):
    os.chdir(r"C:\Program Files\Thorlabs\Kinesis")
else:
    os.add_dll_directory(r"C:\Program Files\Thorlabs\Kinesis")

lib = cdll.LoadLibrary("Thorlabs.MotionControl.Benchtop.DCServo.dll")

# Uncomment this line if you are using simulations
lib.TLI_InitializeSimulations()

x_chan = c_int(1)
y_chan = c_int(2)
serial_num = c_char_p(b"10100001")

# Open the device
if lib.TLI_BuildDeviceList() == 0:
    lib.BDC_Open(serial_num)

    # Enable Channels
    lib.BDC_EnableChannel(serial_num, x_chan)
    lib.BDC_EnableChannel(serial_num, y_chan)

    # Home the device on channels 1 and 2
    lib.BDC_Home(serial_num, x_chan)
    lib.BDC_Home(serial_num, y_chan)
    time.sleep(0.2)

    # Get the device's current x and y positions in device units
    lib.BDC_RequestPosition(serial_num, x_chan)
    lib.BDC_RequestPosition(serial_num, y_chan)
    time.sleep(0.2)

    x_pos_dev = lib.BDC_GetPosition(serial_num, x_chan)
    y_pos_dev = lib.BDC_GetPosition(serial_num, y_chan)

    print(f'X position: {x_pos_dev}\nY Position: {y_pos_dev}')
    
    # Set the X and Y position (in device units)
    x_pos_new = c_int(2000)
    y_pos_new = c_int(2000)

    # BDC_MoveToPosition(serial_number, channel, position)
    lib.BDC_MoveToPosition(serial_num, x_chan, x_pos_new)
    lib.BDC_MoveToPosition(serial_num, y_chan, y_pos_new)

    time.sleep(2)

    # Print the New Positions:
    lib.BDC_RequestPosition(serial_num, x_chan)
    lib.BDC_RequestPosition(serial_num, y_chan)
    time.sleep(0.2)

    x_pos_dev = lib.BDC_GetPosition(serial_num, x_chan)
    y_pos_dev = lib.BDC_GetPosition(serial_num, y_chan)
    print(f'X position: {x_pos_dev}\nY Position: {y_pos_dev}')

    lib.BDC_Close(serial_num)

# Uncomment this line if you are using simulations
lib.TLI_UninitializeSimulations()


