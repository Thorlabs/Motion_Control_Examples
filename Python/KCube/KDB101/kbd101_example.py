"""
kbd101_example.py
=================

This example demonstrates basic control of the Thorlabs KBD101 Brushless motor controller using python.

It achieves control of the device via the Kinesis C API, interfaced with via ctypes. The example connects, homes, moves
and disconnects the device.

"""
import time
import os
import sys
from ctypes import *


def main():
    """
    main():
    ------

    Performs all actions of the KDC101
    :return: None
    """

    if sys.version_info < (3, 8):
        os.chdir(r"C:\Program Files\Thorlabs\Kinesis")
    else:
        os.add_dll_directory(r"C:\Program Files\Thorlabs\Kinesis")

    lib: CDLL = cdll.LoadLibrary("Thorlabs.MotionControl.KCube.BrushlessMotor.dll")

    return None


if __name__ == "__main__":
    main()
