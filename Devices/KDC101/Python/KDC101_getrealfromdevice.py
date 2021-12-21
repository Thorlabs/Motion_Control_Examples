import os
import time
import ctypes
import sys
from ctypes import *

if sys.version_info < (3, 8):
    os.chdir(r"C:\Program Files\Thorlabs\Kinesis")
else:
    os.add_dll_directory(r"C:\Program Files\Thorlabs\Kinesis")
lib = cdll.LoadLibrary("Thorlabs.MotionControl.KCube.StepperMotor.dll")

lib.TLI_InitializeSimulations()

lib.TLI_BuildDeviceList()
serialNumber = c_char_p(b"26000001")
moveTimeout = 60.0

stepsPerRev = 200
gearBoxRatio = 1
pitch = 1

lib.SCC_Open(serialNumber)
lib.SCC_StartPolling(serialNumber, c_int(100))
lib.SCC_EnableChannel(serialNumber)
time.sleep(3)
lib.SCC_ClearMessageQueue(serialNumber)

lib.SCC_SetMotorParamsExt(serialNumber, c_double(stepsPerRev), c_double(gearBoxRatio), c_double(pitch))
lib.SCC_GetPositionCounter(serialNumber)
deviceUnit = c_int(lib.SCC_GetPositionCounter(serialNumber))
realUnit = c_double()
lib.SCC_GetRealValueFromDeviceUnit(serialNumber, deviceUnit, byref(realUnit), 0)
print(realUnit)
print(deviceUnit)


print("Homing Device")
homeStartTime = time.time()
lib.SCC_Home(serialNumber)
homed = False
messageType = c_ushort()
messageID = c_ushort()
messageData = c_ulong()
while messageID.value != 0 or messageType.value != 2:
    lib.SCC_WaitForMessage(serialNumber, byref(messageType), byref(messageID), byref(messageData))
    print(messageID, messageType)

print("Homed")
    
lib.SCC_ClearMessageQueue(serialNumber)

lib.SCC_SetMotorParamsExt(serialNumber, c_double(stepsPerRev), c_double(gearBoxRatio), c_double(pitch))
lib.SCC_LoadSettings(serialNumber)


lib.SCC_GetPositionCounter(serialNumber)
deviceUnit = c_int(lib.SCC_GetPositionCounter(serialNumber))
realUnit = c_double()
lib.SCC_GetRealValueFromDeviceUnit(serialNumber, deviceUnit, byref(realUnit), 0)
print(realUnit)
print(deviceUnit)


time.sleep(5)
lib.SCC_MoveRelative(serialNumber, 409600)
print("Moving")
time.sleep(10)
lib.SCC_GetPositionCounter(serialNumber)
deviceUnit = c_int(lib.SCC_GetPositionCounter(serialNumber))
realUnit = c_double()
lib.SCC_GetRealValueFromDeviceUnit(serialNumber, deviceUnit, byref(realUnit), 0)
print(realUnit)
print(deviceUnit)


lib.SCC_ClearMessageQueue(serialNumber)
lib.SCC_StopPolling(serialNumber)
lib.SCC_Close(serialNumber)
print("Close")

lib.TLI_UninitializeSimulations()
