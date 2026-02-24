"""
Example KST_ctypes_getrealfromdeviceunits.py
Example Date of Creation: 2024-07-25
Example Date of Last Modification on Github: 2024-07-25
Version of Python used for Testing: 3.11
Version of the Thorlabs SDK used: Kinesis 1.14.49 
==================
Example Description: This example homes the KST101, performs a relative move and shows the position in real an device units 
"""


import os
import time
import sys
from ctypes import *

#import library
if sys.version_info < (3, 8):
    os.chdir(r"C:\Program Files\Thorlabs\Kinesis")
else:
    os.add_dll_directory(r"C:\Program Files\Thorlabs\Kinesis")
lib = cdll.LoadLibrary(r"Thorlabs.MotionControl.KCube.StepperMotor.dll")

# Uncomment this line if you are using simulation
#lib.TLI_InitializeSimulations()  

lib.TLI_BuildDeviceList()
serialNumber = c_char_p(b"26003851")
moveTimeout = 60.0

#Values for ZST motor:
stepsPerRev = c_double(49152)
gearBoxRatio = c_double(0.0245)
pitch = c_double(1)

#open device
lib.SCC_Open(serialNumber)
lib.SCC_StartPolling(serialNumber, c_int(100))
lib.SCC_EnableChannel(serialNumber)
lib.SCC_SetMotorParamsExt(serialNumber, stepsPerRev, gearBoxRatio, pitch)
lib.SCC_LoadSettings(serialNumber)
time.sleep(1)

#home
print("Homing Device")
lib.SCC_Home(serialNumber)
time.sleep(10)
print("Homed")
    
#get position
deviceUnit = c_int(lib.SCC_GetPositionCounter(serialNumber))
realUnit = c_double()
time.sleep(1)
lib.SCC_GetRealValueFromDeviceUnit(serialNumber, deviceUnit, byref(realUnit), 0)
print("real unit: ",realUnit.value)
print("device unit: ",deviceUnit.value)

#move
lib.SCC_MoveRelative(serialNumber,  7471104)
print("Moving")
time.sleep(8)

#get position
lib.SCC_GetPositionCounter(serialNumber)
deviceUnit = c_int(lib.SCC_GetPositionCounter(serialNumber))
realUnit = c_double()
lib.SCC_GetRealValueFromDeviceUnit(serialNumber, deviceUnit, byref(realUnit), 0)
print("real unit: ",realUnit.value)
print("device unit: ",deviceUnit.value)

#close
lib.SCC_StopPolling(serialNumber)
lib.SCC_Close(serialNumber)
print("Close")

#lib.TLI_UninitializeSimulations()