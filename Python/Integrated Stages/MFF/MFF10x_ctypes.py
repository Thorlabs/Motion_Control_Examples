import os
import time
import sys

from ctypes import *
from time import sleep

if sys.version_info < (3, 8):
        os.chdir(r"C:\Program Files\Thorlabs\Kinesis")
else:
        os.add_dll_directory(r"C:\Program Files\Thorlabs\Kinesis")

lib = cdll.LoadLibrary("Thorlabs.MotionControl.FilterFlipper.dll")

# Build device list
# This function builds an internal collection of all devices found on the USB that are not currently open. <br />
# NOTE, if a device is open, it will not appear in the list until the device has been closed.
lib.TLI_BuildDeviceList()

# set up serial number variable
# manually replace serial number of specific device
serialNumber = c_char_p(b"37849392")
moveTimeout = 60.0

# set up device
lib.FF_Open(serialNumber)
lib.FF_StartPolling(serialNumber, c_int(200))

time.sleep(3)

lib.FF_ClearMessageQueue(serialNumber)

# homing
lib.FF_Home(serialNumber)

# send move command
print('Moving Device to position 2')
# delays next move by 5 seconds
sleep(1)
# move to position 1
lib.FF_MoveToPosition(serialNumber, 2)



# delays next move by 5 seconds
sleep(5)

# send move command
print('Moving Device to position 1')
sleep(1)

# move to position 2
lib.FF_MoveToPosition(serialNumber, 1)

# clean up and exit
lib.FF_ClearMessageQueue(serialNumber)
# print lib.CC_GetPosition()

lib.FF_StopPolling(serialNumber)
lib.FF_Close(serialNumber)