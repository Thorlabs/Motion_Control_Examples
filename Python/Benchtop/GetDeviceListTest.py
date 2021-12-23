import os
import time

import ctypes
import numpy

from ctypes import *

# os.chdir(r"C:\Program Files\Thorlabs\Kinesis")
os.add_dll_directory(r"C:\Program Files\Thorlabs\Kinesis")
lib = cdll.LoadLibrary("Thorlabs.MotionControl.Benchtop.BrushlessMotor.dll")

lib.TLI_InitializeSimulations()

lib.TLI_BuildDeviceList()

lib.TLI_GetDeviceList('')
serialNos = c_char_p(b'')
print(sizeof(serialNos))

print("1")
deviceID = c_int(73)
lib.TLI_GetDeviceListByTypeExt(serialNos, c_ulong(250), deviceID)

print(serialNos.value)

serialNumber = serialNos.value[:8]
print(serialNumber)

moveTimeout = 60.0

stepsPerRev = 512
gearBoxRatio = 67
pitch = 1

lib.BMC_Open(serialNumber)
lib.BMC_StartPolling(serialNumber, 1, c_int(200))
lib.BMC_LoadSettings(serialNumber, 1)
lib.BMC_EnableChannel(serialNumber, 1)

lib.BMC_StartPolling(serialNumber, 2, c_int(200))
lib.BMC_LoadSettings(serialNumber, 2)
lib.BMC_EnableChannel(serialNumber, 2)

time.sleep(3)
lib.BMC_ClearMessageQueue(serialNumber, 1)

print("Homing Device")
homeStartTime = time.time()
lib.BMC_Home(serialNumber, 1)

homed = False
messageType = c_ushort()
messageID = c_ushort()
messageData = c_ulong()

while messageID.value != 0 or messageType.value != 2:
    lib.BMC_WaitForMessage(serialNumber, 1, byref(messageType), byref(messageID), byref(messageData))

print("Homed")
lib.BMC_ClearMessageQueue(serialNumber, 1)
