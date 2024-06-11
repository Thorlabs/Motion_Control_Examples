"""
BBDXXX ctypes Example
Date of Creation(YYYY-MM-DD): 2023-07-18
Date of Last Modification on Github: 2023-08-11
Python Version Used: python3
Kinesis Version Tested: 1.14.40

"""

import os
import time
import sys
from ctypes import *

# Load the library for the BBD motor
if sys.version_info < (3, 8):
    os.chdir(r"C:\Program Files\Thorlabs\Kinesis")
else:
    os.add_dll_directory(r"C:\Program Files\Thorlabs\Kinesis")
lib = cdll.LoadLibrary("Thorlabs.MotionControl.Benchtop.BrushlessMotor.dll")

lib.TLI_InitializeSimulations()

lib.TLI_UninitializeSimulations()